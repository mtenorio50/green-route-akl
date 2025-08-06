# Project Master Plan Content
## GreenRoute AKL — Project Master Plan
### GreenRoute AKL is an intelligent transport platform for Auckland that blends real-time data, predictive analytics, and carbon insights to help commuters travel smarter and city planners build a greener, more efficient city.

1. Main Objectives
- To create a data-powered, intelligent transportation platform for Auckland, empowering commuters to travel faster, smarter, and greener.
- To provide city planners with actionable insights to improve public transport and reduce urban congestion and emissions.
- To build a project that demonstrates real-world impact and advanced technical skills, making me stand out to employers in New Zealand.

2. MVP & Their Strong Why

a. Smart Route Planner (for Public Users)
- Why: Aucklanders waste time in traffic and on unreliable public transport. Fast, data-informed route recommendations save users time and frustration.

b. Travel Time & Delay Prediction (AI-powered)
- Why: Predicting delays with historic and live data gives users confidence in their plans and sets this app apart from basic planners like AT Mobile.

c. Carbon Footprint Calculator
- Why: There’s increasing demand for eco-friendly options. Helping users see the impact of their choices nudges Auckland toward sustainability.

d. Planner Dashboard (for City/Transport Planners)
- Why: Data visualizations and hotspots help planners identify and fix pain points, improving the city’s infrastructure with real evidence.

3. Tech Stack

- Backend: Python (FastAPI), scikit-learn, Pandas, SQLAlchemy
- Database: Supabase (PostgreSQL managed)
- Frontend: React (web, mobile-friendly)
- Data Viz: Recharts, React-Leaflet
- APIs/Data Sources: Auckland Transport (GTFS/real-time), Waka Kotahi NZTA, Auckland Open Data
- Hosting/DevOps: Supabase (DB), Vercel or Netlify (Frontend), Railway.app/Render (Backend API)
- Authentication: Supabase Auth or JWT (for simple login)

4. Target Users & Impact

- Public Commuters: Need reliable, fast, and eco-friendly transport options.
- City Planners: Need real-time and historic analytics to make data-driven decisions for urban transport improvements.
- Auckland as a City: Reducing congestion and emissions is a win for everyone.

5. Data Sources

- AT Open Data Portal (https://dev-portal.at.govt.nz/)
- Waka Kotahi NZTA APIs (https://opendata-nzta.opendata.arcgis.com/)
- Auckland Council Open Data (https://data.aucklandcouncil.govt.nz/)

6. System Architecture Overview

- Backend: Connects to live & historic transport data, runs ML predictions, exposes REST APIs.
- Database: Stores users, routes, trips, analytics.
- Frontend: Responsive React app for public and dashboard for planners.
- ML: Predicts delays, estimates carbon footprint.

7. Future Features / Roadmap

- User-generated reports (crowdsourced data)
- Personalized commute tips
- Gamified eco challenges
- Mobile app (PWA or native)
- Integration with bike/scooter/ride-share

8. Success Metrics

- X number of users plan a trip weekly
- Prediction accuracy of delay/ETA
- Reduction in average reported commute time
- Planner dashboard actively used by stakeholders

9. Challenges & Risks

- Real-time data reliability
- Scaling ML predictions with growing data
- User privacy/security for location data
- Balancing MVP focus vs. feature creep
