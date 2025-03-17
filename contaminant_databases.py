import pandas as pd
import geopandas as gpd
import numpy as np

from shared_config import CONTAMINANT_DATA_FILE, CUMULATIVE_RESULTS_FILE, MUNICIPALITIES_DATA_FILE, COUNTIES_DATA_FILE


def get_cumulative_user_results():
    return pd.read_excel(CUMULATIVE_RESULTS_FILE)


def get_geographical_data():
    try:
        municipal_gdf = gpd.read_file(MUNICIPALITIES_DATA_FILE)
        county_gdf = gpd.read_file(COUNTIES_DATA_FILE)
    except Exception as e:
        print("Error getting geographical data: ", str(e))
        return None, None
    return municipal_gdf, county_gdf


def get_contaminant_dataframe():
    return pd.read_excel(CONTAMINANT_DATA_FILE, index_col="Contaminant Name")


def get_contaminant_row(contaminant_name):
    contaminant_df = get_contaminant_dataframe()
    row = contaminant_df[contaminant_name]
    if not row.empty:
        return row
    
    
def get_weighted_contaminant_score(test_results_df):
    inorganic_sum = 0
    inorganic_weight_sum = 0
    microorganism_sum = 0
    microorganism_weight_sum = 0
    byproduct_sum = 0
    byproduct_weight_sum = 0
    disinfectant_sum = 0
    disinfectant_weight_sum = 0
    organic_sum = 0
    organic_weight_sum = 0
    pfas_sum = 0
    pfas_weight_sum = 0
    radionuclides_sum = 0
    radionuclides_weight_sum = 0
    
    for contaminant, row in test_results_df.iterrows():
        if row["Exceeds"] >= 0:
            if row["Contaminant Group"] == "Inorganic Chemicals":
                inorganic_sum += row["Exceeds"] * row["Weight"]
                inorganic_weight_sum += row["Weight"]
                
            if row["Contaminant Group"] == "Organic Chemicals":
                organic_sum += row["Exceeds"] * row["Weight"]
                organic_weight_sum += row["Weight"]
                
            if row["Contaminant Group"] == "Microorganisms":
                microorganism_sum += row["Exceeds"] * row["Weight"]
                microorganism_weight_sum += row["Weight"]
            
            if row["Contaminant Group"] == "Disinfection Byproducts":
                byproduct_sum += row["Exceeds"] * row["Weight"]
                byproduct_weight_sum += row["Weight"]
                
            if row["Contaminant Group"] == "Disinfectants":
                disinfectant_sum += row["Exceeds"] * row["Weight"]
                disinfectant_weight_sum += row["Weight"]
            
            if row["Contaminant Group"] == "PFAS":
                pfas_sum += row["Exceeds"] * row["Weight"]
                pfas_weight_sum += row["Weight"]
                
            if row["Contaminant Group"] == "Radionuclides":
                radionuclides_sum += row["Exceeds"] * row["Weight"]
                radionuclides_weight_sum += row["Weight"]
                
    scores = {}
    if inorganic_weight_sum != 0:
        inorganic_score = score_out_of_100(inorganic_sum/inorganic_weight_sum)
        scores.update({"Inorganic Chemicals": inorganic_score})
    
    if organic_weight_sum != 0:
        organic_score = score_out_of_100(organic_sum/organic_weight_sum)
        scores.update({"Organic Chemicals": organic_score})
    
    if microorganism_weight_sum != 0:
        microorganism_score = score_out_of_100(microorganism_sum/microorganism_weight_sum)
        scores.update({"Microorganisms": microorganism_score})
    
    if byproduct_weight_sum != 0:
        byproduct_score = score_out_of_100(byproduct_sum/byproduct_weight_sum)
        scores.update({"Disinfection Byproducts": byproduct_score})
        
    if disinfectant_weight_sum != 0:
        disinfectant_score = score_out_of_100(disinfectant_sum/disinfectant_weight_sum)
        scores.update({"Disinfectants": disinfectant_score})
    
    if pfas_weight_sum != 0:
        pfas_score = score_out_of_100(pfas_sum/pfas_weight_sum)
        scores.update({"PFAS": pfas_score})
        
    if radionuclides_weight_sum != 0:
        radionuclides_score = score_out_of_100(radionuclides_sum/radionuclides_weight_sum)
        scores.update({"Radionuclides": radionuclides_score})
    
    print(scores)
    return scores
    
    
def score_out_of_100(weighted_avg):
    return 100 - 50 * weighted_avg


