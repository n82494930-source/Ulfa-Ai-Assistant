import requests
import json
import os

APP_ID = os.getenv("ADZUNA_API_ID")
APP_KEY = os.getenv("ADZUNA_API_KEY")

SEEN_FILE = "data/seen_jobs.json"

def get_jobs(role = "data engineer",place = "liverpool"):
    url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 10,
        "what": role,
        "where": place
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []

    for job in data.get("results", []):
        title = job.get("title", "No title")
        company = job.get("company", {}).get("display_name", "Unknown company")
        location = job.get("location", {}).get("display_name", "Unknown location")
        salary_min = job.get("salary_min", "N/A")
        salary_max = job.get("salary_max", "N/A")
        link = job.get("redirect_url", "No link")

        jobs.append(
            f"\n📌 {title}\n"
            f"🏢 Company: {company}\n"
            f"📍 Location: {location}\n"
            f"💰 Salary: £{salary_min} - £{salary_max}\n"
            f"🔗 Apply: {link}"
        )

    if not jobs:
        return "No jobs found."

    return "\n".join(jobs)


def get_new_jobs():
    jobs = get_jobs()

    if not os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, "w") as f:
            json.dump([], f)

    with open(SEEN_FILE, "r") as f:
        seen_jobs = json.load(f)

    new_jobs = [job for job in jobs if job not in seen_jobs]

    with open(SEEN_FILE, "w") as f:
        json.dump(jobs, f)
    
    return new_jobs