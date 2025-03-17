import os


APP_TITLE = "ClearWater NJ"

WINDOW_WIDTH = 350
WINDOW_HEIGHT = 622

PRIMARY_THEME_COLOR = "#3275fa"
PRIMARY_THEME_RGBA = (50/255, 117/255, 250/255, 255/255)
SECONDARY_THEME_COLOR = "#38c3ff"
SECONDARY_THEME_RGBA = (56/255, 195/255, 255/255, 255/255)
TERTIARY_THEME_COLOR = "#cce3ed"
TERTIARY_THEME_RGBA = (204/255, 227/255, 237/255, 255/255)
GRAY_THEME_COLOR = "#cbd2d6"
GRAY_THEME_RGBA = (203/255, 210/255, 214/255, 255/255)

icon_colors = ["#3f688c", "#83c5ff", "#7fd7ff", "#b1e3fa"]
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
    },
    "gray": {
        "hex": GRAY_THEME_COLOR,
        "rgba": GRAY_THEME_RGBA
    }
}

ICON_PATH = fr"{os.curdir}/resources/icons"
USER_DATA_FILE = fr"{os.curdir}/resources/user/user_data.json"
CONTAMINANT_DATA_FILE = fr"{os.curdir}/resources/Water_Contaminant_MCLs.xlsx"
CUMULATIVE_RESULTS_FILE = fr"{os.curdir}/resources/Cumulative_User_Results.xlsx"
WATER_SYSTEM_DATA_FILE = f"{os.curdir}/resources/PWS_By_Municipality.xlsx"
CONTACT_INFO_DATA_FILE = fr"{os.curdir}/resources/PWS_Contact_Info.xlsx"
IN_APP_RESOURCES_DATA_FILE = fr"{os.curdir}/resources/InAppResources.xlsx"
MAP_FILE = fr"{os.curdir}/resources/geographical/map.html"
MUNICIPALITIES_DATA_FILE = fr"{os.curdir}/resources/geographical/municipalities_data.geojson"
COUNTIES_DATA_FILE = fr"{os.curdir}/resources/geographical/counties_data.geojson"


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
    "nj_american_water": fr"{ICON_PATH}/nj_am_water_icon.jpg"
}

APP_TEXT = {
    "start_screen": {},
    "home_screen": {
        "title": {
            "en": "Home",
            "es": "Hogar"
        },
        "major_news_feed": {
            "en": "See general news and other current articles below concerning water in NJ.",
            "es": "Vea las noticias y otros artículos actuales a continuación sobre el agua en Nueva Jersey."
        },
        "your_system_feed": {
            "en": "Find recent news from your water system below.",
            "es": ""
        }
    },
    "map_screen": {
        "title": {
            "en": "Map",
            "es": "Mapa"
        },
    },
    "waterquality_screen": {
        "title": {
            "en": "My Water",
            "es": "Mi Agua"
        },    
    },
    "watertestinput_screen": {},
    "watercontaminantselection_screen": {},
    "results_screen": {
        "title": {
            "en": "My Water Test Results",
            "es": "Resultados de Mi Prueba de Agua"
        },      
    },
    "resources_screen": {
        "title": {
            "en": "Educational Resources",
            "es": "Recursos Educativos"
        },   
        "overview": {
            "en": "Interested in learning more about water in NJ? Use the links below to find helpful resources on water contaminants, water quality efforts in NJ, and what you could to do get involved with your drinking water quality.",
            "es": "¿Está interesado en aprender más sobre el agua en Nueva Jersey? Utilice los enlaces a continuación para encontrar recursos útiles sobre los contaminantes del agua, los esfuerzos por la calidad del agua en Nueva Jersey y lo que podría hacer para involucrarse con la calidad del agua potable."
        },
        "educational": {
            "en": "Find general learning resources here.",
            "es": "Encuentre recursos de aprendizaje generales aquí."
        },
        "contaminants": {
            "en": "Learn about common water contaminants here.",
            "es": "Obtenga más información sobre los contaminantes comunes del agua aquí."
        },
        "tools": {
            "en": "These useful tools can help you learn more about your water system and drinking water quality.",
            "es": "Estas útiles herramientas pueden ayudarle a aprender más sobre su sistema de agua y la calidad del agua potable."
        }
    },
    "communication_screen": {
        "title": {
            "en": "Communication & Feedback",
            "es": "Comunicación y Comentarios"
        },   
        "overview": {
            "en": "Have concerns or feedback regarding your water? Use the menus below to help with finding assistance or with reaching out to your local officials.",
            "es": "¿Tiene inquietudes o comentarios sobre su agua? Utilice los menús a continuación para ayudar a encontrar asistencia o comunicarse con sus funcionarios locales."
        },
    },
}

NEWS_SITES = {
    "en": {
        "nj_future": "https://www.njfuture.org/feed/",
        "njdep": "https://dep.nj.gov/newsrel/feed/",
        "nj_american_water": "https://api.client.notified.com/api/rss/publish/view/39558?type=blog"
    },
    "es": {
        
    },
}

NEWS_KEY_WORDS = [
    "water and sewer",
    "water infrastructure",
    "clean water",
    "drinking water and clean water state revolving funds",
    "local waterways",
    "water",
    "drinking",
    "watershed",
    "watershed",
    "waterway",
    "waterways"
]