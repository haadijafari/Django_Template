#!/bin/sh

echo "Making migrations..."
uv run manage.py makemigrations

echo "Applying migrations..."
uv run manage.py migrate

# echo "Collecting static files..."
# uv run core/manage.py collectstatic --noinput

echo "Starting server..."
uv run manage.py runserver 0.0.0.0:8000
