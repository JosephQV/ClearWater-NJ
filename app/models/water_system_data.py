import pandas as pd
import logging
import requests
import json

from data.app_config import WATER_SYSTEM_DATA_FILE, GENERAL_MUNICIPALITIES_DATA_FILE, USER_LOCAL_PATH, DATA_LOCAL_PATH


logger = logging.getLogger(__name__)


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
    
    if cws_df is not None:
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


def download_pdf(url, filename=f"{USER_LOCAL_PATH}/download_test.pdf"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        # Save the content to a file
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"PDF downloaded successfully and saved as '{filename}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")


def get_recent_CCR_by_water_system(water_system: str):
    njaw_systems_link_text = {
        "MOUNT HOLLY": "mountholly",
        "PENNS GROVE": "pennsgrove"
        "ATLANTIC":"atlantic",
        "BELVIDERE": "belvidere",
        "BRIDGEPORT": "bridgeport",
        "CAPE MAY": "capemay",
        "COASTAL NORTH": "coastalnorth",
        "CROSSROADS AT OLDWICK": "crossroadsatoldwick",
        "DEEP RUN": "deeprun",
        "DELAWARE/WESTERN": "delaware",
        "EGG HARBOR CITY": "eggharborcity",
        "FOUR SEASONS AT CHESTER": "fourseasonsatchester",
        "FRENCHTOWN": "frenchtown",
        "HARRISON": "harrison",
        "HOMESTEAD": "homestead",
        "INTERNATIONAL TRADE CENTER": "itc",
        "LIBERTY": "liberty",
        "LITTLE FALLS": "littlefalls",
        "LOGAN": "logan",
        "NEW EGYPT": "newegypt",
        "OCEAN CITY": "oceancity",
        "RARITAN": "raritan",
        "ROXBURY": "roxbury",
        "SALEM": "salem",
        "SHREWSBURY_AVMA": "shrewsburyavma",
        "SHORELANDS": "shorelands",
        "SHORTHILLS": "shorthills",
        "SOUTH ORANGE VILLAGE": "southorange",
        "STRATHMERE": "strathmere",
        "SUNBURY": "sunbury",
        "TWIN LAKES": "twinlakes",
        "UNION BEACH": "unionbeach",
        "VINCENTOWN": "vincentown",
        "WASHINGTON/OXFORD": "washingtonoxford",
        "WEST JERSEY": "mountolivewestjersey",
    }
    if "NJ AMERICAN WATER" in water_system:
        # Implement here
        # Remove the "NJ AMERICAN WATER - " part from the water_system string, and
        # get the last part, which is the specific system name.
        # Use that as the key into the dictionary to get the link part needed.
        key = "" # replace
       
        url = f"https://www.amwater.com/ccr/{njaw_systems_link_text.get(key)}.pdf"
        # Then use the url to download using the above download_pdf() function
        
        
    else:
        # Other water systems, nothing here yet.
        pass


def get_NJAW_alerts():
    url = 'https://amwater.com/api/content/render/false/query/+contentType:ExtendedAlerts%20+(conhost:c07d33c4-6422-4606-b0ce-6082377ac538%20conhost:SYSTEM_HOST)%20+(ExtendedAlerts.active:*Active*%20ExtendedAlerts.active_dotraw:*Active*)%20+languageId:1%20+(categories:newJersey)%20+deleted:false%20+working:true/orderby/modDate%20desc'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f"{DATA_LOCAL_PATH}/water_systems/njaw_alerts.json", "w+") as f:
            json.dump(response.json(), f) # Writing alerts list content to JSON file in water_systems/ folder

    else:
        print(f'Failed to retrieve alerts from endpoint. Status code: {response.status_code}')
        return None
    return response.json()

def extract_NJAW_alerts():
    # Get the raw alerts JSON content
    alerts_content = get_NJAW_alerts()
    # Create the list of alerts that will be returned. Each
    # item in the list will be a dictionary representing one alert
    # with properties like title, published date, description, and link (URL).
    alerts_list = []
    
    if alerts_content is not None:
        # Print the keys of the dictionary for development/testing purposes
        print(alerts_content.keys())
        
        # [implement here]
        
    
    return alerts_list

