# Cyber-Security-Project-
# Website Security Checker

## Project Overview

Website Security Checker is a Python-based web application developed using Flask that performs a basic security assessment of websites. The tool analyzes HTTPS availability, SSL certificate validity, security headers, and generates a security score along with recommendations to improve website security.

This project demonstrates fundamental concepts of Web Security Assessment, Vulnerability Assessment, Secure Configuration Review, and Security Reporting commonly used in Cyber Security and Security Operations Center (SOC) environments.

---

## Features

### HTTPS Verification

* Checks whether the target website uses HTTPS.
* Identifies websites that do not have secure communication enabled.

### SSL Certificate Validation

* Retrieves SSL certificate information.
* Displays:

  * Certificate Issuer
  * Valid From Date
  * Expiry Date
  * Days Remaining
  * Certificate Status

### Security Header Analysis

Checks for the presence of important security headers:

| Header                    | Purpose                        |
| ------------------------- | ------------------------------ |
| Strict-Transport-Security | Forces HTTPS communication     |
| Content-Security-Policy   | Protects against XSS attacks   |
| X-Frame-Options           | Prevents Clickjacking          |
| X-Content-Type-Options    | Prevents MIME-Type attacks     |
| Referrer-Policy           | Controls information leakage   |
| Permissions-Policy        | Restricts browser capabilities |

### Security Score Calculation

Assigns a score based on implemented security controls.

| Security Check                 | Points |
| ------------------------------ | ------ |
| HTTPS Enabled                  | 20     |
| Valid SSL Certificate          | 20     |
| HSTS Present                   | 10     |
| CSP Present                    | 15     |
| X-Frame-Options Present        | 10     |
| X-Content-Type-Options Present | 10     |
| Referrer-Policy Present        | 10     |
| Permissions-Policy Present     | 5      |

### Risk Rating

| Score Range | Rating            |
| ----------- | ----------------- |
| 80 – 100    | Secure            |
| 60 – 79     | Moderate          |
| Below 60    | Needs Improvement |

### Security Recommendations

Provides actionable recommendations for missing security controls.

### Report Generation

Generates a TXT report containing:

* Scan Date
* Website URL
* HTTPS Status
* SSL Information
* Security Header Analysis
* Security Score
* Security Recommendations

---

## Technologies Used

### Programming Language

* Python 3.x

### Framework

* Flask

### Libraries

* requests
* ssl
* socket
* datetime
* reportlab (optional)

### Frontend

* HTML5
* CSS3

---

## Project Structure

Website Security Checker

├── app.py

├── scanner.py

├── report_generator.py

├── static

│ └── style.css

├── templates

│ ├── index.html

│ └── result.html

└── reports

---

## Installation

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Ensure that "Add Python to PATH" is selected during installation.

---

### Step 2: Install Required Packages

Open Command Prompt and execute:

python -m pip install flask requests reportlab

---

### Step 3: Navigate to Project Folder

Example:

cd "C:\Users\prati\OneDrive\Desktop\Website Secuirity Checker"

---

### Step 4: Run the Application

python app.py

Expected Output:

* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000

---

### Step 5: Open the Application

Open a web browser and navigate to:

http://127.0.0.1:5000

---

## Usage

1. Launch the application.
2. Enter a website URL or domain name.
3. Click "Scan Website".
4. View:

   * HTTPS Status
   * SSL Certificate Information
   * Security Headers
   * Security Score
   * Risk Rating
   * Recommendations
5. Review the generated report in the reports folder.

---

## Sample Input

google.com

---

## Sample Output

HTTPS Status:
HTTPS Enabled

SSL Status:
Valid

Security Score:
95/100

Risk Rating:
Secure

Recommendations:
Implement any missing security headers.

---

## Learning Outcomes

### Cyber Security Concepts

* HTTPS Security
* SSL/TLS Certificates
* Security Headers
* Vulnerability Assessment
* Secure Configuration Review

### SOC Concepts

* Security Monitoring
* Risk Assessment
* Security Reporting

### Technical Skills

* Python Programming
* Flask Development
* HTTP Requests
* SSL Inspection
* Report Generation

---

## Future Enhancements

* PDF Report Generation
* HTML Report Export
* Batch Website Scanning
* OWASP Security Header Grading
* Dashboard Analytics
* Historical Scan Records
* Database Integration
* Real-Time Monitoring
* Email Report Delivery

---

## Limitations

* Performs basic security checks only.
* Does not perform vulnerability scanning.
* Does not detect server-side vulnerabilities.
* Results depend on publicly accessible website configurations.

---

## Author

Project Title: Website Security Checker

Developed Using:
Python, Flask, HTML, CSS

Academic Use:
Cyber Security / CEH / SOC Mini Project

---

## Disclaimer

This tool is intended for educational and security assessment purposes only. It performs passive security checks and does not exploit, attack, or modify any target website.

