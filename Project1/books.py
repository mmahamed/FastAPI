from fastapi import FastAPI, Body


app = FastAPI()

BOOKS = [
    {'Title': 'Title1', 'Author': 'Author1', 'category': 'Science'},
    {'Title': 'Title2', 'Author': 'Author2', 'category': 'Science'},
    {'Title': 'Title3', 'Author': 'Author3', 'category': 'History'},
    {'Title': 'Title4', 'Author': 'Author4', 'category': 'Math'},
    {'Title': 'Title5', 'Author': 'Author5', 'category': 'Math'},
    {'Title': 'Title6', 'Author': 'Author2', 'category': 'Math'},
]

# Async is not mandatory

@app.get("/books")
async def get_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def get_books(book_title: str):
    for book in BOOKS:
        if book.get('Title').casefold() == book_title.casefold():
            return book
    return {"Message": "Book not found"}
    # List comprehension version
    # matching_books = [
    #     book for book in BOOKS
    #     if book['Author'] == dynamic_parameter or book['category'] == dynamic_parameter
    # ]
    # return matching_books


@app.get('/books/')
async def get_books_by_category(category: str):
    return [book for book in BOOKS if book.get('category').casefold() == category.casefold()]

# assignment / ORDER MATTERS - smaller apis must be on top


@app.get('/books/author/')
async def get_books_by_author_query(author_name: str):
    return [book for book in BOOKS if book.get('author').casefold() == author_name.casefold()]


@app.get('/books/{author_name}/')
async def get_books_by_author_category(author_name: str, category: str):
    return [book for book in BOOKS if book.get('author').casefold() == author_name.casefold() and book.get('category').casefold() == category.casefold()]


@app.post('/books')  # or /books/create_book
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put('/books')  # or /books/update_book
async def update_book(edited_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == edited_book.get('title').casefold():
            BOOKS[i] = edited_book


@app.delete('/books/{book_title}')  # or /books/delete_book/{book_title}
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

# assignment


@app.get('/books/author/{author_name}')
async def get_books_by_author_path(author_name: str):
    return [book for book in BOOKS if book.get('author').casefold() == author_name.casefold()]
