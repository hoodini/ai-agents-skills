---
name: mongodb
description: Work with MongoDB databases using best practices. Use when designing schemas, writing queries, building aggregation pipelines, or optimizing performance. Triggers on MongoDB, Mongoose, NoSQL, aggregation pipeline, document database, MongoDB Atlas.
---

# MongoDB & Mongoose

Build and query MongoDB databases with best practices.

## Quick Start

```bash
npm install mongodb mongoose
```

### Native Driver
```typescript
import { MongoClient, ObjectId } from 'mongodb';

const client = new MongoClient(process.env.MONGODB_URI!);
const db = client.db('myapp');
const users = db.collection('users');

// Connect
await client.connect();

// CRUD Operations
await users.insertOne({ name: 'Alice', email: 'alice@example.com' });
const user = await users.findOne({ email: 'alice@example.com' });
await users.updateOne({ _id: user._id }, { $set: { name: 'Alice Smith' } });
await users.deleteOne({ _id: user._id });
```

### Mongoose Setup
```typescript
import mongoose from 'mongoose';

await mongoose.connect(process.env.MONGODB_URI!, {
  maxPoolSize: 10,
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 45000,
});

// Connection events
mongoose.connection.on('connected', () => console.log('MongoDB connected'));
mongoose.connection.on('error', (err) => console.error('MongoDB error:', err));
mongoose.connection.on('disconnected', () => console.log('MongoDB disconnected'));

// Graceful shutdown
process.on('SIGINT', async () => {
  await mongoose.connection.close();
  process.exit(0);
});
```

## Schema Design

### Basic Schema
```typescript
import mongoose, { Schema, Document, Model } from 'mongoose';

interface IUser extends Document {
  email: string;
  name: string;
  password: string;
  role: 'user' | 'admin';
  profile: {
    avatar?: string;
    bio?: string;
  };
  createdAt: Date;
  updatedAt: Date;
}

const userSchema = new Schema<IUser>({
  email: {
    type: String,
    required: [true, 'Email is required'],
    unique: true,
    lowercase: true,
    trim: true,
    match: [/^\S+@\S+\.\S+$/, 'Invalid email format'],
  },
  name: {
    type: String,
    required: true,
    trim: true,
    minlength: 2,
    maxlength: 100,
  },
  password: {
    type: String,
    required: true,
    select: false,  // Never return password by default
  },
  role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user',
  },
  profile: {
    avatar: String,
    bio: { type: String, maxlength: 500 },
  },
}, {
  timestamps: true,  // Adds createdAt, updatedAt
  toJSON: {
    transform(doc, ret) {
      delete ret.password;
      delete ret.__v;
      return ret;
    },
  },
});

// Indexes
userSchema.index({ email: 1 });
userSchema.index({ createdAt: -1 });
userSchema.index({ name: 'text', 'profile.bio': 'text' });  // Text search

const User: Model<IUser> = mongoose.model('User', userSchema);
```

### Embedded Documents vs References

```typescript
// ✅ Embed when: Data is read together, doesn't grow unbounded
const orderSchema = new Schema({
  customer: {
    name: String,
    email: String,
    address: {
      street: String,
      city: String,
      country: String,
    },
  },
  items: [{
    product: String,
    quantity: Number,
    price: Number,
  }],
  total: Number,
});

// ✅ Reference when: Data is large, shared, or changes independently
const postSchema = new Schema({
  title: String,
  content: String,
  author: {
    type: Schema.Types.ObjectId,
    ref: 'User',
    required: true,
  },
  comments: [{
    type: Schema.Types.ObjectId,
    ref: 'Comment',
  }],
});

// Populate references
const post = await Post.findById(id)
  .populate('author', 'name email')  // Select specific fields
  .populate({
    path: 'comments',
    populate: { path: 'author', select: 'name' },  // Nested populate
  });
```

### Virtuals
```typescript
const userSchema = new Schema({
  firstName: String,
  lastName: String,
});

// Virtual field (not stored in DB)
userSchema.virtual('fullName').get(function() {
  return `${this.firstName} ${this.lastName}`;
});

// Virtual populate (for reverse references)
userSchema.virtual('posts', {
  ref: 'Post',
  localField: '_id',
  foreignField: 'author',
});

// Enable virtuals in JSON
userSchema.set('toJSON', { virtuals: true });
userSchema.set('toObject', { virtuals: true });
```

## Query Operations

### Find Operations
```typescript
// Find with filters
const users = await User.find({
  role: 'user',
  createdAt: { $gte: new Date('2024-01-01') },
});

// Query builder
const results = await User.find()
  .where('role').equals('user')
  .where('createdAt').gte(new Date('2024-01-01'))
  .select('name email')
  .sort({ createdAt: -1 })
  .limit(10)
  .skip(20)
  .lean();  // Return plain objects (faster)

// Find one
const user = await User.findOne({ email: 'alice@example.com' });
const userById = await User.findById(id);

// Exists check
const exists = await User.exists({ email: 'alice@example.com' });

// Count
const count = await User.countDocuments({ role: 'admin' });
```

