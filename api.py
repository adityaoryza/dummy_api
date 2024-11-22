import logging
from flask import Flask, request, jsonify


app = Flask(__name__)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/api', methods=['GET', 'POST'])
def echo():
    """
    Returns the JSON payload of the request, logging the data.
    """
    data = request.get_json()
    logger.info(f"Received data: {data}")
    return jsonify(data)


if __name__ == '__main__':
    port = 5000
    url = f"http://localhost:{port}/api"
    logger.info(f"API is running at: {url}")
    app.run(debug=True, port=port)

