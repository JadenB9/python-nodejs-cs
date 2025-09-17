# TCP Server-Client Network Communication

A project demonstrating basic TCP server-client communication with implementations in both **Node.js** and **Python**. Features TCP servers with HTTP endpoints and support for multiple concurrent connections.

## Project Structure

```
Networks/
├── server.js          # Node.js server (TCP + HTTP)
├── client.js          # Node.js interactive client
├── test-client.js     # Node.js automated test client
├── server.py          # Python server (TCP + HTTP)
├── client.py          # Python interactive client
├── test-client.py     # Python automated test client
├── package.json       # Node.js dependencies
├── requirements.txt   # Python requirements
└── README.md          # This file
```

## Features

- **Dual Implementation** - Both Node.js and Python versions with identical functionality
- **TCP Servers** - Node.js on `localhost:6666`, Python on `localhost:7777`
- **HTTP Servers** - Node.js on port 3000, Python on port 3001
- **Echo functionality** - Servers echo back all client messages
- **Multi-client support** - Multiple clients can connect simultaneously
- **Interactive clients** - Command-line interface for real-time communication
- **No external dependencies** - Python uses only standard library

## Prerequisites

### For Node.js Implementation:
- Node.js (version 14 or higher)
- npm (comes with Node.js)

### For Python Implementation:
- Python 3.6 or higher (for f-string support)
- No additional packages required (uses standard library only)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd Networks
   ```

2. **For Node.js - Install dependencies:**
   ```bash
   npm install
   ```

3. **For Python - No installation needed** (uses standard library only)

   Verify Python version:
   ```bash
   python3 --version
   ```

## Usage

### Choose Your Implementation

You can use either the **Node.js** or **Python** implementation (they have identical functionality):

### 1. Start a Server

#### Option A: Node.js Server
```bash
node server.js
```

You should see:
```
HTTP Server running on port 3000
TCP Server running on localhost:6666
```

#### Option B: Python Server
```bash
python3 server.py
```

You should see:
```
HTTP Server running on port 3001
TCP Server running on localhost:7777
```

### 2. Connect a Client

#### Option A: Interactive Clients

**Node.js Client (connects to Node.js server on port 6666):**
```bash
node client.js
```

**Python Client (connects to Python server on port 7777):**
```bash
python3 client.py
```

Both clients will:
- Connect to their respective TCP servers
- Show a prompt (`>`) where you can type messages
- Display server responses
- Type `quit` to disconnect

Example session:
```
Connected to server at localhost:7777
Type messages to send to server (type "quit" to exit):
Server response: Welcome to TCP Server on localhost:7777
> Hello World
Server response: Echo: Hello World
> How are you?
Server response: Echo: How are you?
> quit
Connection closed
```

#### Option B: Automated Test Clients

**Node.js Test Client:**
```bash
node test-client.js
```

**Python Test Client:**
```bash
python3 test-client.py
```

These send predefined test messages and automatically disconnect.

### 3. Multiple Clients

You can run multiple clients simultaneously. Each client will have its own independent connection:

**Example with Node.js:**
```bash
# Terminal 1: Start server
node server.js

# Terminal 2: First client
node client.js

# Terminal 3: Second client
node client.js
```

**Example with Python:**
```bash
# Terminal 1: Start server
python3 server.py

# Terminal 2: First client
python3 client.py

# Terminal 3: Second client
python3 client.py
```

**Cross-platform testing** (run both implementations simultaneously):
```bash
# Terminal 1: Node.js server (port 6666)
node server.js

# Terminal 2: Python server (port 7777)
python3 server.py

# Terminal 3: Node.js client to Node.js server
node client.js

# Terminal 4: Python client to Python server
python3 client.py
```

## How It Works

### Server Architecture

Both implementations provide identical functionality with language-specific approaches:

#### Node.js Implementation:
1. **TCP Server (Port 6666)**:
   - Uses Node.js `net` module
   - Handles multiple concurrent connections with events
   - Sends welcome message to new clients
   - Echoes back received messages
   - Logs all client activity

2. **HTTP Server (Port 3000)**:
   - Express.js framework
   - JSON API responses
   - CORS enabled

#### Python Implementation:
1. **TCP Server (Port 7777)**:
   - Uses Python `socket` module
   - Handles multiple concurrent connections with threading
   - Sends welcome message to new clients
   - Echoes back received messages
   - Logs all client activity

2. **HTTP Server (Port 3001)**:
   - Python's built-in `http.server`
   - JSON API responses
   - CORS headers included

### Client Functionality

Both client implementations provide the same user experience:

- **Connection**: Establishes TCP socket connection (Node.js: port 6666, Python: port 7777)
- **Communication**: Sends user input to server
- **Response Handling**: Displays server responses in real-time
- **Disconnection**: Clean connection termination with "quit" command
- **Interactive Mode**: Real-time command-line interface
- **Test Mode**: Automated testing with predefined messages

### Message Flow

```
Client                    Server
  |                         |
  |------ Connect --------> |
  |<--- Welcome Message --- |
  |                         |
  |------ "Hello" --------> |
  |<--- "Echo: Hello" ----- |
  |                         |
  |------ "quit" ---------> |
  |<--- Connection End ---- |
