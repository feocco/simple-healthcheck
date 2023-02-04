# simple-healthcheck


## Docker Commands:

```bash
# Build image
docker build . --tag simple-healthcheck

# Run image to see logging
docker run simple-healthcheck:latest

# Run via docker-compose
docker-compose up -d simple-healthcheck
```

## Development Workflow:

```bash
# Python testing
cd /home/ec2-user/mealie-service/scripts/simple-healthcheck

# Activate virtualenv
source venv/bin/activate

# Run Script w/o Docker using VSCode

# Test Script
./quickTest.py

# If updating libraries, don't forget to
pip freeze > requirements.txt
```