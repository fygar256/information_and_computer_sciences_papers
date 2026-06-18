#!/usr/bin/env python3
# spigot型アルゴリズムでπを発生させ、2桁チャンクで文字にデコードする。
# 修正点: 桁の比較・抽出を浮動小数点除算(/)から整数floor除算(//)に変更。
#   original の a/b, a1/b1 は近似値がπを上下から挟むため実用上かなり深くまで
#   正しい桁を出すが、(1)相異なる有理数が float では == になりうる、
#   (2)整数境界直下で int(a/b) の floor がずれる、という不健全さが原理的に残る。
#   // にすると正しさが IEEE-754 の丸めにも π の桁統計にも依存せず無条件で厳密。
import sys
k, a, b, a1, b1 = 2, 4, 1, 12, 4
i = " 0123456789.,abcdefghijklmnopqrstuvwxyz"
buf = []                      # 2桁バッファ。外ループをまたいで保持する
while True:
    # Next approximation
    p, q, k = k*k, 2*k+1, k+1
    a, b, a1, b1 = a1, b1, p*a + q*a1, p*b + q*b1
    # Decode common digits in disjoint 2-digit chunks
    d = a // b
    d1 = a1 // b1
    while d == d1:
        buf.append(d)
        if len(buf) == 2:
            # (buf0*10+buf1)/100*len(i) を整数演算化(0..99 の範囲で float 版と一致)
            n = (buf[0] * 10 + buf[1]) * len(i) // 100
            print(i[n], end='')
            sys.stdout.flush()
            buf = []
        a, a1 = 10 * (a % b), 10 * (a1 % b1)
        d, d1 = a // b, a1 // b1
 