```

## Testing

### Basic Functionality Test

**Node.js:**
```bash
# Terminal 1: Start server
node server.js

# Terminal 2: Run test client
node test-client.js
```

**Python:**
```bash
# Terminal 1: Start server
python3 server.py

# Terminal 2: Run test client
python3 test-client.py
```

### Interactive Test

**Node.js:**
```bash
# Terminal 1: Start server
node server.js

# Terminal 2: Interactive client
node client.js
# Type some messages and verify echoes
```

**Python:**
```bash
# Terminal 1: Start server
python3 server.py

# Terminal 2: Interactive client
python3 client.py
# Type some messages and verify echoes
```

### Multiple Client Test

**Node.js:**
```bash
# Start server
node server.js

# Run multiple test clients simultaneously
node test-client.js &
node test-client.js &
wait
```

**Python:**
```bash
# Start server
python3 server.py

# Run multiple test clients simultaneously
python3 test-client.py &
python3 test-client.py &
wait
```

## Server Logs

Both implementations display detailed logs:

**Node.js Server:**
```
HTTP Server running on port 3000
TCP Server running on localhost:6666
Client connected: ::1:51234
Received from client: Hello World
Received from client: quit
Client disconnected
```

**Python Server:**
```
Starting Python TCP and HTTP servers...
HTTP Server running on port 3001
TCP Server running on localhost:7777
Client connected: 127.0.0.1:51234
Received from client: Hello World
Received from client: quit
Client disconnected
```

## Troubleshooting

### Port Already in Use
If you get "port already in use" errors:

**For Node.js (ports 6666, 3000):**
```bash
# Check what's using the ports
lsof -i :6666
lsof -i :3000

# Kill the process if needed
kill -9 <PID>
```

**For Python (ports 7777, 3001):**
```bash
# Check what's using the ports
lsof -i :7777
lsof -i :3001

# Kill the process if needed
kill -9 <PID>
```

### Connection Refused
- Ensure the server is running before starting clients
- Check that you're connecting to the correct port:
  - Node.js clients: port 6666
  - Python clients: port 7777

### Client Won't Quit
- Try Ctrl+C to force quit
- Check that the connection is properly established

## Stopping the Project

1. **Stop clients**: Type `quit` or press Ctrl+C
2. **Stop server**: Press Ctrl+C in the server terminal

## Network Details

### Node.js Implementation:
- **Protocol**: TCP
- **Host**: localhost (127.0.0.1)
- **TCP Port**: 6666
- **HTTP Port**: 3000
- **Encoding**: UTF-8
- **Connection Type**: Persistent until client disconnects

### Python Implementation:
- **Protocol**: TCP
- **Host**: localhost (127.0.0.1)
- **TCP Port**: 7777
- **HTTP Port**: 3001
- **Encoding**: UTF-8
- **Connection Type**: Persistent until client disconnects
- **Threading**: One thread per client connection

## Extension Ideas

- Add authentication
- Implement chat rooms
- Add file transfer capability
- Create a web-based client
- Add encryption
- Implement custom protocols

## Dependencies

### Node.js Dependencies:
- `express`: HTTP server framework
- `cors`: Cross-origin resource sharing
- `dotenv`: Environment variable management
- `net`: Built-in Node.js TCP module (no installation needed)
- `readline`: Built-in Node.js module for interactive input

### Python Dependencies:
- `socket`: Built-in Python TCP module (no installation needed)
- `threading`: Built-in Python threading module (no installation needed)
- `http.server`: Built-in Python HTTP server module (no installation needed)
- `json`: Built-in Python JSON module (no installation needed)
- `sys`: Built-in Python system module (no installation needed)
- `time`: Built-in Python time module (no installation needed)

**No external packages required for Python implementation!**
