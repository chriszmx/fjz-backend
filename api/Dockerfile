FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app
COPY requirements.txt requirements.txt
COPY main.py main.py

RUN python -m pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0


# If you're using a relational database and want migrations
# to be run automatically, delete the previous CMD line and
# uncomment the following COPY and CMD lines
# COPY migrations migrations
# # !! PORT env var needs to match with exposed port in caprover dashboard
# CMD python -m migrations up && uvicorn main:app --host 0.0.0.0 --port 80
