# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI application
app = FastAPI()

# Add CORS middleware to the FastAPI application
# This allows the API to be accessed from different origins (i.e., different websites)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# List of RSS feed URLs to fetch news from
DOMAINS = ["https://www.formula1.com/en/latest/all.xml", "https://www.autosport.com/rss/f1/news/", "https://feeds.bbci.co.uk/sport/formula1/rss.xml"]

# Define a route for getting news
@app.get("/news")
def get_news():
    # Initialize an empty list to store articles
    articles_list = []
    
    # Loop over each domain
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
            description = article.find("description").text if article.find("description") else None
            link = article.find("link").text if article.find("link") else None

            # Create a dictionary for the article
            article_dict = {
                "title": title,
                "author": author,
                "description": description,
                "link": link,
            }

            # Add the dictionary to the list of articles
            articles_list.append(article_dict)
    
    # Return the list of articles
    return articles_list