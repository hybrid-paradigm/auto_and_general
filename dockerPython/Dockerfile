FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY basicwebserverapp.py /src/basicwebserverapp.py

EXPOSE  8000
CMD ["python", "/src/basicwebserverapp.py", "-p 8000"]
