from pathlib import Path
import os


APP_TITLE = "ClearWater NJ"

WINDOW_WIDTH = 350
WINDOW_HEIGHT = 622

ICON_PATH = fr"{Path(os.curdir).parent}/assets/icons"
DATA_LOCAL_PATH = fr"{Path(os.curdir).parent}/data"
USER_LOCAL_PATH = fr"{DATA_LOCAL_PATH}/user"
USER_WATER_TEST_RESULTS_PATH = fr"{USER_LOCAL_PATH}/drinking_water_test_results/"
CUMULATIVE_RESULTS_FILE = fr"{DATA_LOCAL_PATH}/misc/Cumulative_User_Results.xlsx"
CONTAMINANT_DATA_FILE = fr"{DATA_LOCAL_PATH}/drinking_water_contaminants/Water_Contaminant_MCLs.xlsx"
HOME_WATER_TESTS_DATA_FILE = fr"{DATA_LOCAL_PATH}/drinking_water_contaminants/drinking_water_home_testing_kits.json"
WATER_SYSTEM_DATA_FILE = f"{DATA_LOCAL_PATH}/water_systems/EPA_Water System Summary_20250507.xlsx"
GEOGRAPHIC_MUNICIPALITIES_DATA_FILE = fr"{DATA_LOCAL_PATH}/geographical/municipal_contaminant_geodata.geojson"
GENERAL_MUNICIPALITIES_DATA_FILE = fr"{DATA_LOCAL_PATH}/geographical/municipalities_by_county.xlsx"
IN_APP_RESOURCES_DATA_FILE = fr"{Path(os.curdir).parent}/assets/InAppResources.xlsx"
MAP_FILE = fr"{DATA_LOCAL_PATH}/geographical/map.html"
LOG_FILE = fr"{DATA_LOCAL_PATH}/logs/app.log"
FONT_FILE = fr"{Path(os.curdir).parent}/app/themes/NotoSans-VariableFont_wdth,wght.ttf"
FONT_ITALIC_FILE = fr"{Path(os.curdir).parent}/app/themes/NotoSans-Italic-VariableFont_wdth,wght.ttf"

IMAGES = {
    "app": fr"{ICON_PATH}/app_icon.png",
    "settings": fr"{ICON_PATH}/menu_icon.webp",
    "user": fr"{ICON_PATH}/user_icon.png",
    "back": fr"{ICON_PATH}/back_icon.webp",
    "mywater": f"{ICON_PATH}/mywater_icon.png",
    "map": fr"{ICON_PATH}/map_icon.png",
    "home": fr"{ICON_PATH}/home_icon.png",
    "resources": fr"{ICON_PATH}/resources_icon.png",
    "communication": fr"{ICON_PATH}/communication_icon.png",
    "mywater_selected": fr"{ICON_PATH}/mywater_icon_selected.png",
    "map_selected": fr"{ICON_PATH}/map_icon_selected.png",
    "home_selected": fr"{ICON_PATH}/home_icon_selected.png",
    "resources_selected": fr"{ICON_PATH}/resources_icon_selected.png",
    "communication_selected": fr"{ICON_PATH}/communication_icon_selected.png",
    "njfuture": fr"{ICON_PATH}/njfuture_icon.png",
    "njdep": fr"{ICON_PATH}/njdep_icon.png",
    "nj_american_water": fr"{ICON_PATH}/nj_am_water_icon.jpg",
    "SJ_Wave_16in1_Test": fr"{ICON_PATH}/SJ_Wave_16in1_Test.jpg",
    "Varify_17in1_Test": fr"{ICON_PATH}/Varify_17in1_Test.jpg",
    "SafeHome_14in1_Test": fr"{ICON_PATH}/SafeHome_14in1_Test.jpg"
}

