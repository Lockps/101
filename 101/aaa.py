from flask import Flask,render_template 

app=Flask(__name__)

    
@app.route('/')
def mainnl():
    return render_template("firstpage.html")

@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/admin')
def root():
    return render_template("admin.html")
   
@app.route('/user/<name>/<age>')
def member(name, age):
    return render_template('member.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login_member():
    return render_template('login.html')

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/test')
def tester():
    return render_template('test.html')

@app.route('/test2')
def tester2():
    return render_template('test2.html')

if __name__ == "__main__":
    app.run(debug=True)