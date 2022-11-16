# VRNetzer_backend_extension_sample

This series teaches you the basic skills you need for developing an extension for the VRNetzer backend module.

<details>
  <summary><h1> Overview </h1></summary>

Here you will get an overview of the VRNetzer platform. You will learn what you can do with the VRNetzer platform and how to use it. Furthermore, you will learn about the essential technical aspects of the VRNetzer platform.

### What is the VRnetzer?

The VRNetzer is a virtual reality platform used to explore and analyze network data.

## Useful Presentations and Tutorials

In the following you can find some resources that might be useful for you:
| Resource | Description | Reference |
| --- | --- | --- |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |
| SOME INTRODUCTION | SOME DESCRIPTION | SOME REFERENCE |

### Get in touch

If you would like to discuss anything about the VRNetzer, you can join our community, contact us directly via email or visit our website.
| Platform | Description | Reference |
| --- | --- | --- |
|(EMAIL/WEBSITE/SOCIALMEDIA)| SOME DESCRIPTION | SOME REFERENCE |
|(EMAIL/WEBSITE/SOCIALMEDIA)| SOME DESCRIPTION | SOME REFERENCE |
|(EMAIL/WEBSITE/SOCIALMEDIA)| SOME DESCRIPTION | SOME REFERENCE |
|(EMAIL/WEBSITE/SOCIALMEDIA)| SOME DESCRIPTION | SOME REFERENCE |
|(EMAIL/WEBSITE/SOCIALMEDIA)| SOME DESCRIPTION | SOME REFERENCE |

### The technology behind the VRNetzer

The VRNetzer 2.0 ...

- Running on Flask 2.0
- UI as html

### Extension of VRNetzer Core

The Core module builds the basis of the VRNetzer. It comes with a basic set of features to
visualize network data. We highly encourage you to extend the VRNetzer and share your results with the community. This way, you can help us to improve the VRNetzer and make it more useful for everyone.

</details>
<!-- <details> -->
  <summary><h1> Start creating your first extension</h1></summary>

### Fork the VRNetzer backend repository

To create a testing environment for your extension you should start by creating a fork of the [VRNetzer backend repository](https://github.com/menchelab/VRNetzer_Backend). This way, you can include your extension in the VRNetzer backend and test it. Furthermore, you can easily keep track of the changes we make to the VRNetzer backend and update your extension accordingly if needed.

### Fork the ExampleExtension repository

To easily share your extension with the community, we recommend creating a fork of the [ExampleExtension repository](https://github.com/menchelab/ExampleExtension). This way you can easily update, and change your extension, as well as keep track of issues. Furthermore, everyone who would like to use it can drop it into their VRNetzer backend without fetching the full backend module.

### Add your extension to the VRNetzer backend

Now that you forked both the VRNetzer backend as well as the ExampleExpansion, you can start by cloning your forked repository of the VRNetzer backend to your desired location.

    git clone https://github.com/<YourGitUsername>/VRNetzer_Backend

Subsequently, you can add your forked ExampleExtension as a submodule to your VRNetzer backend.:

    cd VRNetzer_Backend

    cd extensions

    git submodule add https://github.com/menchelab/ExampleExtension.git

In this manner, you can easily change your extension while keeping it contained in the testing environment of the VRNetzer backend. Whenever you change something in your extension, you can easily commit your changes to your forked ExampleExtension repository.

### Run the VRNetzer with your extension

The ExampleExtension repository gives you a basic idea of what is needed so that your extension can be loaded by the VRNetzer backend. To test your extension, you can simply run the VRNetzer backend running the appropriate script for your platform:

- windows: run `buildandRUN.ps1` in console
- linux: run `linux_buildandrun.sh` in console
- mac: run `mac_buildandrun.sh` in console

This script will create a virtual environment, install all necessary dependencies and run the VRNetzer backend. If everything worked out, you should see the following message in green in your console:

> <span style="color:green"> Loaded extension: ExampleExtension<br>
> Finished loading extensions, server is running...</span>

If you see a yellow warning message similar to this:

> <span style="color:yellow">
> Traceback (most recent call last):<br>
> File "/VRNetzer_Backend/load_extensions.py", line 17, in load<br>
> &nbsp;&nbsp;module.blueprint, url_prefix=module.url_prefix<br>
> &nbsp;&nbsp;&nbsp;&nbsp;AttributeError: module 'extensions.documentation.src.app' has no attribute 'blueprint'<br><br>
> Make sure you have an app.py file in the '/src/' folder of your extension.
> <br>
> Make sure that you have defined a 'url_prefix' for your in the app.py file.
> <br>
> Make sure your flask blueprint is called 'blueprint'.
> </span>

<br>

something seems to be wrong with your extension and it will not be loaded by the flask server. you can check [here](#troubleshooting) for possible solutions.

## Deployment

<!-- </details> -->
<details>
    <summary><h1> Further Resources </h1></summary>
</details>

<h2 id="troubleshooting"> Troubleshooting </h2>
