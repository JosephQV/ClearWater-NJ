import folium
import webview
import logging
import pathlib
from branca.colormap import LinearColormap

from data.app_config import MAP_FILE, WINDOW_HEIGHT, WINDOW_WIDTH
from app.models.drinking_water_contaminant_data import construct_municipal_score_geodata, get_municipal_contaminant_geodata


logger = logging.getLogger(__name__)


nj_coords = (40.0583, -74.4057)
min_lat, max_lat = 38.5, 41.5
min_lon, max_lon = -76, -73
min_zoom = 8


class MapController:
    def __init__(self):
        self.setup_map()
        
    def setup_map(self):
        self.municipality_colormap = LinearColormap(colors=[(1., 0, 0, 1), (0, 1., 0, 1)], vmin=0, vmax=100)
        try:
            if not pathlib.Path(MAP_FILE).exists():
                municipal_gdf = get_municipal_contaminant_geodata()
                self.create_map(municipal_gdf)
            else:
                logger.info(f"Map file already exists, did not overwrite. Location: {MAP_FILE}")
        except Exception as e:
            logger.error(f"Failed to create map: {str(e)}")
        
    def load_map(self):
        webview.create_window(
            title="Water Quality Map", 
            url=MAP_FILE,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            resizable=True,
            on_top=True
        )
    
    def open_map(self):
        try:
            webview.start()
        except Exception as e:
            logger.error(f"Failed to open map: {str(e)}")
    
    def create_map(self, municipal_gdf):
        map = folium.Map(
            location=nj_coords, 
            zoom_start=min_zoom,
            min_zoom=min_zoom,
            max_bounds=True,
            min_lat=min_lat,
            max_lat=max_lat,
            min_lon=min_lon,
            max_lon=max_lon,
            bounds=[[min_lat, min_lon], [max_lat, max_lon]]
        )

        layer2 = folium.FeatureGroup(
            name="Municipalities", 
            control=True
        )

        folium.GeoJson(
            data=municipal_gdf,
            style_function=self.municipalities_style_function,
            popup=folium.GeoJsonPopup(
                fields=["NAME", "Inorganic Chemicals Formatted", "Organic Chemicals Formatted", "Microorganisms Formatted", "Disinfection Byproducts Formatted", "Disinfectants Formatted", "PFAS Formatted", "Radionuclides Formatted", "Overall Formatted"],
                aliases=["Municipality", "Inorganic Chemicals Score", "Organic Chemicals Score", "Microorganisms Score", "Disinfection Byproducts Score", "Disinfectants Score", "PFAS Score", "Radionuclides Score", "Overall Score"],
            )
        ).add_to(layer2)

        layer2.add_to(map)
        
        folium.LayerControl(
            collapsed=False
        ).add_to(map)
        
        map.save(MAP_FILE)
    
    def municipalities_style_function(self, feature):
        return {
            'fillColor': self.municipality_colormap(feature["properties"]["Overall Score"]),  # Fill color of the polygon
            'color': '#000000',    # Border line color
            'weight': 1,           # Border line width
            'fillOpacity': 0.6,    # Transparency of the polygon fill
        }