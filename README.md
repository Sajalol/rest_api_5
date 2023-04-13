# Django REST API for React Task Manager

The Task Manager is a comprehensive web application that helps users manage their tasks with ease and efficiency. Designed with a Django REST API backend and a React frontend, this application streamlines task organization and management by providing a user-friendly interface and a variety of features to enhance productivity. Ideal for individuals, teams, or organizations, the Task Manager allows users to create, update, and delete tasks, while also offering advanced features such as task filtering, searching, sorting, and file attachment support. With a focus on user management and authentication, the application ensures a secure and personalized experience for each user. This repository provides all the necessary information and resources to set up and deploy the Task Manager application.

<br>

## Table of Contents

1.  [Features](#features)
2.  [Installation](#installation)
3.  [Configuration](#configuration)
4.  [Running the Application](#running-the-application)
5.  [API Endpoints](#api-endpoints)
6.  [Technologies Used](#technologies-used)
7.  [Usernames](#usernames)
8.  [Deployment](#deployment)
9.  [Frontend](#frontend-installation)
10. [Credits](#credits)

<br>

## Features

- Task management (create, read, update, and delete tasks)
- Task filtering, searching, and sorting
- User management and authentication
- File attachment support
- Custom permissions

<br>

## API Functionality

The Django REST API for React Task Manager provides the following key features:

1. **Task Management**: Users can create, read, update, and delete tasks through the API endpoints. Tasks can also be filtered, searched, and sorted according to different criteria.

   Example: To create a new task, make a POST request to `/todo/task-create/` with the required task data in the request body.

2. **User Management and Authentication**: The API handles user registration, authentication, and management. It provides endpoints for user registration, login, and user detail retrieval.

   Example: To register a new user, follow the instructions provided by Django's built-in authentication views for user registration. Typically, this involves submitting a registration form, which creates a new user in the database. Or create a new user through `/admin` 

3. **File Attachment Support**: Users can attach files to tasks, which are stored using Cloudinary. The API provides endpoints for uploading and managing these files.

   Example: To attach a file to a task, include the file in the request body when making a POST or PUT request to the appropriate task-related endpoint.

4. **Custom Permissions**: The API implements custom permissions to ensure that users can only access and modify their own tasks and account details.

   Example: A user without admin permissions cannot access or modify another user's tasks or account details.

5. **Pagination**: The API supports pagination for task lists to improve performance and user experience when dealing with large sets of tasks.

   Example: When requesting a list of tasks at `/todo/task-list/`, the response will be paginated. To navigate through pages, use the `page` query parameter in the request URL (e.g., `/todo/task-list/?page=2`).

6. **Admin Interface**: The Django REST API provides an admin interface for managing tasks, users, and other application data. Administrators can access the admin panel to create, update, and delete tasks, as well as manage users and their permissions.

   Example: To access the admin interface, navigate to `/admin` and log in with an admin account. Once logged in, you can manage tasks, users, and other application data.


<br>

## Installation

1. Clone the repository:

git clone https://github.com/Sajalol/rest_api_5.git
cd to the top folder

2. Install the required packages:

pip install -r requirements.txt


<br>

## Configuration

Create a .env file in the root of the project with the following variables:

- import os
- os.environ['CLOUDINARY_URL'] = "Cloudinary URL*"
- os.environ.setdefault("DATABASE_URL", "postgres:"Postgres url" ")
- os.environ['DEV'] = '1'
- os.environ.setdefault("SECRET_KEY", "Secret key")

Replace your-secret-key, your-database-url, and your-cloudinary-url with the appropriate values for your project.


<br>

## Running the Application

1. Apply the migrations:

python manage.py migrate

2. Start the development server:

python manage.py runserver

The API should now be accessible at http://127.0.0.1:8000/.


<br>

## API Endpoints

- /todo/ - API Overview
- /todo/task-list/ - List all tasks
- /todo/task-detail/<int:pk>/ - Get task details
- /todo/task-update/<int:pk>/ - Update a task
- /todo/task-create/ - Create a new task
- /todo/task-delete/<int:pk>/ - Delete a task
- /todo/users/ - List all users
- /todo/user-detail/<int:pk>/ - Get user details
- /admin - Admin login page
- /api-auth/login/ - user login (admin will also work here)


<br>

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- Cloudinary


<br>

## Testing

1. Test user authentication and permissions:
   - Verify that only authenticated users can access protected endpoints.
   - Test different user roles to ensure they have the appropriate permissions.

2. Test task management:
   - Test creating tasks, updating tasks, and deleting tasks.
   - Test task filtering, searching, and sorting.
   - Test file attachment functionality.
   - Test pagination for task lists.

3. Test user management:
   - Test user detail pages for correct information.
   - Test creating new users and updating existing users.
   - Test user login functionality.

4. Test error handling:
   - Test how the application handles incorrect input or missing data.
   - Test error messages and status codes.


<br>

## Testing endpoints
- Testing creating tasks from /todo/task-create/ working as intended, and they showing up /todo/task-list/.
- Testing task updates works as intended in /todo/task-update/<int:pk>/, and checking they getting updated in /todo/task-list/
- Testing task-details page works as intended per tasks
- Testing that tasks actually gets deleted when using /todo/task-delete/<int:pk>/
- Testing all tasks showing up in /todo/task-list/
- Checking and testing user-detail for /todo/user-detail/<int:pk>/ showing correct info
- When creating new users, checking they showing up in /todo/users lists
- Testing login in /api-auth/login/ works as intended

<br>


## Usernames

- User 1:  Username: User1   / Password: Project5Test
- User 2:  Username: User2   / Password: Project5Test
- User 3:  Username: User3   / Password: Project5Test

<br>

## Deployment

## Backend Deployment

1. Create a new Heroku app and provision a PostgreSQL add-on.
2. Configure your Django app for Heroku by adding a `Procfile`, `requirements.txt`, and add data in the config vars settings. 
* Add all these in the config vars keys / values in Heroku:
    - ALLOWED_HOSTS / ** Backend app url ** 
    - CLIENT_ORIGIN / ** Frontend app url **
    - CLIENT_ORIGIN_DEV / ** Fronend app local url **
    - CLOUDINARY_URL / ** CLOUDINARY URL **
    - DATABASE_URL / ** DATABASE URL **
    - DISABLED_COLLECTSTATIC / 1
    - HEROKU_POSTGRESQL_JADE_URL / ** Postgres url **
    - SECRET_KEY / ** Secret key **
      * Requirement.txt file should look something like this:
         - asgiref==3.6.0
         - backports.zoneinfo;python_version<"3.9"
         - cloudinary==1.30.0
         - dj-database-url==0.5.0
         - dj-rest-auth==2.2.6
         - Django==4.1.5
         - django-allauth==0.50.0
         - django-cloudinary-storage==0.3.0
         - django-cors-headers==3.13.0
         - django-crispy-forms==1.14.0
         - django-filter==22.1
         - djangorestframework==3.14.0
         - djangorestframework-simplejwt==5.2.2
         - gunicorn==20.1.0
         - oauthlib==3.2.2
         - Pillow==9.4.0
         - psycopg2==2.9.5
         - PyJWT==2.6.0
         - python3-openid==3.2.0
         - pytz==2022.7
         - requests-oauthlib==1.3.1
         - sqlparse==0.4.3
         - whitenoise==6.3.0
3. Commit your changes and push the project to a new GitHub repository.
4. Connect your Heroku app to your GitHub repository and enable automatic deploys.
5. Deploy your app by triggering a manual deploy.


<br>

## Additional Deployment Notes

- Make sure to set the environment variables for both the backend and frontend deployments, such as the `SECRET_KEY`, `API_URL`, and any other necessary variables.
- Remember to run `collectstatic` for the Django app to serve static files in production.
- Configure CORS settings in the Django backend to allow requests from the React frontend.


<br>

## Frontend Installation

1. Before installing the frontend, remember to follow the instructions in the [Installation](#installation) and [Configuration](#configuration) sections above for the backend.

2. Once the backend server is running, proceed to set up the frontend by following the instructions in the [frontend repository](https://github.com/Sajalol/project-5-react-latest).



<br>

## Credits

- Code Institute for training.
- Various articles and YouTubers for ideas.
- Code Institute Slack and Tutoring assistance.