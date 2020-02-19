def calculRC(carte):
    global RC
    if (carte[0] == '2') or (carte[0] == '3') or (carte[0] == '4') or (carte[0] == '5') or (carte[0] == '6'):
        RC += 1
    elif (carte[0] == '1') or (carte[0] == 'J') or (carte[0] == 'Q') or (carte[0] == 'K') or (carte[0] == 'A'):
        RC += -1
    else:
        RC += 0