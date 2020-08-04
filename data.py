from bs4 import BeautifulSoup
import requests

# import csv

# url_name = (input("Enter the website URL "))
source = requests.get('https://app.neilpatel.com/en/traffic_analyzer/overview?lang=en&locId=2840&domain=binance.com').text
soup = BeautifulSoup(source, 'lxml')

header = soup.find('div', class_='css-frccw8')
# name = header.find('div', class_='Paragraph').text
print(header)

# excelsheetname = input("Enter the sheet name ")
# csv_file = open(f'{excelsheetname}.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['company', 'main_address', 'city', 'state', 'PinCode', 'country', 'contact'])
