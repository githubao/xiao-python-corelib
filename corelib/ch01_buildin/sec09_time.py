#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 15:10
"""

from datetime import datetime
import time

def run():
    """
%a Abbreviated weekday name 
%A Full weekday name 
%b Abbreviated month name 
%B Full month name 
%c Date and time representation appropriate for locale 
%I Hour in 12-hour format (01 - 12) 
%j Day of year as decimal number (001 - 366) 
%p Current locale's A.M./P.M. indicator for 12-hour clock 
%U Week of year as decimal number, with Sunday as first day of week (00 - 51) 
%w Weekday as decimal number (0 - 6; Sunday is 0) 
%W Week of year as decimal number, with Monday as first day of week (00 - 51) 
%x Date representation for current locale 
%X Time representation for current locale 
%z, %Z Time-zone name or abbreviation; no characters if time zone is unknown 
    :return: 
    """
    #
    # str_fmt = '%Y-%m-%d %H:%M:%S'
    #
    # now = time.time()
    #
    # print(now)
    # print(time.strftime(str_fmt,time.localtime()))
    # print(time.strftime(str_fmt,time.gmtime()))
    # print(time.strptime('2018-07-27 15:15:39',str_fmt))

    # Thu Jul 27 15:24:34 2017    03    208    PM    30    4    30    07/27/17    15:24:34    +0800
    str_fmt2 = '    '.join('%c %I %j %p %U %w %W %x %X %z'.split(' '))
    print(time.strftime(str_fmt2, time.localtime()))

def main():
    run()


if __name__ == '__main__':
    main()