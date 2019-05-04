#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():

  if( len(sys.argv) < 2 ) :
    print('Usage : python currency_table_gen.py 100')
    sys.exit()

  before_date = int(sys.argv[1])
  base_import_string = '=IMPORTXML(\'Parameter Sheet\'!$B$1,"//*[@id=\'historical-data\']/div/div[2]/table/tbody/tr[{}]/td[{}]")'
  base_currency_string = 'INDEX(GoogleFinance("currency:USDJPY", "price", A{}),2,2)'

  print('date', '\t', 'start_price', '\t', 'end_price', '\t', 'min_price', '\t', 'max_price', '\t' , 'ave price', sep='')

  for i in range(1, before_date) :
    print( base_import_string.format(i, 1), '\t',
           base_import_string.format(i, 2), ' * ', base_currency_string.format(i + 1), '\t',
           base_import_string.format(i, 5), ' * ', base_currency_string.format(i + 1), '\t',
           base_import_string.format(i, 4), ' * ', base_currency_string.format(i + 1), '\t',
           base_import_string.format(i, 3), ' * ', base_currency_string.format(i + 1), '\t',
           '=AVERAGE(D{}:E{})'.format(i + 1, i + 1) , sep = '')

if __name__ == '__main__':
  main()
