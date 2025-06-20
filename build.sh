#!/bin/bash

# Build script for Railway deployment
echo "🔧 Starting build process..."

# Create staticfiles directory
mkdir -p /app/staticfiles

# Set environment for production
export ENVIRONMENT=production

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Build completed successfully!" 