from flask import Flask, redirect, url_for, render_template, request, session, g, make_response
from models import db  # Import db from models/__init__.py
from models.user import User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from datetime import timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from flask_migrate import Migrate
from models.task import Task
from datetime import datetime
from models.meeting import Meeting

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
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

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
    # Get user's tasks and meetings
    user_tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.due_date).limit(5).all()
    return render_template('dashboard.html', tasks=user_tasks)

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return 'Username already exists'
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/tasks')
@login_required
def tasks():
    user_tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.due_date).all()
    return render_template('tasks.html', tasks=user_tasks)

@app.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        priority = request.form['priority']
        category = request.form['category']
        new_task = Task(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            category=category,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('add_task.html')

@app.route('/meetings')
@login_required
def meetings():
    user_meetings = Meeting.query.filter_by(user_id=current_user.id).order_by(Meeting.date_time).all()
    return render_template('meetings.html', meetings=user_meetings)

@app.route('/add_meeting', methods=['GET', 'POST'])
@login_required
def add_meeting():
    if request.method == 'POST':
        title = request.form['title']
        date_time = datetime.strptime(request.form['date_time'], '%Y-%m-%dT%H:%M')
        location = request.form['location']
        # Check for conflicts
        conflict = Meeting.query.filter_by(user_id=current_user.id, date_time=date_time).first()
        if conflict:
            return 'Time conflict with another meeting.'
        new_meeting = Meeting(
            title=title,
            date_time=date_time,
            location=location,
            user_id=current_user.id
        )
        db.session.add(new_meeting)
        db.session.commit()
        return redirect(url_for('meetings'))
    return render_template('add_meeting.html')

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)

@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/search_tasks', methods=['GET', 'POST'])
@login_required
def search_tasks():
    if request.method == 'POST':
        keyword = request.form['keyword']
        results = Task.query.filter(
            Task.user_id == current_user.id,
            Task.title.contains(keyword)
        ).all()
        return render_template('search_results.html', tasks=results)
    return render_template('search_tasks.html')

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