from flask import Flask
from flask_restful import Api
from resources.test_resource import TestResource
import yaml

# Default Values
CONF_FILE_PATH = "conf.yaml"

# Read Configuration from target Configuration File Path
def read_configuration_file():
    global configuration_dict

    with open(CONF_FILE_PATH, 'r') as file:
        configuration_dict = yaml.safe_load(file)

    return configuration_dict

# Read Configuration file
configuration_dict = read_configuration_file()

print("Read Configuration from file ({}): {}".format(CONF_FILE_PATH, configuration_dict))

app = Flask(__name__)
api = Api(app)

print("Starting HTTP RESTful API Server ...")

api.add_resource(TestResource, configuration_dict['rest']['api_prefix'] + '/test',
                 endpoint="TestEndPoint",
                 methods=['GET'])

if __name__ == '__main__':

    app.run(host=configuration_dict['rest']['host'], port=configuration_dict['rest']['port'])  # run our Flask app