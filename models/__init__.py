#!/usr/bin/python3
"""This is a method for models directory"""

from models.engine.file_storage import FileStorage

# Create a unique instance of FileStoraeg for the application
storage = FileStorage()

# Call the reload method on the storage variable
storage.reload()
