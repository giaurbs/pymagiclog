#!/usr/bin/env python
import os
import fnmatch

PATH_TO_SYSLOG = '/var/log/'

#this function return a list of the syslogs present in /var/log of the system
def syslog_list():
        syslog_list_array = []
        for filepath in os.listdir(PATH_TO_SYSLOG):
                if fnmatch.fnmatch(filepath, 'syslog*'):
                        syslog_list_array.append(filepath)
        return syslog_list_array


filenames = syslog_list()
