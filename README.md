# tictactoe-py

🐍 An implementation of the popular game "Tic Tac Toe" in Python.

This project started as I was exploring Gtk and GObject using the
wonderful [PyGObject](https://pygobject.readthedocs.io/en/latest/)
API bindings. It is meant to serve as an example for other developers
willing to learn Gtk and PyGObject.

The project leverages the Model-View-Controller pattern. In the `model`
directory, you can find all model-related classes and their accompanying
unit-tests. The `main.py` contains all logic related to the UI, which is
split between the `View` and the `Controller`.

You can run the unit tests with the following command:
```
python -m unittest discover .
```

If you found a bug or think there is a better way to implement a certain
feature, feel free to create an issue or pull request.