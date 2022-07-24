from makeFilters import *

def check_equal(description: str, outcome, expected) -> None:
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")

def test_red_channel() -> None:

    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(128, 127, 128))
    set_color(original, 2, 0,  create_color(255, 255, 255))


    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(128, 0, 0))
    set_color(expected, 2, 0,  create_color(255, 0, 0))

    
    test_red_channel=red_channel(original)
    for x, y, color in test_red_channel:
        check_equal('Checking combine pixel ('+ str(x) +', '+ str(y) + ')' , get_color(expected,x,y),color)
        

def test_green_channel() -> None:

    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(128, 127, 128))
    set_color(original, 2, 0,  create_color(255, 255, 255))


    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 127, 0))
    set_color(expected, 2, 0,  create_color(0, 255, 0))


    test_green_channel = green_channel(original)
    for x, y, color in test_green_channel:
        check_equal('Checking combine pixel ('+ str(x) +', '+ str(y) + ')' , get_color(expected,x,y),color)
        
        
def test_blue_channel() -> None:
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(128, 127, 128))
    set_color(original, 2, 0,  create_color(255, 255, 255))


    expected = create_image(3, 1) 
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 128))
    set_color(expected, 2, 0,  create_color(0, 0, 255))


    test_blue_channel = blue_channel(original)
    for x, y, color in test_blue_channel:
        check_equal('Checking combine pixel ('+ str(x) +', '+ str(y) + ')' , get_color(expected,x,y),color)
        

def test_combine() -> None:
    
    red_filter = create_image(6, 1)

    set_color(red_filter , 0, 0, create_color(255, 0, 0))
    set_color(red_filter , 1, 0, create_color(200, 0, 0))
    set_color(red_filter , 2, 0, create_color(14, 0, 0))    
    set_color(red_filter , 3, 0, create_color(25, 0, 0))
    set_color(red_filter , 4, 0, create_color(50, 0, 0))
    set_color(red_filter , 5, 0, create_color(70, 0, 0))     
    
    
    green_filter = create_image(6, 1)
        
    set_color(green_filter, 0, 0, create_color(0, 255, 0))
    set_color(green_filter, 1, 0, create_color(0, 20, 0))
    set_color(green_filter, 2, 0, create_color(0, 100, 0))
    set_color(green_filter, 3, 0, create_color(0, 180, 0))
    set_color(green_filter, 4, 0, create_color(0, 200, 0))
    set_color(green_filter, 5, 0, create_color(0, 55, 0))    
    
    
    
    blue_filter = create_image(6, 1)
        
    set_color(blue_filter , 0, 0, create_color(0, 0, 255))
    set_color(blue_filter , 1, 0, create_color(0, 0, 30))
    set_color(blue_filter , 2, 0, create_color(0, 0, 10))
    set_color(blue_filter , 3, 0, create_color(0, 0, 225))
    set_color(blue_filter , 4, 0, create_color(0, 0, 45))
    set_color(blue_filter , 5, 0, create_color(0, 0, 20))    
    
    
    combine_filter = create_image(6,1)
        
    set_color(combine_filter, 0, 0, create_color(255, 255, 255))
    set_color(combine_filter, 1, 0, create_color(200, 20, 30))
    set_color(combine_filter, 2, 0, create_color(14, 100, 10))
    set_color(combine_filter, 3, 0, create_color(25, 180, 225))
    set_color(combine_filter, 4, 0, create_color(50, 200, 45))
    set_color(combine_filter, 5, 0, create_color(70, 55, 20))    
     
    
    test_combine=combine(red_filter, green_filter, blue_filter)
    for x, y, color in test_combine:
        check_equal('Checking pixel @('+ str(x) +', '+ str(y) + ')' , get_color(combine_filter,x,y),color)
        

def test_three_tone() -> None:

    original = create_image(4, 1)
    set_color(original, 0, 0,  create_color(40,40 ,40 ))
    set_color(original, 1, 0,  create_color(0, 0, 0))
    set_color(original, 2, 0,  create_color(100,100,100))
    set_color(original, 3, 0,  create_color(200, 200, 200))



    expected = create_image(4, 1) 
    set_color(expected, 0, 0,  create_color(0,0,0))
    set_color(expected, 1, 0,  create_color(0,0,0))
    set_color(expected, 2, 0,  create_color(255,255,255))
    set_color(expected, 3, 0,  create_color(0,0,255))


    threetonetest = three_tone(original, "black", "white", "blue")
    for x, y, color in threetonetest:
        print(x,y)
        check_equal('Checking pixel @ ('+ str(x) +', '+ str(y) + ')' , get_color(expected,x,y),color)


