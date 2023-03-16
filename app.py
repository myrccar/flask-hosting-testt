from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello():
    with open("number.txt","r") as f:
        number = int(f.read())
    return render_template("index.html",number=number)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        with open("number.txt","w") as f:
            f.write(request.form['number'])
    return redirect(url_for("hello"))




if __name__ == '__main__':
    app.run(debug=True)