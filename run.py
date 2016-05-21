from app import app
"""
This script starts up the development web server for this application
"""

app.run(debug=True)

# port = int(os.environ.get('PORT', 5000)) 
# app.run(host='0.0.0.0', port=port)