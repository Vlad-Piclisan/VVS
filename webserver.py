from flask import Flask, render_template, request
import sys
import re


maintenanceMode = False


app = Flask(__name__, static_folder='static')




@app.before_request
def before_request_func():
    if request.endpoint != 'maintenance' and maintenanceMode == True and not re.search("\.(png|svg|jpg|gif|css)\?$",request.full_path):
        return render_template('maintenance.html'), 503


@app.route('/maintenance')
def maintenance():
    global maintenanceMode
    maintenanceMode = not maintenanceMode
    return "maintenance", 503



@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/pizza')
def pizza():
    return render_template('pizzahtml.html')


@app.route('/bread')
def bread():
    return render_template('breadhtml.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == "__main__":

    try:
        if sys.argv[1]!="":
            app.run(port=sys.argv[1])
        else:
            app.run(port=8080)
    except:
        app.run(port=8080)


