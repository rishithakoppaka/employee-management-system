# Repository Structure

## 📁 Clean GitHub Repository Structure

```
employee-management-system/
├── .env.example              # Environment configuration template
├── .gitignore                # Git ignore rules (excludes .env, cache, etc.)
├── README.md                 # Main project documentation
├── requirements.txt          # Python dependencies
├── pytest.ini               # Pytest configuration
├── docker-compose.yml        # Docker PostgreSQL setup
├── postman_collection.json   # Postman API collection
│
├── main.py                   # FastAPI backend application
├── streamlit_app.py          # Streamlit frontend application
│
├── db/                       # Database layer
│   ├── __init__.py
│   └── db_utils.py          # Database connection & CRUD operations
│
├── models/                   # Object-Oriented Programming classes
│   ├── __init__.py
│   ├── person.py            # Base Person class
│   ├── employee.py          # Employee class (inherits Person)
│   └── hr_manager.py        # HRManager class
│
└── tests/                    # Test suite
    ├── __init__.py
    ├── test_api.py          # Backend API tests
    └── test_ui_logic.py     # Frontend logic tests
```

## ✅ Environment Configuration

### `.env.example` - Template File
Contains all required environment variables with example values:
- Database configuration (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD)
- API configuration (API_HOST, API_PORT, API_BASE_URL)
- Instructions for setup

### `.env` - Actual Configuration (NOT in repo)
- Excluded by `.gitignore`
- Contains actual credentials
- Created by copying `.env.example`

## 🔒 Security

### Files Excluded from Git (`.gitignore`)
- `.env` - Environment variables with secrets
- `__pycache__/` - Python cache files
- `.pytest_cache/` - Test cache
- `*.pyc` - Compiled Python files
- Virtual environments
- IDE files
- Log files
- Database files

## 📋 Key Files

### Core Application
- **main.py**: FastAPI backend with REST endpoints
- **streamlit_app.py**: Streamlit frontend UI
- **db/db_utils.py**: Database operations (CRUD, statistics)

### Configuration
- **requirements.txt**: All Python dependencies
- **.env.example**: Environment variable template
- **docker-compose.yml**: PostgreSQL Docker setup

### Documentation
- **README.md**: Complete setup and usage guide
- **PROJECT_WALKTHROUGH.md**: Detailed technical walkthrough

### Testing
- **tests/test_api.py**: Backend endpoint tests
- **tests/test_ui_logic.py**: Frontend logic tests
- **pytest.ini**: Pytest configuration

## 🚀 Quick Start

1. **Clone repository**
   ```bash
   git clone https://github.com/rishithakoppaka/employee-management-system.git
   cd employee-management-system
   ```

2. **Setup environment**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start database**
   ```bash
   docker-compose up -d
   ```

5. **Run application**
   ```bash
   # Terminal 1: Backend
   uvicorn main:app --reload --port 8001
   
   # Terminal 2: Frontend
   streamlit run streamlit_app.py
   ```

## 📊 Repository Stats

- **Language**: Python
- **Framework**: FastAPI, Streamlit
- **Database**: PostgreSQL
- **Testing**: Pytest
- **Structure**: Clean, modular, well-organized

