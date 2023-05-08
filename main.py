from libs.yamltoobj import YamlToObj
from libs.logger import Logger
from libs.mysendmail import Off365SendMail
from libs.rsyncbackup import backup

def backapear(conf: object, lg: object)-> None:
    bkp = backup()
    bkp.setconfig(conf)
    lg.set_log(conf.title)
    out = bkp.doBackup()
    lg.set_log(out)
    lg.set_log(f"Fin {conf.title}")

# EntryPoint

if __name__ == "__main__":
    lg = Logger()
    cnf = YamlToObj("conf/config.yaml")
    smtp = cnf.smtpconf
    smtp.subject += lg.textime
    mail = Off365SendMail(smtp)

    backapear(cnf.bkpusers, lg)
    backapear(cnf.bkpgroups, lg)
    
    mail.set_message(lg.get_log())    
    a, msg = mail.send()

    if not a:
        lg.set_log(msg)
        
    lg.write_log()