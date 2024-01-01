#!/bin/bash

sudo docker build -t beta .
sudo docker run -d -p 8000:80 beta


