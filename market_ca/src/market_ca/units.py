from abc import ABC, abstractmethod
from collections import namedtuple
from math import sqrt
import random

from src.market_ca.queues import Queue, PriorityQueue


class MapUnit(ABC):
    _UNIT_TYPES = namedtuple('UNIT_TYPES', 'companies clients products')
    existing_units = _UNIT_TYPES(companies=[],
                                 products=[],
                                 clients=[])
    RADIUS_VIEW = 1

    @abstractmethod
    def __init__(self, row, column, resource):
        self.row = row
        self.col = column
        self.resource = resource

    @abstractmethod
    def drop_unit(self, the_map):
        raise NotImplementedError

    def get_passable_pos(self, the_map: list, current_pos: tuple):
        visible_pos = self._get_visible_pos(len(the_map) - 1, len(the_map[0]) - 1, current_pos)
        return self._get_free_pos(the_map, visible_pos)

    @staticmethod
    def _get_free_pos(the_map, possible_cells) -> list:
        free_pos = []
        for coord in possible_cells:
            row, column = coord
            cell = the_map[row][column]
            if cell.unit is None:
                free_pos.append(coord)
        return free_pos

    def _get_visible_pos(self, rows, cols, current_pos) -> list:
        current_row, current_column = current_pos

        visible_pos = []

        dif_row = current_row - self.RADIUS_VIEW
        sum_row = current_row + self.RADIUS_VIEW

        start_row = dif_row if dif_row >= 0 else current_row
        end_row = sum_row if sum_row <= rows else current_row

        dif_col = current_column - self.RADIUS_VIEW
        sum_col = current_column + self.RADIUS_VIEW

        start_col = dif_col if dif_col >= 0 else current_column
        end_col = sum_col if sum_col <= cols else current_column

        for row in range(start_row, end_row + 1):
            for column in range(start_col, end_col + 1):
                if row == current_row and column == current_column:
                    continue
                visible_pos.append((row, column))
        return visible_pos

    def get_path(self, the_map, start_pos, goal_pos, resource=None):
        came_from = self._a_star_search(the_map, start_pos, goal_pos, resource)
        reconstructed_path = self._reconstruct_path(came_from, start_pos, goal_pos)
        path = Queue()
        if reconstructed_path is not None:
            for path_pos in reconstructed_path:
                path.put(path_pos)
        return path

    @staticmethod
    def _reconstruct_path(came_from, start_pos, goal_pos):
        current = goal_pos
        path = [current]
        while current != start_pos:
            if current in came_from:
                current = came_from[current]
            else:
                return None

            if current != start_pos:
                path.append(current)

        path.reverse()
        return path

    def _a_star_search(self, the_map, start_pos, goal_pos, resource):
        def heuristic(from_pos, to_pos):
            (x1, y1) = from_pos
            (x2, y2) = to_pos
            return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

        (row, column) = start_pos

        frontier = PriorityQueue()
        frontier.put((row, column), 0)

        came_from = {}
        cost_so_far = {}

        came_from[(row, column)] = None
        cost_so_far[(row, column)] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal_pos:
                break

            passable_pos = self.get_passable_pos(the_map, current)

            for next_pos in passable_pos:

                new_cost = cost_so_far[current] + 1

                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    if resource is None or 5 * new_cost <= resource:  # TODO 5 - стоимость перехода пока одинаковая
                        cost_so_far[next_pos] = new_cost
                        priority = new_cost + heuristic(next_pos, goal_pos)
                        frontier.put(next_pos, priority)
                        came_from[next_pos] = current

        return came_from


