def judge(moveA, moveB):

    if moveA == 'rock' and moveB == 'paper':
        return False
    elif moveA == 'rock' and moveB =='scissors':
        return True
    elif moveA == 'paper' and moveB == 'rock':
        return True
    elif moveA == 'paper' and moveB == 'scissors':
        return False
    elif moveA == 'scissors' and moveB == 'rock':
        return False
    else:
        return True
