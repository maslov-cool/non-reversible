# первым ходит синий при желании это изменить можно поменять значение self.now в __init__ класса Board
import pygame
import random


class Board:
    # создание поля
    def __init__(self, width_, height_):
        self.width = width_
        self.height = height_
        self.board = [[random.randrange(2) for _ in range(width_)] for _ in range(height_)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.now = 'blue'

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen_):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]:
                    pygame.draw.circle(screen_, 'red',
                                       [self.left + self.cell_size * j + self.cell_size / 2,
                                        self.top + self.cell_size * i + self.cell_size / 2],
                                       self.cell_size / 2 - 2)
                else:
                    pygame.draw.circle(screen_, 'blue',
                                       [self.left + self.cell_size * j + self.cell_size / 2,
                                        self.top + self.cell_size * i + self.cell_size / 2],
                                       self.cell_size / 2 - 2)
                pygame.draw.rect(screen_, 'white', [self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                    self.cell_size, self.cell_size], 1)

    def get_cell(self, mouse_pos: tuple):
        if (not self.left <= mouse_pos[0] <= self.left + self.cell_size * self.width or
                not self.top <= mouse_pos[1] <= self.top + self.cell_size * self.height):
            return None
        else:
            return (mouse_pos[1] - self.top) // self.cell_size, (mouse_pos[0] - self.left) // self.cell_size

    def on_click(self, cell):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == cell[0] or j == cell[1]:
                    if self.board[i][j]:
                        self.board[i][j] = 0
                    else:
                        self.board[i][j] = 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 500, 500
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Недореверси')

    board = Board(8, 8)
    board.set_view(75, 75, 30)
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
                board.render(screen)
        board.render(screen)
        # обновление экрана
        pygame.display.flip()
    # завершение работы:
    pygame.quit()
