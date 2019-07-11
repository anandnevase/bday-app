FROM python:3.7-alpine
WORKDIR /bday-app
COPY ./app.py .
COPY ./database .
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD [ "python", "./app.py" ]
