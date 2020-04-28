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