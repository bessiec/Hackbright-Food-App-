from flask import Flask, render_template, redirect, g, url_for, request

import model

app = Flask(__name__)

@app.route("/")
def index():

    return render_template('index.html')


@app.route("/get_posts")
def login():   
    model.connect_to_db()
    email = request.args.get('email')
    password = request.args.get('password')  
    title = model.get_all_posts()

    if model.login(email, password):
        return render_template('recent_posts.html', title=title)
    else:
        return redirect("/")


   
    # login = email passwords
    
    # if login == model.login(email, password):
    #     return render_template("recent_posts.html")
    # else:
    #     return render_template("index.html")
    # #if it's in the DB, go to recent posts page
    # else message that says, please create an account
    # insert Javascript popup about needing to create an account
    

if __name__ == "__main__":
    app.run(debug=True)