def test_extreme_contrast() -> None: 
    
    actual = create_image(6,1)
    set_color(actual, 0, 0,  create_color(0, 0, 0))
    set_color(actual, 1, 0,  create_color(42, 42, 42))
    set_color(actual, 2, 0,  create_color(99, 12, 2))
    set_color(actual, 3, 0,  create_color(135, 235, 0))
    set_color(actual, 4, 0,  create_color(200, 200, 200))
    set_color(actual, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    set_color(expected, 3, 0,  create_color(255, 255, 0))
    set_color(expected, 4, 0,  create_color(255, 255, 255))
    set_color(expected, 5, 0,  create_color(255, 255, 255))
    
    test_extreme = extreme_contrast(actual)
    for x, y, col in test_extreme:
        print(x,y)
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

def test_sepia() -> None:

    original = create_image(4, 1)
    set_color(original, 0, 0,  create_color(10,10,10))
    set_color(original, 1, 0,  create_color(0,0 ,0))
    set_color(original, 2, 0,  create_color(50,50,50))
    set_color(original, 3, 0,  create_color(200,210,200))

    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(10, 10, 10))
    set_color(expected, 1, 0,  create_color(0, 0 ,0))
    set_color(expected, 2, 0,  create_color(50, 50, 50))
    set_color(expected, 3, 0,  create_color(220, 210, 180))




    test_sepia=sepia(original)
    for x, y, color in test_sepia:
        check_equal('Checking pixel @('+ str(x) +', '+ str(y) + ')' , get_color(expected,x,y),color)


def test_posterize() -> None:
    
    actual = create_image(6,1) 
    set_color(actual, 0, 0,  create_color(0, 0, 0))
    set_color(actual, 1, 0,  create_color(42, 42, 42))
    set_color(actual, 2, 0,  create_color(99, 12, 2))
    set_color(actual, 3, 0,  create_color(135, 235, 0))
    set_color(actual, 4, 0,  create_color(200, 200, 200))
    set_color(actual, 5, 0,  create_color(255, 255, 255))
    
    expected = create_image(6, 1) 
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(31, 31, 31))
    set_color(expected, 2, 0,  create_color(95, 31, 31))
    set_color(expected, 3, 0,  create_color(159, 223, 31))
    set_color(expected, 4, 0,  create_color(223, 223, 223))
    set_color(expected, 5, 0,  create_color(223, 223, 223))
    
    posterize_test = posterize(actual)
    for x, y, col in posterize_test:
        print(x,y)
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))


def test_edge_detection() -> None: 

    threshold = 5
    original = create_image(2, 3)
    set_color(original, 0,0,  create_color(123, 234, 199))
    set_color(original, 1,0,  create_color(8, 143, 1))
    set_color(original, 0,1,  create_color(127, 127, 127))
    set_color(original, 1,1,  create_color(125, 73, 224))
    set_color(original, 0,2,  create_color(0, 0, 0))
    set_color(original, 1,2,  create_color(255, 255, 255))

    expected = create_image(2, 3)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 1, 1,  create_color(255, 255, 255))
    set_color(expected, 0, 2,  create_color(0, 0, 0))
    set_color(expected, 1, 2,  create_color(255, 255, 255))

    edge_detection = detect_edges(original, threshold)
    for x, y, color in edge_detection:
        check_equal("Checking pixel @(" + str(x) + ', ' + str(y) + ")", color, get_color(expected, x, y))

