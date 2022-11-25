import sys
import os
import platform
import subprocess
import shutil
import winshell

def clean_system_temp_files():
    file_sizes = 0
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.chdir(os.path.join('C:\\Windows\\Temp'))
        for entity in os.listdir(os.getcwd()):
            try:
                temp_file_size = 0
                if os.path.isdir(os.path.join(os.getcwd(), entity)):
                    print(entity)
                    for path, dirs, files in os.walk(entity):
                        for f in files:
                            fp = os.path.join(path, f)
                            temp_file_size += os.stat(fp).st_size
                    shutil.rmtree(entity)
                else:
                    temp_file_size = os.stat(entity)
                    os.remove(entity)
                file_sizes += temp_file_size
                print('DELETED:\t', entity)
            except Exception as e:
                print('FAILED:\t', entity, e)
        return(file_sizes)
    elif system_platform == 'Darwin':
        pass
    elif system_platform == 'Linux':
        pass
    return(file_sizes)

def clean_user_temp_files():
    file_sizes = 0
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.chdir(os.path.join('C:\\Users', os.getlogin(), 'AppData\\Local\\Temp'))
        #os.system('dir')
        for entity in os.listdir(os.getcwd()):
            try:
                temp_file_size = 0
                if os.path.isdir(os.path.join(os.getcwd(), entity)):
                    for path, dirs, files in os.walk(entity):
                        for f in files:
                            fp = os.path.join(path, f)
                            temp_file_size += os.stat(fp).st_size
                    shutil.rmtree(entity)
                else:
                    temp_file_size = os.stat(entity)
                    os.remove(entity)
                file_sizes += temp_file_size
                print('DELETED:\t', entity)
            except:
                print('FAILED:\t', entity)
        return(file_sizes)
    elif system_platform == 'Darwin':
        pass
    elif system_platform == 'Linux':
        pass
    return(file_sizes)

def clean_windows_install_files():
    file_sizes = 0
    temp_file_size = 0
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.chdir('C:\\')
        try:
            for path, dirs, files in os.walk(entity):
                for f in files:
                    fp = os.path.join(path, f)
                    temp_file_size += os.stat(fp).st_size
            shutil.rmtree('Windows.old')
        except FileNotFoundError:
            print('STATUS:\tNo Old Windows Installations to Delete.')
        file_sizes += temp_file_size
    return(file_sizes)

def empty_recycle_bin_files():
    file_sizes = 0
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    print('STATUS\tRecycle Bin has been emptied.')
    return(file_sizes)

def clean_downloads_folders_files():
    file_sizes = 0
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.chdir(os.path.join('C:\\Users', os.getlogin(), 'Downloads'))
        try:
            temp_file_size = 0
            for entity in os.listdir(os.getcwd()):
                try:
                    if os.path.isdir(os.path.join(os.getcwd(), entity)):
                        for path, dirs, files in os.walk(entity):
                            for f in files:
                                fp = os.path.join(path, f)
                                temp_file_size += os.stat(fp).st_size
                        shutil.rmtree(os.path.join(os.getcwd(), entity))
                    else:
                        temp_file_size += os.stat(fp).st_size
                        os.remove(entity)
                    file_sizes += temp_file_size
                    print('DELETED:\t', entity)
                except:
                    print('FAILED:\t', entity)
        except FileNotFoundError:
            print('STATUS:\tNo Downloads Folder in Default Location')
    return(file_sizes)