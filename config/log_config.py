#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""

logging mod
"""

log_path = "../log/logs.txt"

log_format = r"%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s : %(message)s"

"""

 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息

"""


log_level = "debug"

log_datefmt = "%a, %d %b %Y %H:%M:%S"

log_filemode = 'a'
