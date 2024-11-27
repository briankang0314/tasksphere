from flask import Flask, redirect, url_for, render_template, request, session, g
from models import db  # Import db from models/__init__.py
from models.user import User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from datetime import timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Name of the login view

# Set session timeout to 15 minutes
app.permanent_session_lifetime = timedelta(minutes=15)

# User loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Ensure session is permanent for timeout
@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Authenticate user
        user = User.get_by_username(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Protected route example
@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.username}! Welcome to your dashboard.'

def get_db():
    if 'db' not in g:
        g.db = db
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.session.close()

def init_db():
    db.create_all()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Create a test user if one doesn't exist
        if not User.query.filter_by(username='testuser').first():
            hashed_password = generate_password_hash('testpassword')
            new_user = User(username='testuser', password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            print('Test user created: testuser / testpassword')
    app.run(debug=True)