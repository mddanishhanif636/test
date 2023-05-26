from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def checklist():
    return render_template("index.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/strategy')
def strategy():
    return render_template("strategy.html")


if __name__ == "__main__":
    app.run(debug=True)
