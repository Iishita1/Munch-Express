from flask import Flask, render_template , redirect , url_for

app = Flask(__name__)

#ROUTING
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/taj')
def taj():
    return render_template('TajPalace.html')

@app.route('/punjab')
def punjab():
    return render_template('PunjabGrill.html')

@app.route('/dosa')
def dosa():
    return render_template('DosaPlaza.html')

@app.route('/biryani')
def biryani():
    return render_template('BiryaniHouse.html')

@app.route('/sarwana')
def sarwana():
    return render_template('SarwanaBhawan.html')

@app.route('/mughal')
def mughal():
    return render_template('MughalsKitchen.html')

#run app
if __name__ == '__main__':
    app.run(debug=True)
