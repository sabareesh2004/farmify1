
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

# Dummy users
users = {
    'farmer': {'username': 'farmer1', 'password': 'pass123'},
    'consumer': {'username': 'consumer1', 'password': 'pass123'}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/farmer-login', methods=['GET', 'POST'])
def farmer_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['farmer']['username'] and password == users['farmer']['password']:
            session['user'] = username
            return redirect(url_for('farmer_dashboard'))
        else:
            return 'Invalid Credentials for Farmer'
    return render_template('farmer_login.html')

@app.route('/consumer-login', methods=['GET', 'POST'])
def consumer_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['consumer']['username'] and password == users['consumer']['password']:
            session['user'] = username
            return redirect(url_for('consumer_dashboard'))
        else:
            return 'Invalid Credentials for Consumer'
    return render_template('consumer_login.html')

@app.route('/farmer-dashboard')
def farmer_dashboard():
    if 'user' in session:
        return render_template('farmer_dashboard.html', user=session['user'])
    return redirect(url_for('farmer_login'))

@app.route('/consumer-dashboard')
def consumer_dashboard():
    if 'user' in session:
        return render_template('consumer_dashboard.html', user=session['user'])
    return redirect(url_for('consumer_login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
