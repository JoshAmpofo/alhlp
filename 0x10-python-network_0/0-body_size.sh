#!/bin/bash
# This script will display the size of the body of an HTTP response
curl -sSL $1 | wc -c
