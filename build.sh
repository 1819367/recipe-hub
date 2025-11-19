#!/bin/bash
cd client
npm install
npm run build
cp -r dist/* ../server/static/
cp dist/index.html ../server/templates/index.html
cd ../server
pip install -r requirements.txt