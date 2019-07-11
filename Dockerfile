FROM python:3.7-alpine
WORKDIR /bday-app
COPY ./bday-app .
RUN pip install --no-cache-dir -r requirements.txt && mkdir ./database
EXPOSE 80
CMD [ "python", "./app.py" ]
