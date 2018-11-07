from pprint import pprint
import math
from PIL import Image


def distance_formula(p1=[0, 0], p2=[1, 1]) -> float:
    return math.sqrt(
        (math.pow((p2[0] - p1[0]), 2)) + \
        (math.pow((p2[1] - p1[1]), 2))
    )


def number_to_ascii(number):
    if (number <= 1):
        return '@'
    if (number <= 2):
        return '*'
    return '.'


def number_to_RGB(number, max=3):
    return ((abs(number - max) / max) * 255,
            0,
            0)


def transform_coords(coords, origin=[0, 0]) -> [[[]]]:
    ret = []

    for row in coords:
        nr = []
        for p in row:
            nr.append(distance_formula(p, origin))

        ret.append(nr)

    return ret


if __name__ == '__main__':

    width = 101 # do NOT use even numbers ;_;
    height = 101

    coords = [[[x, y] for x in range(-(height// 2), (height//2)+1, 1)]
              for y in range(-(width // 2), (width//2)+1, 1)] # OH GOOD, MATH!!!!! BLBLBLBLBLBLBLBLBLBLBLBLB

    pprint(coords)

    transformed = [[distance_formula(item, [0, 0]) for item in row] for row in coords]
    pprint(transformed)

    asciis = [[number_to_ascii(item) for item in row] for row in transformed]

    print('\n\n')
    for row in asciis:
        print(''.join(row))
    print('\n\n')

    rgbs = []
    for row in transformed:
        for item in row:
            rgbs.append(tuple(int(i) for i in number_to_RGB(item, (width//2)+1)))

    pprint(rgbs)

    im = Image.new('RGB', (width, height))
    im.putdata(rgbs)
    im.save(f'temp-{width}-{height}.jpg')
    im.show()
