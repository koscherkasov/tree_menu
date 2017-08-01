virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py create_menu_example
python manage.py runserver


