FROM python:3.6.8-slim
WORKDIR /app

#ADD HelloWorld.py /app
#COPY ./helloworld /app/
COPY . /app/

#ADD requirements.txt /app 

RUN pip3 --trusted-host pypi.python.org install --no-cache-dir --upgrade pip setuptools

RUN pip3 --no-cache-dir install -r requirements.txt 

ENV PYTHONPATH /app 

EXPOSE 5000

CMD  python /app/helloworld/HelloWorld.py
