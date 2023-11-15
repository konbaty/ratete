from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page web en Python !"

    @app.route('/about')
def about():
    return "À propos de nous"

@app.route('/contact')
def contact():
    return "Contactez-nous"

    if __name__ == '__main__':
    app.run(debug=True)

    python base site web avec python& flask30oct2023.py