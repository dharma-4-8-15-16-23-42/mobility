# Mobility Challenge

This small Python microservice exposes its current running version via the `/version` API endpoint.

## Setup and Install

### Prerequisites

* Python 3.7 - Install using your systems package manager.
* Pipenv - Install using the official [installation instructions](https://github.com/pypa/pipenv#installation).

### Dependencies

Once Pipenv is installed, all necessary dependencies can be installed using:

```console
foo@bar:~$ pipenv install --dev
```

## Build

### Versioning

To release a new version, make sure all changes are commited and run:

```console
foo@bar:~$ pipenv run bump2version patch
```

### Docker Image

To build a production ready Docker image:

```console
foo@bar:~$ docker build -t dharma4815162342/mobility:VERSION .
```

## Usage

### Local

To run the application locally:

```console
foo@bar:~$ FLASK_APP=app/main.py pipenv run flask run
```

The development server can be reached at: [localhost:5000](http://localhost:5000).

## Release

```console
foo@bar:~$ docker run -p 80:80 dharma4815162342/mobility:v0.0.1
```

## External Links

[Dockerhub build pipeline](https://hub.docker.com/repository/docker/dharma4815162342/mobility/builds).