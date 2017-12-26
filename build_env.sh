#!/bin/sh

rm -r env
/usr/bin/python3 -m venv env
env/bin/pip install wheel
env/bin/pip install -r requirements.txt