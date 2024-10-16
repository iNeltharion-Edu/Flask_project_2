from models import db, Book, Genre
from app import app

popular_books = [
    {'title': 'Гарри Поттер и философский камень', 'author': 'Джоан Роулинг', 'genre': 'Фэнтези'},
    {'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин', 'genre': 'Фэнтези'},
    {'title': 'Убить пересмешника', 'author': 'Харпер Ли', 'genre': 'Художественная литература'},
    {'title': '1984', 'author': 'Джордж Оруэлл', 'genre': 'Антиутопия'},
    {'title': 'Великий Гэтсби', 'author': 'Фрэнсис Скотт Фицджеральд', 'genre': 'Классика'},
    {'title': 'Гордость и предубеждение', 'author': 'Джейн Остин', 'genre': 'Классика'},
    {'title': 'Над пропастью во ржи', 'author': 'Джером Дэвид Сэлинджер', 'genre': 'Классика'},
    {'title': 'Хоббит', 'author': 'Джон Р. Р. Толкин', 'genre': 'Фэнтези'},
    {'title': '451 градус по Фаренгейту', 'author': 'Рэй Брэдбери', 'genre': 'Антиутопия'},
    {'title': 'Моби Дик', 'author': 'Герман Мелвилл', 'genre': 'Классика'},
    {'title': 'Код да Винчи', 'author': 'Дэн Браун', 'genre': 'Триллер'},
    {'title': 'Алхимик', 'author': 'Пауло Коэльо', 'genre': 'Приключения'},
    {'title': 'Голодные игры', 'author': 'Сьюзен Коллинз', 'genre': 'Антиутопия'},
    {'title': 'О дивный новый мир', 'author': 'Олдос Хаксли', 'genre': 'Антиутопия'},
    {'title': 'Хроники Нарнии', 'author': 'Клайв Стейплз Льюис', 'genre': 'Фэнтези'},
    {'title': 'Сияние', 'author': 'Стивен Кинг', 'genre': 'Ужасы'},
    {'title': 'Дракула', 'author': 'Брэм Стокер', 'genre': 'Ужасы'},
    {'title': 'Война и мир', 'author': 'Лев Толстой', 'genre': 'Классика'},
    {'title': 'Анна Каренина', 'author': 'Лев Толстой', 'genre': 'Классика'},
    {'title': 'Преступление и наказание', 'author': 'Фёдор Достоевский', 'genre': 'Классика'}
]

with app.app_context():
    db.create_all()

    genres_dict = {}
    for book in popular_books:
        genre_name = book['genre']
        if genre_name not in genres_dict:
            genre = Genre.query.filter_by(name=genre_name).first()
            if not genre:
                genre = Genre(name=genre_name)
                db.session.add(genre)
                db.session.commit()
            genres_dict[genre_name] = genre

    for book in popular_books:
        title = book['title']
        author = book['author']
        genre_name = book['genre']
        genre = genres_dict[genre_name]

        existing_book = Book.query.filter_by(title=title, author=author).first()
        if not existing_book:
            new_book = Book(title=title, author=author, genre_id=genre.id)
            db.session.add(new_book)

    db.session.commit()

print("Данные успешно добавлены!")
