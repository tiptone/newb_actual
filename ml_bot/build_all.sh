#!/bin/bash - 
#===============================================================================
#
#          FILE: build_all.sh
# 
#         USAGE: ./build_all.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 07/15/2018 17:41
#      REVISION:  ---
#===============================================================================

#set -o nounset      # Treat unset variables as an error

declare -A PACKAGES

PACKAGES=(
  python3-tk
)

cd ..
/usr/bin/virtualenv --system-site-packages -p python3  skeefooza
cd skeefooza
source ./bin/activate
pip install -U -r ./requirements.txt
./bin/python -c "import tensorflow as tf; print(tf.__version__)"
./bin/python ./hello_world.py
