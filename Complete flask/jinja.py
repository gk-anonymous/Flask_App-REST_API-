 ### building  URL Dynamically
 ### variable rule
 ### Jinja2 Template Engine
 
''' {{}} expression to print output in html'''
'''{%...%} conditions for loops'''
'''{#...#} this is for comment''' 

from flask import Flask,render_template


'''it creata an instance of flask class for wsgi'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to page griou f"

@app.route("/product")
def product():
    return "This is product page r"

#variable rule
@app.route("/success/<int:score>")
def success(score):
    return " the marks you got is " + str(score)


#Building URL Dynamically
@app.route("/new/<int:score>")
def new(score):
    res="" 
    if score >=50:
        res="PASS"
    else:
        res="FAIL"
    

    exp = {'score':score,"res":res}
    return render_template('result1.html',results=exp)





if __name__=="__main__":
    app.run(debug=True)
    