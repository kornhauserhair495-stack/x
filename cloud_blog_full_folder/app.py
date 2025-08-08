import os
from flask import Flask, render_template, request, redirect, url_for
import cloudinary
import cloudinary.uploader
from datetime import datetime

app = Flask(__name__)

# Cloudinary 配置（Render 上通过环境变量设置）
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# 内存中保存帖子
posts = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        file_url = None
        file_type = None

        if "file" in request.files:
            upload_file = request.files["file"]
            if upload_file.filename:
                ext = upload_file.filename.split(".")[-1].lower()
                allowed = ["jpg", "jpeg", "png", "gif", "pdf", "zip"]
                if ext not in allowed:
                    return "文件类型不允许", 400
                if request.content_length and request.content_length > 20 * 1024 * 1024:
                    return "文件太大", 400
                upload_result = cloudinary.uploader.upload(upload_file, resource_type="auto")
                file_url = upload_result.get("secure_url")
                file_type = ext

        posts.insert(0, {
            "title": title,
            "content": content,
            "file_url": file_url,
            "file_type": file_type,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "comments": []
        })
        return redirect(url_for("index"))

    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    if post_id >= len(posts):
        return "帖子不存在", 404

    post = posts[post_id]

    if request.method == "POST":
        name = request.form.get("name") or "匿名"
        comment = request.form.get("comment")
        if comment.strip():
            post["comments"].append({
                "name": name,
                "comment": comment,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        return redirect(url_for("post", post_id=post_id))

    return render_template("post.html", post=post, post_id=post_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
