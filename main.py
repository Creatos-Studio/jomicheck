from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def login():
    return render_template('pages/login.html')

@app.route('/register')
def register():
    return render_template('pages/register.html')

@app.route('/jomi-passes')
def all_pass():
    return render_template('pages/all_pass.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

if __name__ == "__main__":
    app.run(debug=True)
