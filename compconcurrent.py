from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
import urllib.request

url_list = ["https://loonycorn.com/",
            "https://reuters.com/",
            "https://wwf.panda.org/",
            "https://en.unesco.org/"]

def url_loader(url, time):
    with urllib.request.urlopen(url, timeout=time) as conn:
        return conn.read()

def main_processpool():
    start = time.time()

    with ProcessPoolExecutor(max_workers=7) as executor:
        future_to_page = {executor.submit(url_loader, url, 10):
                          url for url in url_list}