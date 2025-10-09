Trailer Park Boys
=================

This is the codebase for a future pinball homebrew project based on the
Canadian TV Series "Trailer Park Boys".

### Setup for MacOS

See the [MacOS Setup Guide](https://github.com/deathsave/combat/blob/main/README.md#installing-mpf)
from our other project Combat.

### Running the Game

- **Development** - `bin/dev` will run both `mpf` and `mpf-mc`
  without the console GUI. It will also run `mpf monitor` so you can
  interact with it.
- **Production** - `bin/run` will run for production using the real
  hardware devices and the console GUI.
- **Production (Remote)** - `bin/run-remote` allows running the game from a
  remote computer.
- **Test** - Run a test with `bin/test tests/test_something.py` or
  simply `bin/test` to run all tests from the `./tests` folder.
