from bs4 import BeautifulSoup
import requests
from send_mail import send_mail
import os

MY_EMAIL = os.environ.get("EMAIL_KEY")
MY_PASSWORD = os.environ.get("PASSWORD_KEY")

url = "https://appbrewery.github.io/instant_pot/"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
dollars = soup.find('span', class_='a-price-whole').text
cents = soup.find('span', class_='a-price-fraction').text
price = float(dollars + cents)
print(price)
send_mail(product="instant pot", current_price=price, email=MY_EMAIL, password=MY_PASSWORD)
