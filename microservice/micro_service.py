#  A microservice is a small, independent, and loosely coupled service that performs a specific business function within a larger software application. Microservices architecture breaks down complex applications into smaller, manageable services that can be developed, deployed, and scaled independently, enabling flexibility, agility, and easier maintenance.

# In microservice architectures, applications are built and deployed as simple, highly decoupled, focussed services. They connect to each other over lightweight language agnostic communication mechanisms, which often times means simple HTTP APIs and message queues and are resilient in nature.

# BUILD A MICROSERVICE USING FLASK
# make sure you do a pip install for both flask and flask_restplus
# imported the Flask class
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# use the route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def hello_world():
    """
    This function returns the message we want to display in the user’s browser.
    """
    return "<h1>Hello World</h1>"

# in the terminal use this command to run the application
# flask --app micro_service run
# In the command line locate the url and post it on your preferred web browsers. You should be able to see the Hello World message.
from markupsafe import escape
@app.route('/person/<name>')
def hello_name(name):
    return "<p><em>Hello, {}</em></p>".format(escape(name))


# let use flask to render the html index page. make sure you import the render_template. Flask will look for the templates folder so make sure you store all your html file there
from flask import render_template
@app.route('/index')
def index_page():
    return render_template('index.html')


