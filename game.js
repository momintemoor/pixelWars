var myGamePiece1;
var myGamePiece2;

function startGame() {
    myGamePiece1 = new component(30, 30, "red", 10, 10, "image");
    myGamePiece2 = new component(30, 30, "blue", 150, 150, "image");
    myGameArea.start();
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 1500;
        this.canvas.height = 700;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.interval = setInterval(updateGameArea, 20);
    },
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}

function component(width, height, color, x, y) {
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;
    this.update = function(){
        ctx = myGameArea.context;
        ctx.fillStyle = color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}

function updateGameArea() {
    myGameArea.clear();
    myGamePiece1.update();
    myGamePiece2.update();
}

function ajaxGetRequest(path, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

function action_on_response(response){
    console.log("The server responded with: " + response);
}
function called_on_button_press(){
    ajaxPostRequest("/some_path", "Button pressed", action_on_response);
}

function showUsers(response){
    var users = "";
    for(var data in JSON.parse(response)){
        users = users + data.username + "</br>";
    }
    document.getElementById("users").innerHTML = users;
}
function loadUsers(){
    ajaxGetRequest("/users", showUsers);
}

function add_user() {
    var nameElement = document.getElementById("username");

    var username = nameElement.value;
    nameElement.value = "";
    var toSend = JSON.stringify({"username": username});

    ajaxPostRequest("/Login", toSend, showUsers);

}
/*
function keyCode(event) {
    var x = event.keyCode;
    if (x == 087) {
        alert ("W key has been pressed");
    }
}

window.addEventListener("keydown", function (event) {
  if (event.defaultPrevented) {
    return; // Do nothing if the event was already processed
  }

  switch (event.key) {
    case "ArrowDown":
      //"down arrow" key press.
      console.log("arrow is pressed")
    case "ArrowUp":
      //"up arrow" key press.
      break;
    case ArrowLeft:
      //"left arrow" key press.
      break;
    case "ArrowRight":
      //right arrow key press.
      break;
    default:
      return; // Quit when this doesn't handle the key event.
  }
*/