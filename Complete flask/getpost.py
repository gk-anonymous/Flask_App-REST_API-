from flask import Flask,request,render_template


'''it creata an instance of flask class for wsgi'''
app = Flask(__name__)

@app.route("/index",methods=['GET'])
def welcome():
    return "welcome to page griou f"

@app.route("/product")
def product():
    return "This is product page r"

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f"HELLO {name}"
        
    return render_template('form.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f"HELLO {name}"
        
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)
    