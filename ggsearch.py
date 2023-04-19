from googlesearch import search

def google_search(query, num_results=10):
    urls = []
    try:
        for url in search(query, num_results=num_results):
            urls.append(url)
    except Exception as e:
        print(e)
    return urls
