#!/bin/bash - 
#===============================================================================
#
#          FILE: setup.sh
# 
#         USAGE: ./setup.sh 
# 
#   DESCRIPTION: Use this shell script to configure setup
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: @theDevilsVoice 
#  ORGANIZATION: 
#       CREATED: 08/25/2018 20:35
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

sudo apt-get -y install python3-pip git
sudo pip3 install tweepy

