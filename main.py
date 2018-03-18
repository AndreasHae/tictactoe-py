import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

from model.game import Game

class View(Gtk.Window):

    __gsignals__ = {
        'button-clicked': (GObject.SIGNAL_RUN_FIRST, None, (int, int,))
    }

    def __init__(self):
        Gtk.Window.__init__(self, title="Tic Tac Toe")

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.btns = [[self.__generate_btn(row, col) for col in range(3)] for row in range(3)]

    def __generate_btn(self, row, col):
        btn = Gtk.Button()
        btn.set_size_request(50, 50)
        btn.connect('clicked', self.on_btn_clicked)
        self.grid.attach(btn, col, row, 1, 1)

    def on_btn_clicked(self, btn):
        row = self.grid.child_get_property(btn, 'top-attach')
        col = self.grid.child_get_property(btn, 'left-attach')

        self.emit('button-clicked', row, col)

class Controller:

    def __init__(self, game, view):
        self.__game = game
        self.__view = view

        self.__view.connect('button-clicked', self.on_btn_clicked)
        self.__view.connect('destroy', Gtk.main_quit)

        self.__view.show_all()

    def on_btn_clicked(self, view, row, col):
        print("{}, {}".format(row, col))

if __name__ == "__main__":
    Controller(Game(), View())
    Gtk.main()
