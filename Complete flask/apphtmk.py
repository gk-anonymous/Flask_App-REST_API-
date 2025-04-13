from flask import Flask,render_template
#to add html or intregte html template just use render0template

'''it creata an instance of flask class for wsgi'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>hello this is html</h1></html>"

@app.route("/product")
def product():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')





if __name__=="__main__":
    app.run(debug=True)
    