from flask import Flask
from controller import home_bp  
from flask import render_template

app = Flask(__name__)
app.register_blueprint(home_bp)

@app.route('/')
def index():
    return render_template('index.html', total_products=100, total_orders=50, low_stock=10)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
