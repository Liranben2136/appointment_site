from flask import Flask, render_template, request

app = Flask(__SharoNail__)

# קישור לתשלום בביט
BIT_PAYMENT_LINK = "https://pay.bitpay.co.il/YOUR_BIT_PAYMENT_LINK"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        return render_template("confirmation.html", name=name, date=date, time=time, payment_link=BIT_PAYMENT_LINK)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
