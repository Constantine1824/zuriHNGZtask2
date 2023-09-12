```markdown
# ZuriHNGZtask2

This is a simple REST API project that demonstrates basic CRUD operations with django rest framework

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