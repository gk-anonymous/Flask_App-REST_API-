from flask import Flask


'''it creata an instance of flask class for wsgi'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to page griou f"

@app.route("/product")
def product():
    return "This is product page r"





if __name__=="__main__":
    app.run(debug=True)
    