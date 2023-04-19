import json
import os
import random

import flask
from lorem.text import TextLorem

import GlobalData as GD
import uploader
import util
from io_blueprint import IOBlueprint

# Prefix for the extension, as well as the names space of the extension
url_prefix = "/ExampleExtension"  # MANDATORY
extensions_name = "ExampleExtension"

# Define where all templates and static files of your extension are located
templates = os.path.abspath("./extensions/ExampleExtension/templates")
static = os.path.abspath("./extensions/ExampleExtension/static")

# Create a blueprint for the extension this will be loaded by the main app
blueprint = IOBlueprint(
    extensions_name,
    __name__,
    url_prefix=url_prefix,
    template_folder=templates,  # defaults to static of main app.py
    static_folder=static,  # defaults to static of main app.py
)  # MANDATORY

column_1 = [
    "example_main_tab_1.html"
]  # List of tab templates to be loaded in the first column of the main panel
column_2 = [
    "example_main_tab_2.html"
]  # List of tab templates to be loaded in the second column of the main panel
column_3 = [
    "example_main_tab_3.html"
]  # List of tab templates to be loaded in the third column of the main panel

column_4 = [
    "example_main_tab_4.html"
]  # List of tab templates to be loaded in the fourth column of the main panel

upload_tabs = [
    "example_upload_tab.html"
]  # List of tab templates to be loaded in the upload panel


# Define your first route
@blueprint.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"


# Adds a tab to the main panel route to this is /example/main
@blueprint.route("/main", methods=["GET"])
def example_main():
    return flask.render_template("example_main.html")


@blueprint.route("/nodepanel", methods=["GET"])
def example_node_info():
    return "Node Info"


@blueprint.route("/upload", methods=["GET"])
def example_upload():
    return "Upload"


@blueprint.route("/preview", methods=["GET"])
def example_preview():
    return "Example Preview"


@blueprint.route("/uploadfiles", methods=["POST"])
def example_upload_files():
    success = False
    if success:
        return "<a style='color:green;'>Success</a>", 200
    else:
        return "<a style='color:red;'>Error</a>", 500


@blueprint.before_app_first_request
def example_extension_setup():
    # prepare some important variables
    # do more important stuff
    pass


@blueprint.route("/emit", methods=["GET"])
def example_emit_socketio_to_main():
    """This will send a socketio message to the main panel. Check the console of the main panel to see the message."""
    namespace = "/chat"
    room = 1
    blueprint.emit(
        "ex",
        {"id": "someId", "opt": "someOption", "fn": "SomeFunction"},
        namespace=namespace,
        room=room,
    )
    return "sent"


@blueprint.route("/send", methods=["GET"])
def example_send_socketio():
    """Webpage with a button, when pressed a socketio message to this extension is send."""
    return flask.render_template("example_send_socketio.html")


@blueprint.on("example")
def example_receive_socketio(message):
    print("Received example form client:")
    print(message)


@blueprint.on("example", namespace="/chat")
def example_receive_socketio_in_main(message):
    print("Received example form client:")
    print(message)


@blueprint.on("status")
def example_send_status(message):
    text = "Hello World!\n\n"
    lorem = TextLorem()
    for _ in range(0, 2):
        text += lorem.sentence() + "\n"
    message["text"] = text
    print(message)
    blueprint.emit("status", message)
