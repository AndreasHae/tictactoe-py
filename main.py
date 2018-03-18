import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from game import TicTacToe
from components import Field

class TicTacToeWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Tic-Tac-Toe")

        self.game = TicTacToe()

        self.button = Gtk.Button(label=self.game.next_player)
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        self.game.turn(0, 0)
        widget.set_label(self.game.__next_player)



#window = TicTacToeWindow()
window = Gtk.Window(title='Test', resizable=False)
window.set_default_size(200, 200)
#window.add(Field())
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()