#!/bin/bash
# Build the React frontend
cd client
npm install
npm run build

# Make sure Flask folders exist (this fixes the Render error)
mkdir -p ../server/static ../server/templates

# Copy the built React files to Flask
cp -r dist/* ../server/static/
cp dist/index.html ../server/templates/index.html

# Install Python packages
cd ../server
pip install -r requirements.txt
