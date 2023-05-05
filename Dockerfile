# FROM python:3.9-bullseye
# WORKDIR /app
# COPY requirements.txt  requirements.txt
# RUN pip3 install -r requirements.txt
# COPY . .
# CMD ["python3" ,"manage.py" ,"runserver","0.0.0.0:8000"]


docker build -t risk-authentication https://github.com/SrikantShubam/RiskBasedAuthentication.git
docker run -p 8000:8000 risk-authentication python manage.py runserver 0.0.0.0:8000
