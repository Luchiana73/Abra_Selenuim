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
- `settings.py` – configuration (loaded from environment variables)

## How to Run Tests Locally

1. Clone the repository:
```
git clone https://github.com/Luchiana73/Abra_Selenuim.git

```
2. Create environment variables

Create a `.env` file based on `.env.example` and fill in your test credentials.

Some tests (e.g. login and account-related tests) require **pre-created and confirmed user accounts**.  
Please register test accounts manually via the application UI and provide their credentials in the `.env` file.
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
- Explicit waits are used to improve test stability.
