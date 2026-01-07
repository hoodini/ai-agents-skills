---
name: cloudflare
description: Build and deploy on Cloudflare's edge platform. Use when creating Workers, Pages, D1 databases, R2 storage, AI inference, or KV storage. Triggers on Cloudflare, Workers, Cloudflare Pages, D1, R2, KV, Cloudflare AI, Durable Objects, edge computing.
---

# Cloudflare Platform

Build globally distributed applications on Cloudflare's edge network.

## Quick Start

```bash
# Install Wrangler CLI
npm install -g wrangler

# Login
wrangler login

# Create new Worker
wrangler init my-worker

# Deploy
wrangler deploy
```

## Workers

### Basic Worker
```typescript
// src/index.ts
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    
    if (url.pathname === '/api/hello') {
      return Response.json({ message: 'Hello from the edge!' });
    }
    
    return new Response('Not Found', { status: 404 });
  },
};
```

### wrangler.toml Configuration
```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"

[vars]
ENVIRONMENT = "production"

# KV Namespace
[[kv_namespaces]]
binding = "MY_KV"
id = "abc123"

# D1 Database
[[d1_databases]]
binding = "DB"
database_name = "my-database"
database_id = "def456"

# R2 Bucket
[[r2_buckets]]
binding = "BUCKET"
bucket_name = "my-bucket"

# AI
[ai]
binding = "AI"

# Durable Objects
[[durable_objects.bindings]]
name = "COUNTER"
class_name = "Counter"

[[migrations]]
tag = "v1"
new_classes = ["Counter"]
```

### Request Routing
```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const { pathname } = url;
    
    // Router pattern
    const routes: Record<string, () => Promise<Response>> = {
      '/api/users': () => handleUsers(request, env),
      '/api/posts': () => handlePosts(request, env),
    };
    
    const handler = routes[pathname];
    if (handler) {
      return handler();
    }
    
    // Wildcard matching
    if (pathname.startsWith('/api/users/')) {
      const userId = pathname.split('/')[3];
      return handleUser(userId, request, env);
    }
    
    return new Response('Not Found', { status: 404 });
  },
};
```

## KV Storage

```typescript
interface Env {
  MY_KV: KVNamespace;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    
    // Set value
    await env.MY_KV.put('key', 'value', {
      expirationTtl: 3600, // 1 hour
      metadata: { created: Date.now() },
    });
    
    // Get value
    const value = await env.MY_KV.get('key');
    
    // Get with metadata
    const { value: data, metadata } = await env.MY_KV.getWithMetadata('key');
    
    // List keys
    const list = await env.MY_KV.list({ prefix: 'user:' });
    
    // Delete
    await env.MY_KV.delete('key');
    
    return Response.json({ value });
  },
};
```

## D1 Database (SQLite)

```typescript
interface Env {
  DB: D1Database;
}

// Create tables (run once via wrangler d1 execute)
// wrangler d1 execute my-database --file=./schema.sql

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Query
    const { results } = await env.DB.prepare(
      'SELECT * FROM users WHERE id = ?'
    ).bind(1).all();
    
    // Insert
    const { meta } = await env.DB.prepare(
      'INSERT INTO users (name, email) VALUES (?, ?)'
    ).bind('Alice', 'alice@example.com').run();
    
    // Batch operations
    const batch = await env.DB.batch([
      env.DB.prepare('INSERT INTO logs (action) VALUES (?)').bind('login'),
      env.DB.prepare('UPDATE users SET last_login = ? WHERE id = ?').bind(Date.now(), 1),
    ]);
    
    // First result only
    const user = await env.DB.prepare(
      'SELECT * FROM users WHERE email = ?'
    ).bind('alice@example.com').first();
    
    return Response.json({ results, insertId: meta.last_row_id });
  },
};
```

### Schema Example
```sql
-- schema.sql
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## R2 Object Storage

```typescript
interface Env {
  BUCKET: R2Bucket;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const key = url.pathname.slice(1);
    
    switch (request.method) {
      case 'PUT': {
        // Upload file
        const body = await request.arrayBuffer();
        await env.BUCKET.put(key, body, {
          httpMetadata: {
            contentType: request.headers.get('content-type') || 'application/octet-stream',
          },
          customMetadata: {
            uploadedBy: 'api',
          },
        });
        return new Response('Uploaded', { status: 201 });
      }
      
      case 'GET': {
        // Download file
        const object = await env.BUCKET.get(key);
        if (!object) {
          return new Response('Not Found', { status: 404 });
        }
        
        const headers = new Headers();
        object.writeHttpMetadata(headers);
        headers.set('etag', object.httpEtag);
        
        return new Response(object.body, { headers });
      }
      
      case 'DELETE': {
        await env.BUCKET.delete(key);
        return new Response('Deleted');
      }
      
      default:
        return new Response('Method Not Allowed', { status: 405 });
    }
  },
};

// List objects
async function listObjects(env: Env, prefix?: string) {
  const listed = await env.BUCKET.list({
    prefix,
    limit: 100,
  });
  return listed.objects.map(obj => ({
    key: obj.key,
    size: obj.size,
    uploaded: obj.uploaded,
  }));
}
```

## Cloudflare AI

```typescript
interface Env {
  AI: Ai;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const { prompt } = await request.json();
    
