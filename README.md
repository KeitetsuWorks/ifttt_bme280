Script to send BME280 data to IFTTT server
========


## Description

The Python Script to send BME280 data to IFTTT server.


## Requirement for Raspberry Pi


### Hardware

* [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
* [Akizuki BME280 I2C or SPI Temperature Humidity Pressure Sensor](http://akizukidenshi.com/catalog/g/gK-09421/)


### Software

* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
* Python 3
* [Python Library: smbus2](https://pypi.org/project/smbus2/)
* [Python Library: RPi.bme280](https://pypi.org/project/RPi.bme280/)
* [Python Library: requests](https://pypi.org/project/requests/)


## Usage


### Send Temperature Humidity and Pressure to IFTTT server

    $ cd ~/ifttt_bme280
    (py36) $ python ifttt_bme280.py


## Example installation in pyenv environment

1. Clone this project

        $ cd ~
        $ git clone https://github.com/KeitetsuWorks/ifttt_bme280.git
        $ cd ifttt_bme280

2. Install dependent libraries

        $ pyenv virtualenv 3.6.6 py36
        (py36) $ pyenv local py36
        (py36) $ pip install smbus2
        (py36) $ pip install RPi.bme280
        (py36) $ pip install requests

3. Make the configuration file, `ifttt_bme280.json`

        (py36) $ vi ifttt_bme280.json

    Please write your IFTTT webhooks key and your event name in JSON format.

        {
            "ifttt": {
                "key": "your_webhooks_key",
                "event": "your_event_name"
            }
        }

4. (Optional) Edit cron for periodic execution

        $ crontab -e

    `ifttt_bme280.sh` is shell script to run `ifttt_bme280.py` using pyenv environment from crond.

        */30 * * * * cd ~/ifttt_bme280; ./ifttt_bme280.sh


## License

* MIT
