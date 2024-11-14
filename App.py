from flask import Flask,request,render_template,redirect,url_for,jsonify

app=Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    return "<hi>Welcome to my First Flask App</h1>"
@app.route("/index",methods=["GET"])
def index():
    return "<h2>Welcome to index page</h2>"

# Variable Rule

@app.route("/success/<int:score>")
def success(score):
    return "Passed Score of number is: "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "fail score of number is: "+ str(score)

# HTML Rendering Page

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        physics=float(request.form['physics'])
        chemistry=float(request.form['chemistry'])
        average= (maths+physics+chemistry)/3

        result=''
        if average>=50:
            result='success'
        else:
            result='fail'
        return redirect(url_for(result,score=average))

        #return render_template('form.html',score=average)

# # API Creation
@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val+b_val)


if __name__=='__main__':
    app.run(debug=True)
