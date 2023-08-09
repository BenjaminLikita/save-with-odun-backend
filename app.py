import logging
from mysite import create_app
from waitress import serve

app = create_app()


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    logging.basicConfig(level=logging.INFO)
    serve(app, host='0.0.0.0', port=8080)