# OrangeHRM Test Automation Framework

End-to-end test automation framework built with Python and Playwright,
targeting the OrangeHRM demo application.

## Tech Stack
- Python 3.x
- Playwright (Python)
- Pytest
- Page Object Model (POM)
- GitHub Actions (CI/CD) — coming soon

## Project Structure
tests/
ui/          → UI test cases
api/         → API test cases
pages/         → Page Object Models
test-data/     → Test data files
conftest.py    → Pytest fixtures
requirements.txt
.gitignore
## How to Run
```bash
pip install -r requirements.txt
playwright install
pytest tests/ -v
```

## Test Coverage (In Progress)
- Login / Authentication flows
- Employee management (Add, Edit, Delete)
- API endpoint validation
- Cross-browser execution (Chromium, Firefox, WebKit)

## Author
Varun Deshpande
