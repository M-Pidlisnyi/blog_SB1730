from flask import Flask, redirect, render_template, request
import db


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/post/category")
def post_category():
    return render_template("post_category.html", 
                           categories_list=db.getCategories())

@app.route('/post/category/<id>', methods=["GET", "POST"])
def all_posts_in_category(id):

    if request.method == "POST":
        post_text = request.form.get("text")

        if len(post_text) > 0:
            db.addPost(id, post_text)
            return redirect(f'/post/category/{id}')


    return render_template("posts_in_category.html",
                           posts_list=db.getPostsInCategory(id),
                           category_name = db.getCategoryById(id)[0]
                           )

@app.route("/post/view")
def post_view():
    return render_template("post_view.html",
                           posts_list = db.getPosts())

@app.route("/post/delete/<id>")
def delete_post(id):
    db.deletePost(id)
    return redirect("/post/view")


@app.route("/post/view/<id>")
def single_post(id):
    return render_template("single_post.html",
                           post = db.getPost(id))

app.run(debug=True, host="0.0.0.0")
