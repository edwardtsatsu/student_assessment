from datetime import datetime

from sqlalchemy import select, desc, update

from configs.database import db_session


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def find_all(self, query=None):
        return db_session.scalars(select(self.model)
                                  .where(self.model.deleted_at.is_(None))
                                  .order_by(desc(self.model.id))).all()

    def find(self, id):
        return db_session.scalars(select(self.model)
                                  .where(self.model.deleted_at.is_(None))
                                  .where(self.model.id == id)).first()

    def update(self, id, data):
        db_session.execute(update(self.model)
                           .where(self.model.deleted_at.is_(None))
                           .where(self.model.id == id).values(**data))
        db_session.commit()
        return self.find(id)

    def store(self, data):
        resource = self.model(**data)
        db_session.add(resource)
        db_session.commit()
        return resource

    def delete(self, id):
        db_session.execute(update(self.model)
                           # .where(self.model.deleted_at.is_(None))
                           .where(self.model.id == id)
                           .values(deleted_at=datetime.now()))
        db_session.commit()
