Flask Library API Documentation
This is a simple Flask application that serves as a RESTful API for managing a library of books. The application uses SQLite as its database and SQLAlchemy as the Object-Relational Mapping (ORM) tool.

Getting Started
Prerequisites
Before running the application, ensure that you have the following installed:

Python 3.x
Flask
Flask-SQLAlchemy
Install the required dependencies using the following command:

bash
Copy code
pip install Flask Flask-SQLAlchemy
Running the Application
Clone the repository and navigate to the project directory:

bash
Copy code
git clone <repository_url>
cd <project_directory>
Run the Flask application:

bash
Copy code
python app.py
The application will be accessible at http://127.0.0.1:5000/ in your web browser.

API Endpoints
1. Home Page
URL: /
Method: GET
Description: Displays the home page.
2. Get All Books or Add a New Book
URL: /api/books
Methods: GET, POST
Description:
GET: Retrieves a list of all books in the library.
POST: Adds a new book to the library.
Request Payload (POST):
json
Copy code
{
  "book_name": "Book Title",
  "author_name": "Author Name"
}
Response (GET):
json
Copy code
[
  {
    "book_id": 1,
    "book_name": "Book Title",
    "author_name": "Author Name"
  },
  ...
]
Response (POST):
json
Copy code
{
  "book_id": 1
}
3. Update a Book
URL: /api/books/<int:id>
Method: PUT
Description: Updates the details of a specific book.
Request Payload:
json
Copy code
{
  "book_name": "New Book Title",
  "author_name": "New Author Name"
}
Response:
plaintext
Copy code
Book Updated!
Database
The application uses SQLite as its database, and the database file is named database.db. The Library table schema includes the following columns:

book_id (Primary Key, Integer): Unique identifier for each book.
book_name (String, Not Null): The title of the book.
author_name (String, Not Null): The name of the author.
Running Tests
To run the tests for this application, use the following command:

bash
Copy code
python test_app.py
Contributing
Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push to the branch.
Submit a pull request for review.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask: https://flask.palletsprojects.com/
SQLAlchemy: https://www.sqlalchemy.org/
