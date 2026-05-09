import json
from datetime import datetime

def get_today_rota():
    with open("data/rota.json") as f:
        rota = json.load(f)

    today = datetime.now().strftime("%A")
    return rota.get(today, "No shift")