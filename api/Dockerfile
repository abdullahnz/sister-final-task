FROM python:3.8-slim-buster


WORKDIR /app
COPY app/ .

RUN pip install -r requirements.txt

# RUN useradd -ms /bin/bash user
# RUN chown -R user /app

# USER user

EXPOSE 8000

CMD ["python", "app.py"]