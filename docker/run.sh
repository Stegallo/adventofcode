set -e

python3 -m pip -q install pre-commit
pre-commit install

docker build -f docker/Dockerfile -t $(basename $(pwd)) .
docker run -it --rm -w /app -v $(pwd):/app --net host $(basename $(pwd)) /bin/bash
