# Testing usage
from app.models.water_system_data import download_pdf, get_recent_CCR_by_water_system, extract_NJAW_alerts, get_DEP_events


if __name__ == "__main__":
    pdf_url = "https://www.amwater.com/ccr/littlefalls.pdf"
    save_as = "downloaded_sample.pdf"
    download_pdf(pdf_url)
    
    get_recent_CCR_by_water_system("NJ AMERICAN WATER - LOGAN")
    
    extract_NJAW_alerts()
    