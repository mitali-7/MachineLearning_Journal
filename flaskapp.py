from flask import Flask, render_template, request, redirect, url_for

# creating an instance of the Flask class
app = Flask(__name__)

@app.route("/")
def welc():
    return "Welcome to first flask page built by me"

#to use HTML pages, we need to create a templates folder and place our html files
#there since Jinja2 Template ENgine finds it using that

@app.route("/test", methods = ["GET"])
def test():
    return render_template("index.html")

@app.route("/form", methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'The name entered is {name}'
    else:
        return render_template('form.html')
    

#Variable rule - restricting the datatype of param we are passing to int 
@app.route("/success/<int:score>")
def success(score):
    return "The score you got is " + str(score)

# passing value using score var to a html page using JInja2 template
@app.route("/result/<float:score>")
def result(score):
    res = ""
    if score>=50:
        res = "PASS"
    else:
        res = "FAIL"

    return render_template('result.html', res = res) 

#different ways to present info in jinja2
# {{any text we want to display}}
# {# comment content#}
# {%if-else conditions, for, while loops etc%} {% endif %} 

@app.route("/forif_res/<int:score>")
def forif_res(score):
    if score>=50:
        res = "PASS"
    else:
        res = "FAIL"
    val = {'verdict': res, 'marks':score}
    return render_template('forifres.html', res = val)


# dynamically build the URL and redirect from one page to another api
# use redirect url for
@app.route("/submit_marks", methods = ['POST', 'GET'])
def submit_marks():
    if request.method == 'POST':
        sci = float(request.form['sci'])
        math = float(request.form['math'])
        eng = float(request.form['eng'])

        percent = ((sci + math + eng)/300) * 100
        return redirect(url_for('result', score = percent))
    else:
        return render_template('marks_form.html')

# HTTP METHODS:
# POST - to pass values using HTTP Request, opposite of get
# GET - to retrieve values, uses URL appending, less secure and length is limited 
# PUT - update exisiting data
# DELETE - to delete data


if __name__ == "__main__":
    app.run(debug=True)