const net = require('net');
const readline = require('readline');

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

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const client = new net.Socket();
let isConnected = false;

client.connect(SERVER_PORT, SERVER_HOST, () => {
    console.log(`Connected to server at ${SERVER_HOST}:${SERVER_PORT}`);
    console.log('Type messages to send to server (type "quit" to exit):');
    isConnected = true;
    promptUser();
});

client.on('data', (data) => {
    console.log('Server response:', data.toString().trim());
    if (isConnected) {
        promptUser();
    }
});

client.on('close', () => {
    console.log('Connection closed');
    isConnected = false;
    rl.close();
    process.exit(0);
});

client.on('error', (err) => {
    console.log(`Connection error: ${err.message}`);
    isConnected = false;
    rl.close();
    process.exit(1);
});

function promptUser() {
    if (!isConnected) return;

    rl.question('> ', (input) => {
        if (!isConnected) return;

        if (input.toLowerCase() === 'quit') {
            isConnected = false;
            client.end();
            return;
        }

        client.write(input);
    });
}