import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Database connection setup
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='anan5@06',
            database='systems'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/redirect_to_main_page')
def redirect_to_main_page():
    return redirect(url_for('main_page'))

@app.route('/main-page')
def main_page():
    return render_template('main-page.html')

@app.route('/account_creation', methods=['GET', 'POST'])
def account_creation():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO account (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password)
            )
            connection.commit()
            cursor.close()
            connection.close()
        return redirect(url_for('customer_details'))
    return render_template('account_creation.html')

@app.route('/customer_details', methods=['GET', 'POST'])
def customer_details():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        age = request.form.get('age')
        gender = request.form.get('gender')
        license_no = request.form.get('license_no')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')

        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO cust (name, address, age, gender, license_no, email, password, phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (name, address, age, gender, license_no, email, password, phone)
            )
            connection.commit()
            cursor.close()
            connection.close()
        return redirect(url_for('rental_form'))
    return render_template('customer_details.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM account WHERE name = %s AND password = %s", (name, password))
            user = cursor.fetchone()
            cursor.close()
            connection.close()

            if user:
                print("User authenticated successfully:", user)
                return redirect(url_for('customer_details'))
            else:
                return "Invalid credentials", 400
    return render_template('signin.html')

@app.route('/rental_form', methods=['GET', 'POST'])
def rental_form():
    if request.method == 'POST':
        vehicle_type = request.form.get('vehicle_type')
        with_driver = request.form.get('with_driver')
        
        # Convert hours to integer
        hours = request.form.get('hours', type=int)  # Use 'type=int' to automatically convert
        if hours is None:
            hours = 0  # Default value if conversion fails
        
        total_price = hours * 200
        if with_driver == 'yes':
            total_price += hours * 80

        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO rent (vehicle_type, with_driver, hours, total_price) VALUES (%s, %s, %s, %s)",
                (vehicle_type, with_driver, hours, total_price)  # Replace with actual customer ID if necessary
            )
            connection.commit()
            cursor.close()
            connection.close()

        return redirect(url_for('confirmation_page', vehicle_type=vehicle_type, with_driver=with_driver, hours=hours, total_price=total_price))
    return render_template('rental_form.html')

@app.route('/terms-condition', methods=['GET', 'POST'])
def terms_condition():
    if request.method == 'POST':
        if request.form.get('agree'):
            return redirect(url_for('signin'))
        else:
            return "You must agree to the terms to proceed.", 400
    return render_template('terms-condition.html')

@app.route('/confirmation_page')
def confirmation_page():
    vehicle_type = request.args.get('vehicle_type')
    with_driver = request.args.get('with_driver')
    hours = request.args.get('hours', type=int)  # Ensure hours is converted to int
    total_price = request.args.get('total_price', type=float)  # Ensure total_price is converted to float

    print(f"Vehicle Type: {vehicle_type}, With Driver: {with_driver}, Hours: {hours}, Total Price: {total_price}")
    return render_template('confirmation_page.html', vehicle_type=vehicle_type, with_driver=with_driver, hours=hours, total_price=total_price)


if __name__ == '__main__':
    app.run(debug=True)