import streamlit as st
from ggsearch import google_search
from extract_prices import extract_prices


""" def main():
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
    main() """

def main():
    st.title("Product Price Scraper")
    query = st.text_input("Enter a product name to search:", "Samsung French Door Refrigerator")
    num_results = st.slider("Number of search results:", min_value=2, max_value=50, value=10, step=1)

    if st.button("Search"):
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

        st.markdown("### Prices found:")
        for price in product_prices:
            st.write(f"{price[1]} - [Source]({price[0]})")

if __name__ == "__main__":
    main()