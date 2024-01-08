import curses

# setup window 
curses.initscr()
win = curses.newwin(30, 60, 0, 0)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# game elements 
ball = [(15, 30)]
plate_1 = (15, 5)
plate_2 = (15, 55)

# game logic
curses.echo()
curses.endwin()