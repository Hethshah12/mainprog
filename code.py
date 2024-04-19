from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as ms

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace 'username' with your MySQL username
    'password': 'hethshah1',  # Replace 'password' with your MySQL password
    'database': 'student_portal'
}

# Function to establish MySQL connection
def get_db_connection():
    conn = ms.connect(**db_config)
    return conn

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if username and password match in the database
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))  # Fixed the variable name here
        user = cursor.fetchone()

        if user:
            # Login successful
            return redirect(url_for('dashboard'))
        else:
            # Login failed
            return "Invalid username or password"

    return render_template('login.html')

# Dashboard route (protected route)
@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
