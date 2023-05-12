import subprocess
from libs.yamltoobj import YamlToObj
from libs.logger import Logger
from libs.mysendmail import Off365SendMail
from libs.rsyncbackup import backup

def backapear(conf: object, lg: object)-> None:
    bkp = backup()
    bkp.setconfig(conf)
    lg.set_log(conf.title)
    out = bkp.doBackup()
    lg.set_log(f"Estadisticas de la Tarea: {out}\n")
    lg.set_log(f"Fin {conf.title}\n\n")

def diskused(fsmount: str)->str:
        list_files = subprocess.run(["./libs/usodisco", fsmount], capture_output=True, text=True)
        out = list_files.stdout.replace("\n","")
        return out

# EntryPoint

if __name__ == "__main__":
    lg = Logger()
    cnf = YamlToObj("conf/config.yaml")
    fsmount = cnf.fsmount.partition
    smtp = cnf.smtpconf
    smtp.subject += lg.textime
    mail = Off365SendMail(smtp)

    backapear(cnf.bkpusers, lg)
    backapear(cnf.bkpgroups, lg)
    
    lg.set_log(diskused(fsmount))
    lg.set_log(f"Enviando email a {smtp.recipient}")
    
    mail.set_message(lg.get_log())    
    a, msg = mail.send()

    if not a:
        lg.set_log(f"Error: {msg} \n")
    else:
        lg.set_log("Email enviado con exito \n")
    
    lg.write_log()
