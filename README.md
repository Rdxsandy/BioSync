# System Architecture
BioSync follows a modern client–server architecture designed to separate the user interface, application logic, and data management into independent layers. This structure improves scalability, maintainability, and performance
The system integrates lifestyle tracking, AI-powered analysis, and machine learning predictions to generate health insights for users.

The architecture consists of four primary layers:
### 1-Frontend (Client Layer)
### 2-Backend (API Layer)
### 3-Database Layer
### 4-AI / Machine Learning Services

## 1. Frontend Layer

The frontend is responsible for the user interface and user interaction.

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

Each module typically contains:

- `routes.py` – API endpoints  
- `service.py` – business logic  
- `schemas/` – request and response models  
