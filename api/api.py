# Import necessary libraries
from app import get_news
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

# Define a route for getting news
@app.get("/news")
def news():
    return get_news()