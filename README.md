# AuthApp

python version - 3.8.10
django version - 3.2.5


## Setup
  - Setup virtual environment
  ```sh
  virtualenv -p python3.8 venv
  ```

   ```sh
  source venv/bin/activate
  ```

  - start application
    ```sh
  pip install -r requirements.txt
  ```
  - migrate db
    ```sh
    python manage.py migrate
    ```
  - run application

    ```sh
    python manage.py runserver
    ```

# How it works
Swagger documentation of the apis will be available at

http://localhost:8000/api/v1/swagger/

1. Register 

endpoint ```user``` method ```POST``` to register user

2. Authentication

endpoint ```api/token``` to login with credentials 
user can enter username/email field in the username field

3. Authorization

click Authorize button on the top of ui or lock icon to enter the Authorization token in the header

format ```Bearer jwttoken```

Only authorized user can list the users in the database and perform operations on the user

You can access all the other apis after authorization














