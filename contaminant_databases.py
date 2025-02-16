import pandas as pd

from shared_config import CONTAMINANT_DATA_FILE


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