import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import auto_connect_with_message as linkedin


"""
    this module is an executor module which you can be start it by pressing 's'
    and quites by pressing 'e'
"""

# delay (in second) after each execution
delay = 1
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ExecuteProgram(threading.Thread):
    def __init__(self, delay, button):
        super(ExecuteProgram, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_executing(self):
        self.running = True

    def stop_executing(self):
        self.running = False

    def exit(self):
        self.stop_executing()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.execute()     
    def execute(self):
        """ 
        Paste Your Code here !!! it will run when 's' is pressed and stop when 'e' pressed        
        """
        linkedin.connect()
        # pause after running one time
        time.sleep(delay)

mouse = Controller()
click_thread = ExecuteProgram(delay, button)
click_thread.start()


def on_press(key):
    """Key handler for starting and stopping the program"""
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_executing()
        else:
            click_thread.start_executing()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()