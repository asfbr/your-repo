#import pyperclip, os, sys
#if len(sys.argv) > 1:
    #os.chdir(sys.argv[1])
#pyperclip.copy(os.getcwd())

import pyperclip, time

print('Recording clipboard... (Ctrl-C to stop)')
previous_content = ''
try:
    while True:
        content = pyperclip.paste()  # Get clipboard contents.
       
        if content != previous_content:
            # If it's different from the previous, print it:
            print(content)
            previous_content = content

        time.sleep(0.01)  # Pause to avoid hogging the CPU.
except KeyboardInterrupt:
    pass