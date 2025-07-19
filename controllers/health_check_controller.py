from json import dumps
from flask import Response
from flask_restx import Namespace, Resource

# Create a namespace
healthcheck_ns = Namespace("health", description="Health check endpoint")

@healthcheck_ns.route("/")
class HealthCheck(Resource):
    def get(self):
        """
        Health check endpoint
        """
        try:
            json_data = dumps({"msg": "Service is healthy, version 1.0.0, deployed on 2025-07-13 23:44:00"})
            return Response(json_data, status=200, mimetype='application/json')
        except Exception as e:
            json_data = dumps({"status_message": str(e)})
            return Response(json_data, status=400, mimetype='application/json')