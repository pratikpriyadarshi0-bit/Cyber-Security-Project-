# scanner.py

import requests
import ssl
import socket

from urllib.parse import urlparse
from datetime import datetime


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


def normalize_url(url):

    if not url.startswith("http"):
        url = "https://" + url

    return url


def check_https(url):

    if url.startswith("https://"):
        return True

    return False


def get_ssl_info(hostname):

    try:

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443)) as sock:

            with context.wrap_socket(
                    sock,
                    server_hostname=hostname) as ssock:

                cert = ssock.getpeercert()

        issuer = dict(x[0] for x in cert['issuer'])

        issuer_name = issuer.get('organizationName', 'Unknown')

        valid_from = cert['notBefore']
        valid_to = cert['notAfter']

        start_date = datetime.strptime(
            valid_from,
            "%b %d %H:%M:%S %Y %Z"
        )

        end_date = datetime.strptime(
            valid_to,
            "%b %d %H:%M:%S %Y %Z"
        )

        days_remaining = (end_date - datetime.now()).days

        status = "Valid"

        if days_remaining < 0:
            status = "Expired"

        return {
            "issuer": issuer_name,
            "valid_from": start_date,
            "valid_to": end_date,
            "days_remaining": days_remaining,
            "status": status
        }

    except Exception as e:

        return {
            "error": str(e)
        }


def check_headers(url):

    results = {}

    try:

        response = requests.get(url, timeout=10)

        headers = response.headers

        for header in SECURITY_HEADERS:

            if header in headers:
                results[header] = "Present"
            else:
                results[header] = "Missing"

    except:

        for header in SECURITY_HEADERS:
            results[header] = "Error"

    return results


def calculate_score(https_enabled,
                    ssl_valid,
                    header_results):

    score = 0

    if https_enabled:
        score += 20

    if ssl_valid:
        score += 20

    if header_results["Strict-Transport-Security"] == "Present":
        score += 10

    if header_results["Content-Security-Policy"] == "Present":
        score += 15

    if header_results["X-Frame-Options"] == "Present":
        score += 10

    if header_results["X-Content-Type-Options"] == "Present":
        score += 10

    if header_results["Referrer-Policy"] == "Present":
        score += 10

    if header_results["Permissions-Policy"] == "Present":
        score += 5

    return score


def risk_rating(score):

    if score >= 80:
        return "Secure"

    elif score >= 60:
        return "Moderate"

    else:
        return "Needs Improvement"


def generate_recommendations(headers):

    recommendations = []

    mapping = {
        "Strict-Transport-Security":
            "Enable HSTS header.",
        "Content-Security-Policy":
            "Implement CSP to reduce XSS risk.",
        "X-Frame-Options":
            "Enable X-Frame-Options to prevent clickjacking.",
        "X-Content-Type-Options":
            "Enable X-Content-Type-Options.",
        "Referrer-Policy":
            "Add Referrer-Policy header.",
        "Permissions-Policy":
            "Add Permissions-Policy header."
    }

    for h, status in headers.items():

        if status == "Missing":
            recommendations.append(mapping[h])

    return recommendations