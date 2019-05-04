#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():

  print('URL', '\t', '=CONCATENATE(B2, B3, "/historical-data/?start=", C4 , "&end=",C5 )', sep = '')
  print('BaseURL' , '\t', 'https://coinmarketcap.com/ja/currencies/', sep='')
  print('Currency', '\t', 'bitcoin', sep='')
  print('Start_Date', '\t', '=TODAY() - 100' , '\t', '=TEXT(B4, "yyyymmdd")', sep='')
  print('End_Date', '\t', '=TODAY() - 1' , '\t', '=TEXT(B5, "yyyymmdd")', sep='')

if __name__ == '__main__':
  main()
