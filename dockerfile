FROM python:3.10-slim
COPY $PWD /home/apps
WORKDIR /home/apps
RUN pip3 install -r requirements.txt
CMD python Sample.py