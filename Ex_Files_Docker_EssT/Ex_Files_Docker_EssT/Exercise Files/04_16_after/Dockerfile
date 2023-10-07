FROM golang:1.18
COPY . /app
WORKDIR /app
RUN go build -o /test-app . && chmod +x /test-app
ENTRYPOINT [ "/test-app" ]
ENV APP_USER="Default User"
