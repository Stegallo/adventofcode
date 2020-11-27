set -e

docker build -f y_2020/docker/Dockerfile -t stefanogallotti/adventofcode .
docker push stefanogallotti/adventofcode
