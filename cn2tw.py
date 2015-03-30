#coding=utf-8
__author__ = 'peixin'

"""遍历当前文件夹，把所有(指定)文件里的简体中文转换为繁体中文
file_ext_name_list 里指定要替换的文件类型
繁简转换函数用到了https://github.com/skydark/nstools/tree/master/zhtools里的langconv
"""
import os
import os.path as path
import re
from langconv import Converter


cn_char_reg = re.compile(ur'''([\u4e00-\u9fa5])''')
file_ext_name_list = ['.xml']
def get_all_files():
    for file_tuple in os.walk(os.getcwd()):
        if len(file_tuple[2]):
            file_list = [file_name for file_name in file_tuple[2] if path.splitext(file_name)[1] in file_ext_name_list]
            for file_name in file_list:
                convert_file(path.join(file_tuple[0], file_name))


def convert_file(file_name):
	file_handler = open(file_name, 'r')
	text = file_handler.read().decode('utf-8')
	file_handler.close()
	text = cn_char_reg.sub(lambda word: Converter('zh-hant').convert(word.group(1)), text)

	file_handler = open(file_name, 'w')
	file_handler.write(text.encode('utf-8'))
	file_handler.close()


def main():
	get_all_files()


if __name__ == '__main__':
	main()