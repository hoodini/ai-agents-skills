---
name: vercel
description: Deploy and configure applications on Vercel. Use when deploying Next.js apps, configuring serverless functions, setting up edge functions, or managing Vercel projects. Triggers on Vercel, deploy, serverless, edge function, Next.js deployment.
---

# Vercel Deployment

Deploy and scale applications on Vercel's edge network.

## Quick Start

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Production deploy
vercel --prod
```

## vercel.json Configuration

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "framework": "nextjs",
  "regions": ["iad1", "sfo1"],
  "functions": {
    "api/**/*.ts": {
      "memory": 1024,
      "maxDuration": 30
    }
  },
  "rewrites": [
    { "source": "/api/:path*", "destination": "/api/:path*" },
    { "source": "/:path*", "destination": "/" }
  ],
  "headers": [
    {
      "source": "/api/:path*",
      "headers": [
        { "key": "Access-Control-Allow-Origin", "value": "*" }
      ]
    }
  ],
  "env": {
    "DATABASE_URL": "@database-url"
  }
}
```

## Serverless Functions

```typescript
// api/hello.ts
import type { VercelRequest, VercelResponse } from '@vercel/node';

export default function handler(req: VercelRequest, res: VercelResponse) {
  const { name = 'World' } = req.query;
  res.status(200).json({ message: `Hello ${name}!` });
}
```

## Edge Functions

```typescript
// api/edge.ts
export const config = {
  runtime: 'edge',
};

export default function handler(request: Request) {
  return new Response(JSON.stringify({ message: 'Hello from Edge!' }), {
    headers: { 'content-type': 'application/json' },
  });
}
```

## Next.js App Router

```typescript
// app/api/route.ts
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const name = searchParams.get('name') ?? 'World';
  
  return NextResponse.json({ message: `Hello ${name}!` });
}

export async function POST(request: Request) {
  const body = await request.json();
  return NextResponse.json({ received: body });
}
```

## ISR (Incremental Static Regeneration)

```typescript
// app/posts/[id]/page.tsx
export const revalidate = 60; // Revalidate every 60 seconds

export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map((post) => ({ id: post.id }));
}

export default async function Post({ params }: { params: { id: string } }) {
  const post = await getPost(params.id);
  return <article>{post.content}</article>;
}
```

## Redis (Upstash)

Install Upstash Redis from the Vercel Marketplace and use `@upstash/redis`. `Redis.fromEnv()` reads `UPSTASH_REDIS_REST_URL`/`UPSTASH_REDIS_REST_TOKEN` or the `KV_REST_API_URL`/`KV_REST_API_TOKEN` vars the integration sets.

```typescript
import { Redis } from '@upstash/redis';

const kv = Redis.fromEnv();

// Set
await kv.set('user:123', { name: 'Alice', visits: 0 });

// Get
const user = await kv.get('user:123');

// Increment
await kv.incr('user:123:visits');

// Hash operations
await kv.hset('session:abc', { userId: '123', expires: Date.now() + 3600000 });
const session = await kv.hgetall('session:abc');
```

## Vercel Postgres

```typescript
import { sql } from '@vercel/postgres';

// Query
const { rows } = await sql`SELECT * FROM users WHERE id = ${userId}`;

// Insert
await sql`INSERT INTO users (name, email) VALUES (${name}, ${email})`;

// Transaction
await sql.query('BEGIN');
try {
  await sql`UPDATE accounts SET balance = balance - ${amount} WHERE id = ${from}`;
  await sql`UPDATE accounts SET balance = balance + ${amount} WHERE id = ${to}`;
  await sql.query('COMMIT');
} catch (e) {
  await sql.query('ROLLBACK');
  throw e;
}
```

## Environment Variables

```bash
# Add secret
vercel env add DATABASE_URL production

# Pull env vars locally
vercel env pull .env.local

# List env vars
vercel env ls
```

## Cron Jobs

```json
// vercel.json
{
  "crons": [
    {
      "path": "/api/daily-job",
      "schedule": "0 0 * * *"
    }
  ]
}
```

```typescript
// api/daily-job.ts
export default function handler(req, res) {
  // Verify it's from Vercel Cron
  if (req.headers['authorization'] !== `Bearer ${process.env.CRON_SECRET}`) {
    return res.status(401).end();
  }
  
  // Run job
  await runDailyJob();
  res.status(200).end();
}
```

## Resources

- **Vercel Docs**: https://vercel.com/docs
- **Next.js on Vercel**: https://vercel.com/docs/frameworks/nextjs
- **Upstash Redis SDK**: https://upstash.com/docs/redis/sdks/ts/overview
