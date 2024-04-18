# Import necessary libraries
import random
import requests
from bs4 import BeautifulSoup

# List of RSS feed URLs to fetch news from
DOMAINS = ["https://www.formula1.com/en/latest/all.xml", "https://www.autosport.com/rss/f1/news/", "https://feeds.bbci.co.uk/sport/formula1/rss.xml"]

def get_news():
    # Initialize an empty list to store articles
    articles_list = []
    
    # Loop over each domain#editor
    for domain in DOMAINS:
        # Send a GET request to the domain
        response = requests.get(domain)
        
        # Parse the response content with BeautifulSoup
        soup = BeautifulSoup(response.content, "lxml-xml")
        
        # Find all <item> tags in the parsed content
        articles = soup.find_all("item")
        
        # Loop over each article
        for article in articles:
            # Extract the text of each tag, or None if the tag doesn't exist
            title = article.find("title").text if article.find("title") else None
            author = article.find("dc:creator").text if article.find("dc:creator") else None
            description = article.find("description").text.split("<a class='more'")[0] if article.find("description") else None
            link = article.find("link").text if article.find("link") else None

            # Create a dictionary for the article
            article_dict = {
                "title": title,
                # "author": author,
                "description": description,
                "link": link,
            }

            # Add the dictionary to the list of articles
            articles_list.append(article_dict)
    
    # Use a constant seed for the random number generator
    random.seed(5)
    random.shuffle(articles_list)

    # Return the list of articles
    return articles_list

def get_driver_standings():
    # Define the URL of the webpage to scrape
    DOMAIN = "https://www.formula1.com/en/results.html/2024/drivers.html"

    # Send a GET request to the webpage
    response = requests.get(DOMAIN)

    # Parse the HTML content of the webpage with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table with the class "resultsarchive-table" in the parsed HTML
    table = soup.find("table", class_="resultsarchive-table")

    # Initialize an empty list to store the data from the table
    data_list = []

    # Iterate over each row in the table
    for row in table.find_all("tr"):
        # Initialize an empty list to store the data from the current row
        row_data = []

        # Iterate over each cell in the row
        for cell in row.find_all("td"):
            # If the cell contains a span with the class "hide-for-mobile", append its text to row_data
            if cell.find("span", class_="hide-for-mobile"):
                row_data.append(cell.find("span", class_="hide-for-mobile").text)
            # Otherwise, append the text of the cell to row_data
            else:
                row_data.append(cell.text)

        # Append the data from the current row to data_list
        data_list.append(row_data)

    # Initialize an empty list to store the final data
    data = []

    # Iterate over each row in data_list, skipping the first one
    for row in data_list[1:]:
        # Create a dictionary with the data from the current row and append it to data
        row_data = {
            "Position": row[1],
            "Driver": row[2],
            "Team": row[4].replace("\n", ""),
            "Points": row[5]
        }
        data.append(row_data)

    # Return the final data
    return data

if __name__ == "__main__":
    # Call the get_news function and print the list of articles
    articles = get_news()
    print(articles)

    # Call the get_driver_standings function and print the current dirver standings
    driver_standings = get_driver_standings()
    print(driver_standings)