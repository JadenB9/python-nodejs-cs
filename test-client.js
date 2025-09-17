const net = require('net');

const SERVER_HOST = 'localhost';
const SERVER_PORT = 6666;

const client = new net.Socket();

client.connect(SERVER_PORT, SERVER_HOST, () => {
    console.log(`Connected to server at ${SERVER_HOST}:${SERVER_PORT}`);

    client.write('Hello from test client!');

    setTimeout(() => {
        client.write('Second message from client');
    }, 1000);

    setTimeout(() => {
        client.write('quit');
        client.end();
    }, 2000);
});

client.on('data', (data) => {
    console.log('Server response:', data.toString().trim());
});

client.on('close', () => {
    console.log('Connection closed');
    process.exit(0);
});

client.on('error', (err) => {
    console.log(`Connection error: ${err.message}`);
    process.exit(1);
});