from flask import Flask, render_template, request
from utils import sumer, producter, averager

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Gilbert"


@app.route('/sum', methods=['GET', 'POST'])
def sum(total=12):
    if request.form:
        x, y = request.form.values()
        total = sumer(x, y)
    return render_template('sum.html', total=total)


@app.route('/product', methods=['GET', 'POST'])
def product(pdt=None):
    if request.form:
        x, y = request.form.values()
        pdt = producter(x, y)
    return render_template('product.html', pdt=pdt)


@app.route('/average', methods=['GET', 'POST'])
def average(avg=None):
    if request.form:
        x, y = request.form.values()
        avg = averager(x, y)
    return render_template('average.html', avg=avg)


# to start the server, run: python app.py
if __name__ == '__main__':
    app.run(debug=True)