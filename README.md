# What's this?

This is a sample of FastAPI application with AWS Serverless Architecture.

# Demo API

GET https://serverless-fastapi.keita1992.link/articles

# Local Dev

1. Make `.env` file from `.env.sample`
2. You need to install docker & docker compose

```
docker-compose build
docker-compose up -d
```

# build & deploy

Make `samconfig.yaml` if not exists, from `samconfig.sample.yaml`

```
sam build
sam deploy
```
