import json
import os
import random

import flask

import GlobalData as GD
import uploader
import util

# Prefix for the extension, as well as the names space of the extension
url_prefix = "/ExampleExtension"  # MANDATORY
extensions_name = "ExampleExtension"

# Define where all templates and static files of your extension are located
templates = os.path.abspath("./extensions/ExampleExtension/templates")
static = os.path.abspath("./extensions/ExampleExtension/static")

# Create a blueprint for the extension this will be loaded by the main app
blueprint = flask.Blueprint(
    extensions_name,
    __name__,
    url_prefix=url_prefix,
    template_folder=templates,  # defaults to static of main app.py
    static_folder=static,  # defaults to static of main app.py
)  # MANDATORY

main_tabs = [
    "example_main_tab.html"
]  # List of tab templates to be loaded in the main panel
upload_tabs = [
    "example_upload_tab.html"
]  # List of tab templates to be loaded in the upload panel

before_first_request = []  # List of functions to be executed before the first request

# Define your first route
@blueprint.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"


# Adds a tab to the main panel route to this is /example/main
@blueprint.route("/main", methods=["GET"])
def example_main():
    return "Example Main Panel"


@blueprint.route("/upload", methods=["GET"])
def example_node_info():
    return "Example Node Info Panel"


@blueprint.route("/upload", methods=["GET"])
def example_upload():
    return "Example Upload Panel"


@blueprint.route("/preview", methods=["GET"])
def example_preview():
    return "Example Preview Panel"


@blueprint.route("/uploadfiles", methods=["POST"])
def example_upload_files():
    success = False
    if success:
        return "<a style='color:green;'>Success</a>", 200
    else:
        return "<a style='color:red;'>Error</a>", 500
