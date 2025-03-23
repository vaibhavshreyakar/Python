from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import csv

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = "https://example.com" # Replace this with your real target URL

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.find_all("h2") # You can change the tag based on what you want to extract

        data = [title.get_text(strip=True) for title in titles if title.get_text(strip=True)]

        # Save to CSV
        with open("scraped_data.csv", "w", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title"])
            for item in data:
                writer.writerow([item])

        return jsonify({
            "message": "Scraping completed successfully.",
            "total_titles_extracted": len(data),
            "titles": data
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request failed: {e}"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
