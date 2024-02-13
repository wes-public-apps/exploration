FROM node:latest as builder

WORKDIR /client

# copy source
COPY client /client
COPY client/package*.json /client/

# build source
RUN npm install
# RUN npm test
RUN npm run build

# COPY --from=build /app/react-httpd.conf /usr/local/apache2/conf/httpd.conf
# COPY --from=build /app/build /usr/local/apache2/htdocs/
# COPY --from=build /app/react.htaccess /usr/local/apache2/htdocs/.htaccess

FROM python:latest as runner

WORKDIR /

# copy python source
COPY server /server
# copy python tests
COPY server_tests /server_tests
# install dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# run unittests
RUN python -m unittest discover -s /server_tests -p "test*.py"
RUN rm -r /server_tests
# copy compiled react app
COPY --from=builder /client/build/ /build

CMD ["python3", "-m", "server.main"]