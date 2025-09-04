from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

API_KEY = os.getenv("NEWSAPI_KEY")
BASE_URL = os.getenv("NEWSAPI_BASE_URL")

# Home route (default = general)
@app.route("/")
@app.route("/<category>")
def home(category="general"):
    url = f"{BASE_URL}?country=us&category={category}&apiKey={API_KEY}"
    r = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=bab3d307ecb24f41a4dfb30937be3f34").json()

    news = r.get("articles", [])
    categories = ["general", "business", "entertainment", "health", "science", "sports", "technology"]

    return render_template(
        "index.html",
        allNews=news,
        active_category=category,
        categories=categories
    )

if __name__ == '__main__':
    app.run(debug=True)
