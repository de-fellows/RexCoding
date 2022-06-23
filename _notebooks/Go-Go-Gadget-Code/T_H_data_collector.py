# Author: Christina Kampel
# Current Version: v2-3, June 19, 2022
# References:
    # DHT11 data collection code is from grove.py documentation: https://github.com/Seeed-Studio/grove.py/blob/master/doc/README.md
    # DHT20 data collection code is from user ultracold on StackExchange: https://raspberrypi.stackexchange.com/questions/133457/how-can-rpi4b-use-python-to-talk-to-the-i2c-dht20-sht20-temperature-and-humidi 
# Instructions:
    # Run via Raspberry Pi terminal using command: python3 T_H_data_collector_v1.py
    # Stop code using Ctrl + C or Command + C

# Changes from v2-2:
# - Added an if-else statement so that the header of the DataFrame is not written to the CSV file every single time
# - Removed import of csv library (no longer needed)

import time
import pandas as pd
from datetime import datetime, date
import smbus
from seeed_dht import DHT
import os.path

# Exception class will stop the code if we cannot connect to either sensor

class ConnectionError(Exception):
  """Exception raised when a sensor is not connected or responding to test code."""
  pass

# Using a function to write each line of the CSV file containing temperature and humidity data

def write_line():
    """
    Write a line of data to a CSV file. Data is collected by one DHT11 and one DHT20 temperature and humidity sensor.
    Each line contains: current date, current time, dht11_temp, dht11_humi, dht20_temp, dht20_humi.
    - Arguments: None
    - Returns: None
    """
    
    # Let's get data from the DHT11 sensor

    dht11 = DHT("11", 4) # Type, GPIO pin for signal cable

    # Make sure DHT11 can connect. If not, raise ConnectionError

    try:
        dht11_humi, dht11_temp = dht11.read()
    except:
        raise ConnectionError("DHT11 Sensor is not responding. Please check connection.")


    # Let's get data from the DHT20 sensor

    address = 0x38 # Put your device's address here

    i2cbus = smbus.SMBus(1)
    time.sleep(0.5)

    # Check that I2C connection was initialized. If not, raise ConncectionError

    data = i2cbus.read_i2c_block_data(address,0x71,1)
    if (data[0] | 0x08) == 0:
        raise ConnectionError("Initialization Error. Please check connection.")

    i2cbus.write_i2c_block_data(address,0xac,[0x33,0x00])
    time.sleep(0.1)

    # Make sure DHT20 can connect. If not, raise ConnectionError

    try:
        data = i2cbus.read_i2c_block_data(address,0x71,7)
    except:
        raise ConnectionError("DHT20 Sensor is not responding. Please check connection.")

    # Format the DHT20 data so it makes sense to us

    Traw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
    dht20_temp = 200*float(Traw)/2**20 - 50

    Hraw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
    dht20_humi = 100*float(Hraw)/2**20

    # list of date, time --> Need to be converted into list format

    dates = []
    dates.append(date.today())

    times = []
    times.append(datetime.now().strftime("%H:%M:%S"))

    # Save the dictionary of lists into a Pandas DataFrame

    dict = {"Date": dates, "Time": times, "DHT11 Temp": dht11_temp, "DHT11 Humi": dht11_humi, "DHT20 Temp": dht20_temp, "DHT20 Humi": dht20_humi}
    df = pd.DataFrame(dict)

    # Print current line of data to the terminal

    print(df.iloc[0])

    # Write data to CSV file.
    # If the file already exists, append to the file without the header "Date, Time, DHT11 Temp, ...".
    # If the file does not already exist, a new file will be created and the header "Date, Time, DHT11 Temp, ..." will be written to the file along with the data.

    if os.path.exists("DHT_data.csv"):
        with open("DHT_data.csv", "a", newline="") as file:     # "a" ensures you append to the CSV, not overwrite it
            df.to_csv(file, index=False, header=False)
    else:
        with open("DHT_data.csv", "a", newline="") as file:
            df.to_csv(file, index=False)
    

if __name__ == "__main__":
    while True:
        write_line()