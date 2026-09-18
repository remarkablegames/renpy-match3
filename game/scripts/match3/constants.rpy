init -1 python:

    BOARD_ROWS = 8
    BOARD_COLS = 8

    TILE_KINDS = [
        "apple",
        "blueberries",
        "carrot",
        "grapes",
        "lemon",
        "strawberry",
    ]

    TILE_IMAGES = {kind: "match3/" + kind + ".png" for kind in TILE_KINDS}

    TILE_SCALE = 0.3
    TILE_SIZE = int(300 * TILE_SCALE)
    HUD_TITLE_Y = 30
    HUD_SCORE_Y = 100
    HUD_BAR_Y = 203

    BOARD_PX = BOARD_COLS * TILE_SIZE
    BOARD_X = (1920 - BOARD_PX) // 2
    BOARD_Y = 275


    TARGET_SCORE = 1500
    MAX_MOVES = 15

    SCORE_BASE = 30
    SCORE_PER_TILE = 10
