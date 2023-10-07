# https://git.launchpad.net/cloud-images/+oci/ubuntu-base/tree/Dockerfile?h=dist-lunar-amd64-20221207
FROM scratch
ADD ubuntu-lunar-oci-amd64-root.tar.gz /
CMD ["bash"]
