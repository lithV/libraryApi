from flask import Flask, render_template, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy()
db.init_app(app)

class Library(db.Model):
    __tablename__ = "library"
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, nullable=False)
    author_name = db.Column(db.String, nullable=False)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
   
@app.route('/')
def home_page():
    return 'Home Page'

@app.route('/api/books', methods=['GET', 'POST'])
def add_book():
    if(request.method == 'GET'):
        return jsonify([book.as_dict() for book in Library.query.all()])
    else:
        book_data = request.json
        if 'book_name' not in book_data:
            abort(400)
        if 'author_name' not in book_data:
            abort(400)
        
        book_already = Library.query.filter_by(book_name=book_data['book_name']).first()
        if(book_already != None):
            if(book_already.author_name == book_data['author_name']):
                return 'Book already exists!', 400
        
        book = Library(book_name=book_data['book_name'], author_name=book_data['author_name'])
        db.session.add(book)
        db.session.commit()
        return jsonify({'book_id': book.book_id }), 200

@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Library.query.get(id)
    if(book is None):
        abort(404)
    book_data = request.json
    if 'author_name' in book_data:
        if book_data['author_name'] != '':
            book.author_name = book_data['author_name']
        else:
            abort(400)
    if 'book_name' in book_data:
        if book_data['book_name'] != '':
            book.book_name = book_data['book_name']
        else:
            abort(400)
    db.session.commit()
    return 'Book Updated!', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)