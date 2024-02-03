# Kayu Meranti Backend

This is the backend repository for [Kayu Meranti](https://kayumeranti.my.id), a personal project of mine which is a site dedicated to automated scraping of corpus from the internet and analyzing their sentiments.

## Overview

This repository contains the essential tools and modules that power the backend of Kayu Meranti. It comprises of three modules which are named Alpha, Beta, and Gamma all of which have their own purpose and role in ensuring the operation of the site.

The Alpha and Beta modules can be ran and used independently from the rest of the system. I have provided Dockerfiles for each of them which can be ran automatically using the bash scripts provided (build.sh). They serve as microservice web servers with API endpoints. They can be used by sending HTTP requests to their operating port.

## Modules

- Alpha: Data collection module, as of now it fetches comments from Reddit via PRAW.
- Beta: Analysis module, uses NLTK Vader to analyze the sentiments of texts.
- Gamma: Publishing module, contains scripts to publish analysis results to the Kayu Meranti site and test scripts to ensure all Alpha and Beta endpoints are working.

## TODO

- Add an installation section to the README.md file
- Add a more detailed documentation on Alpha and Beta module
- Add more data visualization methods to display historical data of each subreddit
- Add more data source (e.g. Twitter, Facebook, Instagram)
