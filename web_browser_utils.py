import os
import subprocess
import platform
import shutil

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def clean_web_cookies():
    file_sizes = 0
    system_platform = platform.system()
    if system_platform == 'Windows':
        standard_browsers = {'firefox.exe' : os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Roaming\\Mozilla\\Firefox\\Profiles'),
                             'chrome.exe' : os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Local\\Google\\Chrome\\User Data\\Default'),
                             'msedge.exe' : os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Local\\Microsoft\\Edge\\User Data\\Default'),
                             'opera.exe' : os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Roaming\\Opera Software\\Opera Stable'), }
        for browser in standard_browsers.keys():
            if process_exists(browser):
                print('RESOURCE IN USE:\t', browser)
            else:
                print('IN PROGRESS:\t', browser, '\'s Web Cookies Being Cleared')
                try:
                    temp_file_size = 0
                    os.chdir(standard_browsers[browser])
                    if browser == 'firefox.exe':
                        for dir in os.listdir(os.getcwd()):
                            if '.default-release' in dir:
                                os.chdir(os.path.join(os.getcwd(), dir))
                        temp_file_size += os.stat('cookies.sqlite').st_size
                        os.remove('cookies.sqlite')
                    if browser == 'chrome.exe':
                        temp_file_size += os.stat('Cookies').st_size
                        os.remove('Cookies')
                    if browser == 'msedge.exe':
                        temp_file_size += os.stat('Cookies').st_size
                        os.remove('Cookies')
                    if browser == 'opera.exe':
                        temp_file_size += os.stat('Cookies').st_size
                        os.remove('Cookies')
                    print('COMPLETE')
                    file_sizes += temp_file_size
                except FileNotFoundError:
                    print('NO COOKIE FILES\t', browser)
    elif system_platform == 'Darwin':
        pass
    elif system_platform == 'Linux':
        pass

    return(file_sizes)

def analyze_web_cookies():
    file_sizes = 0
    system_platform = platform.system()
    if system_platform == 'Windows':
        standard_browsers = {'firefox.exe' : os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Roaming\\Mozilla\\Firefox\\Profiles'),
                             'chrome.exe' : os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Local\\Google\\Chrome\\User Data\\Default'),
                             'msedge.exe' : os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Local\\Microsoft\\Edge\\User Data\\Default'),
                             'opera.exe' : os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Roaming\\Opera Software\\Opera Stable'), }
        for browser in standard_browsers.keys():
            if process_exists(browser):
                print('RESOURCE IN USE:\t', browser)
            else:
                print('IN PROGRESS:\t', browser, '\'s Web Cookies Being Cleared')
                try:
                    temp_file_size = 0
                    os.chdir(standard_browsers[browser])
                    if browser == 'firefox.exe':
                        for dir in os.listdir(os.getcwd()):
                            if '.default-release' in dir:
                                os.chdir(os.path.join(os.getcwd(), dir))
                        temp_file_size += os.stat('cookies.sqlite').st_size
                    if browser == 'chrome.exe':
                        temp_file_size += os.stat('Cookies').st_size
                    if browser == 'msedge.exe':
                        temp_file_size += os.stat('Cookies').st_size
                    if browser == 'opera.exe':
                        temp_file_size += os.stat('Cookies').st_size
                    print('COMPLETE')
                    file_sizes += temp_file_size
                except FileNotFoundError:
                    print('NO COOKIE FILES\t', browser)
    elif system_platform == 'Darwin':
        pass
    elif system_platform == 'Linux':
        pass

    return(file_sizes)


def clean_web_cache():
    file_sizes = 0
    system_platform = platform.system()
    if system_platform == 'Windows':
        standard_browsers = { #This needs to be changed to the web cache folders instead of cookies
            'firefox.exe': os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Local\\Mozilla\\Firefox\\Profiles'),
            'chrome.exe': os.path.join('C:\\Users\\', os.getlogin(),
                                       'AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache'),
            'msedge.exe': os.path.join('C:\\Users\\', os.getlogin(),
                                       'AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache'),
            'opera.exe': os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Local\\Opera Software'), }
        for browser in standard_browsers.keys():
            if process_exists(browser):
                print('RESOURCE IN USE:\t', browser)
            else:
                print('IN PROGRESS:\t', browser, '\'s Web Cookies Being Cleared')
                try:
                    temp_file_size = 0
                    os.chdir(standard_browsers[browser])
                    if browser == 'firefox.exe':
                        for dir in os.listdir(os.getcwd()):
                            if '.default-release' in dir:
                                os.chdir(os.path.join(os.getcwd(), dir))
                        for path, dirs, files in os.walk('cache2'):
                            for f in files:
                                fp = os.path.join(path, f)
                                temp_file_size += os.stat(fp).st_size
                        shutil.rmtree('cache2')
                    if browser == 'chrome.exe':
                        temp_file_size += os.stat('Cache_Data').st_size
                        shutil.rmtree('Cache_Data')
                    if browser == 'msedge.exe':
                        temp_file_size += os.stat('Cache_Data').st_size
                        shutil.rmtree('Cache_Data')
                    #if browser == 'opera.exe': #not currently working. Need to find default webcache location
                    #    os.remove('Cookies')
                    print('COMPLETE')
                    file_sizes += temp_file_size
                except FileNotFoundError:
                    print('NO CACHE FILES\t', browser)
    elif system_platform == 'Darwin':
        pass
    elif system_platform == 'Linux':
        pass

    return(file_sizes)

def analyze_web_cache():
    file_sizes = 0
    system_platform = platform.system()
    if system_platform == 'Windows':
        standard_browsers = { #This needs to be changed to the web cache folders instead of cookies
            'firefox.exe': os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Local\\Mozilla\\Firefox\\Profiles'),
            'chrome.exe': os.path.join('C:\\Users\\', os.getlogin(),
                                       'AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache'),
            'msedge.exe': os.path.join('C:\\Users\\', os.getlogin(),
                                       'AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache'),
            'opera.exe': os.path.join('C:\\Users\\', os.getlogin(), 'AppData\\Local\\Opera Software'), }
        for browser in standard_browsers.keys():
            if process_exists(browser):
                print('RESOURCE IN USE:\t', browser)
            else:
                print('IN PROGRESS:\t', browser, '\'s Web Cookies Being Cleared')
                try:
                    temp_file_size = 0
                    os.chdir(standard_browsers[browser])
                    if browser == 'firefox.exe':
                        for dir in os.listdir(os.getcwd()):
                            if '.default-release' in dir:
                                os.chdir(os.path.join(os.getcwd(), dir))
                        for path, dirs, files in os.walk('cache2'):
                            for f in files:
                                fp = os.path.join(path, f)
                                temp_file_size += os.stat(fp).st_size
                    if browser == 'chrome.exe':
                        temp_file_size += os.stat('Cache_Data').st_size
                    if browser == 'msedge.exe':
                        temp_file_size += os.stat('Cache_Data').st_size
                    #if browser == 'opera.exe': #not currently working. Need to find default webcache location
                    #    os.remove('Cookies')
                    print('COMPLETE')
                    file_sizes += temp_file_size
                except FileNotFoundError:
                    print('NO CACHE FILES\t', browser)
    elif system_platform == 'Darwin':
        pass
    elif system_platform == 'Linux':
        pass

    return(file_sizes)

if __name__ == '__main__':
    clean_web_cookies()
    clean_web_cache()