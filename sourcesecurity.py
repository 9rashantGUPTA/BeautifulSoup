from bs4 import BeautifulSoup
import requests
import csv

Pageno = int(input("Enter the page no "))
source = requests.get(f'https://www.sourcesecurity.com/companies/cctv/directory.html?page={Pageno}').text
soup = BeautifulSoup(source, 'lxml')

excelsheetname = input("Enter the sheet name ")
csv_file = open(f'{excelsheetname}.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['company', 'main_address', 'city', 'state', 'PinCode', 'country', 'contact'])

for article in soup.find_all('div', class_='h3 mt-2'):
    company = article.a.text
    print(company)
    csv_writer.writerow([company])
for links in soup.find_all('div', class_='h3 mt-2'):
    link = links.a['href']
    link = requests.get(link).text
    details = BeautifulSoup(link, 'lxml')
    address = details.find('li', class_='address-icon').text
    country = address.split(',')[-1]
    PinCode = address.split(',')[-2]
    state = address.split(',')[-3]
    city = address.split(',')[-4]
    try:
        main_address = address.split(',')[0]
    except Exception as e:
        main_address = None
    print(main_address)
    print(city)
    print(state)
    print(PinCode)
    print(country)
    try:
        contact = details.find('li', class_='contact-icon').text
    except Exception as e:
        contact = None
    print(contact)
    print()
    csv_writer.writerow([main_address, city, state, PinCode, country, contact])
csv_file.close()
