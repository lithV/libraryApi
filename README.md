openapi: 3.0.3
info:
  title: Library API - OpenAPI 3.0
  description: |-
    This is a simple library API written by Adarsh Singh.

tags:
  - name: books
    description: Everything about your Pets
    externalDocs:
      description: Find out more
      url: http://swagger.io

paths:
  /api/books:
    put:
      tags:
        - books
      summary: Update an existing pet
      description: Update an existing pet by Id
      operationId: updatePet
      requestBody:
        description: Update an existent pet in the store
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Book'
        required: true
      responses:
        '200':
          description: Successful operation
        '400':
          description: Author name of Book Name Empty
        '404':
          description: Book Not Found
    post:
      tags:
        - books
      summary: Add a new book to the library
      description: Add a new pet to the store
      requestBody:
        description: Create a new pet in the store
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Book'
        required: true
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Book_Created'
        '400':
          description: Invalid input

components:
  schemas:
    Book:
      type: object
      properties:
        book_name:
          type: string
          format: ascii
          example: "Percy Jackson"
        author_name:
          type: string
          format: ascii
          example: "Robert Frost"
    Book_Created:
      type: object
      properties:
        book_id:
          type: integer
          format: int64
          example: 2
          
