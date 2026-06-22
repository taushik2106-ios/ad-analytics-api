from pydantic import BaseModel

class AdMetrics(BaseModel):
    campaign_id: str
    platform: str
    campaign_name: str
    impressions: int
    clicks: int
    spend: float
    ctr: float
    cpc: float

class AIInsight(BaseModel):
    campaign_id: str
    insight: str