### Query Operators
```typescript
// Comparison
await User.find({ age: { $eq: 25 } });      // Equal
await User.find({ age: { $ne: 25 } });      // Not equal
await User.find({ age: { $gt: 25 } });      // Greater than
await User.find({ age: { $gte: 25 } });     // Greater or equal
await User.find({ age: { $lt: 25 } });      // Less than
await User.find({ age: { $lte: 25 } });     // Less or equal
await User.find({ age: { $in: [20, 25, 30] } });   // In array
await User.find({ age: { $nin: [20, 25] } });      // Not in array

// Logical
await User.find({
  $and: [{ age: { $gte: 18 } }, { role: 'user' }],
});
await User.find({
  $or: [{ role: 'admin' }, { isVerified: true }],
});
await User.find({ age: { $not: { $lt: 18 } } });

// Element
await User.find({ avatar: { $exists: true } });
await User.find({ score: { $type: 'number' } });

// Array
await User.find({ tags: 'nodejs' });  // Array contains value
await User.find({ tags: { $all: ['nodejs', 'mongodb'] } });  // Contains all
await User.find({ tags: { $size: 3 } });  // Array length
await User.find({ 'items.0.price': { $gt: 100 } });  // Array index

// Text search
await User.find({ $text: { $search: 'mongodb developer' } });

// Regex
await User.find({ name: { $regex: /^john/i } });
```

### Update Operations
```typescript
// Update one
await User.updateOne(
  { _id: userId },
  { $set: { name: 'New Name' } }
);

// Update many
await User.updateMany(
  { role: 'user' },
  { $set: { isVerified: true } }
);

// Find and update (returns document)
const updated = await User.findByIdAndUpdate(
  userId,
  { $set: { name: 'New Name' } },
  { new: true, runValidators: true }  // Return updated doc, run validators
);

// Update operators
await User.updateOne({ _id: userId }, {
  $set: { name: 'New Name' },          // Set field
  $unset: { tempField: '' },           // Remove field
  $inc: { loginCount: 1 },             // Increment
  $mul: { score: 1.5 },                // Multiply
  $min: { lowScore: 50 },              // Set if less than
  $max: { highScore: 100 },            // Set if greater than
  $push: { tags: 'new-tag' },          // Add to array
  $pull: { tags: 'old-tag' },          // Remove from array
  $addToSet: { tags: 'unique-tag' },   // Add if not exists
});

// Upsert (insert if not exists)
await User.updateOne(
  { email: 'new@example.com' },
  { $set: { name: 'New User' } },
  { upsert: true }
);
```

## Aggregation Pipeline

### Basic Aggregation
```typescript
const results = await Order.aggregate([
  // Stage 1: Match
  { $match: { status: 'completed' } },
  
  // Stage 2: Group
  { $group: {
    _id: '$customerId',
    totalOrders: { $sum: 1 },
    totalSpent: { $sum: '$total' },
    avgOrder: { $avg: '$total' },
  }},
  
  // Stage 3: Sort
  { $sort: { totalSpent: -1 } },
  
  // Stage 4: Limit
  { $limit: 10 },
]);
```

### Pipeline Stages
```typescript
const pipeline = [
  // $match - Filter documents
  { $match: { createdAt: { $gte: new Date('2024-01-01') } } },
  
  // $project - Shape output
  { $project: {
    name: 1,
    email: 1,
    yearJoined: { $year: '$createdAt' },
    fullName: { $concat: ['$firstName', ' ', '$lastName'] },
  }},
  
  // $lookup - Join collections
  { $lookup: {
    from: 'orders',
    localField: '_id',
    foreignField: 'userId',
    as: 'orders',
  }},
  
  // $unwind - Flatten arrays
  { $unwind: { path: '$orders', preserveNullAndEmptyArrays: true } },
  
  // $group - Aggregate
  { $group: {
    _id: '$_id',
    name: { $first: '$name' },
    orderCount: { $sum: 1 },
    orders: { $push: '$orders' },
  }},
  
  // $addFields - Add computed fields
  { $addFields: {
    hasOrders: { $gt: ['$orderCount', 0] },
  }},
  
  // $facet - Multiple pipelines
  { $facet: {
    topCustomers: [{ $sort: { orderCount: -1 } }, { $limit: 5 }],
    stats: [{ $group: { _id: null, avgOrders: { $avg: '$orderCount' } } }],
  }},
];
```

