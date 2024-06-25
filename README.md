
# Event Management System

This is an Event Management System built with Django, designed to facilitate the organization and management of events within an educational institution. The system allows users to create, view, and manage events, as well as register for events and track event attendance.

## Features

- User Authentication: Users can register, log in, and log out. Different user roles (e.g., students, faculty) are supported.
- Event Creation: Authenticated users can create new events, providing details such as title, date, location, and description.
- Event Management: Event creators can edit and delete events they have created. Administrators have full control over all events.
- Event Registration: Users can register for events, and event organizers can manage event registrations.
- Faculty Integration: Events can be associated with faculty members, allowing for better organization and categorization of events.

## Web Design

View the design template of our project on Figma : https://www.figma.com/community/file/1343331997824447596/eventsease
The styling used in the project has been sourced from bootstrap

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/event-management-system.git
```

2. Navigate to the project directory:

```bash
cd event-management-system
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the application at [http://localhost:8000](http://localhost:8000)

## Usage

1. Create a superuser account:

```bash
python manage.py createsuperuser
```

2. Log in to the admin interface at [http://localhost:8000/admin](http://localhost:8000/admin) to manage users and events.

3. Visit [http://localhost:8000](http://localhost:8000) to access the application and start creating, viewing, and managing events.

## Run Server

1. Activate your virtual environment. The environment used here is eventsease
```bash
your_env_name\scripts\Activate
```
2. Run the server and access the output at port 8000
```bash
python manage.py runserver
```
3. Go to url http://127.0.0.1:8000/loginpage/ to access loginpage and move forward with web view

