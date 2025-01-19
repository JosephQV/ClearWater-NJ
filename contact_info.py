import pandas as pd
import os

# Path to your Excel file
Contact_Info_Data_File = fr"{os.curdir}\resources\PWS_Contact_Info_Cleaned.xlsx"


#Display the contents of the Dataframe
def Get_Contact_Info_By_Water_System (pwsid):
    dataframe = pd.read_excel(Contact_Info_Data_File)
    for i in range (len(dataframe)):
        row=dataframe.iloc[i]
        if str (row["PWSID"])==pwsid:
            return row


if __name__=="__main__":
    # testing
    result=Get_Contact_Info_By_Water_System("102001")
    print (result)