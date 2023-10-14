import random

from src.market_ca.cell import Cell
from src.market_ca.units import *

UNIT_TYPE = {'Company': 0, 'Product': 1, 'Client': 2}
COMPANY_START_RESOURCE = 50
PRODUCT_START_RESOURCE = 20
CLIENT_START_RESOURCE = 25


def create_map(rows, columns):
    return [[Cell() for _ in range(columns)] for _ in range(rows)]


def create_unit(unit_type, row: int, column: int):
    map_unit = get_unit(unit_type, row, column)
    return map_unit


def get_unit(unit_type, row_num, col_num):
    if unit_type == 0:
        return Company(row_num, col_num, COMPANY_START_RESOURCE)
    elif unit_type == 1:
        # for test
        return Product(row_num, col_num, PRODUCT_START_RESOURCE, None)
    elif unit_type == 2:
        return Client(row_num, col_num, CLIENT_START_RESOURCE)


def get_color_unit(unit):
    if isinstance(unit, Company):
        return 'red'
    elif isinstance(unit, Client):
        return 'blue'
    elif isinstance(unit, Product):
        return 'green'
    return 'white'


def get_symbol_unit(unit):
    if isinstance(unit, Company):
        return '*'
    elif isinstance(unit, Client):
        return '$'
    elif isinstance(unit, Product):
        return 'P'
    return '1'


def is_exists(unit, the_map):
    if unit.resource <= 0:
        unit.drop_unit(the_map)
        return False
    return True


def handle_unit_actions(the_map: list):
    for client in MapUnit.existing_units.clients[:]:
        if is_exists(client, the_map):
            client.buy_product(the_map)
    for company in MapUnit.existing_units.companies[:]:
        if is_exists(company, the_map):
            company.do_action(the_map)
    for product in MapUnit.existing_units.products[:]:
        if is_exists(product, the_map):
            product.do_action(the_map)


def check_game_status():
    if len(MapUnit.existing_units.companies) == 0:
        return 'Все компании разорились'
    return None


def clear_objects(the_map: list):
    for unit in MapUnit.existing_units.companies[:]:
        unit.drop_unit(the_map)
    for unit in MapUnit.existing_units.clients[:]:
        unit.drop_unit(the_map)


def get_total_number_units():
    total_companies = len(MapUnit.existing_units.companies)
    total_clients = len(MapUnit.existing_units.clients)
    total_products = len(MapUnit.existing_units.products)
    return total_companies + total_products + total_clients


def get_total_number_units_of_type(unit_type):
    if unit_type == 0:
        return len(MapUnit.existing_units.companies)
    elif unit_type == 1:
        return len(MapUnit.existing_units.products)
    elif unit_type == 2:
        return len(MapUnit.existing_units.clients)


def generate_units(unit_type, the_map, percent, rows, columns):
    total_cells = rows * columns
    total_exist_units = get_total_number_units()

    free_cells = total_cells - total_exist_units
    number_units = free_cells * percent // 100

    created = 0
    while created < number_units:
        row = random.randint(0, rows - 1)
        col = random.randint(0, columns - 1)
        if the_map[row][col].unit is None:
            map_unit = get_unit(unit_type, row, col)
            the_map[row][col].unit = map_unit
            created += 1


# for test
def show_map(the_map):
    for row in range(len(the_map)):
        for col in range(len(the_map[0])):
            unit = the_map[row][col].unit
            if unit is not None:
                print(get_symbol_unit(unit), end=' ')
            else:
                print(0, end=' ')
        print()

def test_game():
    ROWS = 10
    COLUMNS = 10
    MAP = [[Cell() for _ in range(COLUMNS)] for _ in range(ROWS)]

    NUM_COMPANIES = 2
    NUM_PRODUCTS = 0
    NUM_CLIENTS = 6

    #generate_units(NUM_COMPANIES, UNIT_TYPE['Company'])
    #generate_units(UNIT_TYPE['Product'], MAP, 1, ROWS, COLUMNS)
    #generate_units(NUM_CLIENTS, UNIT_TYPE['Client'])

    start_row, start_col = (5, 2)
    product = Product(start_row, start_col, 10, Company(5, 5, 100))
    MAP[start_row][start_col].unit = product
    direction = (0, 5)
    product.set_direction(direction)

    MAP[0][4].unit = Client(0, 4, 10)
    MAP[1][4].unit = Client(1, 4, 10)
    MAP[1][5].unit = Client(1, 5, 10)
    MAP[1][6].unit = Client(1, 6, 10)
    MAP[0][6].unit = Client(0, 6, 10)
    start_position = (1, 2)

    """show_map(MAP)
    print()
    iter = 0
    while iter < 10:
        product.do_action(MAP)
        show_map(MAP)
        print()
        iter += 1"""

    came_from = product._a_star_search(MAP, (product.row, product.col), product.direction, product.resource)

    for row in range(len(MAP)):
        for col in range(len(MAP[0])):
            if (row, col) == (start_row, start_col):
                print('0', end=' ')
            elif (row, col) == product.direction:
                print('X', end=' ')
            elif (row, col) in came_from:
                print('1', end=' ')
            else:
                print('*', end=' ')
        print()

    print(product._reconstruct_path(came_from, (product.row, product.col), product.direction))
    print(came_from)

    # show_map(MAP)

    ITERATIONS = 10
    passed_iter = 0
    """while passed_iter < ITERATIONS:
       if len(MapUnit.existing_units.companies) == 0:
            print('Все компании разорились... Итераций: ', passed_iter)
            break
        for company in MapUnit.existing_units.companies[:]:
            if is_exists(company, MAP):
                company.produce_product(MAP)
                print('*: ', company.resource)
        for product in MapUnit.existing_units.products[:]:
            if is_exists(product, MAP):
                product.move(MAP)
                print('P: ', product.resource)
        for client in MapUnit.existing_units.clients[:]:
            if is_exists(client, MAP):
                client.buy_product(MAP)
                print('$: ', client.resource)
        print()
        passed_iter += 1
        show_map(MAP)"""

    # print(MapUnit.existing_units)


#test_game()
