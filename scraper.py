import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract all headings (h1) from the website
        headings = soup.find_all('h1')
        return [heading.get_text() for heading in headings]

    except Exception as e:
        return f"Error: {str(e)}"
