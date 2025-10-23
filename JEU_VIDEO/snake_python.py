import curses
import random

def main(stdscr):
    # Initialisation de l'écran
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(150)

    # Dimensions
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)

    # Position initiale du serpent (au centre)
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]
    direction = curses.KEY_RIGHT

    # Première nourriture
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], curses.ACS_PI)

    # Boucle du jeu
    while True:
        key = w.getch()
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        # Nouvelle tête
        head = [snake[0][0], snake[0][1]]
        if direction == curses.KEY_RIGHT:
            head[1] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1

        snake.insert(0, head)

        # Si serpent mange la nourriture
        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Retirer la queue
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Conditions de fin (collision mur ou soi-même)
        if (snake[0][0] in [0, sh] or
            snake[0][1] in [0, sw] or
            snake[0] in snake[1:]):
            msg = "GAME OVER!"
            w.addstr(sh // 2, sw // 2 - len(msg)//2, msg)
            w.refresh()
            w.nodelay(0)
            w.getch()
            break

        # Afficher la tête
        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

curses.wrapper(main)