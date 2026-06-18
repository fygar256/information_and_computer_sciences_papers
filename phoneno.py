#!/usr/bin/env python3
import os
import binascii
import truerand


def main():
    while(1):
        randomdata=truerand.rand(1) # 1バイトの完全乱数の読み出し
        i='0123456789 '
        n=int(randomdata/256*len(i))
        print(i[n],end='')
    return

if __name__=='__main__':
	main()
	exit(0)
