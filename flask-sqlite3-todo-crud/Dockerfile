FROM python:3-alpine
LABEL org.opencontainers.image.authors="kirillov-sa@yandex.ru"
# Create app directory
WORKDIR /app
 
# Install app dependencies
COPY requirements.txt ./
 
RUN pip install -r requirements.txt
 
# Bundle app source
COPY . .
 
# EXPOSE 5000
# CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:5000", "app:app"]
