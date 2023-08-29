import os
import importlib


# dynamic loading of models
def import_models():
    for filename in os.listdir("app/models"):
        # filter files and import modules dynamically
        if filename.endswith(".py") and filename != "__init__.py":
            module = importlib.import_module(f".{filename[:-3]}", package="app.models")
