# This image is awesome!
FROM ubuntu AS base
ENV curl_bin="curl"
RUN apt -y update && apt -y install "$curl_bin"
RUN curl -i -sS google.com | \
  grep -E '^Date:' | \
  sed 's/^Date: //' | tr -d $'\r' > '/tmp/date.txt'
RUN curl -Lo /tmp/bash \
  'https://github.com/robxu9/bash-static/releases/download/5.1.016-1.2.3/bash-linux-aarch64' && \
  chmod +x /tmp/bash

FROM busybox:uclibc
COPY . /app
COPY --from=base /tmp/date.txt /app/include/date.txt
COPY --from=base /tmp/bash /usr/local/bin/bash
ENTRYPOINT [ "/usr/local/bin/bash", "/app/app.sh" ]
CMD [ "--argument" ]
