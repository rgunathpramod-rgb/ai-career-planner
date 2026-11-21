# The machine every student's codespace starts from, with the libraries already installed.
# GitHub builds this once (see .github/workflows/build-image.yml), so codespaces
# don't need to download anything from pypi.org during the workshop.
FROM mcr.microsoft.com/devcontainers/python:3.11
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --timeout 90 --retries 10 -r /tmp/requirements.txt
