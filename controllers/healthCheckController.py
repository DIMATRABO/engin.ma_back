from flask import Blueprint
from json import dumps
from flask import Response

healthcheck_bp = Blueprint('healthcheck', __name__)

@healthcheck_bp.route('', methods=['GET'])
def healthcheck():
    try:
        json_data = dumps({"msg":"Service is healthy , version 1.0.0 , deployed on 2025-07-13 23:44:00"})
        return Response(json_data , status=200, mimetype='application/json')
    except Exception as e :
        json_data = dumps({"status_message":str(e)})
        return Response(json_data , status=400, mimetype='application/json')
