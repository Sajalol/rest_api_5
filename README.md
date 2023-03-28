# Django REST API Project 5: Task Manager

This project is a Django REST API that serves as the backend for a task manager application. The frontend is built using React. Users can create, view, update, and delete tasks, as well as view the details of individual tasks.

## Features

- Task management (create, read, update, and delete tasks)
- Task filtering, searching, and sorting
- User management and authentication
- File attachment support
- Custom permissions

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- Django Filters
- Django CORS Headers
- Django Cloudinary Storage

## Installation and Setup

1. Clone the repository
git clone 

2. Change into the project directory
cd your-repo

3. Install the required dependencies
pip install -r requirements.txt

4. Set up the database by updating the `DATABASES` configuration in `settings.py` or by setting the `DATABASE_URL` environment variable.

5. Run migrations
python manage.py migrate


7. Create a superuser account (optional)
python manage.py createsuperuser


## Running the Application

1. Start the development server
python manage.py runserver


2. Access the API in your browser or with a tool like Postman:
- API overview: http://localhost:8000/api/
- Task list: http://localhost:8000/api/task-list/
- Task detail: http://localhost:8000/api/task-detail/<int:pk>/
- Task create: http://localhost:8000/api/task-create/
- Task update: http://localhost:8000/api/task-update/<int:pk>/
- Task delete: http://localhost:8000/api/task-delete/<int:pk>/
- User list: http://localhost:8000/api/users/
- User detail: http://localhost:8000/api/users/<int:pk>/

## Testing


## Deployment

