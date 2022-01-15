#Install the package
pip install FLask-Migrate

# Main commands with Flask-Migrate

# Set up env
# MacOS/Linux
export FLASK_APP=myapp.py

# Set up the migration directory
flask db init

# Set up the migration file
flask db migrate -m "Some message"

# Updates the db with migration
flask db upgrade