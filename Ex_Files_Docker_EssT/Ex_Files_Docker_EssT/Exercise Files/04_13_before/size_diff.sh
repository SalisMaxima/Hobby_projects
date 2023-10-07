#!/usr/bin/env bash
IMAGE_NAME="${1:-my-image}"

# First, get the directory this script is located in.
# This way, we can run this script from anywhere.
script_dir=$(dirname "$0")

# Next, calculate the size of our app.
app_size=$(stat --printf="%s" "${script_dir}/app.sh")

# Next, get the size of our image.
# We're assuming you called it 'my-image'.
# If you didn't, just provide the name of it to this script, like this:
# 
# $: ./size_diff.sh [NAME_OF_IMAGE]
image_size="$(docker images "${IMAGE_NAME}:latest" --format '{{.Size}}' | tail -1 | sed 's/.$//')"

# Next, convert the size of the image above into bytes.
# Exercise to reader: Why do you think I'd run 'numfmt' in a Docker container here?
image_size_bytes=$(echo "$image_size" |
  docker run -i --entrypoint numfmt ubuntu --from=iec)

# Finally, calculate the difference.
size_diff="$(((image_size_bytes-app_size)/app_size))"

echo "App size, in bytes: $app_size"
echo "App image size, in bytes: $image_size_bytes"
echo "Size difference: ${size_diff}x"
