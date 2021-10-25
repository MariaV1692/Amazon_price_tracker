from dotenv import load_dotenv


load_dotenv()

import requests
from bs4 import BeautifulSoup
import smtplib
import os

PASSWORD = os.environ["PASSWORD"]
MY_EMAIL = os.environ["MY_EMAIL"]
TARGET_EMAIL = os.environ["TARGET_EMAIL"]

product_url = os.environ["PRODUCT_URL"]
target_price = int(os.environ["TARGET_PRICE"])
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.82 Safari/537.36 ",
    "X-Forwarded-For": "79.180.163.70"
}
response = requests.get(url=product_url, headers=headers)
amazon_response = response.text

soup = BeautifulSoup(amazon_response, "lxml")

price_block = soup.find(name="span", id="priceblock_ourprice")
price_text = price_block.get_text()
product_price = float(price_text.split("$")[1])
product_name = soup.find(name="span", id="productTitle").get_text()

if product_price < target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # make the connection secure
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TARGET_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{product_name.strip()} price is now ${product_price}\n"
                                f"{product_url}")



