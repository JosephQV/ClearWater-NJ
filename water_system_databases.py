import pandas as pd

from shared_config import WATER_SYSTEM_DATA_FILE, CONTACT_INFO_DATA_FILE, GENERAL_MUNICIPALITIES_DATA_FILE


def get_water_system_contact(pwsid):
    df = pd.read_excel(CONTACT_INFO_DATA_FILE, dtype={"PWSID": str})
    return df[df["PWSID"] == pwsid]


def get_water_system_by_municipality(municipality): 
    df = pd.read_excel(WATER_SYSTEM_DATA_FILE, dtype={"PWSID": str, "Municipality": str})
    df.set_index("PWSID", inplace=True)
    systems = []
    # Editing the key to fit the names that appear in the water system dataframe
    municipality = municipality.replace("Township", "Twp")
    municipality = municipality.replace("Borough", "Boro")

    for system, row in df.iterrows():
        if row["Municipality"] == municipality: 
            systems.append(row)
    result_df = pd.DataFrame(systems)
    return result_df


def get_all_counties():
    df = pd.read_excel(WATER_SYSTEM_DATA_FILE, dtype={"PWSID": str, "Municipality": str})
    return df["County"].unique()


def get_all_municipalities():
    df = pd.read_excel(GENERAL_MUNICIPALITIES_DATA_FILE)
    # These are several of the keys present in the municipalities_by_county.xlsx file
    return df[["COUNTY_NAME_COMMON", "MUNICIPALITY_NAME_COMMON", "MUNICIPALITY_NAME_NJ-1040"]]


if __name__ == "__main__":
    # Testing
    result = get_water_system_by_municipality("Union Twp")
    print(result.head())
   
    result = get_water_system_contact("NJ0102001")
    print(result)
    
    
    
    
