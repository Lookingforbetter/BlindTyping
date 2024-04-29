import pygame

from src.button import *
from src.results import *


class Interface:
    pygame.init()

    width = 800
    height = 600

    screen = pygame.display.set_mode((width, height))

    condition = 1

    start_button = Button(200, 75, width // 2 - 100, 150, "Start")

    results_button = Button(200, 75, width // 2 - 100, 250, "Results")

    exit_button = Button(200, 75, width // 2 - 100, 350, "Exit")

    restart_button = Button(200, 75, width // 2 + 50, 300, "Restart")

    back_button_1 = Button(200, 75, width // 2 - 250, 300, "Back to menu")

    back_button_2 = Button(200, 75, width - 200, 0, "Back to menu")

    @classmethod
    def draw_text_center(cls, text, x, y):
        font = pygame.font.Font(None, 30)
        pic_of_text = font.render(text, True, (255, 255, 255))
        text_rect = pic_of_text.get_rect(center=(x, y))
        cls.screen.blit(pic_of_text, text_rect)

    @classmethod
    def get_rect_of_text(cls, text, x, y):
        font = pygame.font.Font(None, 30)
        pic_of_text = font.render(text, True, (255, 255, 255))
        text_rect = pic_of_text.get_rect(center=(x, y))
        return text_rect

    @classmethod
    def draw_text_top_left(cls, text, x, y):
        font = pygame.font.Font(None, 30)
        pic_of_text = font.render(text, True, (255, 255, 255))
        text_rect = pic_of_text.get_rect(topleft=(x, y))
        cls.screen.blit(pic_of_text, text_rect)

    @classmethod
    def draw_results(cls):
        for i in range(len(Results.results)):
            cls.draw_text_top_left(f"{i + 1}. {Results.results[i]}", 10, 10 + i * 25)

    @classmethod
    def draw_button(cls, button):
        pygame.draw.rect(cls.screen, (255, 255, 255), (button.x, button.y, button.width, button.height))

        font = pygame.font.Font(None, 36)

        text = font.render(button.name, True, (0, 0, 0))

        text_rect = text.get_rect(center=(button.x + button.width // 2, button.y + button.height // 2))

        cls.screen.blit(text, text_rect)

    @classmethod
    def draw_menu(cls):
        cls.draw_button(cls.start_button)
        cls.draw_button(cls.results_button)
        cls.draw_button(cls.exit_button)

    @classmethod
    def draw_frame_of_text(cls, rect):
        pygame.draw.rect(cls.screen, (255, 255, 255), (rect[0] - 30, rect[1] - 20,
                                                       rect[2] + 60, rect[3] + 40))

        pygame.draw.rect(cls.screen, (0, 0, 0), (rect[0] - 20, rect[1] - 10,
                                                 rect[2] + 40, rect[3] + 20))

    @classmethod
    def draw_trainer(cls):
        cls.draw_text_center(Text.get_sentence(Trainer.sentence_idx), cls.width // 2, cls.height // 3)

        rect = cls.get_rect_of_text(Text.get_sentence(Trainer.sentence_idx), cls.width // 2, cls.height // 3)

        rect[1] += 100

        cls.draw_frame_of_text(rect)

        Interface.draw_text_top_left(Trainer.current_text, rect[0], rect[1])

    @classmethod
    def end_of_training(cls):
        Interface.draw_text_center(Results.get_last_res(), cls.width // 2, cls.height // 3)
        Interface.draw_button(cls.restart_button)
        Interface.draw_button(cls.back_button_1)

    @classmethod
    def draw_win_of_results(cls):
        Interface.draw_results()
        Interface.draw_button(cls.back_button_2)
