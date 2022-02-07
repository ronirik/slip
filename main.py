# парсинг 
# Вертуальное окружения сов который будет стоять в одном месте не распростронясь на весь пк 
# pip3 instal regvest
# Django 4.0.1
# apt install python3.8-venv установка 
#  python3 -m venv env запуск
# nano requirements.txt
# beautifulsoup4
# lxml
# requests явная вурсия бееблиотеки ==2.3.8
# source env/bin/activate    or           . env/bin/activzte  включить
# deactivate          отключить
# pip3 freeze  проверка модуля и библиотек 
# pip3 install -r requirements.txt установка библиотек

# https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru/?sl=ru



# import random
# import requests
# from bs4 import BeautifulSoup as BS
# import csv

# def get_html(url):
#     response = requests.get(url)
#     print(response.status_code)
    # print(response.text)
#     return response.text

# def get_data(html):
#     soup = BS(html, 'lxml')
#     catalog = soup.find('div', class_='grid-list')
#     mobiles = catalog.find_all('div', class_='ty-column4')
#     # print(mobiles[0].find('img').get('alt'))
#     # print(mobiles[0].find('img').get('data-ssrc'))
#     for mobile in mobiles:
#         try:
#             title = mobile.find('img').get('alt')
#         except:
#             title = ''
#         try:
#             image = mobile.find('img').get('data-ssrc')
#         except:
#             image = ''
        
#         data = {'title' : title, 'image' : image}
        
#         write_csv(data)

# def write_csv(data):
#     with open('mobiles.csv', 'a') as csv_file:
#         writer = csv.writer(csv_file, delimiter='/')

#         writer.writerow((data['title'], data['image']))



# def main():
#     for page in range(1, 16):
#         print(f'Парсинг {page} страницу')
#         url = f'https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru/?sl=ru/page-{page}'
#         html = get_html(url)
#         data = get_data(html)
#         # print(data)

# main()

 






























# import requests
# from bs4 import BeautifulSoup as BS
# import csv

# CSV = "title1.csv"
# HOST = 'https://www.google.com/'
# URL = 'https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en'
# HEADER = {
#     'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
# }

# def get_html(url, params=''):
#     req = requests.get(url, headers=HEADER, params=params)
#     return req

# def get_content(html):
#     soup = BS(html, 'lxml')
#     items = soup.find_all('h3', class_="ipQwMb ekueJc RD0gLb")
#     title_list = []

#     for item in items:
#         title_list.append(
#             {
#                 'title':item.find('a', class_="DY5T1d RZIKme")
#                 # 'value':titl.find('h3', class_="ipQwMb ekueJc RD0gLb").find('a', class_="DY5T1d RZIKme")
#             }
#         )
    
#     return title_list

# def save_doc(items, path):
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(['названия','сылка'])
#         for item in items:
#             writer.writerow([item["title"]])

# def parser():
#     PAGENATION = input('Укажите количество вылок для запроса ')
#     PAGENATION = int(PAGENATION.strip())
#     html = get_html(URL)
#     if html.status_code == 200:
#         title_list = []
#         for page in range(1, PAGENATION):
#             print(f'Парсю страницу {page}')
#             html = get_html(URL, params={'page':page})
#             title_list.extend(get_content(html.text))
#             save_doc(title_list, CSV)
#     else:
#         print('Error')

# parser()


# from operator import index
# import requests
# from bs4 import BeautifulSoup as BS


# def get_html(url):
#     html = requests.get(url).text
#     return html

# def get_data(html):
#     html_page = BS(html, 'lxml')
#     film = html_page.find_all('td', class_="posterColumn")
#     catalogue = dict()
#     for film1 in film:
#         title = film1.find('a').find('img').get('alt')
#         link = "https://www.imdb.com" + film1.find('a').get('href')
#         catalogue.update({title: link})
#     return catalogue

# def get_link(title_list, film1):
#     return f"Ссылка на фильм {film1}: {title_list.get(film1)}"

# def main():
#     url = ('http://www.imdb.com/chart/top')
#     html = get_html(url)
#     fin_dict = get_data(html)
#     print(fin_dict.keys())
#     film_ = input("Какой фильм вы ищете? ")
#     print(get_link(fin_dict, film_))

# main()

# import requests
# from bs4 import BeautifulSoup as BS
# # import csv


# url = 'https://www.kivano.kg/mobilnye-telefony'

# source = requests.get(url)
# main_text = source.text
# soup = BS(main_text)

# table = soup.find('div', class_="list-view" )
# div = table.find_all('div', class_="listbox_title oh")

# print(div)


# import requests
# from bs4 import BeautifulSoup as BS
# import csv

# URL = 'https://www.kivano.kg/mobilnye-telefony'

# def get_html(url):
#     response = requests.get(url)
#     print(response.status_code)


# def get_data(html):
#     page_html = BS(html, "lxml")
#     phones = page_html.find_all('div', class_="item product_listbox oh")
#     for phone in phones:
#         try:
#             title = phone.find('img').get('alt')
#         except:
#             title = ""
#         try:
#             price = phone.find(
#                 'div', class_="listbox_price text-center").text.strip()
#         except:
#             price = ""
#         try:
#             descr = phone.find(
#                 'div', class_="product_text pull-left").text.strip()
#         except:
#             descr = ""
#         try:
#             link = "https://www.kivano.kg" + \
#                 phone.find('div').find('a').get('href')
#         except:
#             link = ""

#         data = {
#             'title': title,
#             'price': price,
#             'descr': descr,
#             'link': link
#         }
#         write_to_file(data)


# def write_to_file(data):
#     with open("phones_kivano.csv", "a", encoding="utf-8") as csv_file:
#         writer = csv.writer(csv_file, delimiter='/')

#         writer.writerow((
#             data['title'],
#             data['price'],
#             data['descr'],
#             data['link']
#         ))


# def main():
#     for page in range(1, 33):
#         print(f"{page} page is parsed")
#         url = f"https://www.kivano.kg/mobilnye-telefony?page={page}"
#         html = get_html(url)
#         get_data(html)


# main()