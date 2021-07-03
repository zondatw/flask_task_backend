from backend.database import Column, db, PkModel

class Task(PkModel):
    __tablename__ = "task"

    name = Column(db.String(100), nullable=False)
    status = Column(db.Boolean(), default=False)