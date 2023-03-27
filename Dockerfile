FROM python:3.10-slim
WORKDIR /app
ADD . /app
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV NAME OpentoAll
CMD ["python","routes.py"]