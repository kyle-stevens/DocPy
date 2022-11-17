import sys
import os
import platform
import subprocess

def clean_system_temp_files():
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.chdir(os.path.join('C:\\Windows\\Temp'))
        for entity in os.listdir(os.getcwd()):
            try:
                if os.path.isdir(os.path.join(os.getcwd(), entity)):
                    os.rmdir(entity)
                else:
                    os.remove(entity)
                print('DELETED:\t', entity)
            except:
                print('FAILED:\t', entity)
        return
    elif system_platform == 'Darwin':
        pass
    elif system_platform == 'Linux':
        pass

    return

def clean_user_temp_files():
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.chdir(os.path.join('C:\\Users', os.getlogin(), 'AppData\\Local\\Temp'))
        #os.system('dir')
        for entity in os.listdir(os.getcwd()):
            try:
                if os.path.isdir(os.path.join(os.getcwd(), entity)):
                    os.rmdir(entity)
                else:
                    os.remove(entity)
                print('DELETED:\t', entity)
            except:
                print('FAILED:\t', entity)
        return
    elif system_platform == 'Darwin':
        pass
    elif system_platform == 'Linux':
        pass

    return

if __name__ == '__main__':
    clean_system_temp_files()
    clean_user_temp_files()