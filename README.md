# simple-healthcheck

## Description:

Super simple healthcheck service to hit my HTTP endpoints and notify via Discord webhook URL

## Documentation

### docker-compose example

```yaml
version: "3.7"
services:
  simple-healthcheck:
    image: simple-healthcheck:latest
    container_name: simple-healthcheck
    environment:
      - DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/INT/STRING
      - HEALTHCHECK_INTERVAL_SEC=300
      - HEALTHCHECK_URL=https://my-simple-site.local
      - VERIFY_SSL=false
      - SERVICE_NAME=my-simple-site
    restart: always
```

### Docker Commands:

```bash
# Build image
docker build . --tag simple-healthcheck

# Run image to see logging
docker run simple-healthcheck:latest

# Run via docker-compose
docker-compose up -d simple-healthcheck
```

### Development Workflow:

```bash
# Activate virtualenv
source venv/bin/activate

# Run Script w/o Docker using VSCode
source env.sh
```