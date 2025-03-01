from flask_restful import Resource


class TestResource(Resource):

    def __init__(self, **kwargs):
        # Initialize a default response
        self.default_response = {"location_id": "test", "location_name": "test", "latitude": 0.0, "longitude": 0.0}

    def get(self):
        # Return the default response and 200 OK code
        return self.default_response, 200  # return data and 200 OK code