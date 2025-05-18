import pandas as pd
import numpy as np
from app.models.water_system_data import get_weighted_contaminant_score, get_all_municipalities

import json
import os

# We want to generate many fake test results. We want a certain number (15) per
# municipality.
# A few hundred x 15 dataframes that will be generated.
def generate_example_water_tests(N_per_municipality):
    df = get_all_municipalities()["MUNICIPALITY_NAME_COMMON"].unique()
    print(len(df) ,df)

    data = {}

    # Loop through each municipality
    for municipality in df:
        # for each municipality
        municipal_tests = []
        
        for i in range(N_per_municipality):
        # Loop through, 15 times
            
            # Generate 15 sample tests.
            
            # use pandas to read this file
            test_df = pd.read_excel(rf"{os.curdir}\test_results_base.xlsx")

            # This will be a dataframe, change the last column to new values.
            # The "Exceeds" column should contain values between -1 and 2

            # Randomize the column so that many rows still have -1 for Exceeds, 
            # some have 0, a smaller number of them have 1, and then the smallest subset has
            # 2 entered.
            n = len(test_df)

            # Calculate counts
            count_neg1 = n  # Start with total
            count_0 = count_neg1 // 2
            remaining_after_0 = count_neg1 - count_0
            count_1 = int(remaining_after_0 * 0.75)
            count_2 = remaining_after_0 - count_1

            # Create the list of values
            values = [-1] * (n - count_0 - count_1 - count_2) + [0] * count_0 + [1] * count_1 + [2] * count_2

            # Shuffle values
            np.random.shuffle(values)

            # Assign back to the DataFrame
            test_df["Exceeds"] = values
            # Use the get_weighted_contaminant_score, by passing the test dataframe and
            # getting back the dictionary of scores.
            scores = get_weighted_contaminant_score(test_df)
            
            municipal_tests.append(scores)
        
        data[municipality] = municipal_tests
    
    with open(f"{os.curdir}/all_generated_tests.json", "w") as f:
        json.dump(data, f)

    return data


def add_example_results_to_cumulative_results_file(example_results_json, cumulative_results_file):
    with open(example_results_json) as f:
        res = json.load(f)
        
    total_df = pd.read_excel(
        cumulative_results_file, 
        index_col="MUNICIPALITY NAME",
        dtype={
            "OBJECTID": "string",
            "MUN": "string",
            "COUNTY": "string",
            "MUNICIPALITY NAME": "string",
            "Total Inorganic Chemicals": "float64",
            "Total Organic Chemicals": "float64",
            "Total Microorganisms": "float64",
            "Total Disinfection Byproducts": "float64",
            "Total Disinfectants": "float64",
            "Total PFAS": "float64",
            "Total Radionuclides": "float64",
            "Total Overall": "float64",
        })
    
    for municipality, test_list in res.items():
        for test in test_list:
            total_df.loc[municipality, "Results Count"] += 1
            total_df.loc[municipality, "Total Inorganic Chemicals"] += test["Inorganic Chemicals"]
            total_df.loc[municipality, "Total Organic Chemicals"] += test["Organic Chemicals"]
            total_df.loc[municipality, "Total Microorganisms"] += test["Microorganisms"]
            total_df.loc[municipality, "Total Disinfection Byproducts"] += test["Disinfection Byproducts"]
            total_df.loc[municipality, "Total Disinfectants"] += test["Disinfectants"]
            total_df.loc[municipality, "Total PFAS"] += test["PFAS"]
            total_df.loc[municipality, "Total Radionuclides"] += test["Radionuclides"]

    print(total_df.head())
    total_df.to_excel(cumulative_results_file)
    
if __name__ == "__main__":
    # d = generate_example_water_tests(5)
    # for key, val in d.items():
    #     print(key, '\t', val, '\n')
    
    add_example_results_to_cumulative_results_file(
        f"{os.curdir}/all_generated_tests.json",
        f"{os.curdir}/resources/Cumulative_User_Results.xlsx"
    )