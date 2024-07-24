from bs4 import BeautifulSoup
import requests
from send_mail import send_mail
import os

MY_EMAIL = os.environ.get("EMAIL_KEY")
MY_PASSWORD = os.environ.get("PASSWORD_KEY")

url = "https://www.flipkart.com/microsoft-xbox-series-x-1024-gb/p/itm5f4b119752568?pid=GMCFVPFCFDFGJHGG&cmpid=product.share.pp&_refId=PP.fa752bb7-216f-4d69-881b-f73bc8255baf.GMCFVPFCFDFGJHGG&_appId=WA"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
price = int(soup.find('div', class_='Nx9bqj CxhGGd').text.replace("₹", "").replace(",", ""))
print(f"Current price = ₹{price}")
if price <= 43000:
    send_mail(product="MICROSOFT Xbox Series X 1024 GB  (Black)", current_price=price, email=MY_EMAIL, password=MY_PASSWORD, url=url)
