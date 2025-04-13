# Flask_App-REST_API-

# **Flask Web Framework - Beginner's Guide**  
*A lightweight Python web framework for building web applications.*  

![Flask Logo](https://flask.palletsprojects.com/en/3.0.x/_images/flask-logo.png)  

## **Table of Contents**  
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Basic Flask App](#basic-flask-app)  
6. [Running the App](#running-the-app)  
7. [Routing](#routing)  
8. [Templates (Jinja2)](#templates-jinja2)  
9. [Static Files](#static-files)  
10. [Handling Forms](#handling-forms)  
11. [Database Integration (SQLite)](#database-integration-sqlite)  
12. [Deployment (Heroku)](#deployment-heroku)  
13. [Common Commands](#common-commands)  
14. [Resources](#resources)  

---

## **Introduction**  
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries, making it easy to get started for beginners while remaining powerful enough for complex applications.  

---

## **Features**  
✅ Lightweight and modular  
✅ Built-in development server  
✅ Jinja2 templating engine  
✅ RESTful request dispatching  
✅ Secure cookies (client-side sessions)  
✅ Easy database integration (SQLAlchemy, Flask-SQLAlchemy)  
✅ Extensible with Flask extensions  

---

## **Prerequisites**  
- Python 3.6+  
- Basic Python knowledge  
- `pip` (Python package manager)  

---

## **Installation**  
Install Flask using `pip`:  

```bash
pip install flask
```

Verify installation:  

```bash
python -c "import flask; print(flask.__version__)"
```

---

## **Basic Flask App**  
Create a file `app.py`:  

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## **Running the App**  
```bash
python app.py
```
- Open `http://127.0.0.1:5000` in your browser.  
- `debug=True` enables auto-reloading on code changes.  

---

## **Routing**  
Define URL routes:  

```python
@app.route('/about')
def about():
    return "About Page"

@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"
```

---

## **Templates (Jinja2)**  
Flask uses **Jinja2** for templating.  

1. Create a `templates` folder.  
2. Add `index.html`:  

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

3. Render it in Flask:  

```python
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('index.html', name=name)
```

---

## **Static Files**  
Store CSS, JS, and images in a `static` folder.  

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

## **Handling Forms**  
Install `flask-wtf` (optional):  

```bash
pip install flask-wtf
```

Example form handling:  

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Logged in as {username}"
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="password" name="password">
            <button type="submit">Login</button>
        </form>
    '''
```

---

## **Database Integration (SQLite)**  
Use **Flask-SQLAlchemy**:  

```bash
pip install flask-sqlalchemy
```

Example:  

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

# Create database
with app.app_context():
    db.create_all()
```

---

## **Deployment (Heroku)**  
1. Install `gunicorn`:  
   ```bash
   pip install gunicorn
   ```
2. Create `Procfile`:  
   ```plaintext
   web: gunicorn app:app
   ```
3. Deploy to Heroku:  
   ```bash
   heroku create
   git push heroku master
   ```

---

## **Common Commands**  
| Command | Description |  
|---------|-------------|  
| `flask run` | Run the Flask dev server |  
| `flask shell` | Open interactive Python shell |  
| `flask db init` | Initialize Flask-Migrate (if used) |  

---

## **Resources**  
📖 [Official Flask Documentation](https://flask.palletsprojects.com/)  
🎥 [Flask Mega-Tutorial (Miguel Grinberg)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)  
💡 [Flask Extensions](https://flask.palletsprojects.com/en/3.0.x/extensions/)  

---

### **License**  
This project is open-source under the **MIT License**.  

---

🚀 **Happy Coding!** Let me know if you need any modifications! 🚀
