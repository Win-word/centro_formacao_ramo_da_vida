from flask import Flask,render_template,url_for,request
import  smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


app = Flask(__name__)


def enviarMSG(nome,data,docfn,certifn,curso):






    
    todamsg = "nome: "+ nome+"\nData de Naicimento: "+data+"\nCurso: "+curso

    msg = MIMEMultipart()
    msg["Subject"] = "<h1>Inscricao de: "+ nome+"</h1>"
    msg["From"] = "mozlimoz0rc@gmail.com"
    msg["To"] = "scaybuch@gmail.com"
    password = "vqcmikhtvwmvooab"
    #msg.add_header("Content-Type", "text/html")
    msg.attach(MIMEText(todamsg,"html"))

    #adicionando o documento


    for fl in [docfn,certifn]:
        argv = open("static/docsb/"+fl,"rb")

        argv_data = argv.read()
        argv_name = argv.name

        att = MIMEBase('application','octet-stream')
        att.set_payload(argv_data)
        encoders.encode_base64(att)
        att.add_header('Content-Disposition', f"attachment; filename= {argv_name}")
        msg.attach(att)

    #msg.add_attachment(argv_data,maintype="application", subtype="octet-stream", filename= argv_name)

    #enviando o credecial
    s = smtplib.SMTP('smtp.gmail.com: 587')
    #login de credenciai
    s.ehlo()
    s.starttls()
    s.login(msg["From"],password)
    s.sendmail(msg["From"],[msg["To"]],msg.as_string())
    s.quit()

    return "Inscricao Feita Com Sucesso!"






@app.route("/")
def home():
    a = "olladsgg"
    return render_template("index.html")

@app.route("/inscricao",methods=["GET","POST"])
def inscri():
    nome = ""
    data = ""
    docf = None
    docname= None
    certifname= None


    if request.method == "POST":
        nome = request.form["nome_completo"]
        data = request.form["data_"]
        curso = request.form["curso_"]
        docf = request.files["documento_foto_"]
        certif = request.files["certificado_foto_"]

        docname = docf.filename

        certifname = certif.filename

        if docname == "" or certifname == "":
            return render_template("inscricao.html",titulof = "os documentos estao Corrompidos.")

        #crie uma coisa para checar a instecao


        docf.save(os.path.join("static/docsb",docname))
        certif.save(os.path.join("static/docsb",certifname))
        
        try:
            print("nome:", nome)
            print("doc", str(docname))
            try:
                respo= enviarMSG(nome,data,docname,certifname,curso)
            except Exception as e:
                respo = "Erro ao Submeter "+str(e)+""
                print(respo)

            return render_template("inscricao.html",titulof = respo)

        except Exception as e2:
            print("error")
            return render_template("inscricao.html",titulof = "Err "+str(e2) )
            print(e2)






        
    else:
        print("formulario InValido")
    return render_template("inscricao.html",titulof = "Inscreva se no CFRV" )

@app.route("/cursos")
def cursosd():
    return render_template("cursos.html")




if __name__ == "__main__":
    app.run(debug="True")


