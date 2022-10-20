from flask import render_template

from saleapp import app, dao


@app.route("/")
def index():
    proucts = dao.load_products()
    return render_template("index.html", proucts = proucts)

if __name__ == '__main__':
    app.run(debug=True, port=5001)