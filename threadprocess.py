from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import urllib.request
import time

url_list = ["https://loonycorn.com/",
            "https://reuters.com/",
            "https://wwf.panda.org/",
            "https://en.unesco.org/"]

def url_loader(url, time):
    with urllib.request.urlopen(url, timeout=time) as conn:
        return conn.read()

def main_threadpool():
    start = time.time()

    with ThreadPoolExecutor(max_workers=7) as executor:
        future_to_page = {executor.submit(url_loader, url, 10):
                          url for url in url_list}

        for future in as_completed(future_to_page):
            url = future_to_page[future]
            result = future.result()
            print("The page %r is %d bytes." % (url, len(result)))
    
    print("Total time taken:", time.time() - start)

main_threadpool()