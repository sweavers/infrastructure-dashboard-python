from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from application import app
import re
import requests
import json
import math

app.config['SECRET_KEY'] = 'somethingsomethingdarkside'

class DashboardCode:
    def convert_json():
        json_file = open('application/static/results.json', encoding='utf-8')
        json_text = json.load(json_file)

        return json_text

    def get_width(root):
        number_of_rows = 0
        width_value = 0

        if root == round(root):
            number_of_rows = root
            width_value = float(100)//number_of_rows
        else:
            number_of_rows = root + 1
            width_value = float(100)//int(root)

        return str(width_value)

    def get_height(root):
        number_of_rows = 0
        height_value = 0

        if root == round(root):
            number_of_rows = root
            height_value = float(90)//number_of_rows
        else:
            number_of_rows = root + 1
            height_value = float(90)//round(number_of_rows)

        return str(height_value)

@app.route('/', methods=['GET'])
def home():
    class_obj = DashboardCode
    json_hash = class_obj.convert_json()

    env = ''
    status = ''
    url = ''
    hash_key = ''
    new_hash = {}

    for idx, item in enumerate(json_hash):
        print(idx)

    item_count = idx + 1

    root = math.sqrt(item_count)

    width_value = class_obj.get_width(root)
    height_value = class_obj.get_height(root)

    return render_template('dashboard_view.html', width_value=width_value, height_value=height_value, json_hash=json_hash)
