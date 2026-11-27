FROM ghcr.io/astral-sh/uv:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends vim \
    && rm -rf /var/lib/apt/lists/*

# Keep the virtualenv outside /app so a bind-mount of the repo does not shadow it.
ENV UV_PROJECT_ENVIRONMENT=/opt/uvenv
ENV HISTCONTROL=ignoreboth:erasedups

WORKDIR /app
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --dev --frozen
