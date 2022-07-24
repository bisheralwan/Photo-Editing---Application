def get_x_y_lists(points:list) -> list:
    xlist = []
    ylist = []
    for (x,y) in points:
        xlist += [x]
        ylist += [y]
    return [xlist,ylist]

def _take_first(elem: tuple) -> int:
    return elem[0]

def sort_points(points:list) -> list:
    return sorted(points,key=_take_first)

