from app import db


class Alunos(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    matricula = db.Column(db.String(9), unique=True)
    password = db.Column(db.String)
    
    def __init__(self, name, email, matricula, password):
        self.name = name
        self.email = email
        self.matricula  = matricula
        self.password = password
        
        

    def __repr__(self):
        return "<Alunos %r>" %  self.matricula
    

class Professores(db.Model):
    __tablename__= "professores"

    id= db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(9), unique=True)
    password= db.Column(db.String)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)

class Chamadas(db.Model):
    __tablename__="chamadas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    chave = db.Column(db.String(5), unique=True)
    prof_id = db.Column(db.Integer, db.ForeignKey('professores.id'))


    prof = db.relationship('Professores', foreign_keys = prof_id)

    def __init__(self, name, prof_id):
        self.name = name;
        self.prof_id = prof_id
    
    def __repr__(self):
        return "<Chamadas %r>" % self.name
    
class Presencas(db.Model):
    __tablename__="presencas"

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'))
    chamada_id = db.Column(db.Integer, db.ForeignKey('chamadas.id'))

    aluno = db.relationship('Alunos', foreign_keys = aluno_id)
    chamada = db.relationship('Chamadas', foreign_keys = chamada_id)

    def __init__(self, aluno_id, chamada_id):
        self.aluno_id = aluno_id
        self.chamada_id = chamada_id

    def __repr__(self):
        return "<Presencas %r>" % self.id





  

