import json
import os
import random

import flask
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
    "exampleModule.html"
]  # List of all modules added to the first column of the main panel
column_2 = []  # List of all modules added to the second column of the main panel
column_3 = []  # List of all modules added to the third column of the main panel
column_4 = []  # List of all modules added to the fourth column of the main panel


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


@GD.socket_execute
def example_function_on_socket_execute(message):
    """The @GD.socket_execute decorator can be used to add a function to the
    backend routine which is executed whenever a socket 'ex' event is triggered.
    This is useful to update certain things at the backend whenever the user
    interacts with the user interface.

    For example, this function is connected with the example_module.html which
    adds a slider to the main panel which changes the size of a text within the
    module.
    The emitted message is received by a socketIO connection established in the exampleScript.js file
    """
    if message["id"] == "slider-exampleHelloWorldSize":
        blueprint.emit(
            "textSize",
            {"id": message["id"], "val": message["val"], "fn": message["fn"]},
        )


@GD.socket_join
def example_function_on_socket_join(message):
    """The @GD.socket_join decorator can be used to add a function to the
    backend routine which is executed whenever a socket 'join' event is
    triggered. This is useful to update certain things at the backend whenever
    a user joins."""
    print(
        f"This is the ExampleExtension reacting to a 'join' socketIO event. Here is the respective message: {message}"
    )


@GD.socket_left
def example_function_on_socket_left(message):
    """The @GD.socket_left decorator can be used to add a function to the
    backend routine which is executed whenever a socket 'left' event is
    triggered. This is useful to update certain things at the backend whenever
    a user leaves."""
    print(
        f"""This is the ExampleExtension reacting to a 'left' socketIO event.
        Here is the respective message:\n{message}"""
    )
