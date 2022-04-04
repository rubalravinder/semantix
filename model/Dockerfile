#Create a ubuntu base image with python 3 installed.
FROM python:3.9.12-slim-buster

#Set the working directory
WORKDIR /

#copy all the files
COPY model_leger.bin ./model_leger.bin
COPY app.py ./app.py
COPY requirements.txt ./requirements.txt

#Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

#Run the command
# RUN python3 model.py

ENV FLASK_APP app.py

CMD ["flask","run"]