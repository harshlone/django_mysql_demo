import os
import sys
import django
import requests
from django.utils.text import Truncator

# ─── Step 1: Add project root to Python path ───
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# ─── Step 2: Set Django settings ───
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo_project.settings")
django.setup()

# ─── Step 3: Import your models ───
from products.models import ExternalPostSummary

# ─── Step 4: Define function to fetch & save data ───
def fetch_and_save(limit=10):
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
        r.raise_for_status()  # raise error if request failed
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return

    posts = r.json()[:limit]

    count_saved = 0
    for p in posts:
        obj, created = ExternalPostSummary.objects.get_or_create(
            external_id=p["id"],  # make sure your model has external_id
            defaults={
                "title": p["title"],
                "body_excerpt": Truncator(p["body"]).chars(200)
            }
        )
        if created:
            count_saved += 1

    print(f"Data fetched successfully! {count_saved} new records saved.")

# ─── Step 5: Run function ───
if __name__ == "__main__":
    fetch_and_save(limit=10)  # change limit if you want more posts