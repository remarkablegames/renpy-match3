<p align="center">
  <img src="game/gui/window_icon.png" width="250" alt="Ren'Py Match3">
</p>

# Ren'Py Match3

[![build](https://github.com/remarkablegames/renpy-match3/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/renpy-match3/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/renpy-match3/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/renpy-match3/actions/workflows/lint.yml)

3️⃣ Ren'Py match 3 minigame demo:

- [remarkablegames](https://remarkablegames.org/renpy-match3/)

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)

### Audio

- [Kenney](https://kenney.nl/assets/interface-sounds)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/renpy-match3.git
cd renpy-match3
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
