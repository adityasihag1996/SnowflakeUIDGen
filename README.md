# Snowflake ID Generator Service

A simple Flask web service to generate unique, distributed, time-sortable identifiers using the Snowflake algorithm, inspired by Twitter's Snowflake project.

## Overview

The Snowflake ID generation system is a way to generate unique IDs for distributed systems at high scale without coordination. This service implements a custom version of the algorithm with the following bit distribution:

- 1-bit sign (unused)
- 41-bits for milliseconds since a custom epoch
- 5-bits for a data center identifier
- 5-bits for a machine or service identifier
- 12-bits for a sequence number within the same millisecond

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3.6+ and pip installed on your system to run this service.
```
pip install -r requirements.txt
```

### Installing

Clone the repository to your local machine:

```
git clone https://github.com/adityasihag1996/snowflake-id-generator.git
cd snowflake-id-generator
```

## Running the service
Start the Flask server with the following command:

```
python server.py
```
The service will start running on `http://127.0.0.1:6969/`.

## Generating IDs
To generate an ID, send a GET request to the root endpoint:

```
curl http://127.0.0.1:6969/
```
You will receive a JSON response with a unique Snowflake ID:

```
{
    "id": 1234567890123456789
}
```

## Handling Errors
If the ID generation service exceeds the sequence limit for the current millisecond, it will respond with an error:

```
{
    "error": "Sequence overflow. Cannot generate ID."
}
```

## Configuration
The service can be configured to specify the `data center ID` and `machine ID` by modifying the following lines in `config.py`:

```
# Initialize the Snowflake generator with your own data center and machine IDs
DATA_CENTRE_ID = <your_data_center_id>
MACHINE_ID = <your_machine_id>)
```
Replace <your_data_center_id> and <your_machine_id> with appropriate values.

## Deployment
For production environments, it's recommended to deploy the service with a WSGI server like Gunicorn and using a reverse proxy like Nginx.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## Acknowledgments
+ Twitter, for the original Snowflake ID generation concept.
