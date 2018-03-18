import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Field(Gtk.Grid):

    def __init__(self, field_data):
        Gtk.Grid.__init__(self)

        self.rows = len(field_data)
        self.cols = len(field_data[0])

        for row in range(self.rows):
            for col in range(self.cols):
                btn = Gtk.Button()
                btn.set_size_request(50, 50)
                self.attach(btn, col, row, 1, 1)

    def update(self, field_data):
        for row in range(self.rows):
            for col in range(self.cols):
                btn = self.get_child_at(row, col)
                btn.set_text(field_data[row][col])
