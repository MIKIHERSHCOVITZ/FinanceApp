from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('../financial_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
            if cursor.fetchone():
                return "Username already exists. Please choose a different username."
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('../financial_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('main.dashboard'))
            return "Invalid username or password. Please try again."
    return render_template('login.html')

@main_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    return render_template('dashboard.html')

@main_bp.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if request.method == 'POST':
        user_id = session['user_id']
        insurance = request.form['insurance']
        pension = request.form['pension']
        bank_balance = request.form['bank_balance']
        loan = request.form['loan']
        credit_card = request.form['credit_card']
        salary = request.form['salary']
        savings = request.form['savings']
        investments = request.form['investments']

        with sqlite3.connect('../financial_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO financial_data (user_id, insurance, pension, bank_balance, loan, credit_card, salary, savings, investments)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, insurance, pension, bank_balance, loan, credit_card, salary, savings, investments))
            conn.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('add_data.html')

@main_bp.route('/view_data')
def view_data():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    user_id = session['user_id']
    with sqlite3.connect('../financial_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, insurance, pension, bank_balance, loan, credit_card, salary, savings, investments FROM financial_data WHERE user_id = ?', (user_id,))
        data = cursor.fetchall()
    return render_template('view_data.html', data=data)

@main_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.index'))
