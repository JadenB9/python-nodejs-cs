const express = require('express');
const cors = require('cors');
const net = require('net');
require('dotenv').config();

const app = express();
const HTTP_PORT = process.env.PORT || 3000;

// optional --port N on the command line
function portFromArgs(defaultPort) {
    const i = process.argv.indexOf('--port');
    if (i === -1) return defaultPort;
    const port = Number(process.argv[i + 1]);
    if (!Number.isInteger(port) || port < 1 || port > 65535) {
        console.log('usage: --port <1-65535>');
        process.exit(1);
    }
    return port;
}

const TCP_PORT = portFromArgs(6666);

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.json({ message: 'Hello from your new Node.js server!' });
});

const tcpServer = net.createServer((socket) => {
    console.log(`Client connected: ${socket.remoteAddress}:${socket.remotePort}`);

    socket.write(`Welcome to TCP Server on localhost:${TCP_PORT}\n`);

    socket.on('data', (data) => {
        const message = data.toString().trim();
        console.log(`Received from client: ${message}`);

        if (message.toLowerCase() === 'quit') {
            socket.end('Bye\n');
            return;
        }

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
