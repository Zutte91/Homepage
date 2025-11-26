from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/services/it-consulting')
def it_consulting():
    return render_template('services/it_consulting.html')

@app.route('/services/training')
def training():
    return render_template('services/training.html')

@app.route('/services/trading')
def trading():
    return render_template('services/trading.html')

@app.route('/services/network')
def network():
    return render_template('services/network.html')

@app.route('/services/homelab')
def homelab():
    return render_template('services/homelab.html')

@app.route('/services/software-development')
def software_development():
    return render_template('services/software_development.html')

if __name__ == '__main__':
    app.run(debug=True)


