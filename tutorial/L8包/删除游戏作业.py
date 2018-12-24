import os
import re

x = os.walk('D:/E')
dirlist = []
for dirpath, dirnames, filelist in x:
    for dirname in dirnames:
        path = os.path.join(dirpath, dirname)
        dirlist.append(path)
        if re.search('.*lol.*', dirname):
            lol = os.listdir(path)
            for dir1, dir2, file2 in os.walk(path):
                for file in file2:
                    path2 = os.path.join(dir1, file)
                    os.remove(path2)
                    print(f'删除文件{path2}')