def append_user_results(user_scores, user_municipality):
    cumulative_gdf = get_cumulative_user_results()
    for contaminant_class, score in user_scores.items():
        cumulative_gdf.at[user_municipality, f"Total {contaminant_class}"] += score
        cumulative_gdf.at[user_municipality, "Results Count"] += 1


def format_score(score):
    return f"{int(score)}/100"


def format_municipality_scores(municipal_gdf):
    municipal_gdf["Inorganic Chemicals Formatted"] = municipal_gdf["Inorganic Chemicals"].apply(format_score)
    municipal_gdf["Organic Chemicals Formatted"] = municipal_gdf["Organic Chemicals"].apply(format_score)
    municipal_gdf["Microorganisms Formatted"] = municipal_gdf["Microorganisms"].apply(format_score)
    municipal_gdf["Disinfection Byproducts Formatted"] = municipal_gdf["Disinfection Byproducts"].apply(format_score)
    municipal_gdf["Disinfectants Formatted"] = municipal_gdf["Disinfectants"].apply(format_score)
    municipal_gdf["PFAS Formatted"] = municipal_gdf["PFAS"].apply(format_score)
    municipal_gdf["Radionuclides Formatted"] = municipal_gdf["Radionuclides"].apply(format_score)
    municipal_gdf["Overall Formatted"] = municipal_gdf["Overall"].apply(format_score)

    municipal_gdf.to_file(MUNICIPALITIES_DATA_FILE)
    
    
def construct_municipal_score_geodata():
    cumulative_gdf = get_cumulative_user_results()
    municipal_gdf, county_gdf = get_geographical_data()
    modified_count = 0
    for index, row in cumulative_gdf.iterrows():
        municipality = row["MUN"]
        if row["Results Count"] > 0:
            modified_count += 1
            # Computing average scores if there is at least 1 result for the given municipality
            municipal_gdf.at[municipality, "Inorganic Chemicals"] = row["Total Inorganic Chemicals"] / row["Results Count"]
            municipal_gdf.at[municipality, "Organic Chemicals"] = row["Total Organic Chemicals"] / row["Results Count"]
            municipal_gdf.at[municipality, "Microorganisms"] = row["Total Microorganisms"] / row["Results Count"]
            municipal_gdf.at[municipality, "Disinfection Byproducts"] = row["Total Disinfection Byproducts"] / row["Results Count"]
            municipal_gdf.at[municipality, "Disinfectants"] = row["Total Disinfectants"] / row["Results Count"]
            municipal_gdf.at[municipality, "PFAS"] = row["Total PFAS"] / row["Results Count"]
            municipal_gdf.at[municipality, "Radionuclides"] = row["Total Radionuclides"] / row["Results Count"]
            municipal_gdf.at[municipality, "Overall"] = row["Total Overall"] / row["Results Count"]
    
    return municipal_gdf
    

def create_empty_municipal_score_geodata(new_file):
    municipal_gdf, _ = get_geographical_data()
    
    municipal_gdf["Inorganic Chemicals"] = -1
    municipal_gdf["Organic Chemicals"] = -1
    municipal_gdf["Microorganisms"] = -1
    municipal_gdf["Disinfection Byproducts"] = -1
    municipal_gdf["Disinfectants"] = -1
    municipal_gdf["PFAS"] = -1
    municipal_gdf["Radionuclides"] = -1
    municipal_gdf["Overall"] = -1
    
    format_municipality_scores(municipal_gdf)
    
    municipal_gdf.to_file(new_file)
    
    
def create_test_municipal_score_geodata(new_file):
    municipal_gdf, _ = get_geographical_data()
    max_pop = np.max(municipal_gdf["POP2020"])
    min_pop = np.min(municipal_gdf["POP2020"])
    
    for index, row in municipal_gdf.iterrows():
        mean_score = 3/4 * (100 - (row["POP2020"] / max_pop * 100))
        
        row["Inorganic Chemicals"] = float(np.random.normal(mean_score, 5))
        row["Organic Chemicals"] = float(np.random.normal(mean_score, 5))
        row["Microorganisms"] = float(np.random.normal(mean_score, 5))
        row["Disinfection Byproducts"] = float(np.random.normal(mean_score, 5))
        row["Disinfectants"] = float(np.random.normal(mean_score, 5))
        row["PFAS"] = float(np.random.normal(mean_score, 5))
        row["Radionuclides"] = float(np.random.normal(mean_score, 5))
        row["Overall"] = float(np.random.normal(mean_score, 5))
    
    format_municipality_scores(municipal_gdf)
    
    municipal_gdf.to_file(new_file)
    
if __name__ == "__main__":
    test_file = "test_data.xlsx"
    create_test_municipal_score_geodata(test_file)