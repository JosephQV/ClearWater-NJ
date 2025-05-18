import webbrowser
import pandas as pd
import os

from data.app_config import IN_APP_RESOURCES_DATA_FILE


class ResourcesController:   
    def get_in_app_resources(self, category):
        resources_df = pd.read_excel(IN_APP_RESOURCES_DATA_FILE)
        return resources_df[resources_df["Category"] == category]
    
    
if __name__ == "__main__":
    r = ResourcesController()
    resources = r.get_in_app_resources(category="External Tool")
    print(resources)