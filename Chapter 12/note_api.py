import xmlrpclib


class NoteAPI:

    def __init__(self, srv, db, user, pwd):
        common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % (srv))
        self.api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % (srv))
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = 'note.note'

    def execute(self, method, args, kwargs=None):
        return self.api.execute_kw(
            self.db, self.uid, self.pwd, self.model,
            method, args, kwargs or {})

    def get(self, ids=None):
        return self.execute('search_read', [ids or [], ['id', 'name']], )

    def set(self, text, id=None):
        if id:
            self.execute('write', [[id], {'name': text}])
        else:
            id = self.execute('create', [{'name': text, 'user_id': self.uid}])
        return id


if __name__ == '__main__':
    srv, db = 'http://localhost:8069', 'todo'
    user, pwd = 'admin', 'admin'
    api = NoteAPI(srv, db, user, pwd)
    from pprint import pprint
    pprint(api.get())
