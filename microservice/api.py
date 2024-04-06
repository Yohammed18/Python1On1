from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'Python Basics', 'author': 'John Doe'},
    {'id': 2, 'title': 'Flask Essentials', 'author': 'Jane Smith'},
     {'id': 3, 'title': 'Data Science 101', 'author': 'Alice Johnson'},
    {'id': 4, 'title': 'Machine Learning Fundamentals', 'author': 'Bob Brown'},
    {'id': 5, 'title': 'Web Development for Beginners', 'author': 'Charlie Davis'}
] 

@app.route("/books", methods=['GET'])
def get_books():
    return jsonify(books), 200, {'Content-Type': 'application/json; charset=utf-8', 'mimetype': 'application/json'}

@app.route("/books/<int:book_id>", methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route("/books", methods=['POST'])
def add_book():
    data = request.get_json()
    books.append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(port=5050)