# DataDiVR backend example extension

This series teaches you the basic skills you need to develop an extension for the DataDiVR Web application.

<h1> Overview </h1>

Here you will get an overview of the DataDiVR platform. You will learn what you can do with the DatDiVR platform and how to use it. Furthermore, you will learn about the essential technical aspects of the DataDiVR platform.

### What is the DataDiVR?

The [DataDiVR](https://github.com/menchelab/DataDiVR_WebApp) is a virtual
reality platform used to explore and analyze network data.

<!-- ## Useful Presentations and Tutorials

In the following you can find some resources that might be useful for you:
| Resource          | Description      | Reference      |
| ----------------- | ---------------- | -------------- |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |

-->

<!-- ### Get in touch

If you would like to discuss anything about the VRNetzer, you can join our community, contact us directly via email or visit our website.
| Platform                    | Description      | Reference      |
| --------------------------- | ---------------- | -------------- |
| (EMAIL/WEBSITE/SOCIALMEDIA) | SOME DESCRIPTION | SOME REFERENCE |
| (EMAIL/WEBSITE/SOCIALMEDIA) | SOME DESCRIPTION | SOME REFERENCE |
| (EMAIL/WEBSITE/SOCIALMEDIA) | SOME DESCRIPTION | SOME REFERENCE |
| (EMAIL/WEBSITE/SOCIALMEDIA) | SOME DESCRIPTION | SOME REFERENCE |
| (EMAIL/WEBSITE/SOCIALMEDIA) | SOME DESCRIPTION | SOME REFERENCE |

-->

### The technology behind the DataDiVR

The DataDiVR runs on Flask 2.0 and its UI consists of webpages (HTML/CSS/JS).

### Extension of DataDiVR Core

The Core module builds the basis of the DataDiVR. It comes with a basic set of features to
visualize network data. We highly encourage you to extend the DataDiVR and share your results with the community.
This way, you can help us to improve the DataDiVR and make it more useful for everyone.

<h1> Start creating your first extension</h1>

### Clone the DataDiVR backend repository

To create a testing environment for your extension you should start by cloning the [DataDiVR WebApp repository](https://github.com/menchelab/DataDiVR_WebApp). This way, you can include your extension in the DataDiVR backend and test it. Furthermore, you can easily keep track of the changes we make to the DataDiVR backend and update your extension accordingly if needed.

    git clone https://github.com/menchelab/DataDiVR_WebApp
    

### Fork the ExampleExtension repository

To easily share your extension with the community, we recommend to create a fork
of the [ExampleExtension repository](https://github.com/menchelab/ExampleExtension).
This way you can easily update, and change your extension, as well as keep 
track of issues. Furthermore, everyone who would like to use it can drop it 
into their DataDiVR backend without fetching the full backend module.

### Add your extension to the DataDiVR backend

Now that you forked the ExampleExtension, you can clone it into
the cloned DataDiVR backend:

    cd DataDiVR_WebApp

    cd extensions

    git clone add https://github.com/<YourGitUsername>/ExampleExtension.git

In this manner, you can easily change your extension while keeping it contained
in the testing environment of the DataDiVR backend. Whenever you change
something in your extension, you can easily commit your changes to your
forked ExampleExtension repository.


### Run the DataDiVR with your extension

The ExampleExtension repository gives you a basic idea of what is needed so 
that your extension can be loaded by the DataDiVR backend. To test your 
extension, you can simply run the DataDiVR backend running the appropriate 
script for your platform:

#### Windows

    cd ..

    .\buildandRUN.ps1

#### Linux

    cd ..

    ./linux_buildandrun.sh

#### Mac

    cd ..

    ./mac_buildandrun.sh

These scripts will create a virtual environment, install all necessary 
dependencies and run the DataDiVR backend. If everything worked out, you 
should see the following message in green in your console:

> <span style="color:green"> Loaded extension: ExampleExtension<br>
> Finished loading extensions, server is running...</span>

If you see a yellow warning message similar to this:

> <span style="color:yellow">
> Traceback (most recent call last):<br>
> File "/DataDiVR/load_extensions.py", line 17, in load<br>
> &nbsp;&nbsp;module.blueprint, url_prefix=module.url_prefix<br>
> &nbsp;&nbsp;&nbsp;&nbsp;AttributeError: module 'extensions.documentation.src.app' has no attribute 'blueprint'<br><br>
> Make sure you have an app.py file in the '/src/' folder of your extension.
> <br>
> Make sure that you have defined a 'url_prefix' for your in the app.py file.
> <br>
> Make sure your flask blueprint is called 'blueprint'.
> </span>

<br>

something seems to be wrong with your extension and it will not be loaded by the flask server. You can check [here](#troubleshooting) for possible solutions.

### Components of an extension

The ExampleExtension repository gives you a basic idea of what is needed so that your extension can be loaded by the DataDiVR backend. In the following, we will give you a more detailed overview of the components of an extension.

**1. `app.py` file in the `src` directory**

The `app.py` file is the entry point of your extension. It has to be included 
in a directory called `src` in the home directory of your Extension. The
`app.py` file has to contain the following attributes:

- A string called `url_prefix`.

  - This string defines the prefix each flask route of your extension will have. For example, if you set the url_prefix to `example`, the route `/test` will be accessible via `http://localhost:5000/example/test`.

- A flask blueprint or an IOBlueprint called `blueprint`.

  - this attribute is defined by the following line of code:

  ```
  blueprint = flask.Blueprint(
      extensions_name,
      __name__,
      url_prefix=url_prefix)
  ```

  or

  ```
  from io_blueprint import IOBlueprint
  blueprint = IOBlueprint(
      extensions_name,
      __name__,
      url_prefix=url_prefix)
  ```

  The blueprint will be registered by the main DataDiVR backend `app.py` and 
  is used to define the routes your extension adds. For further information on 
  Flask blueprints, you can check the
  [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/blueprints/).
  The IOBlueprint is a custom blueprint class that allows extensions to send and receive socket io messages.
---

**2. Include custom templates and static files**

To make templates and static files contained in your extension accessible, it 
has to be defined, where they can be found. We suggest adding two directories 
named templates and static to your extension to be consistent with Flask's 
naming convention. The ExampleExtension already provides these two directories 
together with some example files.
During the initialization of the blueprint, the following lines of code guide 
the Flask server to the correct directories:


    templates =  os.path.abspath("./extensions/<Your url_prefix>/templates")

    static = os.path.abspath("./extensions/<Your url_prefix>/static")

    blueprint = flask.Blueprint( # Or IOBlueprint
        <NameOfYourExtension>,
        __name__,
        url_prefix=url_prefix,
        template_folder=templates, # defaults to static of main app.py
        static_folder=static, # defaults to static of main app.py
    )


To link to files in these directories in your HTML files, you should utilize Flask's `url_for` function. For example, if you want to link to a file called `style.css` in your `"<Your url_prefix>/static/css"` directory, you can use the following line of code:


    "{{ url_for('<Your url_prefix>.static', filename='css/style.css') }}"


For example, if the `url_prefix` is `example`, you can link to the style.css file in `static/css` using:

    "{{ url_for('example.static', filename='css/style.css') }}"
---

**3. Add functions to be executed before the first request**

If some function needs to be executed before the first request, you can decorate this function with the decorator `@blueprint.before_app_first_request` in your app.py.

```
@blueprint.before_app_first_request
def extension_setup():
    # Your code
    pass
```

This tells the main app to execute this function just before the first request 
is made.
This is useful if you want to initialize some variables or load some data 
before the first request is made.

---

**4. Add a module to the Main Panel**

If you want to add a new tab to the DataDiVR Main Panel, you can utilize the 
`example_module.html` template contained in  `ExampleExtension/templates`.
Each HTML that should be added as a module to the main panel, has to be added 
to one of the following lists in the `app.py` file:
- `column_1` to add the module to the first column of the main panel.
- `column_2` to add the module to the second column of the main panel.
- `column_3` to add the module to the third column of the main panel.
- `column_4`to add the module to the fourth column of the main panel.

The flask server will automatically add the modules to their respective position on the main panel. For example to add the described `example_module.html` to the fourth column of the main panel you have to add it to the fourth list in the `app.py` file like this:

    column_4 = ["example_module.html"]

Be sure that your `html` files link to all resources that are additionally needed 
by your module.

<!-- # TODO: Check how to add new uploader etc -->
<!-- All of this applies if you want to add a new tab to the uploader. You can utilize the `example_upload_tab.html` template contained in the ExampleExtension. HTML files to add have to be added to the `upload_tabs` list in the `app.py` file.

If you want to add a new tab to the nodepanel or nodepanelppi, you can utilize the `example_nodepanel_tab.html` and `example_nodepanelppi_tab.html` template contained in the ExampleExtension. HTML files to add have to be added to the list `nodepanel_tabs` and `nodepanelppi_tabs`, respectively, in the `app.py` file.

<h4 id="home_present"><b>5. Present your new routes at DataDiVR's Home</h4>

If you want your route to be presented in one of the categories shown on http://127.0.0.1:6000/home (Windows/Linux) / http://127.0.0.1:3000/home (MacOS), your route has to contain one of the following keywords:
| Keyword                               | Category      | Example                          |
| :------------------------------------ | :------------ | :------------------------------- |
| `main`                                | Main (Panels) | `@blueprint.route("/main")`      |
| `nodepanel`                           | Node Info     | `@blueprint.route("/nodepanel")` |
| `upload` but not `upload` and `files` | Uploader      | `@blueprint.route("/upload")`    |
| `preview`                             | Previews      | `@blueprint.route("/preview")`   | --> |

**6. Perform a socketio emit from extension**

To send a `socketio.emit` from your extension, your blueprint has to be an 
`IOBlueprint`. Then you can use the following code to emit a socketIO message 
in your namespace:

```
blueprint.emit(
    "ex",
    {"id": "someId", "opt": "someOption", "fn": "someFunction"},
)
```
<!--
If you want to emit a message to a certain namespace, you can use the 
namespace argument:

```
namespace="/chat"
room = flask.session.get("room")
blueprint.emit(
    "ex",
    {"id": "someId", "opt": "someOption", "fn": "someFunction"},
    room = room,
    namespace = namespace,
)
``` -->

**6. Receive a socket io message for your extension namespace**

```
@blueprint.on("example")
def example_receive_socketio(message):
    print("Received example form client:")
    print(message)
```

<!-- You can also provide a different namespace for example `/chat`:

```
@blueprint.on("example",namespace="/chat")
def example_receive_socketio_in_main(message):
    print("Received example form client:")
    print(message)
``` -->

This can be useful if your extension adds new UI elements to the main panel 
and you want to send a message to your extension.

**7. Add routines to socketIO `ex`, `join` and `left` events**

The communication between the server and the frontend happens mainly via 
socketio.
Whenever a UI element is changed - e.g. a slider is moved -
a socketIO `ex` event is triggered. If your extension needs to react to such 
events, you can decorate a function with `@socket_execute`. Functions that are 
decorated with this decorator are executed whenever an `ex` event is triggered.
The decorated function has to have only one argument which is the `message` 
argument which reflects the message that comes with the event.
For example, whenever a slider with the `id = slider-exampleHelloWorldSize` is moved, you 
would like to update a value in your settings. You can archive this with the 
following code:

    @socket_execute
    def update_text_size(message):
        if message["id"] == "slider-exampleHelloWorldSize":
            blueprint.emit(
                "textSize",
                {"id": message["id"], "val": message["val"], "fn": message["fn"]},
            )
            # Update the value in the backup settings if necessary

The UI elements are synchronized between every user if you use the UI templates
we provide. For more information on the UI elements please refer to the UI 
element documentation:

- http://localhost:5000/doku/uimodules (Backend on Windows/Linux)
- http://localhost:3000/doku/uimodules (Backend on mac)
  
and

- http://localhost:5000/doku/CustomElements1 (Backend on Windows/Linux)
- http://localhost:3000/doku/CustomElements1 (Backend on mac)

In the same manner, you can add functions to the `join` and `left` routine if 
needed.

<!--
## Deployment

## TODO: Describe the deployment process on a platform where you can present your extension.
-->

<h1> Further Resources </h1>
<h2 id="example_ext"> Example Extensions </h2>
To get an idea of how an extension can be structured, you can check out the following example extensions:

| Extension | Description                                                                            | Link                                         |
| --------- | -------------------------------------------------------------------------------------- | -------------------------------------------- |
| CyEx      | This extension is designed to import networks from Cytoscape to the DataDiVR platform. | [CyEx Repo](https://github.com/ObT1337/CyEx) |
---

<h2 id="Contact"> Contact </h2>

If any questions occur, please don't hesitate to create an issue.
<!--
<h2 id="troubleshooting"> Troubleshooting </h2>
TODO: list common problems and solutions
-->
