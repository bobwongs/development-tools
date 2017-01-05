
# coding: utf-8
# author: BobWong

' MVC Generator '

__author__ = 'BobWong'

import sys
import re
import time
import os
import shutil

# ---------- Parameters Setting ----------

project_name = 'BWiOSProject'
copyright_name = 'BobWongStudio'
author_name = 'BobWong'
import_file = '#import <UIKit/UIKit.h>'
base_vc = 'UIViewController'


path_source = 'Source'

path_generation = 'Generation'
path_generation_history = '%s/History' % path_generation
path_temp = '%s/Temporary' % path_generation
path_mvc = '%s/MVC' % path_temp

year_string = time.strftime('%Y')  # 获得当前年份
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

# 创建VC
def generateMVC(Source):
    (vc, title, comment) = getTuple(Source)
#    print 'vc: %s, title: %s, comment: %s' % (vc, title, comment)
    vc_name = 'BW%sController' % vc
    
    path_vc = '%s/%s' % (path_mvc, vc_name)
    
    os.mkdir(path_mvc)
    os.mkdir(path_vc)
    
    # vc头文件.h
    file_vc_header = open('%s/%s.h' % (path_vc, vc_name), 'wb', 1)
    content_header = (
                      '//\n' +
                      '//  %s .h\n' % (vc_name) +
                      '//  %s\n' % (project_name) +
                      '//\n' +
                      '//  Created by BobWong on %s.\n' % (date_string) +
                      '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                      '//\n' +
                      '\n' +
                      '%s' % (import_file) +
                      '\n' +
                      '@interface %s : %s\n' % (vc_name, base_vc) +
                      '\n' +
                      '@end\n'
                      )
    file_vc_header.write(content_header)
    file_vc_header.close()

    # vc实现文件.m
    file_vc_implement = open('%s/%s.m' % (path_vc, vc_name), 'wb', 1)
    content_implement = (
                         '//\n' +
                         '//  %s .m\n' % (vc_name) +
                         '//  %s\n' % (project_name) +
                         '//\n' +
                         '//  Created by BobWong on %s.\n' % (date_string) +
                         '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                         '//\n' +
                         '\n' +
                         '#import "%s.h"\n' % vc_name +
                         '\n' +
                         '@interface %s () <#<>#>' % (vc_name) +
                         '\n' +
                         '<#Code#>\n' +
                         '\n' +
                         '\n' +
                         '@end\n'
                         )
    file_vc_implement.write(content_implement)
    file_vc_implement.close()

# Tool
def stripSpace(string):
    return string.replace(' ', '')


# Main

def main():
    line = 'VC: Home Title: HomeTitle Comment: HomeComment'
    generateMVC(line)


if __name__=='__main__':
    main()
