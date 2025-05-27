import pandas as pd
import geopandas as gpd
import numpy as np
import logging
import json

from data.app_config import CONTAMINANT_DATA_FILE, CUMULATIVE_RESULTS_FILE, GEOGRAPHIC_MUNICIPALITIES_DATA_FILE, HOME_WATER_TESTS_DATA_FILE
from app.models.user_data import get_user_data


def get_home_water_testing_kits():
    try:
        with open(HOME_WATER_TESTS_DATA_FILE) as f:
            testkits = json.load(f)
    except Exception as e:
        logging.error(f"Failed to read {HOME_WATER_TESTS_DATA_FILE}: {str(e)}")
        return []
    return testkits


def get_cumulative_user_results():
    """
    The cumulative user results are the sum totals of users' water test contaminant scores. These are stored
    by contaminant class and municipality.

    Returns:
        cumulative_results_df: The pandas dataframe containing the data from the cumulative results excel file.
    """
    try:
        cumulative_results_df = pd.read_excel(CUMULATIVE_RESULTS_FILE)
    except Exception as e:
        logging.error(f"Failed to read {CUMULATIVE_RESULTS_FILE}: {str(e)}")
        return None
    return cumulative_results_df


def get_municipal_contaminant_geodata():
    try:
        municipal_gdf = gpd.read_file(GEOGRAPHIC_MUNICIPALITIES_DATA_FILE)
    except Exception as e:
        logging.error(f"Failed to read {GEOGRAPHIC_MUNICIPALITIES_DATA_FILE}: {str(e)}")
        return None
    return municipal_gdf


def get_water_contaminant_regulatory_data():
    try:
        contaminant_df = pd.read_excel(CONTAMINANT_DATA_FILE, sheet_name="NJDEP_Primary_w_EPA_Info", index_col="ContaminantName")
    except Exception as e:
        logging.error(f"Failed to read {CONTAMINANT_DATA_FILE}: {str(e)}")
        return None
    return contaminant_df
    
    
def get_weighted_contaminant_summary_scores(test_results_df):
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
    
    return scores
    
    
def score_out_of_100(weighted_avg):
    return 100 - 50 * weighted_avg


def share_user_test_results():
    cumulative_gdf = get_cumulative_user_results()
    user_municipality = get_user_data()["Municipality"]
    
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

    municipal_gdf.to_file(GEOGRAPHIC_MUNICIPALITIES_DATA_FILE)


def construct_municipal_score_geodata():
    cumulative_gdf = get_cumulative_user_results()
    print(cumulative_gdf.head())
    municipal_gdf = get_municipal_contaminant_geodata()
    print(municipal_gdf.head())
    print(municipal_gdf.columns)
    municipal_gdf.set_index("MUN")
    for index, row in cumulative_gdf.iterrows():
        print(index, row, "3")
        municipality = row["MUN"]
        if row["Results Count"] > 0:
            print(municipal_gdf.at[municipality, "Overall"])
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
    municipal_gdf, _ = get_municipal_contaminant_geodata()
    
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
    municipal_gdf, _ = get_municipal_contaminant_geodata()
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