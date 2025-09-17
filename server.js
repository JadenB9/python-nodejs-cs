const express = require('express');
const cors = require('cors');
const net = require('net');
require('dotenv').config();

const app = express();
const HTTP_PORT = process.env.PORT || 3000;
const TCP_PORT = 6666;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.json({ message: 'Hello from your new Node.js server!' });
});

const tcpServer = net.createServer((socket) => {
    console.log(`Client connected: ${socket.remoteAddress}:${socket.remotePort}`);

    socket.write('Welcome to TCP Server on localhost:6666\n');

    socket.on('data', (data) => {
        const message = data.toString().trim();
        console.log(`Received from client: ${message}`);

        socket.write(`Echo: ${message}\n`);
    });

    socket.on('end', () => {
        console.log('Client disconnected');
    });

    socket.on('error', (err) => {
        console.log(`Socket error: ${err.message}`);
    });
});

tcpServer.listen(TCP_PORT, 'localhost', () => {
    console.log(`TCP Server running on localhost:${TCP_PORT}`);
});

app.listen(HTTP_PORT, () => {
    console.log(`HTTP Server running on port ${HTTP_PORT}`);
});
