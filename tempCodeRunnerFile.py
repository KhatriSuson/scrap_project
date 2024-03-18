import requests
from bs4 import BeautifulSoup

import sqlite3

url = "https://www.scrapethissite.com/pages/forms/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())

contents = soup.find_all("table", class_="table")

for content in contents:
    # print(content.text)

    team_names = content.find_all("td", class_="name")
    for team_name in team_names:
        print(f"Team Name: {team_name.text}")

    years = content.find_all("td", class_="year")
    for year in years:
        print(year.text)

    wins = content.find_all("td", class_="wins")
    for win in wins:
        print(win.text)


# Function to create an SQLite database table

# def create_database():

conn = sqlite3.connect("scrap_data.db")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS scrap_data(
                team_name TEXT, years INTEGER, wins  INTEGER)"""
)

conn.commit()
conn.close()


# Sample data
# data = [(team_name, year, win)]

# Insert scraped data into the SQLite database

conn = sqlite3.connect("scrap_data.db")
cursor = conn.cursor()

conn.execute(
    "INSERT INTO scrap_data (team_name, years, wins) VALUES (?,?,?)",
    (team_name, year, win),
)

conn.commit()
conn.close()
