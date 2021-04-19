FROM python:3.8

WORKDIR /usr/connector

ADD ./connector/ ./
RUN pip install -r requirements.txt
# ADD ./transport/messages_types_python/ ./
ADD ./transport/topics.py ./transport/topics.py
ADD ./transport/messages_types_python ./transport/messages_types_python

# CMD ["python3", "__main__.py"]
CMD ["python3", "-u", "__main__.py"]