class Company(MapUnit):

    def __init__(self, row, col, resource):
        super().__init__(row, col, resource)
        self.existing_units.companies.append(self)
        self.company_products = []
        self.sale_points = Queue()

    def drop_unit(self, the_map):
        the_map[self.row][self.col].unit = None
        self._drop_products(the_map)
        self.existing_units.companies.remove(self)
        del self

    def _drop_products(self, the_map):
        for product in self.company_products[:]:
            product.drop_unit(the_map)

    def do_action(self, the_map):
        produced_products = 0

        passable_pos = self.get_passable_pos(the_map, (self.row, self.col))
        if len(passable_pos) <= 0:
            return None

        if not self.sale_points.empty():
            direction = self.sale_points.get()
            path = self.get_path(the_map, (self.row, self.col), direction, 20)
            if not path.empty():
                start_position = path.get()
                self.produce_product(the_map, start_position, direction, path)
                produced_products += 1

        if produced_products == 0:
            self.produce_product(the_map, random.choice(passable_pos))

    def produce_product(self, the_map, position, direction=None, path=None):
        row, column = position
        new_cell = the_map[row][column]
        product = Product(row=row,
                          col=column,
                          resource=20,
                          company=self)
        new_cell.unit = product
        self.company_products.append(product)
        self.resource -= new_cell.PRICE_PER_MOVE
        if direction is not None:
            product.set_direction(direction)
        if path is not None:
            product.path = path


class Product(MapUnit):

    def __init__(self, row, col, resource, company):
        super().__init__(row, col, resource)
        # self.quality: int
        # self.eco_friendly: int
        # self.price: int
        self.company = company
        self.direction = None
        self.path = Queue()
        self.existing_units.products.append(self)

    def drop_unit(self, the_map):
        the_map[self.row][self.col].unit = None
        self.company.company_products.remove(self)
        self.existing_units.products.remove(self)
        del self

    def set_direction(self, direction):
        self.direction = direction

    def unset_direction(self):
        self.direction = None

    def do_action(self, the_map):
        new_position = None
        # TODO 3 блока кода как отдельные функции - нужен рефакторинг
        if self.direction is not None:
            if (self.row, self.col) == self.direction:
                self.unset_direction()
            else:
                if self.path.empty():
                    self.path = self.get_path(the_map, (self.row, self.col), self.direction, self.resource)
                if not self.path.empty():
                    new_position = self.path.get()

        if new_position is not None:
            row, column = new_position
            if the_map[row][column].unit is not None:  # обработка препятствий
                self.path.reset()
                self.path = self.get_path(the_map, (self.row, self.col), self.direction, self.resource)
                if not self.path.empty():
                    new_position = self.path.get()

        if new_position is None:  # случайное перемещение
            passable_pos = self.get_passable_pos(the_map, (self.row, self.col))
            if len(passable_pos) > 0:
                new_position = random.choice(passable_pos)

        if new_position is not None:
            self.move(the_map, new_position)

    def move(self, the_map, new_position):
        row, column = new_position
        new_cell = the_map[row][column]
        new_cell.unit = self
        the_map[self.row][self.col].unit = None
        self.row = row
        self.col = column
        self.resource -= new_cell.PRICE_PER_MOVE


class Client(MapUnit):
    def __init__(self, row, col, resource):
        super().__init__(row, col, resource)
        self.existing_units.clients.append(self)

    def drop_unit(self, the_map):
        the_map[self.row][self.col].unit = None
        self.existing_units.clients.remove(self)
        del self

    def buy_product(self, the_map):
        visible_pos = self._get_visible_pos(len(the_map) - 1, len(the_map[0]) - 1, (self.row, self.col))
        found_products = self._get_products(the_map, visible_pos)

        if len(found_products) > 0:
            selected_product = random.choice(found_products)
            selected_product.company.resource += 7  # TODO заглушка
            selected_product.company.sale_points.put((selected_product.row, selected_product.col))
            self.resource -= 7
            selected_product.drop_unit(the_map)

    @staticmethod
    def _get_products(the_map, visible_pos) -> list:
        found_products = []
        for position in visible_pos:
            row, column = position
            cell = the_map[row][column]
            if isinstance(cell.unit, Product):
                found_products.append(cell.unit)
        return found_products
