#!/bin/bash -eu

##
## @file        ifttt_bme280.sh
## @brief       Script to send BME280 data to IFTTT server
## @author      Keitetsu
## @date        2018/12/02
## @copyright   Copyright (c) 2018 Keitetsu
## @par         License
##              This software is released under the MIT License.
##

export ENV_NAME=py36
export VIRTUALENV_PATH=/home/your_username/.pyenv/versions/${ENV_NAME}
source ${VIRTUALENV_PATH}/bin/activate
python ifttt_bme280.py
