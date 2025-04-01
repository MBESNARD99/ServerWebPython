#Importer Flask pour creer une application web, 
#request pour gerer les requetes HTTP,
#et render_template pour generer des pages HTML a partir de fichiers de modeles
from flask import Flask, request, render_template

#Creer une instance de l'application Flask et aide a determiner le chemin de l'app
app = Flask(__name__)

#Definir la route principale ('/') qui accepte les methodes GET et POST
@app.route('/', methods=['GET', 'POST'])
def index():
    #Recuperer les parametres de la query-string et les convertir en dictionnaire
    query_params = request.args.to_dict()
    
    #Recuperer les donnees du formulaire et les convertir en dictionnaire
    post_data = request.form.to_dict() if request.method == 'POST' else {}
    
    #Rendre le modele HTML "index.html" avec les donnees passees a la page (query_params et post_data)
    return render_template("index.html", query_params=query_params, post_data=post_data)

#Point d'entree de l'application. Ce bloc s'execute uniquement si le fichier app.py est execute directement
if __name__ == '__main__':
    #Demarrer le serveur Flask en mode debug (debug=True)
    #Cela permet d'afficher les erreurs detaillees dans le navigateur en cas de probleme
    app.run(debug=True)