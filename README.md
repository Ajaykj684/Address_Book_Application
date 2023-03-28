# My FastAPI Project

This is a FastAPI project for demonstrating basic CRUD (Create, Read, Update, Delete) operations using a simple Address book application.

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/Ajaykj684/Address_Book_Application.git`
2. Change into the project directory: `cd Address_Book_Application`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or Linux: `source venv/bin/activate`
5. Install the project dependencies: `pip install -r requirements.txt`
6. Start the server: `uvicorn app.main:app --reload`

## Usage

To use the API, visit `http://localhost:8000/docs` in your web browser to view the Swagger UI documentation. From there, you can create, read, update, and delete todo items.


