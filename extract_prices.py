import requests
from bs4 import BeautifulSoup
import re



def extract_prices(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    site_title = soup.title.string if soup.title else 'Unknown'

    price_regex = re.compile(r'(\$\d+(?:\.\d{2})?)')
    prices = []

    for match in price_regex.finditer(soup.text):
        prices.append((site_title, url, match.group(1)))

    return prices

