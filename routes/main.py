from flask import Blueprint, render_template, jsonify, request, current_app
import datetime
import json
from models import db
from models.sleep_time import Sleep_time
from models.weight import Weight

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/sleep')
def sleep():
    return render_template('sleep.html')


@main_blueprint.route('/api/sleep-data',methods=['GET'])
def sleep_data():
    results = Sleep_time.query.all()
    print(results)
    data = [
        {
            'id'       : r.id,
            'go_to_bed': r.go_to_bed,
            'wake_up'  : r.wake_up,
            'duration' : round((r.wake_up - r.go_to_bed).total_seconds() / 3600, 1), # hours
            }
        for r in results
        ]
    print(data)
    return jsonify(data)

