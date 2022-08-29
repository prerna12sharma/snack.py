from turtle import Turtle
starting=[(0,0),(-20,0),(-40,0)]
moving_distance=20
up=90
down=270
left=100
right=0

class snake:
    def _init_(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        
    def create_snake(self):
        for position in starting:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.got(position)
    
    def extend(self):
        self.add_segment(self.segment[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segmnet)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(moving_distance)
        
    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
            
    def  down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
            
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
            
            