from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Defina seus modelos de banco de dados usando o SQLAlchemy
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

# books = [
#     {
#         'id' : 1,
#         'titulo': 'Papiro',
#         'autor': 'Autor desconhecido 1'
#     },

#     {
#         'id' : 2,
#         'titulo': 'Conhecimento e riqueza',
#         'autor': 'Autor desconhecido 2'
#     }
# ]

@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    for book in books:
        print(book.title, book.author)
    #return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_id_book(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_for_id(id):
    edited_book = request.get_json()
    for idx,book in enumerate(books):
        if book.get('id') == id:
            books[idx].update(edited_book)
            return jsonify(books[idx])

@app.route('/books', methods=['POST'])
def include_new_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for idx, book in enumerate(books):
        if book.get('id') == id:
            del books[idx]

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)