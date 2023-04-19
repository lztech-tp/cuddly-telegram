import streamlit as st
import pandas as pd
from ggsearch import google_search
from extract_prices import extract_prices



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

            df = pd.DataFrame(product_prices, columns=['Price', 'URL', 'Site'])
            df = df.sort_values(by="Price", ascending=False)
            df = df.head(50)

        st.markdown("### Prices found:")
        st.write(df)

if __name__ == "__main__":
    main()



