@echo off

call cd %~dp0

call py -m venv venv

call venv/Scripts/activate

call pip install -r requirements.txt

call cls

call py main.py
