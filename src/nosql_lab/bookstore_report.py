#!/usr/bin/env python3

import os
import logging
import pymongo

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():
    """Connect to MongoDB Atlas and print each author in the list, the books linked to that author, with title and publication year"""
    try:
        # Connect to Atlas using the credentials from the environment
        client = pymongo.MongoClient(MONGODB_ATLAS_URL, username=MONGODB_ATLAS_USER, password=MONGODB_ATLAS_PWD)
        logging.info("Connected to MongoDB Atlas")

        # Select the bookstore database and the two collections
        db = client["bookstore"]
        authors = db["authors"]
        books = db["books"]

        #list of authors including author_001-003 (from the loaded files) and author_004 (the one I added)
        author_ids = ["author_001", "author_002", "author_003", "author_004"]
        
        #print number of authors in the list
        total_authors = authors.count_documents({"_id": {"$in": author_ids}})
        print(f"Authors: {total_authors}")

        #for each author print their name and the books linked to them
        for author in authors.find({"_id": {"$in": author_ids}}):
            print(author["name"])
            for book in books.find({"author_ids": author["_id"]}):
                print(f" {book['title']} ({book['published_year']})")
            print()

        # Close the connection when done
        client.close() 
 
    except Exception as e:
        logging.error(f"MongoDB error: {e}")

if __name__ == "__main__":
    main()
