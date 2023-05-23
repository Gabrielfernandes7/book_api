from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id' : 1,
        'titulo': 'Papiro',
        'autor': 'Autor desconhecido 1'
    },

    {
        'id' : 2,
        'titulo': 'Conhecimento e riqueza',
        'autor': 'Autor desconhecido 2'
    }
]

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

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

app.run(port=5000, host='localhost', debug=True)