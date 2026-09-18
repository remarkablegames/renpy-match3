<p align="center">
  <img src="web-icon.png" width="250" alt="Ren'Py Template">
</p>

# Ren'Py Template

[![release](https://img.shields.io/github/v/release/remarkablegames/renpy-match3)](https://github.com/remarkablegames/renpy-match3/releases)
[![build](https://github.com/remarkablegames/renpy-match3/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/renpy-match3/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/renpy-match3/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/renpy-match3/actions/workflows/lint.yml)

📖 Write visual novels with Ren'Py Template.

Play in your browser:

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

Replace the assets:

- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`
- [ ] [`icon.icns`](https://anyconv.com/png-to-icns-converter/)
- [ ] [`icon.ico`](https://anyconv.com/png-to-ico-converter/)
- [ ] `web-icon.png`
- [ ] `web-presplash.webp`

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
