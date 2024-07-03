# Mess-Management-System

# Prerequisites
Before you begin, ensure you have the following installed:

1. Python (3.x)
2. pip (Python package manager)
3. Git

# Installation
1. Clone the repository
   
First, clone the repository to your local machine using Git:

2. Create a virtual environment
Create and activate a virtual environment to manage dependencies:


On Windows:
python -m venv venv
venv\Scripts\activate

On macOS and Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
Install the required packages using pip:

pip install -r requirements.txt

4. Set up the database
Run the following commands to set up the database:

python manage.py makemigrations
python manage.py migrate

5. Create a superuser
Create a superuser to access the Django admin panel:

python manage.py createsuperuser

Follow the prompts to set up the superuser account.

6. Run the development server
Start the development server:

python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.
