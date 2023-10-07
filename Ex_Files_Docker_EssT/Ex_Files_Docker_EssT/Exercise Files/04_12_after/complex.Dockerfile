# This image is awesome!
FROM ubuntu
ENV curl_bin="curl"
RUN apt -y update && apt -y install "$curl_bin"
RUN curl -i -sS google.com | \
  grep -E '^Date:' | \
  sed 's/^Date: //' > '/app/include/date.txt'
COPY . /app
ENTRYPOINT [ "/app/app.sh" ]
CMD [ "--argument" ]
