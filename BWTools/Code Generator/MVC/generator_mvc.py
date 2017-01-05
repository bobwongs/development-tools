
# coding: utf-8
# author: BobWong

' MVC Generator '

__author__ = 'BobWong'

import sys
import re

# ---------- Parameters Setting ----------

project_name = 'BWiOSProject'
copyright_name = 'BobWongStudio'
import_file = '#import <UIKit/UIKit.h>'
base_vc = 'UIViewController'


path_source = 'Source'

path_generation = 'Generation'
path_generation_history = '%s/History' % path_generation
path_temp = '%s/Temporary' % path_generation
path_mvc = '%s/MVC' % path_temp

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
    vc_name = 'BW%sController' % vc

    path_vc = '%s/%s' % (path_mvc, vc_name)
    
    os.mkdir(path_mvc)
    os.mkdir(path_vc)

    file_vc_header = open('%s/%s.h' % (path_vc, vc_name), 'wb', 1)
    content_header = (
                      '//\n' +
                      '//  ' + vc_name + '.h\n' +
                      '//  ' + project_name + '\n' +
                      '//\n' +
                      '//  Created by BobWong on '+ date_string + '.\n' +
                      '//  Copyright © 2016年 ' + copyright_name + '. All rights reserved.\n' +
                      '//\n' +
                      '\n' +
                      '#import "' + base_api_manager + '.h"\n' +
                      '\n' +
                      '@interface ' + api_manager_name +' : ' + base_api_manager + '\n' +
                      '\n' +
                      '@end\n'
                    )


if __name__=='__main__':
    main()
