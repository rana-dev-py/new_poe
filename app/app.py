from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route and a function to handle it
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run()