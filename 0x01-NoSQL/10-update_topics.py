#!/usr/bin/env python3
"""Update a document in Python"""


def update_topics(mongo_collection, name, topics):
    """Update"""
    documents = {"name": name}
    new_val = {"$set": {"topics": topics}}
    mongo_collection.update_many(documents, new_val)
