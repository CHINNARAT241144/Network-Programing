const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app)
const {Server} = require("socket.io");
const io = new Server(server);

app.get('/',(reg, res) => {
    res.sendFile(__dirname + '/index.html');
});

io.on('conection',(socket) => {
    console.log('a user connected');

    socket.on("disconect", function () {
        console.log("user disconected");
    });
});

server.listen(3000, ()=> {
    console.log('listening on *:3000')
});
