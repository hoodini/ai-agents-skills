---
name: bun
description: Build fast applications with Bun JavaScript runtime. Use when creating Bun projects, using Bun APIs, bundling, testing, or optimizing Node.js alternatives. Triggers on Bun, Bun runtime, bun.sh, bunx, Bun serve, Bun test, JavaScript runtime.
---

# Bun - The Fast JavaScript Runtime

Build and run JavaScript/TypeScript applications with Bun's all-in-one toolkit.

## Quick Start

```bash
# Install Bun (macOS, Linux, WSL)
curl -fsSL https://bun.sh/install | bash

# Windows
powershell -c "irm bun.sh/install.ps1 | iex"

# Create new project
bun init

# Run TypeScript directly (no build step!)
bun run index.ts

# Install packages (faster than npm)
bun install

# Run scripts
bun run dev
```

## Package Management

```bash
# Install dependencies
bun install              # Install all from package.json
bun add express          # Add dependency
bun add -d typescript    # Add dev dependency
bun add -g serve         # Add global package

# Remove packages
bun remove express

# Update packages
bun update

# Run package binaries
bunx prisma generate     # Like npx but faster
bunx create-next-app

# Lockfile
bun install --frozen-lockfile  # CI mode
```

### bun.lockb vs package-lock.json
```bash
# Bun uses binary lockfile (bun.lockb) - much faster
# To generate yarn.lock for compatibility:
bun install --yarn

# Import from other lockfiles
bun install  # Auto-detects package-lock.json, yarn.lock
```

## Bun Runtime

### Run Files
```bash
# Run any file
bun run index.ts         # TypeScript
bun run index.js         # JavaScript
bun run index.jsx        # JSX

# Watch mode
bun --watch run index.ts

# Hot reload
bun --hot run server.ts
```

### Built-in APIs
```typescript
// File I/O (super fast)
const file = Bun.file('data.json');
const content = await file.text();
const json = await file.json();
const bytes = await file.arrayBuffer();

// Write files
await Bun.write('output.txt', 'Hello, Bun!');
await Bun.write('data.json', JSON.stringify({ key: 'value' }));
await Bun.write('image.png', await fetch('https://example.com/img.png'));

// File metadata
const file = Bun.file('data.json');
console.log(file.size);       // bytes
console.log(file.type);       // MIME type
console.log(file.lastModified);

// Glob files
const glob = new Bun.Glob('**/*.ts');
for await (const file of glob.scan('.')) {
  console.log(file);
}
```

### HTTP Server
```typescript
// Simple server
const server = Bun.serve({
  port: 3000,
  fetch(req) {
    const url = new URL(req.url);
    
    if (url.pathname === '/') {
      return new Response('Hello, Bun!');
    }
    
    if (url.pathname === '/json') {
      return Response.json({ message: 'Hello!' });
    }
    
    return new Response('Not Found', { status: 404 });
  },
});

console.log(`Server running at http://localhost:${server.port}`);
```

### Advanced Server
```typescript
Bun.serve({
  port: 3000,
  
  // Main request handler
  async fetch(req, server) {
    const url = new URL(req.url);
    
    // WebSocket upgrade
    if (url.pathname === '/ws') {
      const upgraded = server.upgrade(req, {
        data: { userId: '123' },  // Attach data to socket
      });
      if (upgraded) return undefined;
    }
    
    // Static files
    if (url.pathname.startsWith('/static/')) {
      const filePath = `./public${url.pathname}`;
      const file = Bun.file(filePath);
      if (await file.exists()) {
        return new Response(file);
      }
    }
    
    // JSON API
    if (url.pathname === '/api/data' && req.method === 'POST') {
      const body = await req.json();
      return Response.json({ received: body });
    }
    
    return new Response('Not Found', { status: 404 });
  },
  
  // WebSocket handlers
  websocket: {
    open(ws) {
      console.log('Client connected:', ws.data.userId);
      ws.subscribe('chat');  // Pub/sub
    },
    message(ws, message) {
      // Broadcast to all subscribers
      ws.publish('chat', message);
    },
    close(ws) {
      console.log('Client disconnected');
    },
  },
  
  // Error handling
  error(error) {
    return new Response(`Error: ${error.message}`, { status: 500 });
  },
});
```

### WebSocket Client
```typescript
const ws = new WebSocket('ws://localhost:3000/ws');

