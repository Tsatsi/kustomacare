from app import app
import json


@app.route('/', methods=['GET'])
def get_customer_list():
    return json.dumps([{"name": "vodacom", "description": "communication company"},
                       {"name": "Econet", "description": "communication company"}])
