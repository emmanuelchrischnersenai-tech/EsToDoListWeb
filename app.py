from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "emmanuel"

#Dados de acesso do adm
ADM_EMAIL = "emmanuel.chrischner1@gmail.com"
ADM_SENHA = "123456"

@app.route("/") #Homepage
def home():
    if "login" not in session:
        return redirect("/login")

    #Usuário logado
    return render_template("index.html")

#Rota para o tamplate login
@app.route("/login", methods=["GET", "POST"])
def login():
    if 'login' in session:
        return redirect("/")
    
    if request.method == "GET":
        return render_template("login.html")

    #POST
    email = request.form.get("email") #PEGANDO EMAIL QUE ESTAVA NO FORM
    senha = request.form.get("senha") #PEGANDO A SENHA QUE ESTAVA NO FORM

    

    if email == ADM_EMAIL and senha == ADM_SENHA:
        session["login"] = True
        return redirect("/") #Redireciona para a rota inicial

    else:
        return render_template("login.html", msgerro = "E-mail ou senha estão incorretos!")


#rota logout
@app.route("/logout")
def logout():
    session.clear()  #Limpar sessão
    return redirect("/login")

#Tratamento de erro 404
@app.errorhandler(404)
def not_found(erro):
    return render_template('erro404.html')





if __name__=="__main__":
    app.run(debug=True, port= 5000) #host='0.0.0.0' Habbilita o ip público #Debug mostra ao usuário os erros do sistema