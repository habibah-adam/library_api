from models.Page import Page
from schemas.PageSchema import page_schema, pages_schema
from main import db
from flask import Blueprint, json, request, jsonify, abort, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import joinedload


pages = Blueprint('pages', __name__, url_prefix="/pages")

@pages.route("/", methods=["GET"])
def pages_index():
    #pages = Page.query.all()
    query = """
    SELECT p.id, p.page_number, b.id as book_id, b.title, p.page_content
    FROM pages p
    INNER JOIN books b
    ON p.book_id = b.id; 
    """
    pages = db.engine.execute(query)
    # return jsonify(pages_schema.dump(pages))
    return render_template("pages.html", pages=pages)

@pages.route("/numberOfPages", methods=["GET"])
def page_wordcound(id):
    query = """
    SELECT b.title, count(p.page_number) 
    FROM pages p
    INNER JOIN books b
    GROUP BY b.title;
    """
    pages_count = db.engine.execute(query)
    return jsonify(pages_schema.dump(pages))

@pages.route("/", methods=["POST"])
def page_create():
    page_fields = page_schema.load(request.json)

    new_page = Page()
    new_page.page_number = page_fields["page_number"]
    new_page.page_content = page_fields["page_content"]
    new_page.book_id = page_fields["book_id"]

    db.session.add(new_page)
    db.session.commit()

    return jsonify(page_schema.dump(new_page))

@pages.route("/<int:id>", methods=["GET"])
def page_show(id):
    page = Page.query.get(id)
    return jsonify(page_schema.dump(page))

@pages.route("/<int:id>", methods=["PUT", "UPDATE"])
def page_update(id):
    page = Page.query.get(id)
    page_fields = page_schema.load(request.json)
    page.page_content = page_fields['page_content']
    db.session.commit()
    return jsonify(page_schema.dump(page))

@pages.route("/<int:id>", methods=["DELETE"])
def page_delete(id):
    page = Page.query.get(id)   
    db.session.delete(page)
    db.session.commit()
    return jsonify(page_schema.dump(page))
