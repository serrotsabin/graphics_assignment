from tkinter import *
from math import *


class MatrixHelpers:
  def transpose_matrix(self, matrix):
    return list(zip(*matrix))

  def translate_vector(self, x, y, dx, dy):
    return x + dx, y + dy

  def matrix_multiply(self, matrix_a, matrix_b):
    zip_b = list(zip(*matrix_b))
    return [[
        sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
        for col_b in zip_b
    ] for row_a in matrix_a]

  def rotate_along_x(self, x, shape):
    return self.matrix_multiply(
        [[1, 0, 0], [0, cos(x), -sin(x)], [0, sin(x), cos(x)]], shape)

  def rotate_along_y(self, y, shape):
    return self.matrix_multiply(
        [[cos(y), 0, sin(y)], [0, 1, 0], [-sin(y), 0, cos(y)]], shape)

  def rotate_along_z(self, z, shape):
    return self.matrix_multiply(
        [[cos(z), sin(z), 0], [-sin(z), cos(z), 0], [0, 0, 1]], shape)


class Cube(MatrixHelpers):

  last_x = 0
  last_y = 0

  def __init__(self, root):
    self.root = root
    self.init_data()
    self.create_canvas()
    self.create_frame()
    self.create_control()
    self.epsilon = lambda d: d * 0.01

  def init_data(self):
    self.cube = self.transpose_matrix([[-100, -100, -100],
                                       [-100,  100, -100],
                                       [-100, -100,  100],
                                       [-100,  100,  100],
                                       [ 100, -100, -100],
                                       [ 100,  100, -100],
                                       [ 100, -100,  100],
                                       [ 100,  100,  100]])

  def create_canvas(self):
    self.canvas = Canvas(
        self.root, width=400, height=400)
    self.canvas.pack(fill=BOTH, expand=YES)

  def create_frame(self):
    self.frame = Frame(
        self.root, width=400, height=400)
    self.frame.pack(fill=BOTH, expand=YES)

  def create_control(self):
    self.rotX = Button(self.frame,text="Draw",command=self.rotaX)
    self.rotX.pack()
    self.rotX = Button(self.frame,text="Rotate along X",command=self.rotaX)
    self.rotX.pack()
    self.rotY = Button(self.frame,text="Rotate along Y",command=self.rotaY)
    self.rotY.pack()

  def draw_cube(self):
    cube_points = [[0, 1, 2, 4],
                   [3, 1, 2, 7],
                   [5, 1, 4, 7],
                   [6, 2, 4, 7]]
    
    w = self.canvas.winfo_width() / 2
    h = self.canvas.winfo_height() / 2
    self.canvas.delete(ALL)
    for i in cube_points:
      for j in i:
        self.canvas.create_line(self.translate_vector(self.cube[0][i[0]], self.cube[1][i[0]], w, h),
                                self.translate_vector(self.cube[0][j], self.cube[1][j], w, h))
        self.canvas.create_text(self.translate_vector(self.cube[0][i[0]],
                                                      self.cube[1][i[0]], w, h),
                                                      text=str("{0:.2f}".format(self.cube[0][i[0]]))
                                                         + " , "
                                                         + str("{0:.2f}".format(self.cube[1][i[0]]))
                                                         + " , "
                                                         + str("{0:.2f}".format(self.cube[2][i[0]])))
        self.canvas.create_text(self.translate_vector(self.cube[0][j],
                                                      self.cube[1][j], w, h),
                                                      text=str("{0:.2f}".format(self.cube[0][j]))
                                                         + " , "
                                                         + str("{0:.2f}".format(self.cube[1][j]))
                                                         + " , "
                                                         + str("{0:.2f}".format(self.cube[2][j])))



  def rotaX(self):
      self.cube = self.rotate_along_x(self.epsilon(5), self.cube)
      self.draw_cube()

  def draw(self):
      self.cube = self.rotate_along_x(0, self.cube)
      self.draw_cube()


  def rotaY(self):
      self.cube = self.rotate_along_y(self.epsilon(5), self.cube)
      self.draw_cube()

def main():
  root = Tk()
  Cube(root)
  root.mainloop()


if __name__ == '__main__':
  main()
