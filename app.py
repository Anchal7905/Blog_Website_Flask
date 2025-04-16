from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# --- Database Setup ---
DB_NAME = "posts.db"

def init_db():
    if not os.path.exists(DB_NAME):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            """)
            conn.commit()

# --- Routes ---

@app.route('/')
def home():
    with sqlite3.connect(DB_NAME) as conn:
        posts = conn.execute("SELECT * FROM posts").fetchall()
    return render_template("home.html", posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    with sqlite3.connect(DB_NAME) as conn:
        post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    if post:
        return render_template("post.html", post=post)
    return "Post not found", 404

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
        return redirect(url_for('home'))
    return render_template("create.html")

# --- Run App ---
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
