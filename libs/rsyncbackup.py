import os
import subprocess
import datetime

class backup:
    conf = None
    time = ""
    inc = ""
    
    def __init__(self) -> None:
        self.time = self.setftime("%Y-%m-%d %H:%M")
        self.inc = self.setftime()
            
    def __createDir(self, path: str)-> bool:
        try:
            os.makedirs(path)
            return True
        except OSError as error:
            return False
    
    def setconfig(self, config:object)-> None:
        self.conf = config
        fcreated = f"{self.conf.destination}{self.inc}"
        
        if not self.__createDir(fcreated):
            raise(f"No se pudo crear el directorio {fcreated}")
        
        self.inc = fcreated
    
    def setftime(self, ftext="%Y%m%d_%H%M")-> str:
        nw = datetime.datetime.now()
        out = nw.strftime(ftext)
        return out
    
    def doBackup(self)-> str:
        cmmd = f"rsync {self.conf.options}{self.inc} {self.conf.origin} {self.conf.destination}{self.conf.folder}"
        result = subprocess.run(cmmd, shell=True, capture_output=True, text=True)
        #result = subprocess.run(cmmd, capture_output=True)
        #result = subprocess.run(cmmd)
        #out = result.stdout.decode()
        #out += "<br><br>"
        #out += result.stderr.decode()
        #return out
        return result