ws.onopen = () => {
  ws.send('Hello, server!');
};

ws.onmessage = (event) => {
  console.log('Received:', event.data);
};
```

## Bun APIs

### SQLite (Built-in)
```typescript
import { Database } from 'bun:sqlite';

const db = new Database('mydb.sqlite');

// Create table
db.run(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
  )
`);

// Insert
const insert = db.prepare('INSERT INTO users (name, email) VALUES (?, ?)');
insert.run('Alice', 'alice@example.com');

// Query
const query = db.prepare('SELECT * FROM users WHERE id = ?');
const user = query.get(1);

// All results
const allUsers = db.prepare('SELECT * FROM users').all();

// Transaction
const insertMany = db.transaction((users) => {
  for (const user of users) {
    insert.run(user.name, user.email);
  }
});

insertMany([
  { name: 'Bob', email: 'bob@example.com' },
  { name: 'Charlie', email: 'charlie@example.com' },
]);
```

### Password Hashing (Built-in)
```typescript
// Hash password
const hash = await Bun.password.hash('mypassword', {
  algorithm: 'argon2id',  // or 'bcrypt'
  memoryCost: 65536,      // 64 MB
  timeCost: 2,
});

// Verify password
const isValid = await Bun.password.verify('mypassword', hash);
```

### Spawn Processes
```typescript
// Spawn process
const proc = Bun.spawn(['ls', '-la'], {
  cwd: '/home/user',
  env: { ...process.env, MY_VAR: 'value' },
  stdout: 'pipe',
});

const output = await new Response(proc.stdout).text();
console.log(output);

// Spawn sync
const result = Bun.spawnSync(['echo', 'hello']);
console.log(result.stdout.toString());

// Shell command
const { stdout } = Bun.spawn({
  cmd: ['sh', '-c', 'echo $HOME'],
  stdout: 'pipe',
});
```

### Hashing & Crypto
```typescript
// Hash strings
const hash = Bun.hash('hello world');  // Wyhash (fast)

// Crypto hashes
const sha256 = new Bun.CryptoHasher('sha256');
sha256.update('data');
const digest = sha256.digest('hex');

// One-liner
const md5 = Bun.CryptoHasher.hash('md5', 'data', 'hex');

// HMAC
const hmac = Bun.CryptoHasher.hmac('sha256', 'secret-key', 'data', 'hex');
```

## Bundler

```bash
# Bundle for browser
bun build ./src/index.ts --outdir ./dist

# Bundle options
bun build ./src/index.ts \
  --outdir ./dist \
  --minify \
  --sourcemap \
  --target browser \
  --splitting \
  --entry-naming '[dir]/[name]-[hash].[ext]'
```

### Build API
```typescript
const result = await Bun.build({
  entrypoints: ['./src/index.ts'],
  outdir: './dist',
  minify: true,
  sourcemap: 'external',
  target: 'browser',  // 'bun' | 'node' | 'browser'
  splitting: true,
  naming: {
    entry: '[dir]/[name]-[hash].[ext]',
    chunk: '[name]-[hash].[ext]',
    asset: '[name]-[hash].[ext]',
  },
  external: ['react', 'react-dom'],
  define: {
    'process.env.NODE_ENV': JSON.stringify('production'),
  },
  loader: {
    '.png': 'file',
    '.svg': 'text',
  },
});

if (!result.success) {
  console.error('Build failed:', result.logs);
}
```

## Testing

