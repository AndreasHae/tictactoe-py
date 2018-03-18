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

## Running

Before trying to run the program, make sure to have Gtk3 and
gobject-introspection installed. Then run the following command
to install PyGObject:
```
pip install -r requirements.txt
```
After that, you can run the program with:
```
python main.py
```

You can run the unit tests with the following command:
```
python -m unittest discover .
```

## Contributing

If you found a bug or think there is a better way to implement a certain
feature, feel free to create an issue or pull request.

Note that this project has only been tested on Linux yet, so support for
Windows or OS-X is not guaranteed.
