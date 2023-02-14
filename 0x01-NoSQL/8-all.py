#!/usr/bin/env python3
"""List all documents in Python"""

import pymongo


def list_all(mongo_collection):
    """List documents"""
    documents = mongo_collection.find()
    return [i for i in documents]
