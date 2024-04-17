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

if __name__ == "__main__":
    # Call the get_news function and print the list of articles
    articles = get_news()
    print(articles)