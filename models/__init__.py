#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv 
storage_type = ""

if getenv("HBNH_TYPE_STORAGE") == "db":
    storage_type = "db"
    from models.engine.db_storage import DBSrorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
