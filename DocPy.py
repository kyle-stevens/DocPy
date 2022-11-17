import argparse
import clean_temp_files
import clean_web_cache
import clean_windows_install

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='DocPy',
                                     description='A Windows Cleanup Tool to free drive space and clear Web Cache' +
                                                 ' and Cookies',
                                     epilog='Kyle Stevens 2022 - It\'s all gone to shit...')
    parser.add_argument('--temp-files',
                        action='store_true')
    parser.add_argument('--sys-temp-files',
                        action='store_true')
    parser.add_argument('--web-cache',
                        action='store_true',
                        help='Microsoft Edge may return a \'browser in use\' message even when closed. This is due to' +
                        ' the \'Startup Boost\' feature. This can be turned off from the setting in Microsoft Edge.')
    parser.add_argument('--web-cookies',
                        action='store_true',
                        help='Microsoft Edge may return a \'browser in use\' message even when closed. This is due to' +
                             ' the \'Startup Boost\' feature. This can be turned off from the setting in Microsoft Edge.')
    parser.add_argument('--windows-installs',
                        action='store_true',
                        help='Delete old Windows Installation files.')
    parser.add_argument('--empty-bin',
                        action='store_true',
                        help='Empty the Windows Recycle Bin.')

    args = parser.parse_args()
    print('')
    if (args.temp_files):
        print('CLEANING: Computer\'s User Temporary Files...')
        clean_temp_files.clean_user_temp_files()
        print('')
    if (args.sys_temp_files):
        print('CLEANING: Computer\'s System Temporary Files...')
        clean_temp_files.clean_system_temp_files()
        print('')
    if (args.web_cache):
        print('CLEANING: Computer\'s Web Cache...')
        clean_web_cache.clean_web_cache()
        print('')
    if (args.web_cookies):
        print('CLEANING: Computer\'s Web Cookies...')
        clean_web_cache.clean_web_cookies()
        print('')
    if (args.windows_installs):
        print('CLEANING: Old Windows Installs...')
        clean_windows_install.clean_windows_install()
        print('')
    if (args.empty_bin):
        print('CLEANING: Emptying Recycle Bin...')
        clean_windows_install.empty_recycle_bin()
        print('')
    if not (
            args.temp_files or args.sys_temp_files or
            args.web_cache or args.web_cookies or
            args.windows_installs or args.empty_bin
    ):
        print("Please see the help(--help) menu for DocPy Options")