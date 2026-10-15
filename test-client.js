const net = require('net');

const SERVER_HOST = 'localhost';

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

const SERVER_PORT = portFromArgs(6666);

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