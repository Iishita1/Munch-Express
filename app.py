from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'mini'  # Required for session management

# Database configuration (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# ROUTING
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
        else:
            email = request.form.get('email')
            password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.password == password:  # Note: In production, use proper password hashing
            session['user_id'] = user.id
            session['user_name'] = user.name
            
            # Return user data as JSON
            return jsonify({
                'success': True,
                'user_id': user.id,
                'name': user.name,
                'email': user.email,
                'message': 'Successfully logged in!'
            })
        else:
            if not user:
                return jsonify({
                    'success': False,
                    'error': 'email_not_found',
                    'message': 'No account found with this email'
                }), 401
            else:
                return jsonify({
                    'success': False,
                    'error': 'invalid_password',
                    'message': 'Incorrect password'
                }), 401
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Basic validation
        if not name or not email or not password:
            flash('All fields are required', 'error')
            return redirect(url_for('login'))
            
        if len(password) < 8:
            flash('Password must be at least 8 characters', 'error')
            return redirect(url_for('login'))
            
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('An account with this email already exists', 'error')
            return redirect(url_for('login'))
            
        try:
            new_user = User(name=name, email=email, password=password)  # Note: In production, hash the password
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again.', 'error')
            return redirect(url_for('login'))
            
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

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

# Run app
if __name__ == '__main__':
    app.run(debug=True)