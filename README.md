# Networks

Small project I wrote for a networking class: the same TCP echo server and
client implemented twice, once in Node.js and once in Python, so I could
compare how the two languages handle sockets.

Both servers do the same thing — accept multiple clients, send a welcome
line, echo anything the client sends, and reply `Bye` and hang up on `quit`.

## Running it

### Node.js version

```bash
npm install
node server.js      # TCP on 6666, plus an Express HTTP route on 3000
node client.js      # interactive client, or: node test-client.js
```

### Python version

```bash
python3 server.py   # TCP on 7777, HTTP on 3001 — standard library only
python3 client.py   # interactive client, or: python3 test-client.py
```

You can run both servers at once on their own ports. Every script also
takes `--port N` if the default is taken:

```bash
node server.js --port 6700
node client.js --port 6700
```

`npm test` just syntax-checks the JS files. The GitHub Actions workflow
does that plus a quick smoke test: start each server, run its test client,
and check the echo came back.

## Notes

- Node uses the `net` module with event callbacks for concurrency.
- Python uses `socket` + one thread per connection.
- Both use UTF-8 and a plain newline-terminated protocol, nothing fancy.
- The HTTP endpoints were mostly so I could hit the server from a browser
  while debugging.

Written for a class assignment, kept around because it's a handy socket
reference when I want to remember how to do this in either language.
