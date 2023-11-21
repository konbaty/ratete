from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/357magnum')
def products():
    return render_template('357magnum.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/ak 47')
def payment():
    return render_template('ak 47.html')
    
@app.route('/fusil a pompe')
def index():
    return render_template('fusil a pompe.html')
    
    
    
    
    
    
    
    
    

@app.route('/process_payment', methods=['POST'])
def process_payment():
    if request.method == 'POST':
        # Récupération des données du formulaire
        card_number = request.form['card_number']
        expiration = request.form['expiration']
        cvv = request.form['cvv']
        name = request.form['name']
        
        # Logique pour traiter le paiement
        # Ici, vous pouvez intégrer la logique de traitement du paiement
        # Par exemple, une intégration à une passerelle de paiement
        
        return "Paiement effectué avec succès!"
    else:
        return "Méthode non autorisée."


if __name__ == '__main__':
    app.run(debug=True)
