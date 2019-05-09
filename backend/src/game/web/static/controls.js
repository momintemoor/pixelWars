var keys = {
    "w": false,
    "a": false,
    "s": false,
    "d": false
};

function handleEvent(event, state){
    if(event.key === "w" || event.key === "ArrowUp"){
        if(keys["w"] !== state){
            keys["w"] = state
            socket.emit("keys", JSON.stringify(keys));
        }
    }else if(event.key === "a" || event.key === "ArrowLeft"){
        if(keys["a"] !== state){
            keys["a"] = state
            socket.emit("keys", JSON.stringify(keys));
        }
    }else if(event.key === "s" || event.key === "ArrowDown"){
        if(keys["s"] !== state){
            keys["s"] = state
            socket.emit("keys", JSON.stringify(keys));
        }
    }else if(event.key === "d" || event.key === "ArrowRight"){
        if(keys["d"] !== state){
            keys["d"] = state
            socket.emit("keys", JSON.stringify(keys));
        }
    }
}

document.addEventListener("keydown", function (event) {
    handleEvent(event, true);
});

document.addEventListener("keyup", function (event) {
    handleEvent(event, false);
});
