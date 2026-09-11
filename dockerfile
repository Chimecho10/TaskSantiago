FROM python:3.10-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
ENV UV_LINK_MODE=copy  
COPY pyproject.toml uv.lock ./
RUN uv sync --no-install-project
COPY . .
RUN uv sync