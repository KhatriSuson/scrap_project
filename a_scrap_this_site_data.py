import requests
from bs4 import BeautifulSoup

import sqlite3


def create_database():
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
def insert_data(team_name, year, win):
    conn = sqlite3.connect("scrap_data.db")
    cursor = conn.cursor()

    conn.execute(
        "INSERT INTO scrap_data (team_name, years, wins) VALUES (?,?,?)",
        (team_name, year, win),
    )

    conn.commit()
    conn.close()


url = "https://www.scrapethissite.com/pages/forms/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())

contents = soup.find_all("table", class_="table")

for content in contents:
    # print(content.text)

    team_names = content.find_all("td", class_="name")
    teams = []
    for team_name in team_names:
        print(f"Team Name: {team_name.text}")
        teams.append(team_name.text)

    years = content.find_all("td", class_="year")
    year_list = []
    for year in years:
        print(year.text)
        year_list.append(int(year.text))

    wins = content.find_all("td", class_="wins")
    win_list = []
    for win in wins:
        print(win.text)
        win_list.append(win.text)

    for team, year, win in zip(teams, year_list, win_list):
        insert_data(team, year, win)


# Function to create an SQLite database table

# def create_database():
