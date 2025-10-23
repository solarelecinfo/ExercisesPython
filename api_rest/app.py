import connexion

def hello():
    return {"message": "Bienvenue !"}

def echo(body):
    return body

# Création de l'app Connexion
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml', strict_validation=True, validate_responses=True)

if __name__ == '__main__':
    app.run(port=5000)