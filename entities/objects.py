from entities.square import Square


"""Objects module containing predefined square instances."""

sqr_small_white = Square(500, 0, 50, (255, 255, 255), 0.1)
sqr_red = Square(500, 0, 75, (255, 0, 0), 0.2)  
sqr_green = Square(500, 0, 100, (0, 255, 0), 0.3)
sqr_blue = Square(500, 0, 125, (0, 0, 255), 0.4)
sqr_yellow = Square(500, 0, 150, (255, 255, 0), 0.5)
sqr_big_cyan = Square(500, 0, 175, (0, 255, 255), 0.6)


squares = [sqr_small_white, sqr_red, sqr_green, sqr_blue, sqr_yellow, sqr_big_cyan]
squares_in_game = [sqr_small_white]

