#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import logging
from config.host_config import host_path
from config.host_config import hosts


def insert_host():

    with open(host_path, 'w') as file_open:
        file_open.write("\n")
        for host in hosts:
            file_open.write(host)
            file_open.write("\n")
    logging.info("hosts was be changed")