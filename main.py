import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

from model.game import Game

class View(Gtk.Window):

    __gsignals__ = {
        'cell-clicked': (GObject.SIGNAL_RUN_FIRST, None, (Gtk.Button, int, int,)),
        'new-game': (GObject.SIGNAL_RUN_FIRST, None, ())
    }

    def __init__(self):
        Gtk.Window.__init__(self, title="Tic Tac Toe")

        self.wrapper_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                                   spacing=10,
                                   margin=10)
        self.add(self.wrapper_box)

        self.info_label = Gtk.Label()
        self.wrapper_box.add(self.info_label)

        self.field_grid = Gtk.Grid(row_spacing=5,
                                   column_spacing=5)
        self.wrapper_box.add(self.field_grid)

        self.btns = [[self.__generate_btn(row, col) for col in range(3)] for row in range(3)]

        self.new_game_btn = Gtk.Button(label="New Game")
        self.new_game_btn.connect('clicked', lambda btn: self.emit('new-game'))
        self.wrapper_box.add(self.new_game_btn)

    def __generate_btn(self, row, col):
        btn = Gtk.Button()
        btn.set_size_request(100, 100)
        btn.connect('clicked', self.on_btn_clicked)
        self.field_grid.attach(btn, col, row, 1, 1)

    def set_info(self, info):
        self.info_label.set_label(info)

    def set_field_sensitive(self, sensitive):
        self.field_grid.set_sensitive(sensitive)

    def reset_field(self):
        self.set_field_sensitive(True)
        for btn in self.field_grid.get_children():
            btn.set_label("")

    def on_btn_clicked(self, btn):
        row = self.field_grid.child_get_property(btn, 'top-attach')
        col = self.field_grid.child_get_property(btn, 'left-attach')

        self.emit('cell-clicked', btn, row, col)


class Controller:

    def __init__(self, view):
        self.__game = Game()
        self.__view = view

        self.__view.set_info("Next player: {}".format(self.__game.next_player))

        self.__view.connect('cell-clicked', self.on_cell_clicked)
        self.__view.connect('new-game', self.on_new_game)
        self.__view.connect('destroy', Gtk.main_quit)

        self.__view.show_all()

    def on_cell_clicked(self, view, btn, row, col):
        if self.__game.winner is None:
            player = self.__game.next_player

            try:
                self.__game.turn(row, col)
            except:
                return

            btn.set_label(player)

            if self.__game.winner is not None:
                self.__view.set_info("{} has won. Congratulations!".format(self.__game.winner))
                self.__view.set_field_sensitive(False)
            else:
                self.__view.set_info("Next player: {}".format(self.__game.next_player))
        else:
            self.__view.set_info("{} has won. Congratulations!".format(self.__game.winner))

    def on_new_game(self, view):
        self.__game = Game()
        self.__view.reset_field()
        self.__view.set_info("Next player: {}".format(self.__game.next_player))
        pass

if __name__ == "__main__":
    Controller(View())
    Gtk.main()
