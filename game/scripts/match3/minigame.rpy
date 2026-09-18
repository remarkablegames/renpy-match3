default match3_game = None
default match3_result = None


init -1 python:

    class Match3Game:

        def __init__(self):
            self.board = Match3Board(BOARD_ROWS, BOARD_COLS, TILE_KINDS)
            self.score = 0
            self.moves_left = MAX_MOVES
            self.target = TARGET_SCORE
            self.selected = None
            self.anim_cells = set()
            self.won = False
            self.lost = False

        def begin_swap(self, r1, c1, r2, c2):
            if not self.board.would_match(r1, c1, r2, c2):
                return False
            self.moves_left -= 1
            self.anim_cells = {(r1, c1), (r2, c2)}
            return True

        def animate_swap(self, r1, c1, r2, c2):
            renpy.show_screen("match3_swap_anim", source=(r1, c1), target=(r2, c2))
            renpy.pause(0.18)
            renpy.hide_screen("match3_swap_anim")

        def finish_swap(self, r1, c1, r2, c2):
            self.board.swap(r1, c1, r2, c2)
            self.anim_cells = set()
            renpy.pause(0.06)
            self.cascade()
            self.ensure_moves()
            self.check_end()

        def cascade(self):
            cells = self.board.find_matches()
            level = 0
            while cells:
                level += 1
                self.score += match_score(len(cells), level)
                renpy.play("audio/ui/drop_003.ogg", channel="sound")
                self.board.remove(cells)
                self.board.drop()
                renpy.pause(0.25)
                cells = self.board.find_matches()

        def ensure_moves(self):
            if not self.board.possible_moves():
                self.board.regenerate()
                renpy.play("audio/ui/switch29.ogg", channel="sound")

        def check_end(self):
            if self.score >= self.target:
                self.won = True
            elif self.moves_left <= 0:
                self.lost = True

        def end_result(self):
            if self.won:
                return ("win", self.score)
            if self.lost:
                return ("lose", self.score)
            return ("quit", self.score)


transform match3_glide(source, target):
    subpixel True
    pos (BOARD_X + source[1] * TILE_SIZE, BOARD_Y + source[0] * TILE_SIZE)
    linear 0.15 pos (BOARD_X + target[1] * TILE_SIZE, BOARD_Y + target[0] * TILE_SIZE)


transform match3_glide_reverse(source, target):
    subpixel True
    pos (BOARD_X + target[1] * TILE_SIZE, BOARD_Y + target[0] * TILE_SIZE)
    linear 0.15 pos (BOARD_X + source[1] * TILE_SIZE, BOARD_Y + source[0] * TILE_SIZE)


screen match3_screen():
    zorder 100

    fixed:
        xsize 1920
        ysize 1080

        text "Fruit Match" size 36 bold True:
            xalign 0.5
            ypos HUD_TITLE_Y
            outlines [(2, "#000", 0, 0)]

        add Solid("#1b202c"):
            xysize (BOARD_PX + 24, BOARD_PX + 24)
            xpos BOARD_X - 12
            ypos BOARD_Y - 12

        for r in range(BOARD_ROWS):
            for c in range(BOARD_COLS):
                if match3_game.selected == (r, c):
                    add Solid("#ffe60066"):
                        xysize (TILE_SIZE, TILE_SIZE)
                        xpos BOARD_X + c * TILE_SIZE
                        ypos BOARD_Y + r * TILE_SIZE
                else:
                    add Solid("#ffffff08"):
                        xysize (TILE_SIZE, TILE_SIZE)
                        xpos BOARD_X + c * TILE_SIZE
                        ypos BOARD_Y + r * TILE_SIZE

        for r in range(BOARD_ROWS):
            for c in range(BOARD_COLS):
                if (r, c) not in match3_game.anim_cells:
                    imagebutton:
                        idle Transform(TILE_IMAGES[match3_game.board.get(r, c)], zoom=TILE_SCALE)
                        hover Transform(TILE_IMAGES[match3_game.board.get(r, c)], zoom=TILE_SCALE)
                        xpos BOARD_X + c * TILE_SIZE
                        ypos BOARD_Y + r * TILE_SIZE
                        action Return(("tap", r, c))

        frame:
            xalign 0.5
            ypos HUD_SCORE_Y
            xpadding 40
            ypadding 10
            hbox:
                spacing 90
                vbox:
                    text "Score" size 26
                    text "[match3_game.score]" size 44 bold True xalign 0.5
                vbox:
                    text "Moves Left" size 26
                    text "[match3_game.moves_left]" size 44 bold True xalign 0.5
                vbox:
                    text "Target" size 26
                    text "[match3_game.target]" size 44 bold True xalign 0.5

        bar:
            value StaticValue(match3_game.score, match3_game.target)
            xmaximum 600
            ysize 18
            xalign 0.5
            ypos HUD_BAR_Y

        textbutton "Quit":
            xalign 0.75
            yalign 0.05
            text_size 28
            text_color "#1b202c"
            text_hover_color "#1b202c"
            background Solid("#e8e8e8CC")
            hover_background Solid("#ffffffDD")
            padding (24, 10)
            action Return(("quit",))


screen match3_swap_anim(source, target):
    zorder 200

    add TILE_IMAGES[match3_game.board.get(source[0], source[1])] zoom TILE_SCALE at match3_glide(source, target)
    add TILE_IMAGES[match3_game.board.get(target[0], target[1])] zoom TILE_SCALE at match3_glide_reverse(source, target)


label match3_play:
    $ match3_game = Match3Game()
    $ match3_done = False
    $ action = None
    show screen match3_screen

    while not match3_done:
        if match3_game.won or match3_game.lost:
            $ match3_result = match3_game.end_result()
            $ match3_done = True
        elif action is not None and action[0] == "quit":
            $ match3_result = ("quit", match3_game.score)
            $ match3_done = True
        else:
            $ action = ui.interact()

            if action is not None and action[0] == "quit":
                $ match3_result = ("quit", match3_game.score)
                $ match3_done = True
            elif action is not None and action[0] == "tap":
                python:
                    g = match3_game
                    r, c = action[1], action[2]
                    if g.selected is None:
                        g.selected = (r, c)
                        renpy.play("audio/ui/click_003.ogg", channel="sound")
                    elif g.selected == (r, c):
                        g.selected = None
                        renpy.play("audio/ui/click_003.ogg", channel="sound")
                    elif (r, c) in g.board.neighbors(g.selected[0], g.selected[1]):
                        sr, sc = g.selected
                        g.selected = None
                        if g.begin_swap(sr, sc, r, c):
                            renpy.play("audio/ui/switch13.ogg", channel="sound")
                            g.animate_swap(sr, sc, r, c)
                            g.finish_swap(sr, sc, r, c)
                    else:
                        g.selected = (r, c)
                        renpy.play("audio/ui/click_003.ogg", channel="sound")

    hide screen match3_screen
    return
