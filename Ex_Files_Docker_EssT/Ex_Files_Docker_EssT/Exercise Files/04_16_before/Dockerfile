# This Dockerfile does not produce a working image.
# Complete it so that it does and name the image "test-app"
#
# NOTE: Assuming your USER environment variable is set to "Carlos",
# you should see the following output after running 'docker run --rm test-app'
#
# ```sh
# # $: docker run --rm test-app
# Hello, Carlos! Last step: run this app again, but put '--finish' at the end of your 'docker run' command
#
# # $: docker run --rm test-app --finish
# Hello again, Carlos! You've completed the challenge. Congrats, you rock!
# ```

FROM golang:1.18
WORKDIR /app
RUN go build -o /test-app /app && chmod +x /test-app
ENTRYPOINT [ "/test-app" ]
