#!/bin/bash

sudo docker stop $(docker ps -a -q)
sudo docker build alpha -t
sudo docker run -d -p 8000:80 alpha


