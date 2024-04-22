import sys
import time

from interface import *

while True:
    Interface.screen.fill((0, 0, 0))

    if Interface.condition == 1:
        Interface.draw_menu()
    elif Interface.condition == 2:
        Interface.draw_trainer()
    elif Interface.condition == 3:
        Interface.end_of_training()
    elif Interface.condition == 4:
        Interface.draw_win_of_results()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if Interface.condition == 1:
                if Interface.start_button.pressed(mouse_x, mouse_y):
                    Interface.condition = 2
                    Trainer.start()
                elif Interface.exit_button.pressed(mouse_x, mouse_y):
                    sys.exit()
                elif Interface.results_button.pressed(mouse_x, mouse_y):
                    Interface.condition = 4

            elif Interface.condition == 3:
                if Interface.restart_button.pressed(mouse_x, mouse_y):
                    Interface.condition = 2
                    Trainer.start()
                elif Interface.back_button_1.pressed(mouse_x, mouse_y):
                    Interface.condition = 1

            elif Interface.condition == 4 and Interface.back_button_2.pressed(mouse_x, mouse_y):
                Interface.condition = 1

        if event.type == pygame.KEYDOWN and Interface.condition == 2:
            if Text.get_sentence(Trainer.sentence_idx)[len(Trainer.current_text)] == event.unicode:
                if Trainer.made_mistake:
                    Trainer.mistakes_count += 1
                    Trainer.made_mistake = False

                if Trainer.begun:
                    Trainer.begun = False
                    Trainer.start_time = time.time()

                Trainer.current_text += event.unicode
                if len(Trainer.current_text) == len(Text.get_sentence(Trainer.sentence_idx)):
                    Trainer.next_sentence()

                    if Trainer.sentence_idx == Text.sentences_count:
                        Results.new_result(Trainer.start_time, time.time())
                        Interface.condition = 3
            else:
                Trainer.made_mistake = True

    pygame.display.update()
