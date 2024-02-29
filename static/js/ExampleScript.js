uid = makeid(10);
let exampleExSocket = io.connect("http://" + location.host + "/ExampleExtension");
$(document).ready(function() {
    let sliderDOM = document.getElementById("slider-exampleHelloWorldSize")
    let textDOM = document.getElementById("example_HelloWorld")
    let numberDOM = document.getElementById("example_HelloWorld_textSize")
    let slider = sliderDOM.shadowRoot.getElementById("myRange");
    // textDOM.style.fontSize = slider.value + "px"
    // numberDOM.innerHTML = slider.value

    exampleExSocket.on("textSize", function(data) {
        console.log("TEXTSIZE SHOULD BE: " + data["val"]);
        textDOM.style.fontSize = data["val"] + "px"
        numberDOM.innerHTML = data["val"]
    });
});