```typescript
// test.ts
import { describe, test, expect, beforeAll, afterAll, mock } from 'bun:test';

describe('Math operations', () => {
  test('addition', () => {
    expect(1 + 1).toBe(2);
  });
  
  test('array contains', () => {
    expect([1, 2, 3]).toContain(2);
  });
  
  test('object matching', () => {
    expect({ name: 'Alice', age: 30 }).toMatchObject({ name: 'Alice' });
  });
  
  test('async test', async () => {
    const result = await Promise.resolve(42);
    expect(result).toBe(42);
  });
  
  test('throws error', () => {
    expect(() => {
      throw new Error('fail');
    }).toThrow('fail');
  });
});

// Mocking
const mockFn = mock(() => 'mocked');
mockFn();
expect(mockFn).toHaveBeenCalled();

// Mock modules
mock.module('./database', () => ({
  query: mock(() => [{ id: 1 }]),
}));
```

```bash
# Run tests
bun test

# Watch mode
bun test --watch

# Specific file
bun test user.test.ts

# Coverage
bun test --coverage
```

## Node.js Compatibility

```typescript
// Most Node.js APIs work out of the box
import fs from 'fs';
import path from 'path';
import { createServer } from 'http';
import express from 'express';

// Bun implements Node.js APIs
const data = fs.readFileSync('file.txt', 'utf-8');
const fullPath = path.join(__dirname, 'file.txt');

// Express works!
const app = express();
app.get('/', (req, res) => res.send('Hello!'));
app.listen(3000);
```

### Node.js vs Bun APIs
```typescript
// Node.js way
import { readFile } from 'fs/promises';
const content = await readFile('file.txt', 'utf-8');

// Bun way (faster)
const content = await Bun.file('file.txt').text();

// Node.js crypto
import crypto from 'crypto';
const hash = crypto.createHash('sha256').update('data').digest('hex');

// Bun way (faster)
const hash = Bun.CryptoHasher.hash('sha256', 'data', 'hex');
```

## Environment Variables

```typescript
// .env file support (built-in, no dotenv needed!)
// .env
// DATABASE_URL=postgres://localhost/db
// API_KEY=secret

// Access env vars
const dbUrl = Bun.env.DATABASE_URL;
const apiKey = process.env.API_KEY;  // Also works

// bunfig.toml for Bun config
// [run]
// preload = ["./setup.ts"]
```

## HTTP Client

```typescript
// Fetch (optimized in Bun)
const response = await fetch('https://api.example.com/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token',
  },
  body: JSON.stringify({ key: 'value' }),
});

const data = await response.json();

// Streaming response
const response = await fetch('https://api.example.com/stream');
const reader = response.body?.getReader();

while (true) {
  const { done, value } = await reader!.read();
  if (done) break;
  console.log(new TextDecoder().decode(value));
}
```

## Project Structure

```
my-bun-project/
├── src/
│   ├── index.ts          # Entry point
│   ├── routes/
│   │   └── api.ts
│   └── lib/
│       └── database.ts
├── tests/
│   └── index.test.ts
├── public/
│   └── static files
├── package.json
├── bunfig.toml           # Bun config (optional)
├── tsconfig.json
└── .env
```

### bunfig.toml
```toml
[install]
# Use exact versions by default
exact = true

# Registry
registry = "https://registry.npmjs.org"

[run]
# Scripts to run before `bun run`
preload = ["./instrumentation.ts"]

[test]
# Test configuration
coverage = true
coverageDir = "coverage"

[bundle]
# Default bundle config
minify = true
sourcemap = "external"
```

## Performance Comparison

| Operation | Node.js | Bun | Speedup |
|-----------|---------|-----|---------|
| Start time | ~40ms | ~7ms | 5.7x |
| Package install | ~10s | ~1s | 10x |
| File read | baseline | faster | 10x |
| HTTP server | baseline | faster | 4x |
| SQLite | external | built-in | 3x |
| TypeScript | compile needed | native | ∞ |

## Resources

- **Bun Docs**: https://bun.sh/docs
- **Bun API Reference**: https://bun.sh/docs/api
- **Bun Discord**: https://bun.sh/discord
- **GitHub**: https://github.com/oven-sh/bun
