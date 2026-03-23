# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# Task 4
# create an instance of Flask
app = Flask(__name__) 

boostrap = Bootstrap5(app)

# Task 2
# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '''Hello world from Flask!<br>
  Andrew R. : AR<br>
  Victoria H. : SYBAU<br>
  Tyler P. : TP
  '''

# Task 3
# in hello_flask.py
@app.route('/AndrewAR')
def t_test():
   return render_template('template.html')

# Task 5
# Github Link:
# 