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

### Installing

Clone the repository to your local machine:

```
git clone https://github.com/your-username/snowflake-id-generator.git
cd snowflake-id-generator
```

