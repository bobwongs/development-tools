
# coding: utf-8

' MVC Generator '

__author__ = 'BobWong'

import sys
import re

string_to_check = sys.argv[1]

# 手机号自定义规则1开头第二位为358接下来的9位都为数字
regex_phone_number = r'^1(3|5|8)\d{9}$'
regex_split = r'[ |,|a-z|A-Z]+'
regex_match = r'^(\d{3})-(\d{3,8})$'
regex_match = r'^([0-9]+)$'
regex_find_all_decimal = r'\d'

regex = regex_phone_number

def main():
#    if re.match(regex, string_to_check):
#        print 'Match'
#    else:
#        print 'Not Match'

#    array = re.split(regex_split, '442 ,  sds, 3  ,  9dsdf8 7')  # 切割字符串
#    print array

    string_to_find = 'fdjio323joi34j34jio34'
    string_finded = re.findall(regex_find_all_decimal, string_to_find)
    print (string_finded)


if __name__=='__main__':
    main()
