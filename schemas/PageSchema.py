from main import ma
from models.Page import Page
from schemas.BookSchema import BookSchema
from marshmallow.validate import Length

class PageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Page

    page_content = ma.String(required=True, validate=Length(min=1))
    book_id = ma.Integer()
    title = ma.String(validate=Length(min=1))
    #book_id = ma.Nested(BookSchema)
    #title = ma.Nested(BookSchema)
    
page_schema = PageSchema()
pages_schema = PageSchema(many=True)
