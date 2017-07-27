#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 18:29
"""

import struct

import pickle

def run2():
    data = pickle.dumps('123')
    print(data)
    print(type(data))

def run():
    """
x	pad byte	no value	1
c	char	string of length 1	1
b	signed char	integer	1
B	unsigned char	integer	1
?	_Bool	bool	1
h	short	integer	2
H	unsigned short	integer	2
i	int	integer	4
I	unsigned int	integer or long	4
l	long	integer	4
L	unsigned long	long	4
q	long long	long	8
Q	unsigned long long	long	8
f	float	float	4
d	double	float	8
s	char[]	string	1
p	char[]	string	1
P	void *	long
    :return: 
    """
    buffer = struct.pack('ihb',1,2,3)
    print(buffer)
    print(struct.unpack('ihb',buffer))


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()