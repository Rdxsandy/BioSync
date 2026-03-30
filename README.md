# BioSync – AI-Based Health Tracking System
## Project Overview

BioSync is an AI-powered health tracking system that monitors user lifestyle activities such as meals, physical activity, and daily habits to generate personalized health insights. The system integrates lifestyle tracking, AI-powered analysis, and machine learning predictions to help users understand and improve their health.

The platform uses a modern client–server architecture to ensure scalability, maintainability, and performance. BioSync provides a dashboard that visualizes health data and displays AI-generated recommendations.

## Architecture Diagram

BioSync follows a layered architecture consisting of four main layers:

### Frontend (Client Layer)
### Backend (API Layer)
### Database Layer
### AI / Machine Learning Services
### Architecture Flow

User → Frontend (React) → Backend (FastAPI) → Database (MongoDB)
                              ↓
                         AI/ML Services → Predictions → Backend → Frontend Dashboard


## Technology Stack

### React
### Vite
### Axios
### JWT Authentication

## Responsibilities

#### User authentication (login / signup)
#### Activity tracking interface
#### Meal image upload
#### Dashboard visualization
#### Display AI-generated health insights
#### Communicate with backend APIs

The frontend sends HTTP requests to the FastAPI backend using Axios and includes the JWT token in request headers for secure communication.

## 1. Backend Layer

The backend is built using **FastAPI**, which provides high-performance asynchronous APIs for handling application logic and data processing.

### Responsibilities

- Authentication and JWT validation  
- User data management  
- Activity tracking logic  
- Meal image processing  
- Machine learning prediction execution  
- AI-generated health insights  
- Dashboard data aggregation  

The backend follows a **modular architecture** to keep the code organized and maintainable.

Example backend structure:

backend/
 ├── auth/
 ├── activity/
 ├── meals/
 ├── dashboard/
 ├── health/
 ├── ml/
 └── database/

 ## API Documentation

The backend APIs are documented using FastAPI Swagger UI.

![FastAPI Docs](docs/images/Screenshot%202026-03-29%20123954.png)
![FastAPI Docs](docs/images/Screenshot%202026-03-29%20125242.png)
![FastAPI Docs](docs/images/Screenshot%202026-03-29%20125516.png)
![FastAPI Docs](docs/images/Screenshot%202026-03-29%20125630.png)

Each module typically contains:

- `routes.py` – API endpoints  
- `service.py` – business logic  
- `schemas/` – request and response models

  

Added  setup instructions

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```


## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Environment Setup

Create a `.env` file in backend:

```bash
MONGODB_URL=your_mongodb_url
SECRET_KEY=your_secret
HF_TOKEN=your_token
```


Added end-to-end project execution steps for frontend and backend

## How to Run

1. Start backend server  
2. Start frontend server  
3. Open browser at http://localhost:5173  




