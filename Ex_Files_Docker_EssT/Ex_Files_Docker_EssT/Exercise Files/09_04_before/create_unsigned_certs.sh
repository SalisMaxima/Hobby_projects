#!/usr/bin/env bash
EXERCISE_FILES_DIR="$(dirname "$0")"
OPENSSL_COMMAND=(
  openssl                                 # OpenSSL is a program that manages SSL certificates. Very useful to learn.
  req                                     # Tells OpenSSL to request a new cert. Since we are self-signing it, this request will be granted immediately.
  -x509                                   # -x509 tells openssl that this is a self-signed certificate.
  -newkey rsa:4096                        # This tells OpenSSL to create a private key for the cert with a 4096-bit long RSA key.
  -keyout /work/certs/key.pem             # This exports our RSA key to our certs directory.
  -out /work/certs/cert.pem               # This exports our cert to our certs directory.
  -nodes                                  # This prevents OpenSSL from encrypting the private key generated earlier.
  -sha256                                 # This uses a SHA256 hash to sign the cert.
  -subj "/CN=localhost"                   # This configures the certificate to be associated with our own computer.
)

# Remove the certs directory, if it exists.
test -d "${EXERCISE_FILES_DIR}/certs" && rm -rf "${EXERCISE_FILES_DIR}/certs"
mkdir -p "${EXERCISE_FILES_DIR}/certs"

# Create an Alpine container with a /work directory bind-mounted to our exercise files directory.
# Use it to install OpenSSL via "apk add openssl" and run our OpenSSL command above.
docker run --rm -v "$EXERCISE_FILES_DIR:/work" -w /work alpine \
  sh -c "apk add openssl && ${OPENSSL_COMMAND[*]}"
