FROM python:3.8

WORKDIR /usr/connector

ADD ./connector/requirements.txt ./
RUN pip install -r requirements.txt
ADD ./connector/ ./
ADD ./transport/topics.py ./
ADD ./transport/messages_types_python/ ./

CMD ["python3", "__main__.py"]