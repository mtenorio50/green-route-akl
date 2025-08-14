# Project Master Plan Content
## GreenRoute AKL — Project Master Plan
### GreenRoute AKL is an intelligent transport platform for Auckland that blends real-time data, predictive analytics, and carbon insights to help commuters travel smarter and city planners build a greener, more efficient city.

### The name “GreenRoute AKL” was chosen because this project is all about helping Aucklanders (AKL) find the fastest, smartest, and greenest ways to travel. It’s not just a route planner; it’s a step toward a more sustainable Auckland, using real-time data and analytics to optimize commutes for both people and the planet

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

# GreenRoute AKL – Project Roadmap

## Phase 1: Foundation & Setup (Week 1–2)
- Set up project repository and folder structure
- Establish coding conventions and standards
- Publish initial README, documentation, and project plan
- Register and confirm access to required APIs (AT, NZTA, Council)
- Onboard team members (if applicable)

---

## Phase 2: Data & Backend MVP (Week 2–5)
- Develop data ingestion scripts for Auckland Transport, NZTA, Council datasets
- Design and implement Supabase/PostgreSQL database schema
- Scaffold FastAPI backend
- Create REST endpoints for route planning, delay prediction, and carbon calculation
- Integrate basic ML model for delay prediction
- Set up authentication (Supabase Auth or JWT)

---

## Phase 3: Frontend MVP (Week 4–7)
- Scaffold React app for both public and planner users
- Create wireframes/mockups for journey planner and dashboard
- Develop journey planner UI (trip input, map, results)
- Integrate APIs: fetch and display real-time route and ETA information
- Add carbon calculator to trip results page
- Build planner dashboard UI (analytics, congestion maps)
- Ensure responsive/mobile-friendly design

---

## Phase 4: Testing, Quality, & Deployment (Week 6–8)
- Write unit and integration tests for backend and frontend
- Perform manual QA for all main user flows
- Conduct accessibility audit (WCAG)
- Deploy backend (Railway/Render), frontend (Vercel/Netlify), and database (Supabase)
- Complete documentation and setup guides

---

## Phase 5: Feedback & Iteration (Week 8–10)
- Enable in-app feedback tools
- Implement analytics for user actions and feature usage
- Conduct user and planner interviews/surveys
- Address major bugs and improvement requests
- Plan/prioritize next sprint(s) based on real feedback

---

## Phase 6: Enhancement & Stretch Goals (Post-MVP, Week 10+)
- Add user-generated incident reports
- Implement gamified eco challenges or reward systems
- Integrate micro-mobility/bike-share/ride-share routing
- Convert to PWA/mobile app
- Expand analytics and dashboard features
- Prepare codebase for open-source collaboration and scaling

---

## Ongoing: Maintenance & Growth
- Conduct regular security and privacy reviews
- Report progress and impact to stakeholders
- Optimize performance continuously
- Plan for wider rollout (city-wide or national)



