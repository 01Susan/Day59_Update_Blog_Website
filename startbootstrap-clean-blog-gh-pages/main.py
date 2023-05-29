from flask import Flask, render_template
import requests


app = Flask(__name__)

# Requesting the API to get the data of my blogs
posts_data = requests.get("https://api.npoint.io/ccfb92f87aebf1be8e65").json()


@app.route("/")
def home():
    return render_template("index.html", blogs_data=posts_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post_data=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
