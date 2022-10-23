FROM python:latest

WORKDIR /home/api

ADD *.py ./
ADD requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /home/
COPY wait-for-it.sh ./wait-for-it.sh

EXPOSE 8000

ENTRYPOINT [ "./wait-for-it.sh", "0.0.0.0:7687", "--timeout=15", "--" ]
CMD ["uvicorn", "--app-dir=/home/api", "mcu_api:api", "--reload", "--host", "172.19.0.4"]