### Analytics Examples
```typescript
// Sales by month
const salesByMonth = await Order.aggregate([
  { $match: { status: 'completed' } },
  { $group: {
    _id: {
      year: { $year: '$createdAt' },
      month: { $month: '$createdAt' },
    },
    totalSales: { $sum: '$total' },
    orderCount: { $sum: 1 },
  }},
  { $sort: { '_id.year': -1, '_id.month': -1 } },
]);

// Top products
const topProducts = await Order.aggregate([
  { $unwind: '$items' },
  { $group: {
    _id: '$items.productId',
    totalQuantity: { $sum: '$items.quantity' },
    totalRevenue: { $sum: { $multiply: ['$items.price', '$items.quantity'] } },
  }},
  { $lookup: {
    from: 'products',
    localField: '_id',
    foreignField: '_id',
    as: 'product',
  }},
  { $unwind: '$product' },
  { $project: {
    name: '$product.name',
    totalQuantity: 1,
    totalRevenue: 1,
  }},
  { $sort: { totalRevenue: -1 } },
  { $limit: 10 },
]);
```

## Middleware (Hooks)

```typescript
// Pre-save middleware
userSchema.pre('save', async function(next) {
  if (this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 12);
  }
  next();
});

// Post-save middleware
userSchema.post('save', function(doc) {
  console.log('User saved:', doc._id);
});

// Pre-find middleware
userSchema.pre(/^find/, function(next) {
  // Exclude deleted users by default
  this.find({ isDeleted: { $ne: true } });
  next();
});

// Pre-aggregate middleware
userSchema.pre('aggregate', function(next) {
  // Add match stage to all aggregations
  this.pipeline().unshift({ $match: { isDeleted: { $ne: true } } });
  next();
});
```

## Transactions

```typescript
const session = await mongoose.startSession();

try {
  session.startTransaction();
  
  // All operations in the transaction
  const user = await User.create([{ name: 'Alice' }], { session });
  await Account.create([{ userId: user[0]._id, balance: 0 }], { session });
  await Order.updateOne({ _id: orderId }, { $set: { status: 'paid' } }, { session });
  
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
  throw error;
} finally {
  session.endSession();
}

// With callback
await mongoose.connection.transaction(async (session) => {
  await User.create([{ name: 'Alice' }], { session });
  await Account.create([{ userId: user._id }], { session });
});
```

## Indexing

```typescript
// Single field index
userSchema.index({ email: 1 });

// Compound index
userSchema.index({ role: 1, createdAt: -1 });

// Unique index
userSchema.index({ email: 1 }, { unique: true });

// Partial index
userSchema.index(
  { email: 1 },
  { partialFilterExpression: { isActive: true } }
);

// TTL index (auto-delete after time)
sessionSchema.index({ createdAt: 1 }, { expireAfterSeconds: 3600 });

// Text index for search
postSchema.index({ title: 'text', content: 'text' });

// Geospatial index
locationSchema.index({ coordinates: '2dsphere' });

// Check indexes
const indexes = await User.collection.getIndexes();
```

## Performance Tips

```typescript
// Use lean() for read-only queries
const users = await User.find().lean();

// Select only needed fields
const users = await User.find().select('name email');

// Use cursor for large datasets
const cursor = User.find().cursor();
for await (const user of cursor) {
  // Process one at a time
}

// Bulk operations
const bulkOps = [
  { insertOne: { document: { name: 'User 1' } } },
  { updateOne: { filter: { _id: id1 }, update: { $set: { name: 'Updated' } } } },
  { deleteOne: { filter: { _id: id2 } } },
];
await User.bulkWrite(bulkOps);

// Explain query
const explanation = await User.find({ role: 'admin' }).explain('executionStats');
```

## MongoDB Atlas

```typescript
// Atlas connection string
const uri = 'mongodb+srv://user:password@cluster.mongodb.net/dbname?retryWrites=true&w=majority';

// Atlas Search (full-text search)
const results = await Product.aggregate([
  { $search: {
    index: 'default',
    text: {
      query: 'wireless headphones',
      path: ['name', 'description'],
      fuzzy: { maxEdits: 1 },
    },
  }},
  { $project: {
    name: 1,
    score: { $meta: 'searchScore' },
  }},
]);

// Atlas Vector Search
const results = await Product.aggregate([
  { $vectorSearch: {
    index: 'vector_index',
    path: 'embedding',
    queryVector: [0.1, 0.2, ...],
    numCandidates: 100,
    limit: 10,
  }},
]);
```

## Resources

- **MongoDB Docs**: https://www.mongodb.com/docs/
- **Mongoose Docs**: https://mongoosejs.com/docs/
- **MongoDB University**: https://learn.mongodb.com/
- **Atlas Docs**: https://www.mongodb.com/docs/atlas/
