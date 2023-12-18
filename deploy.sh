sudo apt-get update
sudo apt-get upgrade
sudo apt install net-tools

docker build -t alpha .
docker run -d -p 8000:80 alpha