from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db, bcrypt
from app.models import User, ParkingSlot
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    slots = ParkingSlot.query.all()
    return render_template('index.html', slots=slots)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.dashboard'))
        
        flash('Login unsuccessful. Check email and password', 'danger')
    
    return render_template('login.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@main.route('/create_slots', methods=['GET', 'POST'])
@login_required
def create_slots():
    if request.method == 'POST':
        slot_number = request.form.get('slot_number')
        slot = ParkingSlot(slot_number=slot_number)
        db.session.add(slot)
        db.session.commit()
        
        flash('Parking slot created!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('create_slots.html')

@main.route('/toggle_slot/<int:slot_id>')
@login_required
def toggle_slot(slot_id):
    slot = ParkingSlot.query.get(slot_id)
    if slot.is_occupied:
        slot.is_occupied = False
        slot.occupied_by = None
        slot.time_occupied = None
    else:
        slot.is_occupied = True
        slot.occupied_by = current_user.id
        slot.time_occupied = datetime.utcnow()
    
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
