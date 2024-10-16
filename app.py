from flask import Flask, render_template, request, redirect, url_for
from models import db, Book, Genre
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def index():
    # Получаем последние 20 записей
    books = Book.query.order_by(Book.created_at.desc()).limit(20).all()
    return render_template('index.html', books=books)

@app.route('/genre/<int:genre_id>')
def genre_view(genre_id):
    # Книги по жанру
    genre = Genre.query.get_or_404(genre_id)
    books = Book.query.filter_by(genre_id=genre_id).all()
    return render_template('genre.html', genre=genre, books=books)


@app.route('/update_is_read', methods=['POST'])
def update_is_read():
    selected_books = request.form.getlist('book_is_read')
    books = Book.query.all()

    for book in books:
        book.is_read = str(book.id) in selected_books

    db.session.commit()
    return redirect(url_for('index'))

@app.route('/read-books')
def read_books():
    books = Book.query.filter_by(is_read=True).all()
    return render_template('read_books.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)