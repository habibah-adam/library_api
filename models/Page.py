from main import db

class Page(db.Model):
    __tablename__ = "pages"
    
    id = db.Column(db.Integer, primary_key=True)
    page_number = db.Column(db.Integer)
    page_content = db.Column(db.String())
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)

    def __repr__(self):
        return f"<Page {self.page_number}>"
