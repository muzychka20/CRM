<img width="1507" alt="Screenshot 2024-11-27 at 00 44 25" src="https://github.com/user-attachments/assets/ba08cf90-b828-4571-8e35-2d208aa79829"># Django CRM Application

## Overview
This is a Customer Relationship Management (CRM) application built using Django. It provides functionalities for user registration, authentication, and management of customer records. The application includes forms for user registration, adding, updating, and deleting customer records.

<img width="1507" alt="Screenshot 2024-11-27 at 00 44 25" src="https://github.com/user-attachments/assets/ac5deed9-2234-4346-a836-eec29c210416">

## Features
- User Authentication (Login, Logout, Register)
- Add, View, Update, and Delete Customer Records
- Bootstrap 5 Integration for a responsive and user-friendly interface

## Prerequisites
Before running this project, ensure you have the following installed:

- Python (3.x)
- Django (4.x or higher)
- Bootstrap 5 (integrated via CDN)

<img width="1507" alt="Screenshot 2024-11-27 at 00 44 12" src="https://github.com/user-attachments/assets/d85afcac-2c41-4404-8e47-f173515b4770">

## File Structure

### Forms
- **`SignUpForm`**: A custom user registration form inheriting from `UserCreationForm`, with added fields for first name, last name, and email.
- **`AddRecordForm`**: A form for adding customer records, linked to the `Record` model.

<img width="1507" alt="Screenshot 2024-11-27 at 00 43 33" src="https://github.com/user-attachments/assets/fbf5b16c-fd89-4b7f-89c0-a1c5645631be">

### Models
- **`Record`**: Represents customer data, with fields for `first_name`, `last_name`, `email`, `phone`, `address`, `city`, `state`, and `zipcode`.

### Views
- **`home`**: Displays all customer records.
- **`login_user`**: Handles user login.
- **`logout_user`**: Logs out the user.
- **`register_user`**: Handles user registration.
- **`customer_record`**: Displays a specific customer record.
- **`add_record`**: Adds a new customer record.
- **`update_record`**: Updates an existing record.
- **`delete_record`**: Deletes a customer record.

### URLs
The `urlpatterns` in `urls.py` maps views to paths:
- `/`: Home page displaying all records.
- `/login/`: Login page.
- `/logout/`: Logout action.
- `/register/`: User registration page.
- `/record/<int:pk>`: View a specific record.
- `/delete_record/<int:pk>`: Delete a specific record.
- `/add_record`: Add a new record.
- `/update_record/<int:pk>`: Update a specific record.

## Bootstrap Integration
The application uses Bootstrap 5 for a clean and responsive design. Bootstrap is included via CDN links in the `base.html` template.

## How to Use
1. Register as a new user or log in with existing credentials.
2. Add customer records through the "Add" button in the navbar.
3. View customer details by clicking on a record.
4. Update or delete records using the respective options on the record detail page.
