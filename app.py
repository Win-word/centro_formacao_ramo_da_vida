from flask import Flask,render_template,url_for,request


app = Flask(__name__)


@app.route("/")
def home():
    a = "olla"
    return render_template("index.html")

@app.route("/inscricao",methods=["GET","POST"])
def inscri():

    if request.method == "POST":
        nome = request.form["nome_completo"]
        data = request.form["data_"]
        docf = request.form["documento_foto_"]
        certif = request.form["certificado_foto_"]
        curso = request.form["curso_"]
    else:
        print("formulario Inalido")
    
    try:
        print("nome:", nome)
    except:
        print("error")
    return render_template("inscricao.html")



if __name__ == "__main__":
    app.run(debug="True")


