from note_api import NoteAPI
from Tkinter import Text, Tk
import tkMessageBox


class NoteText(Text):

    def __init__(self, api, text='', id=None):
        self.master = Tk()
        self.id = id
        self.api = api
        Text.__init__(self, self.master, bg='#f9f3a9', wrap='word', undo=True)
        self.bind('<Control-n>', self.create)
        self.bind('<Control-s>', self.save)
        if id:
            self.master.title('#%d' % id)
        self.delete('1.0', 'end')
        self.insert('1.0', text)
        self.master.geometry('220x235')
        self.pack(fill='both', expand=1)

    def save(self, event=None):
        text = self.get('1.0', 'end')
        self.id = self.api.set(text, self.id)
        tkMessageBox.showinfo('Info', 'Note %d Saved.' % self.id)

    def create(self, event=None):
        NoteText(self.api, '')


if __name__ == '__main__':
    srv, db = 'http://localhost:8069', 'v9dev'
    user, pwd = 'admin', 'admin'
    api = NoteAPI(srv, db, user, pwd)
    for note in api.get():
        x = NoteText(api, note['name'], note['id'])
    x.master.mainloop()
