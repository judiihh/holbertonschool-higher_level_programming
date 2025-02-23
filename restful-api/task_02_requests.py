#!/usr/bin/python3
"""
This module defines functions for fetching and printing
posts from a RESTful API,
and for fetching and saving posts to a CSV file.
"""

import requests
import csv

def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to retrieve posts")

def fetch_and_save_posts():
    """Fetch posts and save them as a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structure data into a list of dictionaries
        data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
        
        # Write data to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
        
        print("Data successfully written to posts.csv")
    else:
        print("Failed to retrieve posts")
