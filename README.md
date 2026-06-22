# AI Ad Analytics Engine (FastAPI)

## Overview
This project is an AdTech-focused REST API built with FastAPI. It simulates the ingestion of unstructured, cross-platform ad data (e.g., Google Ads, Meta Ads), normalizes it into a strict unified schema, and utilizes an AI service to generate automated budget and performance optimization insights.

## Core Features
- **Cross-Platform Data Normalization:** Ingests varying JSON structures from different platforms and maps them to a single `AdMetrics` Pydantic model.
- **AI-Driven Optimization Endpoint:** Evaluates specific campaign metrics (CTR, CPC) to generate actionable automation recommendations.
- **Resilient Architecture:** Implements exponential backoff (`tenacity`) to handle simulated API rate limits from external ad networks.
- **Production-Ready Endpoints:** Utilizes FastAPI features like `response_model`, `Query` pagination, and comprehensive HTTP error handling.

## Technologies Used
- Python 3
- FastAPI & Uvicorn
- Pydantic (Data Validation)
- Tenacity (Exponential Backoff/Retry Logic)
- OpenAI API (Generative Insights)

## API Endpoints
- `GET /` – API health check  
- `GET /api/v1/ads?limit=10` – Returns paginated, normalized campaign data  
- `POST /api/v1/ads/{campaign_id}/optimize` – Returns an AI-generated insight for the specified campaign

## Installation & Execution
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn main:app --reload`
4. Access the interactive Swagger documentation at `http://127.0.0.1:8000/docs`
