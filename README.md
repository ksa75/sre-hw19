python3 json_exporter.py 1234 http://api.open-notify.org/iss-now.json  


python3 -m venv .venv  
source .venv/bin/activate  
python3 -m pip install -U flask  flask_sqlalchemy  
cd flask-sqlite3-todo-crud/  
flask --app app --debug run -p 81 -h 0.0.0.0  

pip install prometheus-flask-exporter  

https://pypi.org/project/prometheus-flask-exporter/
