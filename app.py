from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail, Message
from email_validator import validate_email, EmailNotValidError
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Flask-Mail
mail = Mail(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Route to redirect unauthorized users

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)  # Email verification status
    verification_token = db.Column(db.String(100), nullable=True)  # Token for email verification

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Generate verification token
def generate_verification_token():
    return secrets.token_urlsafe(32)

# Send verification email
def send_verification_email(user):
    token = user.verification_token
    verification_link = url_for('verify_email', token=token, _external=True)
    msg = Message('Verify Your Email', recipients=[user.email])
    msg.body = f'Please click the following link to verify your email: {verification_link}'
    mail.send(msg)

# Routes
@app.route('/')
def index():
    return render_template('index.html', user=current_user)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        email = request.form.get('loginEmail')
        password = request.form.get('loginPassword')
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            if user.is_verified:
                login_user(user)
                flash('Successfully logged in!', 'success')  
                return redirect(url_for('index'))
            else:
                flash('Please verify your email before logging in.', 'error')
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form.get('signupName')
        email = request.form.get('signupEmail')
        password = request.form.get('signupPassword')

        # Validate email format
        try:
            valid = validate_email(email)
            email = valid.email  # Normalize the email address
        except EmailNotValidError as e:
            flash('Invalid email address', 'error')
            return render_template('login.html')

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered', 'error')
        else:
            # Generate verification token
            verification_token = generate_verification_token()

            # Create new user
            new_user = User(
                name=name,
                email=email,
                password=password,
                verification_token=verification_token,
                is_verified=False
            )
            db.session.add(new_user)
            db.session.commit()

            # Send verification email
            send_verification_email(new_user)

            flash('Account created successfully! Please check your email to verify your account.', 'success')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/verify_email/<token>')
def verify_email(token):
    user = User.query.filter_by(verification_token=token).first()

    if user:
        user.is_verified = True
        user.verification_token = None  # Clear the token after verification
        db.session.commit()
        flash('Your email has been verified! You can now log in.', 'success')
    else:
        flash('Invalid or expired verification link.', 'error')

    return redirect(url_for('login'))

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    logout_user()
    session.pop('_flashes', None)  # Clears old flash messages
    flash('Logged out successfully!', 'info')
    return redirect(url_for('login'))

@app.route('/cart/')
@login_required
def cart():
    return render_template('cart.html', user=current_user)

@app.route('/payment/')
@login_required
def payment():
    return render_template('payment.html', user=current_user)

# Restaurant pages
@app.route('/one')
def BH():
    return render_template('BiryaniHouse.html', user=current_user)

@app.route('/two')
def DP():
    return render_template('DosaPlaza.html', user=current_user)

@app.route('/three')
def MK():
    return render_template('MughalsKitchen.html', user=current_user)

@app.route('/four')
def PG():
    return render_template('PunjabGrill.html', user=current_user)

@app.route('/five')
def TP():
    return render_template('TajPalace.html', user=current_user)

@app.route('/six')
def SB():
    return render_template('SarwanaBhawan.html', user=current_user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)