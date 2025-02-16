import pandas as pd

from shared_config import WATER_SYSTEM_DATA_FILE, CONTACT_INFO_DATA_FILE


def get_water_system_contact(pwsid):
    df = pd.read_excel(CONTACT_INFO_DATA_FILE, dtype={"PWSID": str})
    return df[df["PWSID"] == pwsid]


def get_water_system_by_municipality(municipality): 
    df = pd.read_excel(WATER_SYSTEM_DATA_FILE, dtype={"PWSID": str, "Municipality": str})
    df.set_index("PWSID", inplace=True)
    systems = []
    print(df.head())
    for system, row in df.iterrows():
        if row["Municipality"] == municipality: 
            systems.append(row)
    result_df = pd.DataFrame(systems)
    return result_df


if __name__ == "__main__":
    # Testing
    result = get_water_system_by_municipality("Atlantic City")
    print(result.head())
   
    result = get_water_system_contact("NJ0102001")
    print(result)
    
    
    
    
