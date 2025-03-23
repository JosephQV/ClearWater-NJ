import pandas as pd
from contaminant_databases import get_weighted_contaminant_score
from water_system_databases import get_all_municipalities

import json

# We want to generate many fake test results. We want a certain number (15) per
# municipality.

# A few hundred x 15 dataframes that will be generated.

# with open(r"C:\Users\josep\Desktop\Code\Local Projects\New folder\GSSTeam12Project\test_results_base.xlsx") as f:
#     data = json.load(f)

data = {
    "all_tests":
        [
            
        ]
}

# Loop through each municipality

    # for each municipality
    
    municipal_dict = {
            "municipality": "current municipality",
            "tests": [

            ]
        }
    
    # Loop through, 15 times

        # Generate 15 sample tests.
        
        # use pandas to read this file
        # GSSTeam12Project\test_results_base.xlsx
        
        # This will be a dataframe, change the last column to new values.
        # The "Exceeds" column should contain values between -1 and 2

        # Randomize the column so that many rows still have -1 for Exceeds, 
        # some have 0, a smaller number of them have 1, and then the smallest subset has
        # 2 entered.
        
        # Use the get_weighted_contaminant_score, by passing the test dataframe and
        # getting back the dictionary of scores.
        scores = get_weighted_contaminant_score()
        
        municipal_dict["current municipality"]["tests"].append(scores)
    
    data["all_tests"].append(municipal_dict)
        
        

if __name__ == "__main__":
    # df = get_all_municipalities().unique()
    
    # print(df)
    
    df = pd.read_excel(r"C:\Users\josep\Desktop\Code\Local Projects\New folder\GSSTeam12Project\test_results_base.xlsx")
    
    scores = get_weighted_contaminant_score(df)
    
    print(scores)