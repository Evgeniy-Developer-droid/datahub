import requests
from bs4 import BeautifulSoup as bs

# categories = input("Enter categories ID with space delimeter").split(" ")
categories = [127, 3605, 606, 166]


for category in categories:
    
    try:
        category = int(category)
        headers = {
            "x-requested-with": "XMLHttpRequest"
        }
        data = {
            "sort": "date-a-z",
            "category_id": category,
        }
        page = 1
        pages = 1
        response = requests.post(
            url=f"https://besplatka.ua/category/index?page={page}&query=",
            data=data,
            headers=headers
        )
        response_data = response.json()
        pagination = response_data["pagination"]
        count = pagination["count"]
        on_page = pagination["onPage"]
        res = int(count / on_page)
        pages = res if res else 1

        for page in range(1, pages+1):
            print(" \n---------------------")
            print(f"Page {page} of {pages}. Category {category}")
            print("---------------------\n")
            response = requests.post(
                url=f"https://besplatka.ua/category/index?page={page}&query=",
                data=data,
                headers=headers
            )
            
            try:
                response = response.json()
            except Exception as e:
                print(data, headers)
                print("response not json ", page)
                continue
            posts = response.get("messages", [])
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
                        print("Error meta data request")

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
                    name = soup.find_all('div', attrs={"class": "user-name"})
                    a = ul.find_all('a')
                    
                    if name:
                        name = name[0].text
                    else:
                        name = "No name"
                    for phone in a:
                        data_send = {
                            "number": phone.text.strip(),
                            "name": meta_data["name"],
                            "city": meta_data["city"],
                            "meta": response_data.get("watchlist_label", "")
                        }
                        response = requests.post("http://127.0.0.1:8000/master/besplatka/add-number", data=data_send)
                        if response.status_code == 201:
                            print(f"Success!")
                        else:
                            print(f"Already exist!")
                except Exception as e:
                    print(e)
            
    except Exception as e:
        print(f"Category error {category} - {e}")