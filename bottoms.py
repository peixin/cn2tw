# coding=utf-8

import os
import os.path as path
import shutil
import subprocess
import time
import commands
import re
import collections

img_extensions = ['.jpg', '.png']
tw_resource_dir_name = 'zh_TW'
tw_package_file = '_Packager_TW.js'


def main():
    list_dir(os.getcwd())


def list_dir(root_name):
    file_list = []
    for dir_path, dir_name, files in os.walk(root_name):
        # if tw_resource_dir_name in dir_name:
        #     # print(dir_path, dir_name, files)
        #     # compare_i18n_dir_del(dir_path, os.listdir(path.join(dir_path, tw_resource_dir_name)), files)
        #     pass
    #     if tw_package_file in files:
    #         file_list.append(path.join(dir_path, tw_package_file))
    # run_package_js(file_list)
        if tw_package_file in files:
           move_swf_file(dir_path, files)
    print(objDir)

objDir = path.join(path.split(path.realpath(path.join('')))[0], 'bin\update\i18n\zh_TW')

def move_swf_file(dir_path, file_list):
    to_path = objDir
    if dir_path.find('panelAssets') != -1:
        to_path = path.join(objDir, 'panelAssets')
    src_swf_name = path.split(dir_path)[1] + '.swf'
    file_list = [x for x in file_list if path.splitext(x)[1].lower() == '.swf']
    if src_swf_name in file_list:
        panel_id_list = filedFiles(file_list)
        if len(panel_id_list):
            for id_swf in panel_id_list:
                if path.join(dir_path, src_swf_name) != path.join(dir_path, id_swf):
                    shutil.copyfile(path.join(dir_path, src_swf_name), path.join(dir_path, id_swf))
                shutil.copyfile(path.join(dir_path, src_swf_name), path.join(to_path, id_swf))


PANEL_NAME_PREFIX = 'PANEL'
PANEL_NAME_PREFIX_REG = re.compile(r'PANEL\d+.*')


def filedFiles(fileList):
    panelNameRight = []
    mathObj = None
    for swfName in fileList:
        mathObj = PANEL_NAME_PREFIX_REG.match(swfName)
        if mathObj != None:
            panelNameRight.append(swfName)
    return panelNameRight




def run_package_js(file_list):
    for file_path in file_list:
        os.chdir(path.split(file_path)[0])
        subprocess.check_call(file_path, shell=True)
        time.sleep(20)
        # a = os.popen(file_path)
        # print(a)

def compare_i18n_dir_del(dir_path, i18n_img_files, root_img_files):
    filter_img = lambda x: True if path.splitext(
        x)[1].lower() in img_extensions else False
    i18n_img_files = set(filter(filter_img, i18n_img_files))
    root_img_files = set(filter(filter_img, root_img_files))
    intersection = i18n_img_files & root_img_files
    # print(i18n_img_files)
    # print(root_img_files)
    for del_file_name in intersection:
        del_file_name = path.join(dir_path, del_file_name)
        # print(del_file_name)
        os.remove(del_file_name)


def check_conflict_id():
    all_swf_name = collections.defaultdict(list)
    for dir_path, dir_name, files in os.walk(os.getcwd()):
        for x in files:
            if path.splitext(x)[1].lower() == '.swf':
                all_swf_name[x].append(path.join(dir_path, x))

    for k in all_swf_name:
        if len(all_swf_name[k]) > 1:
            print(k, all_swf_name[k])

if __name__ == '__main__':
    main()
