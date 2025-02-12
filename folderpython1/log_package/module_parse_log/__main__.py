#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import sys, getopt, re
import argparse
import os
from datetime import datetime
import matplotlib.pyplot as plt


def prepare_list(counter, list, match_object):
    result_line = counter + "-value match--" + match_object.group(1) + "--" + match_object.group(
        3) + "--" + match_object.group(5)
    print(result_line)
    return list.append(result_line)


def convert_bytes(size_bytes, units):
    result_list = []
    if units == "K":
        MegaBytes = 0
        KiloBytes = int(size_bytes / 1024)
        Kilo_residu = size_bytes % 1024
        result_list = [MegaBytes, KiloBytes, Kilo_residu]
    elif units == "M":
        MegaBytes = int(size_bytes / pow(1024, 2))
        Kilo_residu_byte = size_bytes % pow(1024, 2)
        Kilo_residu = int(Kilo_residu_byte / 1024)
        Byte_residu = size_bytes % pow(1024, 1)
        result_list = [MegaBytes, Kilo_residu, Byte_residu]
    else:
        sys.exit()
    return result_list


def get_MB(size_bytes):
    return size_bytes / pow(1024, 2)


def check_bytes_sum(list_data, expected_value):
    resultMEGA = list_data[0]
    resultKILO = list_data[1]
    resultBYTE = list_data[2]
    total_bytes = (resultMEGA * 1024 * 1024 + resultKILO * 1024 + resultBYTE)
    boolean_result = total_bytes == expected_value
    print("Total bytes are ", str(total_bytes), "equals ====", str(expected_value) + " Result=", str(boolean_result))
    return boolean_result

def get_datetime_list(list_string):
    datetime_list = []
    format = "%Y-%m-%dT%H:%M:%S.%f%z"
    for i in list_string:
        datetime_obj = datetime.strptime(i, format)
        datetime_list.append(datetime_obj)
    return datetime_list

def construct_graph(date_list,bytes_list,color,sub_title):
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.ticklabel_format(useOffset=False, style='plain')
    lines = ax.plot_date(date_list, bytes_list, "P")
    for i in lines:
        i.set_color(color)
    plt.grid(True)
    plt.xlabel("Datetime UTC+2")
    plt.ylabel("KBytes")
    plt.title('KiloBytes vs Time('+sub_title+')')
  #  plt.show()

def get_kb_list(list_string):
    float_kb_list = []
    for i in list_string:
        float_kb_list.append(float(i/1024))
    return float_kb_list
def main():
    # User supported console arguments
    parser = argparse.ArgumentParser(description='Process sudo log statics parsing to display on console')
    parser.add_argument('-f', action='store', dest='var_logfile', help='Provide sudo.log path ')

    # Objects conversion from USER input parameters
    result = parser.parse_args()
    config_file = os.path.realpath(result.var_logfile)

    print("Beginning on parssing")
    regular_kernel = re.compile(
        r'^([0-9]+-.*)([ ]localhost.*)(Sent[ ]([0-9]+)[ ]bytes).*(received[ ]([0-9]+)[ ]bytes).*$')

    # OUTPUTS
    # general values
    row_matched = 0
    list_time_stamp = []
    #extra
    list_time_stamp_real=[]
    # data sent
    total_sent_data = 0
    list_sent_data = []
    # data_received
    total_received_data = 0
    list_received_data = []


    with open(config_file) as f:
        for line in f:
            result_groups = re.match(regular_kernel, line)
            if result_groups is not None:
                if len(result_groups.groups()) == 6:
                    print("this row has a match", result_groups.group(0))
                    row_matched += 1
                    # GET BYTES DATA SENT FROM FILE
                    list_sent_data.append(int(result_groups.group(4)))
                    # GET BYTES DATA RECEIVED FROM FILE
                    list_received_data.append(int(result_groups.group(6)))
                    # FORMAT LOG MATCHING ROW
                    prepare_list(str(row_matched), list_time_stamp, result_groups)

                    #GET TIMESTAMP ONLY VALUE
                    list_time_stamp_real.append(result_groups.group(1))
                else:
                    print("this row is not null but doesnt match size ")
            else:
                pass

    for i, k in zip(list_sent_data, list_received_data):
        # CALCULATE TOTAL DATA SENT
        total_sent_data += i
        # CALCULATE TOTAL DATA RECEIVED
        total_received_data += k


    # FORMAT SENT DATA RESULT OUTPUTS
    format_list = convert_bytes(total_sent_data, "M")
    format_detail_datasent = "Result=" + str(format_list[0]) + "MB " + str(format_list[1]) + "KB " + str(
        format_list[2]) + "B"
    print(format_list, total_sent_data)
    total_sent_data_float = str(round(get_MB(total_sent_data), 6)) + "MB"

    # FORMAT RECEIVED DATA RESULT OUTPUTS
    format_list_received = convert_bytes(total_received_data, "M")
    format_detail_datareceive = "Result=" + str(format_list_received[0]) + "MB " + str(
        format_list_received[1]) + "KB " + str(format_list_received[2]) + "B"
    print(format_list_received, total_received_data)
    total_received_data_float = str(round(get_MB(total_received_data), 6)) + "MB"

    # PRINT OUTPUT STATICS ON CONSOLE
    print("\n ###########################SHOW DATA SENT RESULT##########################")
    prefix_sent = "TOTAL SENT DATA "
    print(prefix_sent, total_sent_data_float)
    print(prefix_sent, total_sent_data, "Bytes")
    print("DETAILS", format_detail_datasent)
    print("MAX BYTES ELEMENT IS ", max(list_sent_data), "MIN ELEMENT IS", min(list_sent_data))

    print("\n ###########################SHOW DATA RECEIVED RESULT##########################")
    prefix_received = "TOTAL RECEIVED DATA "
    print(prefix_received, total_received_data_float)
    print(prefix_received, total_received_data, "Bytes")
    print("DETAILS", format_detail_datareceive)
    print("MAX BYTES ELEMENT IS ", max(list_received_data), "MIN ELEMENT IS", min(list_received_data))

    print("##############################SHOW GENERAL RESULTS##########################")
    print("number of row matcher=", row_matched)
    check_bytes_sum(format_list, total_sent_data)
    print("TOTAL DETAILS ELEMENTS=")
    for i in list_time_stamp:
        print(i)
    #CREATING GRAPHE
    #extra calculate datetime list for plot
    list_time_stamp_real_obj=get_datetime_list(list_time_stamp_real)


    construct_graph(list_time_stamp_real_obj,get_kb_list(list_sent_data),'green',"DATA_SENT")
    construct_graph(list_time_stamp_real_obj, get_kb_list(list_received_data),'blue',"DATA_RECEIVED")
    #plt.tight_layout(4)
    plt.show()

if __name__ == "__main__":
    main()