import argparse
import windows_systems_utils
import web_browser_utils

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
    parser.add_argument('--clean-downloads',
                        action='store_true',
                        help='Empty the Windows Download Folder.')

    args = parser.parse_args()
    print('')
    if (args.temp_files):
        print('CLEANING: Computer\'s User Temporary Files...')
        print(windows_systems_utils.clean_user_temp_files(), 'Bytes')
        print('')
    if (args.sys_temp_files):
        print('CLEANING: Computer\'s System Temporary Files...')
        print(windows_systems_utils.clean_system_temp_files(), 'Bytes')
        print('')
    if (args.web_cache):
        print('CLEANING: Computer\'s Web Cache...')
        print(web_browser_utils.clean_web_cache(), 'Bytes')
        print('')
    if (args.web_cookies):
        print('CLEANING: Computer\'s Web Cookies...')
        print(web_browser_utils.clean_web_cookies(), 'Bytes')
        print('')
    if (args.windows_installs):
        print('CLEANING: Old Windows Installs...')
        print(windows_systems_utils.clean_windows_install_files(), 'Bytes')
        print('')
    if (args.empty_bin):
        print('CLEANING: Emptying Recycle Bin...')
        print(windows_systems_utils.empty_recycle_bin_files(), 'Bytes')
        print('')
    if (args.clean_downloads):
        print('CLEANING: Emptying Downloads Folder...')
        print(windows_systems_utils.clean_downloads_folders_files(), 'Bytes')
        print('')
    if not (
            args.temp_files or args.sys_temp_files or
            args.web_cache or args.web_cookies or
            args.windows_installs or args.empty_bin or
            args.clean_downloads
    ):
        print("Please see the help(--help) menu for DocPy Options")