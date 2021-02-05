def letterPos(w, y):

    for i in range(0, len(w)):
        if w[i] == y:
            return i + 1

    return 0