from flask import Blueprint, render_template, jsonify, request, current_app
import datetime
import json
from models import db
from models.sleep_time import Sleep_time
from models.weight import Weight

iphone_blueprint = Blueprint('iphone', __name__)

@iphone_blueprint.route('/api/go-to-bed',methods=['POST'])
def go_to_bed():
    print(datetime.datetime.now(), 'going to bed')
    current_app.config['go_to_bed_time'] = datetime.datetime.now()
    return '', 204 # return No Content status

@iphone_blueprint.route('/api/wake-up',methods=['POST'])
def wake_up():
    print(datetime.datetime.now(), 'waking up')
    new_sleep_time = Sleep_time(go_to_bed=current_app.config['go_to_bed_time'], wake_up=datetime.datetime.now())
    print(new_sleep_time)
    db.session.add(new_sleep_time)
    db.session.commit()
    return '', 204 # return No Content status

@iphone_blueprint.route('/api/record-weight',methods=['POST'])
def record_weight():
    data = json.loads(request.data.decode('utf-8'))
    new_weight_entry = Weight(weight=int(data['weight']))
    db.session.add(new_weight_entry)
    db.session.commit()
    return '', 204 # return No Content status

