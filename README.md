# Flask Library API

This is a simple Flask application that serves as a RESTful API for managing a library of books. The application uses SQLite as its database and SQLAlchemy.

# Documentation

## GET /api/books

Returns a list of 'Book' objects in a JSON.

## POST /api/books

Create a new Book. Expects a Book object in the request body. Returns status 200 if all inputs validated with a JSON containing ID of the book added. 400 otherwise.

## PUT /api/books/<book_id>

Update an existing book. Expects a Book object in the request body. 200 if successful, 400 otherwise.

# List of Schemas

## Book Object

```json
{
  "book_name": "Name of Book",
  "author_name": "Name of Author"
}
```
## List of Books
```json
[
    {
        "author_name": "Robert Frost",
        "book_id": 1,
        "book_name": "Percy Jackson"
    },
    {
        "author_name": "JK Rowling",
        "book_id": 2,
        "book_name": "Harry Potter"
    },
    {
        "author_name": "JK Rowling",
        "book_id": 3,
        "book_name": "Harry Potter and the Prisoner of Azkaban"
    },
    {
        "author_name": "Adarsh Singh",
        "book_id": 4,
        "book_name": "Battle Havens"
    }
]
```

## Book ID Object

```json
{
  "book_id": "Book ID"
}
```
