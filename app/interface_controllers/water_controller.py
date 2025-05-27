import datetime, time
import os
import json

from app.models.drinking_water_contaminant_data import get_water_contaminant_regulatory_data, get_home_water_testing_kits
from data.app_config import USER_DATA_FILE


class WaterQualityController:
    pass


class TestingKitSelectionController:
    
    def get_testing_kits(self):
        testing_kits = get_home_water_testing_kits()
        return testing_kits


class WaterContaminantSelectionController:
    
    def get_all_contaminants(self):
        contaminant_df = get_water_contaminant_regulatory_data()
        contaminant_dict = {
            "Common": [],
            "Rare": [],
            "Very Rare": []
        }
        common_level_map = {
            "1": "Common",
            "2": "Rare",
            "3": "Very Rare"
        }
        for contaminant, row in contaminant_df.iterrows():
            contaminant_dict[common_level_map[str(int(row["RarityRanking"]))]].append(
                {
                    "Contaminant": contaminant,
                    "Contaminant Group": row["ContaminantClass"],
                    "Unit": row["Unit"],
                    "Health Impacts Text": row["HealthEffects"],
                    "Sources Text": row["CommonSources"]
                }
            )
        return contaminant_dict
    
    def process_contaminant_selections(self, water_contaminant_selections):
        pass


class WaterTestInputController:
    
    def get_chosen_contaminants(self, contaminant_selection):
        all_contaminants = get_water_contaminant_regulatory_data()
        return all_contaminants.loc[contaminant_selection]
    
    def process_water_test(self, water_test_input_data):
        # The saved results dataframe will begin as a copy of the contaminant
        # MCL reference dataframe.
        user_results_df = get_water_contaminant_regulatory_data()
        # Values for "Exceeds" for each contaminant are initially set to -1; signifying
        # that the contaminant was not tested for (there won't be results for it).
        user_results_df["Exceeds"] = -1
        
        summary_results_list = []
        
        for contaminant, input_item in self.contaminant_entries.items():
            
            row = user_results_df.loc[contaminant]
            try:
                user_level = float(input_item.level_input_text)
            except ValueError as e:
                print("Error reading input: ", e)
                continue
                           
            if row is not None:
                mcl = float(row["Maximum Contaminant Level (MCL)"])
                mclg = float(row["Maximum Contaminant Level Goal (MCLG)"])
                
                message = f"{contaminant}\t\tMCL: {mcl}\tMCLG: {mclg}\t{user_level}"
                
                try:
                    if user_level > mcl:
                        status = "Exceeded MCL"
                        # A +2 for the contaminant signifies it exceeded the MCL (worst case)
                        user_results_df.loc[contaminant, "Exceeds"] = 2
                    elif user_level > mclg:
                        status = "Exceeded MCLG"
                         # A +1 for the contaminant signifies it exceeded the MCLG (second worst case)
                        user_results_df.loc[contaminant, "Exceeds"] = 1
                    else:
                        status = "Did Not Exceed"
                        # A 0 value for the contaminant signifies that it was tested for but did not exceed
                        # the MCL or MCLG; this is a good result.
                        user_results_df.loc[contaminant, "Exceeds"] = 0
                        
                    summary_results_list.append(
                        {
                            "Contaminant": contaminant,
                            "MCL": mcl,
                            "MCLG": mclg,
                            "Measured Level": user_level,
                            "Status": status
                        }
                    )
                    message += f"\t\t{status}"
                        
                except ValueError as e:
                    message += "\t\tError: " + str(e)
            else:
                message = "Row is None; contaminant not found in dataframe"
                
            print(message)
        
        for item in summary_results_list:
            print(item)

        # Saving the entered results to a file
        user_results_df.to_excel(fr"{os.curdir}/resources/user/test_results_{datetime.date.today()}_{time.time()}.xlsx")
        user_scores = get_weighted_contaminant_score(user_results_df)
        
        user_data = get_user_data()
        user_data["water_tests"].append({"date": str(datetime.date.today()), "scores": user_scores, "results": summary_results_list})

        with open(USER_DATA_FILE, "w") as file:
            json.dump(user_data, file)