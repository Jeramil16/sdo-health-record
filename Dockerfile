
# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy code
COPY ./app ./app
COPY start.sh ./start.sh

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy jinja2 qrcode[pil] passlib[bcrypt] python-multipart aiofiles

# Expose port
EXPOSE 8000

# Start the app
CMD ["bash", "start.sh"]
