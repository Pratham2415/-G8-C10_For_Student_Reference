import turtle
speed=[10,20,30,40,50]
colors=["orange","red","green","blue","yellow"]
def draw_star(c,s,size,x,y):
    for i in c:
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.fillcolor(#Make the speed change by using speed elements)
        turtle.begin_fill()
        #Pop the last color
        #Append the color cyan into the colors list
        for i in range(5):
            turtle.fd(#Make the turtle move in the forward direction by size variable)
            turtle.right(144)
            turtle.speed(#Make the speed change by using speed elements)
        turtle.end_fill()
        turtle.ht()
#Call the function 5 times by using parameters
#Pass the parameters as ==> colors,speed,10,0,20
#Pass the parameters as ==> colors,speed,30,15,30
#Pass the parameters as ==> colors,speed,40,50,40
#Pass the parameters as ==> colors,speed,50,100,50
#Pass the parameters as ==> colors,speed,70,160,70