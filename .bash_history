adduser Mikko
adduser Ded
adduser matt
usermod -aG sudo matt
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
sudo -u postgres psql
adduser matt
sudo -H pip3 install virtualenv
su matt
ls
cat requirements.txt
