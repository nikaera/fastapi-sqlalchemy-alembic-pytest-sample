class Crud:
    @classmethod
    def read_by_id(cls, db_session, _id):
        return db_session.query(cls).get(_id)

    @classmethod
    def read_one(cls, db_session, _filter):
        return db_session.query(cls).filter(_filter).one_or_none()

    @classmethod
    def read(cls, db_session, _filter):
        return db_session.query(cls).filter(_filter).all()

    @classmethod
    def exists(cls, db_session, _id):
        return db_session.query(cls).get(_id).one_or_none() is not None

    # upsert by id (create and delete)
    def save(self, db_session):
        if self.id is None:
            db_session.add(self)
        db_session.commit()
        db_session.refresh(self)
        return self

    # delete
    def destroy(self, db_session):
        db_session.delete(self)
        db_session.commit()
        return self
