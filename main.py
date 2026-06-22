from fastapi import FastAPI, HTTPException, Query
from typing import List
from models import AdMetrics, AIInsight
from services import fetch_and_normalize_ads, generate_optimization_insight

app = FastAPI(
    title="AI Ad Analytics Engine",
    description="Cross-platform AdTech API featuring data normalization and automated AI insights.",
    version="2.0.0"
)

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "AI Ad Analytics Engine"}

@app.get("/api/v1/ads", response_model=List[AdMetrics])
def get_standardized_ads(limit: int = Query(10, ge=1, le=100)):
    """Fetches and normalizes cross-platform ad data."""
    try:
        data = fetch_and_normalize_ads()
        return data[:limit]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch data from ad platforms.")

@app.post("/api/v1/ads/{campaign_id}/optimize", response_model=AIInsight)
def optimize_campaign(campaign_id: str):
    """Generates an AI-driven optimization insight for a specific campaign."""
    ads = fetch_and_normalize_ads()
    
    # Find the specific campaign
    target_ad = next((ad for ad in ads if ad.campaign_id == campaign_id), None)
    
    if not target_ad:
        raise HTTPException(status_code=404, detail="Campaign not found")
        
    insight_text = generate_optimization_insight(target_ad)
    return AIInsight(campaign_id=campaign_id, insight=insight_text)
