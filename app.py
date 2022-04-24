from flask import Flask, redirect, render_template, url_for, request
import qrcode

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/sitemap')
def sitemap():
    return redirect("https://aneeshpavan.github.io/QR-Code-Generator/sitemap.xml")

@app.route('/result',methods=['POST', 'GET'])
def result():
        qwerty = request.form.get("link")
        asdf = qrcode.make(qwerty)  
        print(asdf)
        asdf.save("static/qr.jpg")
        return render_template('index.html',asdf = asdf)

if __name__ == "__main__":
    app.run(debug=False)