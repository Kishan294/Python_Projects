# import colorgram
import random
import turtle as t
# rgb_colors = []
# colors = colorgram.extract('Image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.forward(350)
tim.pendown()
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()
    tim.dot(20, random.choice(color_list))

    if dot_count%10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()

screen = t.Screen()
screen.exitonclick()