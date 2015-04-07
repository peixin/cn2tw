# coding=utf-8
import os,os.path as path
import zipfile


compress_list = [r'panel', r'story', r'common']
file_extension_name = r'.zip'
def main():
    for dir_name in compress_list:
        if dir_name != r'common':
            dir_list = [path.join(dir_name, x) for x in os.listdir(dir_name) if path.isdir(path.join(dir_name, x))]
        else:
            dir_list = [dir_name]
        walk_folder(dir_list)

def walk_folder(dir_list):
    for dir_name in dir_list:
        file_list =[]
        for root, dirs, files in os.walk(dir_name):
            for file_name in files:
                file_list.append(path.join(root, file_name))
        zip_file_name = dir_name + file_extension_name
        zip_dir(zip_file_name, file_list)

def zip_dir(zip_file_name, file_list):
    if not file_list or len(file_list) == 0:
        return
    zf = zipfile.ZipFile(zip_file_name, "w", zipfile.zlib.DEFLATED)
    for tar in file_list:
        arc_name = tar.split(os.sep)
        arc_name = path.join(arc_name[-2], arc_name[-1])
        zf.write(tar, arc_name)
    zf.close()


if __name__ == '__main__':
    main()