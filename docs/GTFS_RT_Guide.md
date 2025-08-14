# Auckland Transport Real-time API Information

## Current Situation:
Your current API key (2fa50e2cd58543a9bc6cb06aa5da8989) appears to be on a basic/free tier that only provides:
- Static GTFS data (stops, routes, schedules)
- No real-time vehicle positions

## To Get Real-time Data:

### 1. Upgrade Auckland Transport API Subscription
- Visit: https://dev-portal.at.govt.nz/
- Log into your account
- Check available subscription tiers
- Look for plans that include:
  - Real-time vehicle positions
  - Trip updates  
  - Service alerts

### 2. Typical Real-time Endpoints (when available):
- GET /realtime/v1/vehicle-positions
- GET /realtime/v1/trip-updates
- GET /realtime/v1/alerts

### 3. Cost Considerations:
- Free tier: Usually static data only
- Paid tiers: Real-time data, higher rate limits
- Commercial: Full access, SLA guarantees

## Alternative Data Sources:

### 1. Open Data Portals
- Auckland Open Data: https://data.govt.nz/
- Some cities provide free GTFS-RT feeds

### 2. Third-party Transit APIs
- TransitLand: https://www.transit.land/
- OpenTripPlanner: Real-time capable
- Citymapper API: Commercial but comprehensive

### 3. Web Scraping (Use Carefully)
- AT Mobile website
- Real-time boards at stops
- Note: Check terms of service!

## Implementation Steps:

1. Contact Auckland Transport
2. Request real-time API access
3. Understand pricing structure
4. Test endpoints in development
5. Implement caching for production
