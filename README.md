# 🧪 Abra_Selenium

Automated testing of the **Abra** web application using **Python** and **Selenium WebDriver**.  
This project demonstrates practical skills in **UI test automation** following best QA practices.

---

## 📋 Project Overview

The purpose of this project is to validate core functionality of the Abra web platform through automated browser tests.  
The test suite checks:
- Visibility and behavior of UI elements  
- Login and authentication flow  
- Navigation between sections  
- Error handling for invalid input  

---

## 🧰 Tech Stack

| Tool / Library | Purpose |
|----------------|----------|
| **Python 3.x** | Core programming language |
| **Selenium WebDriver** | Browser automation |
| **Pytest** | Test runner and structure |
| **ChromeDriver / GeckoDriver** | Browser drivers |
| **Page Object Model (POM)** | Test architecture pattern |

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```
bash
git clone https://github.com/Luchiana73/Abra_Selenium.git
cd Abra_Selenium
```
2️⃣ Install dependencies
```
pip install -r requirements.txt
```
3️⃣ Configure the driver
Make sure ChromeDriver or GeckoDriver is installed and added to your system PATH.

4️⃣ Run the tests
```
pytest -v
```

## 🧪 Project Structure
```
bash
Abra_Selenium/
│
├── pages/              # Page Object files
├── tests/              # Test scripts
├── conftest.py         # Pytest configuration
├── requirements.txt    # Dependencies
└── README.md
```

## 📈 Possible Improvements
1.Add test reporting (Allure, HTMLTestReport)
2.Integrate CI/CD (GitHub Actions)
3.Add test data parametrization
4.Extend coverage with API tests (REST / GraphQL)
5.Include Docker setup for reproducible runs

## 🧩 Key QA Concepts Used
1.Page Object Model (POM)
2.Test isolation and fixtures (Pytest)
3.Browser synchronization (implicit / explicit waits)
4.Assertions and error validation
5.Structured test naming and maintainability

👩‍💻 Author
Luchiana73

QA Automation Engineer

Python • Selenium • Pytest • GitHub Actions

📫 Open to collaborations and QA automation projects.




