
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Website URL
URL = "https://news.ycombinator.com/"

def scrape_headlines():
    try:
        # Send HTTP request
        response = requests.get(
            URL,
            timeout=10,
            headers={"User-Agent": "StudentHeadlineScraper/1.0"}
        )
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = []

        # Extract headline titles and links
        for item in soup.select("span.titleline"):
            link = item.find("a")

            if link:
                headlines.append({
                    "title": link.get_text(strip=True),
                    "url": link.get("href")
                })

        if not headlines:
            print("No headlines found. Check the webpage HTML.")
            return

        # Save headlines as JSON
        data = {
            "source": URL,
            "scraped_at": datetime.now().isoformat(timespec="seconds"),
            "total_headlines": len(headlines),
            "headlines": headlines
        }

        with open("headlines.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        # Save headlines as a text file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            for number, headline in enumerate(headlines, start=1):
                file.write(f"{number}. {headline['title']}\n")
                file.write(f"   Link: {headline['url']}\n\n")

        print("Headlines scraped successfully!")
        print("Total headlines:", len(headlines))
        print("Files saved: headlines.json and headlines.txt")

        for number, headline in enumerate(headlines[:5], start=1):
            print(f"{number}. {headline['title']}")

    except requests.exceptions.RequestException as error:
        print("HTTP request failed:", error)
    except OSError as error:
        print("File error:", error)


if __name__ == "__main__":
    scrape_headlines()
