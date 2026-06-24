# app.py
print("APP STARTED")
from flask import Flask
from flask import render_template
from flask import request

from scanner import *
from report_generator import generate_txt_report

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():

    url = request.form["url"]

    url = normalize_url(url)

    hostname = urlparse(url).hostname

    https_enabled = check_https(url)

    ssl_info = get_ssl_info(hostname)

    headers = check_headers(url)

    ssl_valid = False

    if "status" in ssl_info:
        ssl_valid = ssl_info["status"] == "Valid"

    score = calculate_score(
        https_enabled,
        ssl_valid,
        headers
    )

    rating = risk_rating(score)

    recommendations = generate_recommendations(headers)

    data = {
        "url": url,
        "https": https_enabled,
        "ssl": ssl_info,
        "headers": headers,
        "score": score,
        "rating": rating,
        "recommendations": recommendations
    }

    report_file = generate_txt_report(data)

    return render_template(
        "result.html",
        result=data,
        report=report_file
    )


if __name__ == "__main__":

    app.run(debug=True)