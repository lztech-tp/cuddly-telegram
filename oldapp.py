import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re
import streamlit as st




def extract_prices(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    price_regex = re.compile(r'(\$\d+(?:\.\d{2})?)')
    prices = []

    for match in price_regex.finditer(soup.text):
        prices.append(match.group(1))

    return prices

def main():
    st.title("Price Scraper")
    st.write("Enter a product name to search and scrape prices from Google search results:")

    query = st.text_input("Product name")
    num_results = st.number_input("Number of search results", min_value=1, max_value=50, value=10, step=1)

    if st.button("Search and Scrape"):
        urls = google_search(query, num_results=num_results)
        product_prices = []

        with st.spinner("Scraping prices..."):
            for url in urls:
                try:
                    prices = extract_prices(url)
                    if prices:
                        product_prices.extend(prices)
                except:
                    continue

        st.write("Prices found:")
        for price in product_prices:
            st.write(price)

if __name__ == '__main__':
    main()