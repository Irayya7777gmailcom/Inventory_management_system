Django-based inventory management system

Technology Stack
Backend: Django (Python)
Database: PostgreSQL
Caching: Redis
Authentication: JWT-based authentication (simple_jwt)

Installation Instructions

Packages mentioned in the `requirements.txt` file need to be installed.

pip install -r requirements.txt

To install Redis on Windows, it is generally recommended to use Windows Subsystem for Linux (WSL) because Redis is primarily developed for Unix-like systems and doesn't have an official Windows version. 
link `https://learn.microsoft.com/en-us/windows/wsl/install`

Django Settings

Add the Packages: Add the packages you mentioned under INSTALLED_APPS. 

INSTALLED_APPS = [
    
    #other apps....
    `rest_framework`,
    `rest_framework_simplejwt`,
    `rest_framework_simplejwt.token_blacklist`,
    `debug_toolbar`,
    # Other apps...
]

Find MIDDLEWARE: Look for the MIDDLEWARE list in the settings.py file. 
MIDDLEWARE = [
    `django.middleware.security.SecurityMiddleware`,
    # other middle wares...
]

API Endpoints

Method	Endpoint	Description
GET	   items/	Get a list of all items
POST	items/	Add a new item
GET	   items/<id>/	Get details of a specific item
PUT	   items/<id>/	Update an item
DELETE items/<id>/	Delete an item

POST   'jwt/token/', TO GENERATE ACCESS TOKEN AND REFRESH TOKEN
POST   'jwt/token/refresh/', USINF REFRESH TOKEN GENERATE ACCESS TOKEN

Add the following line to your project's URL patterns to enable the Debug Toolbar:
path('__debug__/', include('debug_toolbar.urls')),  in project urls patterns to view debugtoolbar 

Log File

The `debug.log` file is used for monitoring and reviewing application logs.


Tests

The `tests.py` file contains test cases to verify the functionality of all CRUD (Create, Read, Update, Delete) endpoints in the application.


