from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/campaign')
def campaign():
    return render_template("campaign.html")

@app.route('/halloffame')
def halloffame():
        return render_template("halloffame.html")

@app.route('/training')
def trialling():
        return render_template("training.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)