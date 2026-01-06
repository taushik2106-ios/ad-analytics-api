from fastapi import FastAPI
from data import ads_data

app = FastAPI(title="Ad Analytics API")

@app.get("/")
def home():
    return {"message": "Ad Analytics API is running"}

@app.get("/ads")
def get_ads():
    return ads_data

@app.get("/analytics")
def analytics():
    insights = []
    for ad in ads_data:
        ctr = round((ad["clicks"] / ad["impressions"]) * 100, 2)
        insights.append({
            "campaign": ad["campaign"],
            "CTR (%)": ctr
        })
    return insights