    // Text generation (Llama, Mistral, etc.)
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: prompt },
      ],
      max_tokens: 1024,
    });
    
    return Response.json(response);
  },
};

// Image generation
async function generateImage(env: Env, prompt: string) {
  const response = await env.AI.run('@cf/stabilityai/stable-diffusion-xl-base-1.0', {
    prompt,
    num_steps: 20,
  });
  
  return new Response(response, {
    headers: { 'content-type': 'image/png' },
  });
}

// Text embeddings
async function getEmbeddings(env: Env, text: string) {
  const response = await env.AI.run('@cf/baai/bge-base-en-v1.5', {
    text: [text],
  });
  return response.data[0]; // Float32Array
}

// Image classification
async function classifyImage(env: Env, imageData: ArrayBuffer) {
  const response = await env.AI.run('@cf/microsoft/resnet-50', {
    image: [...new Uint8Array(imageData)],
  });
  return response;
}

// Speech to text
async function transcribe(env: Env, audioData: ArrayBuffer) {
  const response = await env.AI.run('@cf/openai/whisper', {
    audio: [...new Uint8Array(audioData)],
  });
  return response.text;
}
```

## Durable Objects

```typescript
// Durable Object class
export class Counter {
  state: DurableObjectState;
  
  constructor(state: DurableObjectState) {
    this.state = state;
  }
  
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    
    let value = (await this.state.storage.get<number>('count')) || 0;
    
    switch (url.pathname) {
      case '/increment':
        value++;
        await this.state.storage.put('count', value);
        break;
      case '/decrement':
        value--;
        await this.state.storage.put('count', value);
        break;
    }
    
    return Response.json({ count: value });
  }
}

// Worker using Durable Object
interface Env {
  COUNTER: DurableObjectNamespace;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Get unique ID for this counter (e.g., per user)
    const counterId = env.COUNTER.idFromName('global-counter');
    const counter = env.COUNTER.get(counterId);
    
    // Forward request to Durable Object
    return counter.fetch(request);
  },
};
```

## Cloudflare Pages

### pages.toml (Functions Config)
```toml
[build]
command = "npm run build"
output_directory = "dist"

[[redirects]]
from = "/old-page"
to = "/new-page"
status = 301

[[headers]]
for = "/api/*"
[headers.values]
Access-Control-Allow-Origin = "*"
```

### Pages Functions
```typescript
// functions/api/hello.ts
export const onRequestGet: PagesFunction = async (context) => {
  return Response.json({ message: 'Hello!' });
};

export const onRequestPost: PagesFunction<Env> = async (context) => {
  const body = await context.request.json();
  
  // Access bindings
  await context.env.KV.put('key', JSON.stringify(body));
  
  return Response.json({ success: true });
};

// functions/api/users/[id].ts
export const onRequestGet: PagesFunction = async (context) => {
  const userId = context.params.id;
  return Response.json({ userId });
};

// Middleware: functions/_middleware.ts
export const onRequest: PagesFunction = async (context) => {
  // Auth check
  const auth = context.request.headers.get('Authorization');
  if (!auth) {
    return new Response('Unauthorized', { status: 401 });
  }
  
  // Continue to next handler
  return context.next();
};
```

## Queues

```typescript
// Producer
interface Env {
  MY_QUEUE: Queue;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Send message to queue
    await env.MY_QUEUE.send({
      type: 'email',
      to: 'user@example.com',
      subject: 'Welcome!',
    });
    
    // Batch send
    await env.MY_QUEUE.sendBatch([
      { body: { task: 'process', id: 1 } },
      { body: { task: 'process', id: 2 } },
    ]);
    
    return Response.json({ queued: true });
  },
};

// Consumer
export default {
  async queue(batch: MessageBatch<any>, env: Env): Promise<void> {
    for (const message of batch.messages) {
      try {
        await processMessage(message.body);
        message.ack();
      } catch (error) {
        message.retry();
      }
    }
  },
};
```

## Cron Triggers

```toml
# wrangler.toml
[triggers]
crons = ["0 0 * * *", "*/15 * * * *"]  # Daily at midnight, every 15 min
```

```typescript
export default {
  async scheduled(event: ScheduledEvent, env: Env, ctx: ExecutionContext): Promise<void> {
    switch (event.cron) {
      case '0 0 * * *':
        await dailyCleanup(env);
        break;
      case '*/15 * * * *':
        await checkHealthStatus(env);
        break;
    }
  },
};
```

## WebSockets

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const upgradeHeader = request.headers.get('Upgrade');
    
    if (upgradeHeader === 'websocket') {
      const [client, server] = Object.values(new WebSocketPair());
      
      server.accept();
      server.addEventListener('message', (event) => {
        server.send(`Echo: ${event.data}`);
      });
      
      return new Response(null, {
        status: 101,
        webSocket: client,
      });
    }
    
    return new Response('Expected WebSocket', { status: 400 });
  },
};
```

## Resources

- **Workers Docs**: https://developers.cloudflare.com/workers/
- **D1 Docs**: https://developers.cloudflare.com/d1/
- **R2 Docs**: https://developers.cloudflare.com/r2/
- **Pages Docs**: https://developers.cloudflare.com/pages/
- **AI Docs**: https://developers.cloudflare.com/workers-ai/
- **Wrangler CLI**: https://developers.cloudflare.com/workers/wrangler/
