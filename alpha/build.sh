#!/bin/bash

sudo docker build -t alpha .
sudo docker run -d -p 8000:80 alpha


