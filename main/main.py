from speech import speak, speech_input, talk_toggled
from text_input import tinput
from web_communication import check_settings
import time

ON = True
if __name__ == "__main__":
    while (ON):
        input_type = check_settings('input')
        print(input_type)
        output_type = check_settings('output')
        print(output_type)
        browser = check_settings('browser')
        print(browser)
        print('-------------')
        if talk_toggled() == True:
            speech_input()
        time.sleep(3)