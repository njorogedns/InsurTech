from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Dummy user data for demonstration
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'}
]

# Square Customers API integration
def create_customer(email, given_name, family_name):
    url = 'https://connect.squareup.com/v2/customers'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'given_name': given_name,
        'family_name': family_name,
        'email_address': email
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['customer']
    else:
        return None

# Square Catalog API integration
def create_catalog_item(name, description, price):
    url = 'https://connect.squareup.com/v2/catalog/object'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Generate a UUID for idempotency_key
    idempotency_key = str(uuid.uuid4())
    
    data = {
        'type': 'ITEM',
        'idempotency_key': idempotency_key,
        'item_data': {
            'name': name,
            'description': description,
            'variations': [{
                'type': 'FIXED_PRICING',
                'price_money': {
                    'amount': price,
                    'currency': 'USD'
                }
            }]
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['catalog_object']
    else:
        return None
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        given_name = request.form['given_name']
        
        # Register the user and call the create_customer function to create a customer in Square
        create_customer(email, given_name, family_name)

        print(f"Registered: Username - {username}, Password - {password}")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username and password match any user in the users list
        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('dashboard'))
        # If no matching user found, redirect back to the login page
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Logic for displaying user dashboard
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
