import os


APP_TITLE = "WaterWise NJ"

PRIMARY_THEME_COLOR = "#3275fa"
PRIMARY_THEME_RGBA = (50/255, 117/255, 250/255, 255/255)
SECONDARY_THEME_COLOR = "#38c3ff"
SECONDARY_THEME_RGBA = (56/255, 195/255, 255/255, 255/255)
TERTIARY_THEME_COLOR = "#cce3ed"
TERTIARY_THEME_RGBA = (204/255, 227/255, 237/255, 255/255)
COLORS = {
    "primary": {
        "hex": PRIMARY_THEME_COLOR,
        "rgba": PRIMARY_THEME_RGBA
    },
    "secondary": {
        "hex": SECONDARY_THEME_COLOR,
        "rgba": SECONDARY_THEME_RGBA
    },
    "tertiary": {
        "hex": TERTIARY_THEME_COLOR,
        "rgba": TERTIARY_THEME_RGBA
    }
}

ICON_PATH = fr"{os.curdir}/resources/icons"
CONTAMINANT_DATA_FILE = fr"{os.curdir}/resources/Water_Contaminant_MCLs.xlsx"
WATER_SYSTEM_DATA_FILE = f"{os.curdir}/resources/PWS_By_Municipality.xlsx"
CONTACT_INFO_DATA_FILE = fr"{os.curdir}/resources/PWS_Contact_Info.xlsx"

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
    "communication_selected": fr"{ICON_PATH}/communication_icon_selected.png"
}

APP_TEXT = {
    "start_screen": {},
    "home_screen": {},
    "map_screen": {},
    "waterquality_screen": {},
    "watertestinput_screen": {},
    "watercontaminantselection_screen": {},
    "results_screen": {
        
        },
    "resources_screen": {
        "overview": {
            "en": "Educational Resources\nInterested in learning more about water in NJ? Use the links below to find helpful resources on water contaminants, water quality efforts in NJ, and what you could to do get involved with your drinking water quality.",
            "es": "Recursos educativos\n¿Está interesado en aprender más sobre el agua en Nueva Jersey? Utilice los enlaces a continuación para encontrar recursos útiles sobre los contaminantes del agua, los esfuerzos por la calidad del agua en Nueva Jersey y lo que podría hacer para involucrarse con la calidad del agua potable."
        },
    },
    "communication_screen": {
        "overview": "Communication & Feedback\nHave concerns or feedback regarding your water? Use the menus below to help with finding assistance or with reaching out to your local officials."
    }
}