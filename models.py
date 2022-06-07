from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
#   Cada Máquina tem o seu respetivo Job e Task ->
#   Uma máquina não pode executar uma nova task até que a anterior esteja concluida
#   
#   Machine ->  job( JobID,TaskID )
#               [T    I    M    E]
#

class Process(db.Model):    
    
    __tablename__ = 'processes'                                                    # JobID, Task Nr (FK), Time

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer)
    time = db.Column(db.Integer)
 
    def __init__(self, id):
        self.id = id

