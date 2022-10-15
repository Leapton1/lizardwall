from python
workdir /app
run pip install flask
copy . .
expose 80
cmd ["python","LizardWall.py"]