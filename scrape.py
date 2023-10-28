import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# Initialize arrays to hold the data we want to scrape
titles = []
prices = []
ratings = []

# Initialize dataframe to add values later
df = pd.DataFrame()

# Initialize web driver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)



# Set the number of pages you want to scrape data from
pages = 51

for page in range(pages):
    print("Extracting data from page " + str(page+1))
    # Access content from page URL
    try:
        driver.get("https://books.toscrape.com/catalogue/page-" + str(page+1) + ".html")
    except Exception: # TODO: correct exception type (message not printing)
        print("Exceeded the number of pages available.")
        break
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")

    # Extract book data from web page 
    book_data = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    # Extract titles, prices, and ratings from book data
    for books in book_data:
        titles.append(books.h3.a["title"])
        price = books.findAll("p", {"class": "price_color"})
        prices.append(price[0].text.strip())
        rating = books.findAll("p", {"class": "star-rating"})
        rating = re.findall(r"[^.]\s([A-Z]\w+)", str(rating))
        ratings.append(rating[0])

# Add array values as columns to dataframe
df["Titles"] = titles
df["Prices"] = prices
df["Ratings"] = ratings

# Write dataframe to csv file
df.to_csv("./Books.csv")
