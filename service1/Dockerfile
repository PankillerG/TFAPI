FROM python:3.8

WORKDIR /usr/service1

ADD ./service1/requirements.txt ./
RUN pip install -r requirements.txt
ADD ./service1/ ./
ADD ./transport/topics.py ./
ADD ./transport/messages_types_python/ ./

CMD ["python3", "__main__.py"]