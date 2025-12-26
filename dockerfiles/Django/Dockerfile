FROM python:3.12-alpine

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.7.15 /uv /uvx /bin/

# Install build dependencies for pygraphviz
RUN apk add --no-cache gcc musl-dev graphviz-dev

# Set the working directory
WORKDIR /django_app

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Copy project files
COPY backend/pyproject.toml backend/uv.lock ./
# Install dependencies using uv
RUN uv sync

# Copy project files
COPY backend/ ./
COPY .env ./
COPY backend/entrypoint.sh ./

# Expose the Django port
EXPOSE 8000
 
# Run Django
CMD ["./entrypoint.sh"]
