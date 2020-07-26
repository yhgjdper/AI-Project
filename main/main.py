from speech import speak, speech_input
from text_input import tinput
from web_communication import check_settings

ON = True
if __name__ == "__main__":
    input_type = check_settings('input')
    output_type = check_settings('output')
    browser = check_settings('browser')