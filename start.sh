#!/bin/bash
source /home/opc/app/env/bin/activate
export FLASK_APP=/home/opc/app/hello.py
flask run --host=0.0.0.0

