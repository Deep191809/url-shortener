from flask import Flask, render_template, request, redirect
from db import (
    insert_url,
    get_url_by_short_id,
    get_short_id_by_original_url,
    get_last_urls,
    get_total_pages
)
import string
import random

app = Flask(__name__)
CUSTOM_PATH = "/psquare_lab_iitr"

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route(f"{CUSTOM_PATH}/", methods=["GET", "POST"])
def home():
    short_id = None
    page = int(request.args.get('page', 1))
    per_page = 5
    theme = request.form.get("theme") if request.method == "POST" else "light"

    if request.method == "POST":
        original_url = request.form["original_url"].strip()
        if not original_url:
            return render_template("index.html",
                                   short_id=None,
                                   urls=get_last_urls(offset=(page - 1) * per_page, limit=per_page),
                                   page=page,
                                   total_pages=get_total_pages(per_page),
                                   path=CUSTOM_PATH,
                                   theme=theme)

        # Check if this URL is already shortened
        existing_short_id = get_short_id_by_original_url(original_url)
        if existing_short_id:
            short_id = existing_short_id
        else:
            short_id = generate_short_id()
            insert_url(original_url, short_id)

    urls = get_last_urls(offset=(page - 1) * per_page, limit=per_page)
    total_pages = get_total_pages(per_page)

    return render_template("index.html",
                           short_id=short_id,
                           urls=urls,
                           page=page,
                           total_pages=total_pages,
                           path=CUSTOM_PATH,
                           theme=theme)

@app.route(f"{CUSTOM_PATH}/<short_id>")
def redirect_to_original(short_id):
    original_url = get_url_by_short_id(short_id)
    if original_url:
        # Ensure it includes a valid scheme
        if not original_url.startswith(("http://", "https://")):
            original_url = "http://" + original_url
        return redirect(original_url)
    else:
        return "Invalid URL", 404

if __name__ == "__main__":
    print(f"🚀 Click to open: http://127.0.0.1:5000{CUSTOM_PATH}/")
    app.run(debug=True)
