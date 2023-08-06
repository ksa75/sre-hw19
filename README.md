python3 -m venv .venv  
source .venv/bin/activate  
python3 -m pip install -U flask  flask_sqlalchemy gunicorn prometheus-flask-exporter  coverage
cd flask-sqlite3-todo-crud/  
flask --app app --debug run -p 81 -h 0.0.0.0  


