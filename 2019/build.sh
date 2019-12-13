set -e
docker build -t $(basename $(pwd)) .
docker run -it --rm -w /adventofcode -v $(pwd):/adventofcode --net=host $(basename $(pwd))
