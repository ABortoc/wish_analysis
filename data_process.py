import pytesseract
from PIL import Image, ImageEnhance
import re
import itertools
import graph_create as gc
import spreadsheet_create as sc

_four_star = []
_five_star = {}

# Images modified using threshold, so far 200 seems to work best.


def image_color_change(path):
    img = Image.open(f"{path}")
    img = img.point(lambda x: x > 200 and 255)
    img.save(f"{path}")


def image_color_process():
    with open('screenshots/screenshots.txt', 'r') as file:
        for elem in file:
            if elem != "":
                image_color_change(elem[:-1])


def image_text_process(path):
    data_str = pytesseract.image_to_string(Image.open(f'{path}'))
    data_list = re.findall(
        r'(?!Item|Type|Name|[0-9]|Time|Received|Weapon|Character)(\b\w.+\b\)|\b\w.+\b)', data_str)
    return data_list[::-1]


def image_batch_process(path):
    with open(f'{path}', 'r') as file:
        items = []
        for elem in file:
            if elem != "":
                items.append(image_text_process(elem[:-1]))
        return list(itertools.chain.from_iterable(items))


def dict_pity_create(lst):
    pity_four = {}
    for elem in lst:
        keys = pity_four.keys()
        if elem in keys:
            continue
        else:
            pity_four[elem] = lst.count(elem)
    return pity_four


def wish_data_process():
    image_color_process()
    wish_list = image_batch_process('screenshots/screenshots.txt')
    counter_four = 0
    counter_five = 0
    for elem in wish_list:
        counter_four += 1
        counter_five += 1
        if "4-Star" in elem:
            _four_star.append(counter_four)
            counter_four = 0
        elif "5-Star" in elem:
            _five_star[elem] = counter_five
            counter_five = 0
            counter_four = 0


def bar_graph_four_create():
    temp_dict = dict_pity_create(_four_star)
    sc.spreadsheet_create(4, temp_dict)
    gc.graph_create(temp_dict)


def bar_graph_five_create():
    sc.spreadsheet_create(5, _five_star)
    gc.graph_create(_five_star)
