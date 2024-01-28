# This will import Flask library in flask LAB.
# Here in PWSkills Lab we an make our APIs global and if we are doing it on our own local machine then we couldn't able to implement it.
from flask import Flask

# Taking input from user
from flask import request

# 'app' is the OBJECT of Flask. Here __name__ is Dunder function...
app = Flask(__name__)

# Exposing below Function hello_world() to outer world.
# We will create server and put this on server. 
# My Client is browser for today's class. Tomorrow it can be any programming Language or App. like GooglePay or Blinkit...
# This lab will behave as server for me. 
# This lab will execute this program continuously with multiple functions...


# We are decorate the Custom function with route... 
# Instead of calling function using Function name directly, we call it with help of URL and create route.
# As, function name is Language dependent/ platform dependent and url is independent. URL make it global and depend on HTTP.
# Steps to access URL: 1. Reach out to Server 2. Connect on Port Number (5000) 3. Take route and connect to function.

# Sample API is: https://mango-farmer-ddnmq.pwskills.app:5000/hello3

@app.route("/hello1")
def hello_world1():
    return "Hello, World1!"


@app.route("/hello2")
def hello_world2():
    return "Hello, World2!"

@app.route("/hello3")
def hello_world3():
    return "Hello, World3!"

@app.route("/test_add")
def test():
    data=request.args.get('x')
    a = data
    return "this is my first func in flask to add of 5+6 =  {} & having fun".format(a)


# We can call below as: https://mango-farmer-ddnmq.pwskills.app:5000/input_url?x=data%20Science
@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
