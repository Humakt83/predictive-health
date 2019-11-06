FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir Flask-JSON

#COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

