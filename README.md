# Order Integration Testing Framework

## Stack
- Python 3.10
- Pytest
- Selenium (UI)
- PostgreSQL (DB validation)
- CORBA (stub via omniORB concept)
- Allure reports

---

## Architecture
- Page Object Model (UI layer)
- Service layer (business logic)
- Core layer (DB + CORBA clients)

---

## Running tests

```bash
pip install -r requirements.txt
pytest --alluredir=allure-results
