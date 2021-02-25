FROM python:3.8

WORKDIR /usr/service2

ADD ./service2/requirements.txt ./
RUN pip install -r requirements.txt

ADD ./service2/__main__.py ./
ADD ./service2/transport_client.py ./

# ADD ./service2/ ./

# ADD ./transport/topics.py ./
ADD ./transport/messages_types_python/ ./messages_types_python

# RUN mkdir -p /usr/service2/rest_module
ADD ./transport/rest_module/ ./rest_module

CMD ["python3", "__main__.py"]