import requests
from bs4 import BeautifulSoup as bs
from logger import Logger
from config import IMPORT_URL, WORKER_NAME, WORKER_DATA_URL, SECRET_WORKER_KEY
import time

logger = Logger(WORKER_NAME)
log = logger.get_logger()

while True:
    categories = []
    # get data from server about worker with params
    response_worker = requests.get(WORKER_DATA_URL+"?name="+WORKER_NAME, headers={"SECRET_CODE": SECRET_WORKER_KEY})
    if response_worker.status_code == 200:
        response_worker = response_worker.json()
        if "id" in response_worker:
            if response_worker['status'] == 'work':
                categories = [item for item in response_worker['params'].split(' ')]
            else:
                time.sleep(5)
                categories = []
                continue
        else:
            log.debug(f"Worker data not found")
            time.sleep(5)
            categories = []
            continue
    else:
        log.debug(f"Worker data not found")
        time.sleep(5)
        categories = []
        continue

    for category in categories:
        
        try:
            category = int(category)
            headers = {"x-requested-with": "XMLHttpRequest"}
            data = {"sort": "date-a-z", "category_id": category}
            pages = 2
            for page in range(1, pages+1):
                logger.logger_file_update()
                response_main = requests.post(
                    url=f"https://besplatka.ua/category/index?page={page}&query=",
                    data=data,
                    headers=headers
                )
                
                try:
                    response_main = response_main.json()
                except Exception as e:
                    log.debug(f"Critical! Data from response is broken(not json).")
                    continue
                posts = response_main.get("messages", [])
                for post in posts:
                    try:
                        #get meta
                        meta_data = {"city": "unknown", "name": "unknown"}
                        try:
                            respons_meta = requests.get("https://besplatka.ua"+post.get("url"))
                            soup_meta = bs(respons_meta.content, "html.parser")
                            name = soup_meta.find('div', attrs={'class': "user-name"})
                            city = soup_meta.find('span', attrs={'itemprop': "addressLocality"})
                            if name:
                                meta_data['name'] = name.text.strip()
                            if city:
                                meta_data['city'] = city.text.strip()
                        except Exception as e:
                            log.debug(f"Error meta data response")

                        #get phone
                        url = "https://besplatka.ua/modal/load"
                        headers_ = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
                        data_p = {
                            "name": "show-phone",
                            "params[id]": post.get("_id"),
                            "params[mobile]": False
                        }
                        response = requests.post(url, data=data_p)
                        data_response = response.json()
                        soup = bs(data_response.get("content", ""), "html.parser")
                        ul = soup.find('ul', attrs={"class": "title-phones"})
                        a = ul.find_all('a')

                        for phone in a:
                            data_send = {
                                "number": phone.text.strip(),
                                "name": meta_data["name"],
                                "city": meta_data["city"],
                                "meta": response_main.get("watchlist_label", ""),
                                "source": "besplatka"
                            }
                            response = requests.post(IMPORT_URL, data=data_send, headers={"SECRET_CODE": SECRET_WORKER_KEY})
                            if response.status_code == 201:
                                log.debug(f"Added {data_send}")
                            else:
                                log.debug(f"Already exist. {data_send}")
                    except Exception as e:
                        log.debug(f"Error get phone information. {e}")
                
        except Exception as e:
            log.debug(f"Category error {category}. {e}")
