import os
import openai
from tenacity import retry, wait_exponential, stop_after_attempt
from models import AdMetrics
from data import raw_external_ads_data

# Use python-dotenv in production to load this securely
openai.api_key = os.getenv("OPENAI_API_KEY", "mock-key-for-now")

@retry(wait=wait_exponential(multiplier=1, min=1, max=5), stop=stop_after_attempt(3))
def fetch_and_normalize_ads() -> list[AdMetrics]:
    """Simulates fetching from external APIs with retry logic, then normalizes the data."""
    normalized_data = []
    
    for raw in raw_external_ads_data:
        if raw.get("source") == "google":
            clicks = raw["clicks_count"]
            impressions = raw["views"]
            spend = raw["cost"]
            
            normalized_data.append(AdMetrics(
                campaign_id=raw["campaign_id"],
                platform="Google Ads",
                campaign_name=raw["name"],
                impressions=impressions,
                clicks=clicks,
                spend=spend,
                ctr=round((clicks / impressions) * 100, 2) if impressions > 0 else 0.0,
                cpc=round(spend / clicks, 2) if clicks > 0 else 0.0
            ))
            
        elif raw.get("source") == "meta":
            clicks = raw["link_clicks"]
            impressions = raw["impressions"]
            spend = raw["spend"]
            
            normalized_data.append(AdMetrics(
                campaign_id=raw["id"],
                platform="Meta Ads",
                campaign_name=raw["campaign_name"],
                impressions=impressions,
                clicks=clicks,
                spend=spend,
                ctr=round((clicks / impressions) * 100, 2) if impressions > 0 else 0.0,
                cpc=round(spend / clicks, 2) if clicks > 0 else 0.0
            ))
            
    return normalized_data

def generate_optimization_insight(metrics: AdMetrics) -> str:
    """Generates an AI recommendation based on standardized metrics."""
    
    # --- REAL AI IMPLEMENTATION (Uncomment when you have an API key) ---
    # prompt = f"Act as an AdTech AI. Provide a 1-sentence optimization for this campaign: Platform: {metrics.platform}, CTR: {metrics.ctr}%, CPC: ${metrics.cpc}"
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return response.choices[0].message.content.strip()
    # -------------------------------------------------------------------
    
    # MOCK AI IMPLEMENTATION (So the project runs out of the box for recruiters)
    if metrics.ctr > 5.0 and metrics.cpc < 0.40:
        return "High performance detected. Recommend increasing daily budget by 15% to scale conversions."
    elif metrics.ctr < 3.0:
        return "Below average CTR. Recommend pausing ad and A/B testing new creative assets."
    else:
        return "Campaign is stable. Continue monitoring for audience fatigue."
