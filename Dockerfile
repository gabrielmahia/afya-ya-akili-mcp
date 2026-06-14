# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for afya-ya-akili-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/afya-ya-akili-mcp"
LABEL org.opencontainers.image.description="afya-ya-akili-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir afya-ya-akili-mcp

CMD ["afya-ya-akili-mcp"]
