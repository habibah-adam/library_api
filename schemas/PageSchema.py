from main import ma
from models.Page import Page
from marshmallow.validate import Length

class PageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Page

    page_content = ma.String(required=True, validate=Length(min=1))
    
page_schema = PageSchema()
page_schemas = PageSchema(many=True)