import sys
import os
import platform
import subprocess
import shutil
import winshell

def clean_windows_install():
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.chdir('C:\\')
        try:
            shutil.rmtree('Windows.old')
        except FileNotFoundError:
            print('STATUS:\tNo Old Windows Installations to Delete.')
    return

def empty_recycle_bin():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    print('STATUS\tRecycle Bin has been emptied.')
    return

if __name__ == '__main__':
    clean_system_temp_files()
    empty_recycle_bin()