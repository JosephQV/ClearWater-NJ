import pandas as pd
import os

 
system_data = f"{os.curdir}/resources/water system data.xlsx"


def get_water_system_by_municipality(town): 
    df = pd.read_excel(io=system_data)
    result_df = pd.DataFrame(df.columns)
    systems = []
    for row in range(len(df)):
        row_data = df.iloc[row]
        if row_data["Municipality"] == town: 
            print(town)
            systems.append(row)
    result_df = pd.concat([result_df, pd.DataFrame(systems)])
    return result_df


if __name__ == "__main__":
    # Testing
    result = get_water_system_by_municipality("Chester")
    print(result.head())
