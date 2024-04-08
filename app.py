from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_policy', methods=['GET', 'POST'])
def select_policy():
    if request.method == 'POST':
        policy = request.form['policy']
        # Redirect to payment page based on selected policy
        if policy == 'comprehensive':
            return redirect(url_for('make_payment', policy='Comprehensive Insurance'))
        elif policy == 'personal':
            return redirect(url_for('make_payment', policy='Personal Insurance'))
        elif policy == 'accident':
            return redirect(url_for('make_payment', policy='Accident Insurance'))
    return render_template('select_policy.html')

@app.route('/make_payment/<policy>', methods=['GET', 'POST'])
def make_payment(policy):
    if request.method == 'POST':
        # Process payment logic can be added here
        return redirect(url_for('index'))  # Redirect to homepage after payment
    return render_template('make_payment.html', policy=policy)

if __name__ == '__main__':
    app.run(debug=True)
