from flask import Flask, render_template
import db


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/post/category")
def post_category():
    return render_template("post_category.html", 
                           categories_list=db.getCategories())

@app.route("/post/view")
def post_view():
    return render_template("post_view.html",
                           posts_list = db.getPosts())

@app.route("/about")
def about():
    return render_template("base.html")


app.run(debug=True, host="0.0.0.0")
