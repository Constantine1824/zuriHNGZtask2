# ZuriHNGZ task2 Documentation

This is provides the sample body, responses and status codes for different endpoint of the API

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Constantine1824/ZuriHNGZTask2.git
   cd ZuriHNGZTask2
   ```

2. Install dependencies and spawn virtual environment with poetry:

   ```shell
   poetry install
   poetry shell 
   ```


3. Migrate the database:

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```


4. Start the development server:

   ```shell
   python manage.py runserver
   ```

The API should now be running locally at `http://127.0.0.1:8000/`.

## API Endpoints

### Create a New Object

- **Endpoint:** `/api`
- **Method:** POST
- **Request Body:**

  ```json
  {
      "name": "John",
  }
  ```
- **Sample Response:**

    ```json
    {
        "id" :"1",
        "name" : "John"
    }
    ```
- **Status Code:** 201

### Retrieve all objects

- **Endpoint:** `/api`
- **Method:** GET
- **Sample Response:**

    ```json
    [
        {
            "id" : 1,
            "name" : "John"
        },
        {
            "id" : 2,
            "name": "Joe"
        }
    ]
    ```
- **Status Code:** 200


### Retrieve an object

- **Endpoint:** `/api/<int:id>`
- **Method:** GET
- **Sample Response:**

    ```json
        {
            "id" : 1,
            "name" : "John"
        }
    ```
- **Status Code:** 200


### Update an Object by ID

- **Endpoint:** `/api/<int:id>`
- **Method:** PUT
- **Request Body:**

  ```json
  {
      "name": "new_name",
  }
  ```
- **Sample Response:**

    ```json
    {
        "id" : 1,
        "name" : "new_name"
    }
    ```
- **Status Code:** 201


### Delete an Object by ID

- **Endpoint:** `/api/<int:id>`
- **Method:** DELETE
- **Sample Response:**

    ```json
    {
        "details" : "deleted successfully"
    }
    ```
- **Status Code:** 200
