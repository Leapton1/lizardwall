from python
workdir /app
run pip install flask
copy . .
expose 8080
cmd ["python","LizardWall.py"]