# MongoDB Atlas and DuckDB

## What is MongoDB?

MongoDB Atlas is a cloud-based database service provided by MongoDB that allows developers to deploy, manage, and scale MongoDB databases with ease. It offers a fully managed, globally distributed database solution, eliminating the need for managing servers or manual configurations.

MongoDB Atlas uses document storage, a type of NoSQL database that organizes data in a flexible, schema-less format. Instead of tables and rows (like in traditional relational databases), MongoDB stores data in documents represented in JSON-like structures called BSON (Binary JSON). This makes it ideal for handling unstructured or semi-structured data.

## Install MongoDB

### For Mac

```
brew tap mongodb/brew

brew install mongodb-community@8.0

brew services start mongodb-community@8.0
```

### For Windows using WSL Ubuntu

```

-- Import the MongoDB GPG Key

curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor

-- Add the MongoDB Repository

echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

```

Replace focal with the appropriate codename for your Ubuntu version:
focal: Ubuntu 20.04
jammy: Ubuntu 22.04

```
-- Update the Package List

sudo apt update


--Install MongoDB

sudo apt install -y mongodb-org

-- Start MongoDB

sudo systemctl start mongod

-- Enable MongoDB to start on boot

sudo systemctl enable mongod

-- Check the MongoDB status

sudo systemctl status mongod

```

