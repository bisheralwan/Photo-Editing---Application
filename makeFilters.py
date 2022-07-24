from ImageOptions import *
from xyPoints import *
from numpy import polyfit, polyval


def red_channel(image: Image) -> Image:
    new_image = copy(image)

    for x, y, (r, g, b) in image:
        red = create_color(r, 0, 0)
        set_color(new_image, x, y, red)
    return new_image


def green_channel(image: Image) -> Image:
    new_image = copy(image)

    for x, y, (r, g, b) in image:
        green = create_color(0, g, 0)
        set_color(new_image, x, y, green)
    return new_image


def blue_channel(image: Image) -> Image:
    new_image = copy(image)

    for x, y, (r, g, b) in image:
        blue = create_color(0, 0, b)
        set_color(new_image, x, y, blue)
    return new_image


def combine(red_img: Image, green_img: Image, blue_img: Image) -> Image:

    new_image = copy(red_img)

    for x, y, (r, g, b) in new_image:
        r1, g1, b1 = get_color(green_img, x, y)
        r2, g2, b2 = get_color(blue_img, x, y)
        set_color(new_image, x, y, create_color(r, g1, b2))

    return new_image


def three_tone(image: Image, color1: str, color2: str, color3: str) -> Image:
    newimage = copy(image)

    colors = [("black", (0, 0, 0)), ("white", (255, 255, 255)), ("red", (255, 0, 0)),
              ("lime", (0, 255, 0)), ("blue", (0, 0, 255)), ("yellow", (255, 255, 0)),
              ("cyan", (0, 255, 255)), ("magenta", (255, 0, 255)), ("grey", (128, 128, 128))]

    c1 = c2 = c3 = 0
    for i in colors:
        if color1 == i[0]:
            c1 = create_color(i[1][0], i[1][1], i[1][2])
        elif color2 == i[0]:
                c2 = create_color(i[1][0], i[1][1], i[1][2])
        elif color3 == i[0]:
            c3 = create_color(i[1][0], i[1][1], i[1][2])

    if c1 == 0 or c2 == 0 or c3 == 0:
        print("invalid color")
        return None

    for x, y, (r, g, b) in image:
        avg = (r + g + b) / 3
        if avg <= 84:
            set_color(newimage, x, y, c1)
        elif 85 < avg <= 170:
            set_color(newimage, x, y, c2)
        else:
            set_color(newimage, x, y, c3)

    return newimage


def extreme_contrast(image: Image) -> Image:
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:

        if r < 127:
            r = 0
        else:
            r = 255

        if g < 127:
            g = 0
        else:
            g = 255

        if b < 127:
            b = 0
        else:
            b = 255

        extreme_filter = create_color(r, g, b)
        set_color(new_image, x, y, extreme_filter)
    return new_image


def sepia(image: Image) -> Image:
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
    x = get_width(new_image)
    y = get_height(new_image)

    for h in range(x):
        for v in range(y):
            c = get_color(image, h, v)
            r, g, b = c
            if r > 63:
                SR = r * 1.1
                SB = b * 0.9

            elif 63 <= r <= 191:
                SR = r * 1.15
                SB = b * 0.85

            elif r > 191:
                SR = r * 1.08
                SB = b * 0.93

    SepiaChange = create_color(SR, g, SB)
    set_color(new_image, h, v, SepiaChange)

    return new_image


def _adjust_component(col: int) -> int:

    if 0 <= col <= 63:
        col = 31
    elif 64 <= col <= 127:
        col = 95
    elif 128 <= col <= 191:
        col = 159
    else:
        col = 223
    return col


def posterize(image: Image) -> Image:
    new_image = copy(image)

    for x, y, (r, g, b) in new_image:
        r1, g1, b1 = _adjust_component(r), _adjust_component(g), _adjust_component(b)
        posterize_filter = create_color(r1, g1, b1)
        set_color(new_image, x, y, posterize_filter)
    return new_image


def detect_edges(image: Image, threshold: int) -> Image:
    edge_detect = copy(image)
    height = get_height(image)

    for pixel in edge_detect:
        x, y, (r, g, b) = pixel

        if y < height - 1:
            b1 = (r + g + b) / 3
            rgb = get_color(edge_detect, x, y + 1)
            red, green, blue = rgb
            b2 = (red + green + blue) / 3
            new_contrast = b1 - b2

            if new_contrast > threshold:
                black = create_color(0, 0, 0)
                set_color(edge_detect, x, y, black)

            elif new_contrast < threshold:
                white = create_color(255, 255, 255)
                set_color(edge_detect, x, y, white)
    return edge_detect


