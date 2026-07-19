# Project 03 — FastAPI Compose Stack

## Overview

A production-style FastAPI backend running with Docker Compose.

This project builds a User Management REST API using FastAPI, PostgreSQL, Redis, and modern backend tools.

## Tech Stack

- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Alembic
- Docker
- Docker Compose
- GitHub Actions

## Goal

Build a complete backend application with:

- REST API
- Database integration
- CRUD operations
- Containerized development environment
- CI automation

## Final Architecture

```text
Client
  |
FastAPI
  |
+-------------+
|             |
PostgreSQL   Redis

Docker Compose
```

## Project Structure

```text
project-03-fastapi-compose-stack/

├── app/                  # Application code
├── tests/                # Tests
├── scripts/              # Helper scripts
├── docs/                 # Documentation
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Status

🚧 In Development

## Module 1 - FastAPI Fundamentals

Built a production-style FastAPI application structure.

Learned:

- FastAPI application lifecycle
- Uvicorn ASGI server
- Routing with APIRouter
- Pydantic validation
- Service layer architecture
- Dependency Injection

Architecture:

Client
 ↓
FastAPI Router
 ↓
Service Layer
 ↓
Database (future)

Dependency Injection applied