def draw_curve_test() -> None:
    
    actual = create_image(5, 3)
    set_color(actual, 0, 0,  create_color(1, 1, 15))
    set_color(actual, 1, 0,  create_color(1, 2, 14))
    set_color(actual, 2, 0,  create_color(1, 3, 13))
    set_color(actual, 3, 0,  create_color(1, 4, 12))
    set_color(actual, 4, 0,  create_color(1, 4, 10))
    set_color(actual, 0, 1,  create_color(1, 6, 10))
    set_color(actual, 1, 1,  create_color(1, 7, 9))
    set_color(actual, 2, 1,  create_color(1, 8, 8))
    set_color(actual, 3, 1,  create_color(1, 9, 7))
    set_color(actual, 4, 1,  create_color(1, 10, 6))
    set_color(actual, 0, 2,  create_color(1, 11, 5))
    set_color(actual, 1, 2,  create_color(1, 12, 4))
    set_color(actual, 2, 2,  create_color(1, 13, 3))
    set_color(actual, 3, 2,  create_color(1, 14, 2))
    set_color(actual, 4, 2,  create_color(1, 15, 1))

        
    expected = create_image(5, 3)
    set_color(expected, 0, 0,  create_color(1, 1, 15))
    set_color(expected, 1, 0,  create_color(1, 2, 14))
    set_color(expected, 2, 0,  create_color(1, 3, 13))
    set_color(expected, 3, 0,  create_color(1, 4, 12))
    set_color(expected, 4, 0,  create_color(1, 4, 10))
    set_color(expected, 4, 1,  create_color(1, 10, 6))
    set_color(expected, 3, 1,  create_color(1, 9, 7))
    set_color(expected,2, 1,  create_color(1, 8, 8))
    set_color(expected, 1, 1,  create_color(1, 7, 9))
    set_color(expected, 0, 1,  create_color(1, 6, 10))
    set_color(expected, 4, 2,  create_color(1, 15, 1))
    set_color(expected, 3, 2,  create_color(1, 14, 2))
    set_color(expected, 2, 2,  create_color(1, 13, 3))
    set_color(expected, 1, 2,  create_color(1, 12, 4))
    set_color(expected, 0, 2,  create_color(1,11, 5))

   
    draw,borders= draw_curve(actual,'cyan',[(110,340),(200,150),(550,20)]) 
    for x, y, col in draw:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
    if borders==[]:
        print("Test Passed")
    else:
        print("Test Failed")
        
def test_horizontal_flip() -> None:
    
    original = create_image(3, 2)
    set_color(original, 0,0,  create_color(123, 234, 199))
    set_color(original, 1,0,  create_color(8, 143, 1))
    set_color(original, 0,1,  create_color(127, 127, 127))
    set_color(original, 1,1,  create_color(125, 73, 224))
    set_color(original, 2,0,  create_color(0, 0, 0))
    set_color(original, 2,1,  create_color(255, 255, 255))

    expected = create_image(3, 2)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(8, 143, 1))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 1, 1,  create_color(125, 73, 224))
    set_color(expected, 2, 0,  create_color(123, 234, 199))
    set_color(expected, 2, 1,  create_color(127, 127, 127))
    
    horizontal = flip_horizontal(original)
    for x, y, col, in horizontal:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))    

def flip_vertical_test() -> None:

    actual = create_image(5, 3)
    set_color(actual, 0, 0,  create_color(1, 1, 15))
    set_color(actual, 1, 0,  create_color(1, 2, 14))
    set_color(actual, 2, 0,  create_color(1, 3, 13))
    set_color(actual, 3, 0,  create_color(1, 4, 12))
    set_color(actual, 4, 0,  create_color(1, 4, 10))
    set_color(actual, 0, 1,  create_color(1, 6, 10))
    set_color(actual, 1, 1,  create_color(1, 7, 9))
    set_color(actual, 2, 1,  create_color(1, 8, 8))
    set_color(actual, 3, 1,  create_color(1, 9, 7))
    set_color(actual, 4, 1,  create_color(1, 10, 6))
    set_color(actual, 0, 2,  create_color(1, 11, 5))
    set_color(actual, 1, 2,  create_color(1, 12, 4))
    set_color(actual, 2, 2,  create_color(1, 13, 3))
    set_color(actual, 3, 2,  create_color(1, 14, 2))
    set_color(actual, 4, 2,  create_color(1, 15, 1))


    expected = create_image(5, 3)
    set_color(expected, 0, 0,  create_color(1, 11, 5))
    set_color(expected, 1, 0,  create_color(1, 12, 4))
    set_color(expected, 2, 0,  create_color(1, 13, 3))
    set_color(expected, 3, 0,  create_color(1, 14, 2))
    set_color(expected, 4, 0,  create_color(1, 15, 1))
    set_color(expected, 4, 1,  create_color(1, 10, 6))
    set_color(expected, 3, 1,  create_color(1, 9, 7))
    set_color(expected,2, 1,  create_color(1, 8, 8))
    set_color(expected, 1, 1,  create_color(1, 7, 9))
    set_color(expected, 0, 1,  create_color(1, 6, 10))
    set_color(expected, 4, 2,  create_color(1, 4, 10))
    set_color(expected, 3, 2,  create_color(1, 4, 12))
    set_color(expected, 2, 2,  create_color(1, 3, 13))
    set_color(expected, 1, 2,  create_color(1, 2, 14))
    set_color(expected, 0, 2,  create_color(1,1, 15))


    vertical = vertical_flip(actual)
    for x, y, col, in vertical:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))



#Main Script

test_red_channel()
test_green_channel()
test_blue_channel()
test_combine()
test_three_tone()
test_extreme_contrast()
test_sepia()
test_posterize()
test_edge_detection()
draw_curve_test() 
test_horizontal_flip()
flip_vertical_test()