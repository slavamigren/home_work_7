python3 -m venv ven
source env/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
deactivate