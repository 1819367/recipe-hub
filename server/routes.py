from app import app

# API routes will go here later
@app.route('/api/test')
def test():
    return {"message": "Flask backend is working!"}