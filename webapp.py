from flask import Flask, render_template,send_from_directory


Index = """
 <!DOCTYPE html>
<html>
<body>

<p><a href="http://127.0.0.1:5000/pizza">Pizza</a></p>
<br>
<p><a href="http://127.0.0.1:5000/bread">Bread</a></p>

</body>
</html> 


"""




app = Flask(__name__)

@app.route('/')
def index():
    return "Choose: "+Index

@app.route('/pizza')
def index1():
    return render_template('pizzahtml.html')


@app.route('/bread')
def index2():
    return render_template('breadhtml.html')


if __name__ == '__main__':
    app.run(debug=True)