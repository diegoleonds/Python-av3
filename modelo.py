from config import *

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable = True)
    sobrenome = db.Column(db.String(20), nullable = True)
    email = db.Column(db.String(40), nullable = True)

    def __str__(self) -> str:
        return f'(id={self.id}) {self.nome}, '+\
               f'{self.sobrenome}, {self.email}'
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "email": self.email
        }

if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all()

    contato1 = Contato(nome="Joaquim", sobrenome="Pereira", email="emaildojoaquim@gmail.com")

    contato2 = Contato(nome="José", sobrenome="Pereira", email="emaildojose@gmail.com")

    db.session.add(contato1)
    db.session.add(contato2)
    db.session.commit()

    print(contato1)