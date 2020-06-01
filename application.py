from flask import Flask, render_template, request

app = Flask(__name__)

def estdiv(x, y, z):
        div = (x // y) * z//100
        return (div)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/service", methods=['GET', 'POST'])
def service():
    estimation = 0
    if request.method == "GET":
        return render_template('service.html', estimation=estimation)
    else:
        kwh = int(request.form.get('bill'))
        cov = int(request.form.get('cover'))
        panelMonth = (0.2*5*30)
        price = 0.15
        estimation = estdiv(kwh, panelMonth, cov)
        return render_template('service.html', estimation=estimation, panelMonth=panelMonth, price=price)

@app.route('/contact')
def contact():
    return render_template('contact.html')