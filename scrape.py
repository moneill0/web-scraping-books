import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import os

# Initialize arrays to hold the data we want to scrape
titles = []
prices = []

# Initialize dataframe to add values later
df = pd.DataFrame()

# Initialize web driver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Access content from page URL
driver.get("https://books.toscrape.com/")
content = driver.page_source
soup = BeautifulSoup(content, features="lxml")

book_data = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

 
for books in book_data:
 
    # Extract titles and prices
    titles.append(books.h3.a["title"])
    book_price = books.findAll("p", {"class": "price_color"})
    prices.append(book_price[0].text.strip())

# Add array values as columns to dataframe
df["Titles"] = titles
df["Prices"] = prices

# Write dataframe to csv file
df.to_csv("./Books.csv")
