# This file is coming as the split of game logic and ui contines. But for now the goal is to have something displayed on the screen


# from ui.game_ui import Minesweeper
# import pygame

# def main_loop():
#     while True:
#         Minesweeper.draw_surface()
#         Minesweeper.event_checker()
#         pygame.display.flip()
#         Minesweeper.clock.tick(60)

# def event_checker():
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             Minesweeper.x_position = event.pos[0]
#             Minesweeper.y_position = event.pos[1]

#         if event.type == pygame.K_ESCAPE:
#             pygame.quit()
#             exit()

#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()