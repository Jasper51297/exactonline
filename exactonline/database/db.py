# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Provides an DB storage class to the Exact Online REST API Library.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2015-2018 Walter Doekes, OSSO B.V.

Usage:

    storage = DBStorage(db_session_object, db_model_object)

Example values in db model:
    auth_url = https://start.exactonline.co.uk/api/oauth2/auth
    rest_url = https://start.exactonline.co.uk/api
    token_url = https://start.exactonline.co.uk/api/oauth2/token
    base_url = https://example.com
    access_expiry = 1426492503
    access_token = dAfjGhB1k2tE2dkG12sd1Ff1A1fj2fH2Y1j1fKJl2f1sD1ON275zJNUy...
    code = dAfj!hB1k2tE2dkG12sd1Ff1A1fj2fH2Y1j1fKJl2f1sD1ON275zJNUy...
    division = 123456
    refresh_token = SDFu!12SAah-un-56su-1fj2fH2Y1j1fKJl2f1sDfKJl2f1sD11FfUn1...

Example DB model:
    class ExactOnlineModel(Base):
        __tablename__ = "exact_online"
        key = Column(String(50), primary_key=True)
        value = Column(String(500))

Client ID (EXACTONLINE_CLIENT_ID) and Client secret (EXACTONLINE_CLIENT_SECRET) 
are retrieved through environment variables.
"""

import os


class DBStorage():
    """
    Takes a SQLAlchemy db_session and db_model object
    """
    def __init__(self, db_session, db_model, **kwargs):
        super(DBStorage, self).__init__(**kwargs)
        self.db_session = db_session
        self.db_model = db_model

    def native_string(self, value):
        if isinstance(value, str):
            return value
        if isinstance(value, bytes):
            return value.decode('utf-8')
        return str(value)
        
    def get_auth_url(self):
        with self.db_session() as db:
            return self.native_string(db.query(self.db_model).filter(self.db_model.key == 'auth_url').first().value)

    def get_rest_url(self):
        with self.db_session() as db:
            return self.native_string(db.query(self.db_model).filter(self.db_model.key == 'rest_url').first().value)
        
    def get_token_url(self):
        with self.db_session() as db:
            return self.native_string(db.query(self.db_model).filter(self.db_model.key == 'token_url').first().value)

    def get_base_url(self):
        with self.db_session() as db:
            return self.native_string(db.query(self.db_model).filter(self.db_model.key == 'base_url').first().value)

    def get_response_url(self):
        with self.db_session() as db:
            return self.native_string(db.query(self.db_model).filter(self.db_model.key == 'response_url').first().value)

    def get_client_id(self):
        return os.getenv('EXACTONLINE_CLIENT_ID')

    def get_client_secret(self):
        return os.getenv('EXACTONLINE_CLIENT_SECRET')

    def get_access_expiry(self):
        with self.db_session() as db:
            return int(self.native_string(db.query(self.db_model).filter(self.db_model.key == 'access_expiry').first().value))

    def set_access_expiry(self, value):
        with self.db_session() as db:
            db.query(self.db_model).filter(self.db_model.key == 'access_expiry').update({'value': value})

    def get_access_token(self):
        with self.db_session() as db:
            return self.native_string(db.query(self.db_model).filter(self.db_model.key == 'access_token').first().value)

    def set_access_token(self, value):
        with self.db_session() as db:
            db.query(self.db_model).filter(self.db_model.key == 'access_token').update({'value': value})

    def get_division(self):
        with self.db_session() as db:
            return int(self.native_string(db.query(self.db_model).filter(self.db_model.key == 'division').first().value))
        
    def set_division(self, value):
        with self.db_session() as db:
            db.query(self.db_model).filter(self.db_model.key == 'division').update({'value': value})

    def get_refresh_token(self):
        with self.db_session() as db:
            return self.native_string(db.query(self.db_model).filter(self.db_model.key == 'refresh_token').first().value)

    def set_refresh_token(self, value):
        with self.db_session() as db:
            db.query(self.db_model).filter(self.db_model.key == 'refresh_token').update({'value': value})
        
    def get_refresh_url(self):
        return self.get_token_url()

    def get_iteration_limit(self):
        with self.db_session() as db:
            return int(self.native_string(db.query(self.db_model).filter(self.db_model.key == 'iteration_limit').first().value))

    def set_iteration_limit(self, value):
        with self.db_session() as db:
            db.query(self.db_model).filter(self.db_model.key == 'iteration_limit').update({'value': value})