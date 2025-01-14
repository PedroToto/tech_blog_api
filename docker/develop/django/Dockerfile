ARG PYTHON_VERSION=Python 3.11.2-bulleseye

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=develop

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev


COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt