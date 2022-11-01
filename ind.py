#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    def akkerman(m, n):
        if m == 0 and n > 0:
            return n + 1
        elif m > 0 and n == 0:
            return akkerman(m - 1, 1)
        elif m > 0 and n > 0:
            return akkerman(m - 1, akkerman(m, n - 1))
        else:
            return None

    print(akkerman(2, 3))
      
