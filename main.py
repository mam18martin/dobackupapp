from libs.yamltoobj import YamlToObj
from libs.logger import Logger
from libs.mysendmail import Off365SendMail
from libs.rsyncbackup import backup

# EntryPoint

if __name__ == "__main__":
    lg = Logger()
    cnf = YamlToObj("conf/config.yaml")
    smtp = cnf.smtpconf
    smtp.subject += lg.textime
    mail = Off365SendMail(smtp)

    def backapear(conf: object):
        bkp = backup()
        bkp.setconfig(conf)
        out = bkp.doBackup()
        return out


    lg.set_log("Comienzo Backup FS Usuarios")
    #bkp.setconfig(cnf.bkpusers)
    exctusers = backapear(cnf.bkpusers)
    lg.set_log(exctusers)
    lg.set_log("Fin Backup FS Usuarios")
    lg.write_log()

    lg.set_log("Comienzo Backup FS Grupos")
    #bkp.setconfig(cnf.bkpgroups)
    exctgroups = backapear(cnf.bkpgroups)
    lg.set_log(exctgroups)
    lg.set_log("Fin Backup FS Grupos")
    lg.write_log()

    mail.set_message(lg.get_log())
    
    if not mail.send():
        lg.set_log("No se pudo enviar el email")
        lg.write_log()