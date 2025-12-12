# Abra Selenium Test Automation Project

This repository contains automated UI tests for the Abra web application, built using **Python, Selenium WebDriver and Pytest**.

## Project Overview

The project covers:
- User registration (supplier and seller)
- Login flow validation
- Main page navigation
- End-to-end supplier account creation and setup

The tests are written using the **Page Object Model (POM)** approach.

## Tech Stack

- Python 3
- Selenium WebDriver
- Pytest
- Requests (for email confirmation handling)
- dotenv (environment variables)

## Project Structure

- `pages/` – Page Object classes
- `tests/` – UI and E2E test cases
- `support/` – helpers (temporary email, utilities)
- `settings.py` – configuration via environment variables

## How to Run Tests Locally

1. Clone the repository:
```
git clone https://github.com/your-username/Abra_Selenium.git
cd Abra_Selenium
```
2. Create a .env file in the project root and provide your test data:
```
BASE_URL=https://dev.marketabra.com
SUPPLIER_EMAIL=your_test_supplier@email.com
SELLER_EMAIL=your_test_seller@email.com
PASSWORD=your_password
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run tests:
```
pytest
```
## Notes

- Sensitive data is not stored in the repository.
- Tests that require authentication expect valid test accounts.
- Temporary email services are used for registration confirmation in E2E flows.