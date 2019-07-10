FROM python:3.7-alpine
WORKDIR /bday-app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./app.py" ]
