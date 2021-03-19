import base64
import datetime
import struct
base64_string ="2FHwatDmlkowShVCc3FfQq4qKUADcS9bXw=="
hex_string1 = base64.b64decode(base64_string).hex()

def split_hex_to_bytes(hex_string):
    hex_list =[]
    for i in range(0,len(hex_string),2):
        hex_list.append(hex_string[i:i+2])
    return hex_list

def concat(list):
    s =""
    for elements in list:
        s = s + elements
    return s

hex_bytes_list = split_hex_to_bytes(hex_string1)

ID = hex_bytes_list[0:8]
longtitude_BE = hex_bytes_list[8:12] #долгота биг эндиан
longtitude_LE = concat(longtitude_BE[::-1]) #долгота литл эндиан
latitude_BE = hex_bytes_list[12:16] #широта биг эндиан
latitude_LE = concat(latitude_BE[::-1]) #широта литл эндиан
altitude_BE = hex_bytes_list[16:20] #высота биг эндиан
altitude_LE = concat(altitude_BE[::-1]) #высота литл эндиан
cmd = hex_bytes_list[20]
timestamp_bytes_BE = hex_bytes_list[21:] #время в байтах биг эндиан
timestamp_bytes_LE = concat(timestamp_bytes_BE[::-1]) #время в байтах литл эндиан пока под вопросом перевод времени
print(timestamp_bytes_LE)
print("Latitude - Широта = {}".format(round(struct.unpack('!f', bytes.fromhex(latitude_LE))[0],2)))
print("Longtitude - Долгота = {}".format(round(struct.unpack('!f', bytes.fromhex(longtitude_LE))[0],2)))
print("Altitude - Высота = {}".format(round(struct.unpack('!f', bytes.fromhex(altitude_LE))[0],2)))
print(datetime.datetime.fromtimestamp(int(timestamp_bytes_LE,16))) # время в ответе надо записать в GMT я перевел часы в системе так же
