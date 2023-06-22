# **Notestore API**

This is a Django API for managing notes and user registration.

## Getting Started

To get started with the Notestore API, follow these steps:

1. Clone the repository:
<<<<<<< HEAD

`git clone https://github.com/nydtab001/notestore.git`

2. Install the dependencies:

`pip install -r requirements.txt`

3. Apply the database migrations:

`python manage.py migrate`

4. Generate a new secret key and update `notestore/settings.py`:
- Open a Python shell:
  ```python
  python manage.py shell
  ```

- Generate a new secret key:
  ```python
  >>> from django.core.management.utils import get_random_secret_key
  >>> get_random_secret_key()
  ```

- Copy the generated secret key and replace the value of `SECRET_KEY` in `notestore/settings.py` with the new key.

5. Run the development server:

`python manage.py runserver`


## API Endpoints

- Note List/Create
- **GET** `/notes/` - Retrieve a list of notes.
- **POST** `/notes/` - Create a new note.

- Note Get/Update/Delete
- **GET** `/notes/<note-id>/` - Retrieve a specific note.
- **PUT** `/notes/<note-id>/` - Update a specific note.
- **DELETE** `/notes/<note-id>/` - Delete a specific note.

- User Registration
- **POST** `/register/` - Register a new user.

- User List
- **GET** `/users/` - Retrieve a list of users.

- User Get/Update/Delete
- **GET** `/users/<user-id>/` - Retrieve a specific user.
- **PUT** `/users/<user-id>/` - Update a specific user.
- **DELETE** `/users/<user-id>/` - Delete a specific user.

## Contributing

Contributions are welcome! If you'd like to contribute to the Notestore API, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Commit your changes and push them to your forked repository.
6. Submit a pull request.
=======
>>>>>>> origin/master
