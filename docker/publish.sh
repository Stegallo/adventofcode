set -e

docker build -f docker/Dockerfile -t stefanogallotti/adventofcode .
docker push stefanogallotti/adventofcode
