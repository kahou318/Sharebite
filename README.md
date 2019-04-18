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
