

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
 
    user_shape  = input("Shape?: ")

    if user_shape.lower() == "pyramid" or user_shape.lower() == "square" or user_shape.lower() == "triangle" or user_shape.lower() == "rev_triangle" or user_shape.lower() == "rev_pyramid" or user_shape.lower() == "diamond":
        return user_shape.lower()
    else:
        return get_shape()

# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")
    if height.isdigit():
        height = int(height)
        if height < 80 or height > 0:
            return height
        else:
            return get_height()
    else:
        return get_height()


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        n = 0
        for i in range(1,height+1): 
            for j in range (height - i):  #print space
                print(end = " ")    
            while n != (2 * i - 1):       #print stars
                print("*", end = "") 
                n += 1
            n = 0                         #reset to next line
            print()

    if outline == True:
        n = 0
        for i in range(1,height+1): 
            for j in range (height - i):  #print space
                print(end = " ")    
            while n != (2 * i - 1):       #print stars
                if n == 0 or n == (2 * i - 1)-1 or i == height : 
                    print("*", end = "")
                else:
                    print(end = " ")  
                n += 1
            n = 0                         #reset to next line
            print()

# TODO: Step 3
def draw_square(height, outline):
    i =0
    if outline == False:
        while i < height:
            for base in range(height):
                print("*",end='')
            i =i+1
            print()
    elif outline == True:
        while i < height:
            for base in range(height):
                if i ==0 or i ==height-1 or base ==0 or base== height-1:
                    print("*",end='')
                else:
                    print(" ",end='')
            i =i+1
            print()

# TODO: Step 4
def draw_triangle(height, outline):
    i =0
    base =1
    if outline == False:
        while i < height:
            for i in range(base):
                print("*",end='')
            base =base +1
            i =i+1
            print()
    elif outline == True:
        while i < height:
            for k in range(base):
                if i ==0 or i == height-1 or k==0 or k ==base-1:
                    print("*",end='')
                else:
                    print(" ",end='')
            base =base +1
            i =i+1
            print()

def rev_pyramid(height,outline):   
    if outline == False:
        k = 1
        n = 1
        for i in range(height): 
            for j in range (k): 
                print(end = " ") 

            print("*", end = "")
            while n <= (2 * (height - i) -2): 
                if i==0 or n == (2 * (height - i) -2) :
                    print("*", end = "") 
                else:
                    print(end = " ")
                n +=1
            n = 1
            k += 1
            print()
    elif outline == True:
        k = 1
        n = 1
        for i in range(height): 
            for j in range (1, k + 1): 
                print(end = " ") 
            k += 1
            while n <= (2 * (height - i) - 1): 
                print("*", end = "") 
                n +=1
            n = 1
            print()

def rev_triangle(height, outline):   
    if outline == True:
        k = 1
        n = 1
        for i in range(height): 
            for j in range (k): 
                print(end = "") 

            print("*", end = "")
            while n <= (2 * (height - i) -2): 
                if i==0 or n == (2 * (height - i) -2) :
                    print("*", end = "") 
                else:
                    print(end = " ")
                n +=1
            n = 1
            k += 1
            print()
    elif outline == False:
        k = 1
        n = 1
        for i in range(height): 
            for j in range (1, k + 1): 
                print(end = "") 
            k += 1
            while n <= (2 * (height - i) - 1): 
                print("*", end = "") 
                n +=1
            n = 1
            print()

def diamond(height, outline):
    if outline == True:
        n = 0
        height=int(height/2)+1
        for i in range(1,height+1): 
            for j in range (height - i):  #print space
                print(end = " ")    
            while n != (2 * i - 1):       #print stars
                if n == 0 or n == (2 * i - 1)-1 : 
                    print("*", end = "")
                else:
                    print(end = " ")  
                n += 1
            n = 0                         #reset to next line
            print()
    # It was a pyramid up to here.
        k = 1
        n = 1
        for i in range(1, height): 
            for j in range (1, k + 1): 
                print(end = " ") 
            k += 1
            while n <= (2 * (height - i) - 1):
                if n ==1 or n ==(2 * (height - i) - 1): 
                    print("*", end = "")
                else:
                    print(end = " ")
                n +=1
            n = 1
            print()
    if outline == False:
        n = 0
        height=int(height/2)+1
        for i in range(1,height+1): 
            for j in range (height - i):  #print space
                print(end = " ")    
            while n != (2 * i - 1):       #print stars
                print("*", end = "") 
                n += 1
            n = 0                         #reset to next line
            print()
    # It was a pyramid up to here.
        k = 1
        n = 1
        for i in range(1, height): 
            for j in range (1, k + 1): 
                print(end = " ") 
            k += 1
            while n <= (2 * (height - i) - 1): 
                print("*", end = "") 
                n +=1
            n = 1
            print()

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'square':
        draw_square(height, outline)
    elif shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'rev_triangle':
        rev_triangle(height, outline)
    elif shape == 'rev_pyramid':
        rev_pyramid(height, outline)
    elif shape == 'diamond':
        diamond(height, outline)



# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    Parameter   = str(input("Outline only? (y/N):"))
    if Parameter.lower() == 'y':
        return True
    elif Parameter.lower() == 'n' or Parameter.lower() == '':
        return False


if __name__ == "__main__":

    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