def draw_curve(image: Image, colour: str, pointlist: list = None) -> (Image, list):
    colour_codes = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0),
                    (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                    (128, 128, 128)]

    colour_names = ["black", "white", "blood", "lime", "blue", "yellow",
                    "cyan", "magenta", "gray"]

    for i in range(len(colour_names)):
        if colour == colour_names[i]:
            c = colour_codes[i]
            rgb = create_color(c[0], c[1], c[2])

    pixel_x = get_width(image)
    pixel_y = get_height(image)
    image_size = [pixel_x, pixel_y]

    if pointlist == None:
        print("Your Photo is", pixel_x, "by", pixel_y)

        pointlist = []

    pointlist = sort_points(pointlist)
    interpoly = _interpolation(pointlist)
    borders = _image_border_finding(image_size, interpoly)

    new_image = copy(image)
    for x in range(0, pixel_x):
        y_1 = round(polyval(interpoly, x))
        for y in range(y_1 - 2, y_1 + 3):
            if 0 <= y < pixel_y:
                set_color(new_image, x, y, rgb)

    return new_image, borders


def _interpolation(lst: list):
    xy_list = get_x_y_lists(lst)
    x_coordinate = xy_list[0]
    y_coordinate = xy_list[1]

    if len(lst) <= 2:
        interpoly = polyfit(x_coordinate, y_coordinate, 1)
        return interpoly

    else:
        interpoly = polyfit(x_coordinate, y_coordinate, 2)

        return interpoly


def _image_border_finding(size: list, polynom: list) -> list:
    coordinates = []

    max_pixelx = size[0] - 1
    max_pixely = size[1] - 1

    w = _exhaustive_search(max_pixelx, polynom, 0)
    h = _exhaustive_search(max_pixely, polynom, size[1] - 1)

    if w != None:
        coordinates.append((w, 0))
        return coordinates
    if h != None:
        coordinates.append((h, max_pixely))
        return coordinates
    if 0 < polyval(polynom, max_pixelx) <= max_pixely:
        coordinates.append((max_pixelx, polyval(polynom, max_pixelx)))

    if 0 < polyval(polynom, 0) <= max_pixely:
        coordinates.append((0, polyval(polynom, 0)))

    return coordinates


def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
    EPSILON = 1
    i = EPSILON ** 2
    estimate = 0

    while estimate <= max_x:
        estimate += i
        if estimate > max_x:
            return None
        elif abs(polyval(polycoeff, estimate) - val) <= EPSILON:
            return estimate


def flip_horizontal(image: Image) -> Image:
    new_image = copy(image)
    H = get_height(image)
    W = get_width(image)

    for y in range(H):
        for x in range(W // 2):
            L = get_color(image, x, y)
            R = get_color(image, W - 1 - x, y)
            set_color(new_image, x, y, R)
            set_color(new_image, W - 1 - x, y, L)
    return new_image


def vertical_flip(image: Image) -> Image:
    new_image = copy(image)
    H = get_height(image)
    W = get_width(image)

    for y in range(H // 2):
        for x in range(W):
            left_side = get_color(image, x, H - 1 - y)
            right_side = get_color(image, x, y)
            set_color(new_image, x, H - 1 - y, right_side)
            set_color(new_image, x, y, left_side)
    return new_image


"""image = load_image('riveter.jpg')
file1 = ("riveter.jpg")

show(red_channel(image))

show(green_channel(image))

show(blue_channel(image))

red_img = load_image('red_image.png')
green_img = load_image('green_image.png')
blue_img = load_image('blue_image.png')
show(combine(red_img, green_img, blue_img))

show(three_tone(image, "black", "blue", "white"))

show(extreme_contrast(image))

show(sepia(image))

show(posterize(image))

show(detect_edges(image, 5))

new_image,borders=draw_curve(load_image(file1),"cyan",[(145,28),(189,70),(4,20)])
show(new_image)
print(borders)

show(flip_horizontal(image))

show(vertical_flip(image))
"""
