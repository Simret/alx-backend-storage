#!/usr/bin/env python3
"""Insert a document in Python"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert a document"""
    documents = mongo_collection.Insert_one(kwargs)
    return documents.inserted_id
