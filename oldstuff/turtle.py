import turtle
def main():
    window = turtle.Screen()
    leon = turtle.Turtle()
    
    make_square(leon)
    turtle.mainloop()

def make_square(leon):
   length = int(input('tamano del cuadrado: '))


  for i in range(4):
    make_line_and_turn(leon, length)

def make_line_and_turn(leon, length):
  leon.forward(length)
  leon.left(90)

if __name__ == '__main__':
  main()