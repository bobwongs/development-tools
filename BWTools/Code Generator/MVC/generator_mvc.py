
# coding: utf-8
# author: BobWong

' MVC Generator '

__author__ = 'BobWong'

import sys
import re

# ---------- Parameters Setting ----------

path_source = 'Source'
path_generation = 'Generation'
path_generation_history = '%s/History' % path_generation
path_temp = '%s/Temporary' % path_generation
path_module = 'MVC'

date_string = time.strftime("%Y/%m/%d")  # 获得当前日期，转换为字符串

# Function Definition

def getTuple(line):
    # ---------Controller----------
    find_words_vc = 'VC:'
    find_words_title = 'Title:'
    find_words_comment = 'Comment:'
    regex = r'%s|%s|%s' % (find_words_vc, find_words_title, find_words_comment)
    array = re.split(regex, line)
    for item in array:
        if item.strip() =='':
            array.remove(item)
    print array
    # VC
    vc = stripSpace(array[0])
    # Title
    title = stripSpace(array[1])
    # Comment
    comment = stripSpace(array[2])

    return (vc, title, comment)
    # ---------Controller----------

def stripSpace(string):
    return string.replace(' ', '')


# Main

def main():
    line = 'VC: Home Title: HomeTitle Comment: HomeComment'
    (vc, title, comment) = getTuple(line)
#    print 'vc: %s, title: %s, comment: %s' % (vc, title, comment)

    mvc_path = '%s/%s' % 


if __name__=='__main__':
    main()
