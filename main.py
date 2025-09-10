from comunidadeimpressionadora import app
from comunidadeimpressionadora import database

with app.app_context():
    database.create_all()


if __name__ == '__main__':
    app.run(debug=True)

