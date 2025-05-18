import pandas as pd
import logging

from data.app_config import WATER_SYSTEM_DATA_FILE, GENERAL_MUNICIPALITIES_DATA_FILE


def get_all_water_systems():
    """
    We're using the EPA Water System Summary Report for NJ, filtered for community water systems (CWS)
    serving at least 1,000 residents.

    Returns:
        DataFrame: The pandas dataframe containing the data from the water system report excel file.
    """
    try:
        cws_df = pd.read_excel(WATER_SYSTEM_DATA_FILE, index_col="PWS ID")
        return cws_df
    except Exception as e:
        logging.error(f"Failed to read {WATER_SYSTEM_DATA_FILE}: {str(e)}")
        return None
    

def get_water_system_by_municipality(municipality): 
    cws_df = get_all_water_systems()
    # Editing the key to fit the names that appear in the water system dataframe
    municipality = municipality.replace("Township", "Twp")
    municipality = municipality.replace("Borough", "Boro")
    
    def check_if_municipality_in_cities_served(cities):
        cities = cities.lower().replace(" ", "").split(',')
        for city in cities:
            if municipality.lower() in city:
                return True
        return False
    
    result_df = cws_df[cws_df["Cities Served"].apply(check_if_municipality_in_cities_served)].copy()
    return result_df
    

def get_all_counties():
    """
    Retrieves all NJ counties from a data file containing all 564 municipalities.

    Returns:
        np.ndarray: List of all NJ counties.
    """
    df = pd.read_excel(GENERAL_MUNICIPALITIES_DATA_FILE)    
    return df["COUNTY_NAME_COMMON"].unique()


def get_all_municipalities():
    """
    Retrieves all 564 NJ municipalities and their respective counties from a data file.

    Returns:
        DataFrame: Contains each municipality and county. Columns: [COUNTY_NAME_COMMON, MUNICIPALITY_NAME_COMMON, MUNICIPALITY_NAME_NJ-1040]
    """
    df = pd.read_excel(GENERAL_MUNICIPALITIES_DATA_FILE)
    return df[["COUNTY_NAME_COMMON", "MUNICIPALITY_NAME_COMMON", "MUNICIPALITY_NAME_NJ-1040"]]


if __name__ == "__main__":
    # Testing
    result = get_water_system_by_municipality("Union Township")
    print(result.head())
