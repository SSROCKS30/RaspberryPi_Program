import os       # import os module
import glob     # import glob module
import time     # import time module

# Initialize the device by loading one-wire communication device kernel modules
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'  # point to the address
# Find device with address starting from 28*
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'  # store the details

def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()  # read the device details
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':  # ignore first line if not valid
        time.sleep(0.2)
        lines = read_temp_raw()
    
    equals_pos = lines[1].find('t=')  # find temperature in the details
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0  # convert to Celsius
        temp_f = temp_c * 9.0 / 5.0 + 32.0    # convert to Fahrenheit
        return temp_c, temp_f

while True:
    print("Temperature: {:.2f}°C / {:.2f}°F".format(*read_temp()))
    time.sleep(1)
