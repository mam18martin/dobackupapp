from datetime import datetime

class Logger():
    log = ""
    textime = ""
    
    def __init__(self) -> None:
        self.textime = datetime.now().strftime("%Y%m%d-%H%M")
    
    def set_log(self, ev: str)-> None:
        fmttime = datetime.now().strftime("%Y%m%d[%H:%M:%S]")
        text = f"{fmttime} -- {ev} \n"
        self.log = self.log + text

    def get_log(self, html=True)-> str:
        if html:
            htm = "<br>".join(self.log.split("\n"))
            return htm
         
        return self.log
    
    def write_log(self):
        file = f"./logs/dumplog-{self.textime}.txt"
        
        with open(file, "a+") as dlogs:
            dlogs.write(self.log + "\n")
    
    def __str__(self) -> str:
        return self.log
    
    
