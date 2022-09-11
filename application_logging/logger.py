# customize logging file which will show at what data , time and message of the code. 

from datetime import datetime

class App_Logger():
    def __init__(self):
        pass
    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date= datetime.date()
        self.current_time = self.now.strftime("%H,%M,%S")
        file_object.write(
            str(self.date) + "/"  +str(self.current_time) + "\t\t" + log_message + "\n")