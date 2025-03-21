from flask import Flask,render_template,url_for,request
import  smtplib

import email.message
#from email.message import EmailMessage


app = Flask(__name__)


def enviarMSG(nome,data,docf,certif,curso):




    
    todamsg = "nome: "+ nome+"\nData de Naicimento: "+data+"\nCurso: "+curso

    msg = email.message.Message()
    msg["Subject"] = "Inscricao de: "+ nome
    msg["From"] = "mozlimoz0rc@gmail.com"
    msg["To"] = "scaybuch@gmail.com"
    password = "vqcmikhtvwmvooab"
    #msg.add_header("Content-Type", "text/html")
    msg.set_payload(todamsg)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    #login de credenciais

    s.login(msg["From"],password)
    s.sendmail(msg["From"],[msg["To"]], msg.as_string().encode("utf-8"))

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


    if request.method == "POST":
        nome = request.form["nome_completo"]
        data = request.form["data_"]
        docf = request.form["documento_foto_"]
        certif = request.form["certificado_foto_"]
        curso = request.form["curso_"]


        
    else:
        print("formulario InValido")
    if request.method == "POST":

        try:
            print("nome:", nome)
            print("doc", str(docf))
            try:
                respo= enviarMSG(nome,data,docf,certif,curso)
            except Exception as e:
                respo = "Erro ao Submeter "+str(e)+""
                print(respo)

            return render_template("inscricao.html",titulof = respo)

        except Exception as e2:
            print("error")
            return render_template("inscricao.html",titulof = "Err "+str(e2) )
            print(e2)
    return render_template("inscricao.html",titulof = "Inscreva se no CFRV" )

@app.route("/cursos")
def cursosd():
    return render_template("cursos.html")




if __name__ == "__main__":
    app.run(debug="True")


