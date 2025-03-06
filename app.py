from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('start.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/learn')
def learn():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
