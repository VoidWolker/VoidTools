#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
循环获取FTP文件列表，实现下载整个目录

create by VOidWalker in 2017.7.24
"""

import os
from ftplib import FTP
from config.ftp_config import ftp_host
from config.ftp_config import ftp_port
from config.ftp_config import ftp_user
from config.ftp_config import ftp_pwd
from config.ftp_config import ftp_path
from config.ftp_config import local_path


def download_ftp():
    ftp = FTP()
    ftp.connect(ftp_host, ftp_port)  # 链接服务器
    ftp.login(ftp_user, ftp_pwd)  # 执行登录操作
    ftp.cwd(ftp_path)  # 切换目录
    get_file_list = ftp.nlst()  # 获取文件列表
    print(get_file_list)
    os.chdir(local_path)  # 进入到本地目录
    for file_name in get_file_list:
        # 循环获取文件
        with open(file_name, "wb") as file:
            ftp.retrbinary('RETR %s' % file_name, file.write)  # 下载并写入到本地文件
    ftp.close()

download_ftp()