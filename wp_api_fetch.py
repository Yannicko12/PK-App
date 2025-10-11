import requests

BASE_URL = "http://mediplus-cvo.de"
API_ENDPOINT = f"{BASE_URL}/wp-json/wp/v2/posts"

def get_posts():
    try:
        response = requests.get(API_ENDPOINT, verify=False)
        response.raise_for_status()
        posts = response.json()
        print(f"{len(posts)} Beiträge gefunden:\n")
        for post in posts:
            print("Titel: ", post["title"]["rendered"])
            print("Inhalt HTML:", post["content"]["rendered"][:150], "...")
            print("-----")
    except requests.exceptions.RequestException as e:
        print("Fehler beim Abrufen:", e)

if __name__ == "__main__":
    get_posts()