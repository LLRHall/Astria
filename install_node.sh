# !/bin/sh


# Ensure that the shell script is run from root
if [[ $EUID -ne 0 ]]; then
   echo -e "This script must be run as root\n" 
   exit 1
fi

# Install node and npm
apt-get install nodejs
apt-get install npm


