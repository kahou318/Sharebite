# Sharebite
Restaurant Menu Section API
- Uses Django and sqlite3

Required Installations:
- have python3
- sudo apt install python3-pip
- pip3 install django

Setting Up Database:
- It may be necessary to migrate database changes for the application to work properly
    - python3 manage.py makemigrations restaurant
    - python3 manage.py migrate restaurant

Running the Application:
- Open the project directory (where manage.py is)
- Run application using command:
    - python3 manage.py runserver
- Application is on http://localhost:8000

API:
1) Get a menu section by id
    - GET request: 127.0.0.1:8000/menusection/19
2) Get all menu sections
    - GET request: 127.0.0.1:8000/menusection
3) Add a new menu section
    - POST request to 127.0.0.1:8000/menusection
4) Edit a menu section
    - POST request to i.e: 127.0.0.1:8000/menusection/19
5) Delete a menu section
    - DELETE request to 127.0.0.1:8000/menusection/20