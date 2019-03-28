# !/bin/sh


# Ensure that the shell script is run from root
if [[ $EUID -ne 0 ]]; then
   echo -e "This script must be run as root\n" 
   exit 1
fi
# set up keys
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -

# Update files and install default-jre
apt-get update
apt-get install default-jre -y


# Install JDK
apt-get install default-jdk -y

# Install Oracle JDK
add-apt-repository ppa:webupd8team/java
apt-get update

# Install JDK 9
apt-get install oracle-java8-installer -y

echo -e '\n#####################\n'
echo -e 'java is installed\n'
echo -e '#####################\n'

# Import the Elasticsearch PGP key
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -

# Install transport-https package 
apt-get install apt-transport-https -y
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-6.x.list

# Install elastic-search 
apt-get update 
apt-get install elasticsearch -y

# Running Elasticsearch with systemd
/bin/systemctl daemon-reload
/bin/systemctl enable elasticsearch.service

# Start elasticsearch
systemctl start elasticsearch.service

# Make a GET request, to check if elasticsearch node is running
# curl -X GET "localhost:9200/"

# Install the libraries from pip
pip install -r requirements.txt

# # Install nodejs
# apt-get install nodejs
# apt-get install npm

