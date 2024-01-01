#!/bin/bash

sudo docker stop $(docker ps -a -q)
sudo docker build -t  beta .
sudo docker run -d -p 8000:80 beta


