from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def get_index():
    return render_template("index.html")

@index_bp.route("/about")
def about():
    return render_template("vistas/about.html")

@index_bp.route("/blog")
def blog():
    return render_template("vistas/blog.html")

@index_bp.route("/blog/post")
def blog_single():
    return render_template("vistas/blog-single.html")

@index_bp.route("/contact")
def contact():
    return render_template("vistas/contact.html")

@index_bp.route("/project")
def project_single():
    return render_template("vistas/project-single.html")

@index_bp.route("/services")
def services():
    return render_template("vistas/services.html")

@index_bp.route("/testimonials")
def testimonials():
    return render_template("vistas/testimonials.html")
