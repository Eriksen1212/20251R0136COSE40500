# NoSQL Database Overview

## 1. What Is NoSQL?
NoSQL databases provide flexible schemas for unstructured or semi-structured data. They trade some ACID guarantees for scalability and performance.

## 2. Main Types
1. **Key–Value Stores** (e.g., Redis)  
2. **Document Stores** (e.g., MongoDB)  
3. **Column-Family Stores** (e.g., Cassandra)  
4. **Graph Databases** (e.g., Neo4j)  

## 3. When to Use NoSQL
- Rapidly changing schemas  
- Large-scale distributed data  
- High read/write throughput  

## 4. Example: MongoDB Document

```json
// Insert into "products" collection
{
  "name": "Wireless Mouse",
  "price": 25.99,
  "tags": ["electronics", "peripherals"],
  "stock": { "warehouse": 200, "retail": 50 }
}
