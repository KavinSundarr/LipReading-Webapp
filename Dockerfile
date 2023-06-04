FROM python:3.11

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt


CMD ["streamlit","run","streamlitapp.py"]