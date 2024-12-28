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

MongoDB Atlas itself is a cloud service and cannot be directly run in Docker. However, we can use a self-hosted MongoDB instance in Docker to mimic the behavior of MongoDB Atlas for the following reasons:

1. Local Development and Testing

We want to test your application locally without connecting to the internet or incurring cloud costs.
We want to mimic the behavior of MongoDB Atlas by running a Dockerized MongoDB instance.

2. Containerized Environments

The development or deployment workflow relies heavily on Docker and you want MongoDB to run as part of a containerized stack.

3. Offline or Air-Gapped Scenarios

We are working in an environment where an internet connection is unavailable or restricted (e.g., secure networks, air-gapped systems).
Example Use Case
We are developing an application that reads data from MongoDB and writes it to DuckDB, and we want a fully containerized setup for local testing.