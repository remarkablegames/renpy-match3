label start:

    scene bg lecturehall

    show eileen happy

    e "Welcome to the Ren’Py match 3 minigame!"
    e "Swap fruits to line up three or more of the same kind."
    e "Reach [TARGET_SCORE] points in [MAX_MOVES] moves to win."

    call match3_play

    if match3_result[0] == "win":
        e vhappy "Amazing! You scored [match3_result[1]] points. What a combo master!"
    elif match3_result[0] == "lose":
        e concerned "So close... you reached [match3_result[1]] points."
    else:
        e concerned "Stopping so soon? The fruit won’t match themselves, you know!"

    jump end
