FROM python:3.8 #or lts-alpine or latest-alpine or slim
COPY . /app
WORKDIR /app #the commands will be executed within this directory (like cd command)
RUN pip install -r requirements.txt
CMD python app.py
