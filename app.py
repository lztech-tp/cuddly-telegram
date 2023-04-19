import streamlit as st
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

        st.markdown("### Prices found:")
        for price in product_prices:
            st.write(f"{price[2]} - {price[0]} - [Source]({price[1]})")

if __name__ == "__main__":
    main()



