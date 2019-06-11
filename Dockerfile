FROM ubuntu
RUN apt-get update -y
Run apt-get upgrade -y
RUN apt-get install -y python3.7  python3-pip
RUN python3.7 -m pip install flask pafy youtube_dl --user
RUN mkdir /home/app
COPY downloads /home/app/downloads
COPY javascript /home/app/javascript
COPY templates /home/app/templates
COPY __main__.py /home/app/__main__.py
COPY config.py /home/app/config.py
WORKDIR /home/app
CMD [ "python3.7",  "__main__.py" ]
