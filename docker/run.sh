set -e

docker build -f docker/Dockerfile -t $(basename $(pwd)) .
docker run -it --rm -w /app -v $(pwd):/app --net host $(basename $(pwd)) /bin/bash
