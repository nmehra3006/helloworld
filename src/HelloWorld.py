from flask import Flask, request
from appData.app_data_controller import *
from appLogger.app_logger import *
from flask import json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
# app.logger.disabled = True
# logging.getLogger('werkzeug').disabled = True


class HelloWorld:

    _logger = None
    _data_controller = None

    def __init__(self):
        self._app_logger = AppLogger.getInstance()
        self._data_controller = AppDataController.getInstance()

    def get_request_handler(self, request):

        req_dict = request.__dict__
        url = req_dict['environ']['werkzeug.request']

        if req_dict['environ']['HTTP_ACCEPT'] == 'application/json':
            raw_response = {"message": "Hello, World"}

        else:
            raw_response = """<p>Hello, World</p>"""

        self._app_logger.writeDebugLog(str(url))

        response = self._response_formatting_helper(raw_response)
        return response

    def post_request_handler(self, request):
        req_dict = request.__dict__
        url = req_dict['environ']['werkzeug.request']

        # fieldnames = ['timestamp', 'method', 'url']
        # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writerow({'timestamp': str(datetime.now(tz=None)), 'method': "POST", 'url': str(url)})

        raw_response = ""
        self._data_controller.write()

        return self._response_formatting_helper(raw_response)

    def _response_formatting_helper(self, raw_response):
        # generate resp body + status
        return raw_response


my_hello_world = HelloWorld()
@app.route('/', methods=['GET', 'POST'])
def hello_world_entry():

    if request.method == 'GET':
        response = my_hello_world.get_request_handler(request)

    if request.method == 'POST':
        response = my_hello_world.post_request_handler(request)

    return response

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)





