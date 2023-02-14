#!/usr/bin/env python3
"""List a document in Python"""


def schools_by_topic(mongo_collection, topic):
    """List"""
    return mongo_collection.find({"topics": topic})
