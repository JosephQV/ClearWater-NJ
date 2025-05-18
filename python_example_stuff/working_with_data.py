import pandas as pd
import json
import os


# Paths to data files
grading_data = f"{os.curdir}/python_example_stuff/Students_Grading_Dataset.json"
movies_data = f"{os.curdir}/python_example_stuff/top_1000_movies.csv"


class MoviesAnalyzer:
    def __init__(self, data_file):
        self.data = pd.read_csv(data_file)

 


class GradesAnalyzer:
    def __init__(self, data_file):
        with open(data_file, "r") as f:
            self.data = json.load(f)

    


# Anything within this if-statement will be executed only when this file is ran.
if __name__ == "__main__":
    pass