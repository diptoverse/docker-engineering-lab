# Product Catalog API

A small containerized product catalog API built as part of my **Docker Engineering Lab**.

The API is intentionally simple. The focus here is understanding how **Docker, networking, PostgreSQL, Redis, volumes, and CI** work together.

## Stack

- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Docker & Docker Compose
- Pytest
- GitHub Actions

## Architecture

    GitHub
       │
       ▼
    GitHub Actions
       │
       ├── Tests
       ├── Docker Build
       └── Compose Validation
       │
       ▼
    Docker Compose
       │
       ├── FastAPI
       ├── PostgreSQL
       └── Redis
              │
       Docker Network
              │
       PostgreSQL Volume

**Runtime:** FastAPI talks to PostgreSQL and Redis through the Docker network.

**CI:** GitHub Actions runs tests, builds the Docker image, and validates the Compose configuration.

## API

    GET    /products
    GET    /products/{id}
    POST   /products
    PUT    /products/{id}
    DELETE /products/{id}

    GET    /health

## Run

    docker compose up -d

Check the stack:

    docker compose ps

Run tests:

    python -m pytest

## Caching

`GET /products/{id}` checks Redis first.

On a cache miss, the product is fetched from PostgreSQL and then cached in Redis.

Product updates and deletes invalidate the corresponding Redis cache.

## CI

Project 01 has its own GitHub Actions workflow inside the larger `docker-engineering-lab` repository.

It runs automatically when Project 01 changes and can also be triggered manually.

    Push
      ↓
    Tests
      ↓
    Docker Build
      ↓
    Compose Validation
      ↓
    Success

## Focus

The goal wasn't to build a complicated API.

It was to understand the full path:

**Application → Container → Network → Database → Cache → CI**