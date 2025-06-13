# Relational Database Overview

## 1. What Is a Relational Database?
A Relational Database stores data in tables (rows & columns) and uses SQL for querying. Key principles:
- **Schema:** Defines tables, columns, data types.  
- **ACID Properties:** Atomicity, Consistency, Isolation, Durability.  
- **Keys & Constraints:** Primary keys, foreign keys, unique constraints.

## 2. Common SQL Operations
- **CREATE** — Define tables  
- **INSERT** — Add rows  
- **SELECT** — Query data  
- **UPDATE** — Modify existing rows  
- **DELETE** — Remove rows  

## 3. Example: Simple Table & Query

```sql
-- Create table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);

-- Insert data
INSERT INTO users (name, email)
VALUES ('Alice', 'alice@example.com');

-- Query data
SELECT id, name FROM users WHERE email LIKE '%@example.com';
