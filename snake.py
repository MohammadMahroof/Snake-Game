from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):        #start from the last segment 
            new_x = self.segments[seg_num - 1].xcor()               #Tail -> follows body
            new_y = self.segments[seg_num - 1].ycor()               #Body -> follows head
                                                                #Head -> moves forward

            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        