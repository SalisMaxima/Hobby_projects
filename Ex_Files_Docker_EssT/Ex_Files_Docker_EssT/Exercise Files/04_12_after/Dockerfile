# This image is awesome!
FROM ubuntu AS base
ENV curl_bin="curl"
RUN apt -y update && apt -y install "$curl_bin"
RUN curl -i -sS google.com | \
  grep -E '^Date:' | \
  sed 's/^Date: //' | tr -d $'\r' > '/tmp/date.txt'

FROM bash
COPY . /app
COPY --from=base /tmp/date.txt /app/include/date.txt
ENTRYPOINT [ "/usr/local/bin/bash", "/app/app.sh" ]
CMD [ "--argument" ]
