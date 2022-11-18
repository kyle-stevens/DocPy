import sys
import os
import platform
import subprocess
import shutil

def clean_downloads():
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.chdir(os.path.join('C:\\Users', os.getlogin(), 'Downloads'))
        try:
            for entity in os.listdir(os.getcwd()):
                try:
                    if os.path.isdir(os.path.join(os.getcwd(), entity)):
                        shutil.rmtree(os.path.join(os.getcwd(), entity))
                    else:
                        os.remove(entity)
                    print('DELETED:\t', entity)
                except:
                    print('FAILED:\t', entity)
        except FileNotFoundError:
            print('STATUS:\tNo Downloads Folder in Default Location')
    return

if __name__ == '__main__':
    clean_downloads()