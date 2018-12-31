#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
## @file        ifttt_bme280.py
## @brief       Script to send BME280 data to IFTTT server
## @author      Keitetsu
## @date        2018/12/02
## @copyright   Copyright (c) 2018 Keitetsu
## @par         License
##              This software is released under the MIT License.
##

import json
import requests

import smbus2
import bme280
import time


def post_BME280Data_to_IFTTT(data):
    with open('ifttt_bme280.json', 'r') as f:
        dict_configs = json.load(f)

    str_key = dict_configs['ifttt']['key']
    str_event = dict_configs['ifttt']['event']
    str_url = 'https://maker.ifttt.com/trigger/' \
        + str_event \
        + '/with/key/' \
        + str_key

    str_temperature = '{0:-.2f}'.format(data.temperature)
    str_humidity = '{0:.2f}'.format(data.humidity)
    str_pressure = '{0:.2f}'.format(data.pressure)
    dict_json_data = {
        "value1": str_temperature,
        "value2": str_humidity,
        "value3": str_pressure
    }
    json_data = json.dumps(dict_json_data)

    dict_headers = {'Content-Type': 'application/json'}

    # IFTTT Webhooks
    print("begin request")
    ifttt_session = requests.Session()
    ifttt_response = ifttt_session.post(str_url, data = json_data, headers = dict_headers)
    print("response status code: %d" % (ifttt_response.status_code))
    if ifttt_response.status_code == 200:
        print("response text: %s" % (ifttt_response.text))
        ret_val = True
    else:
        ret_val = False
    print("end request")

    return ret_val


if __name__ == '__main__':
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)

    calibration_params = bme280.load_calibration_params(bus, address)

    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)

    for i in range(0, 5):
        result = post_BME280Data_to_IFTTT(data)
        if result == True:
            break
        time.sleep(2)

