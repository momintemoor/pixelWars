var socket = io.connect({transports: ['websocket']});
socket.on('gameState', parseGameState);

const tile = 30;

var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
context.globalCompositeOperation = 'source-over';

function parsing(event){
    const gs =JSON.parse(event);
    drawGrid(gs['gridsize']);
    const health = gameState['baseHealth'];

    for (let player of gameState['players']) {
        placeCircle(player['x'], player['y'], player['id'] === socket.id ? '#ffff00' : '#56bcff', 2.0);
    }
}

function drawGrid(size){
    const width = size['x'];
    const height = size['y'];
    context.clearRect(0, 0, width * tile, height * tile);
    canvas.setAttribute("w", width * tile);
    canvas.setAttribute("h", height * tile);

    context.strokeStyle = '#bbbbbb';
    for (let j = 0; j <= width; j++) {
        context.beginPath();
        context.moveTo(j * tile, 0);
        context.lineTo(j * tile, height * tile);
        context.stroke();
    }
    for (let k = 0; k <= height; k++) {
        context.beginPath();
        context.moveTo(0, k * tile);
        context.lineTo(width * tile, k * tile);
        context.stroke();
    }
}

function getColor(r, g, b) {
    return "#" + helperColor(r) + helperColor(g) + helperColor(b);
}

function helperColor(input) {
    const value = Math.round(input);
    const asString = value.toString(16);
    return value > 15 ? asString : "0" + asString;
}

function placeSquare(x, y, color) {
    context.fillStyle = color;
    context.fillRect(x * tileSize, y * tileSize, tileSize, tileSize);
    context.strokeStyle = 'black';
    context.strokeRect(x * tileSize, y * tileSize, tileSize, tileSize);
}

function placeCircle(x, y, color, size) {
    context.fillStyle = color;
    context.beginPath();
    context.arc(x * tileSize,
        y * tileSize,
        size / 10.0 * tileSize,
        0,
        2 * Math.PI);
    context.fill();
    context.strokeStyle = 'black';
    context.stroke();
}