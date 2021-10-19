# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from pygame.cursors import load_xbm
from pygame.display import update
from maze_generate import Node
import maze_generate
import pygame
import sys
import time
#from data_structure import heap, FIFO, FILO, priority_queue, Manhattan_Distance, Euclidean_distance
from algorithm import Dijkstra, DFS, IDS, Astar, BFS

import os
import constants



class Main_Menu(object):
    def __init__(self):
        self.maze_sim = None
        self.selected_alg = "DFS"
        self.maze = None
        self.cur_step = 0
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 291)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 270, 61, 16))
        self.label.setObjectName("label")
        self.statusLabel = QtWidgets.QLabel(Dialog)
        self.statusLabel.setGeometry(QtCore.QRect(80, 270, 300, 16))
        self.statusLabel.setObjectName("statusLabel")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 71))
        self.groupBox.setObjectName("groupBox")
        self.showMazeBtn = QtWidgets.QPushButton(self.groupBox)
        self.showMazeBtn.setGeometry(QtCore.QRect(280, 30, 75, 23))
        self.showMazeBtn.setObjectName("showMazeBtn")
        self.fileTextBox = QtWidgets.QLineEdit(self.groupBox)
        self.fileTextBox.setGeometry(QtCore.QRect(70, 30, 113, 20))
        self.fileTextBox.setObjectName("fileTextBox")
        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label1.setObjectName("label1")
        self.loadBtn = QtWidgets.QPushButton(self.groupBox)
        self.loadBtn.setGeometry(QtCore.QRect(200, 30, 75, 23))
        self.loadBtn.setObjectName("loadBtn")
        self.algGroupBox = QtWidgets.QGroupBox(Dialog)
        self.algGroupBox.setGeometry(QtCore.QRect(10, 90, 391, 51))
        self.algGroupBox.setObjectName("algGroupBox")
        self.algorithmCboBox = QtWidgets.QComboBox(self.algGroupBox)
        self.algorithmCboBox.setGeometry(QtCore.QRect(20, 20, 111, 22))
        self.algorithmCboBox.setObjectName("algorithmCboBox")
        self.solveBtn = QtWidgets.QPushButton(self.algGroupBox)
        self.solveBtn.setGeometry(QtCore.QRect(150, 20, 75, 23))
        self.solveBtn.setObjectName("solveBtn")
        self.solveTimeLbl = QtWidgets.QLabel(self.algGroupBox)
        self.solveTimeLbl.setGeometry(QtCore.QRect(240, 20, 141, 16))
        self.solveTimeLbl.setObjectName("solveTimeLbl")
        self.ctrl_groupBox = QtWidgets.QGroupBox(Dialog)
        self.ctrl_groupBox.setGeometry(QtCore.QRect(10, 140, 391, 111))
        self.ctrl_groupBox.setObjectName("ctrl_groupBox")
        self.startAnimationBtn = QtWidgets.QPushButton(self.ctrl_groupBox)
        self.startAnimationBtn.setGeometry(QtCore.QRect(10, 30, 101, 21))
        self.startAnimationBtn.setObjectName("startAnimationBtn")
        self.stepLeftBtn = QtWidgets.QPushButton(self.ctrl_groupBox)
        self.stepLeftBtn.setGeometry(QtCore.QRect(130, 30, 101, 21))
        self.stepLeftBtn.setObjectName("stepLeftBtn")
        self.stepRightBtn = QtWidgets.QPushButton(self.ctrl_groupBox)
        self.stepRightBtn.setGeometry(QtCore.QRect(250, 30, 91, 21))
        self.stepRightBtn.setObjectName("stepRightBtn")
        self.speedSlider = QtWidgets.QSlider(self.ctrl_groupBox)
        self.speedSlider.setGeometry(QtCore.QRect(100, 80, 160, 22))
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(100)
        self.speedSlider.setProperty("value", 4)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setObjectName("speedSlider")
        self.labelSpeed = QtWidgets.QLabel(self.ctrl_groupBox)
        self.labelSpeed.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.labelSpeed.setObjectName("labelSpeed")
        self.sliderLbl = QtWidgets.QLabel(self.ctrl_groupBox)
        self.sliderLbl.setGeometry(QtCore.QRect(270, 80, 71, 16))
        self.sliderLbl.setObjectName("sliderLbl")
        #hide buttons until file is loaded
        self.showMazeBtn.hide()
        self.algGroupBox.hide()
        self.ctrl_groupBox.hide()

        self.timer=QTimer()
        self.timer.timeout.connect(self.stepRightBtn_click)

        #add algorithms to alg combo box
        self.algorithmCboBox.addItems(["BFS", "Dijkstras", "DFS", "IDS", "A*"])
        self.algorithmCboBox.currentIndex = 0
        self.algorithmCboBox.currentIndexChanged.connect(self.algorithmSelection_change)



        self.showMazeBtn.clicked.connect(self.showMazeBtn_click)
        self.loadBtn.clicked.connect(self.loadBtn_click)
        self.startAnimationBtn.clicked.connect(self.startBtn_click)
        self.stepLeftBtn.clicked.connect(self.stepLeftBtn_click)
        self.stepRightBtn.clicked.connect(self.stepRightBtn_click)
        self.solveBtn.clicked.connect(self.solveBtn_click)
        self.speedSlider.valueChanged.connect(self.speed_slider_change)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Maze Project"))
        self.label.setText(_translate("Dialog", "Status:"))
        self.statusLabel.setText(_translate("Dialog", "Waiting File Load"))
        self.groupBox.setTitle(_translate("Dialog", "File Select"))
        self.showMazeBtn.setText(_translate("Dialog", "Show Maze"))
        self.label1.setText(_translate("Dialog", "File Name:"))
        self.loadBtn.setText(_translate("Dialog", "Load"))
        self.algGroupBox.setTitle(_translate("Dialog", "Algorithm Selection"))
        self.solveBtn.setText(_translate("Dialog", "Solve"))
        self.solveTimeLbl.setText(_translate("Dialog", "Solve Time: "))
        self.ctrl_groupBox.setTitle(_translate("Dialog", "Animation Controls"))
        self.startAnimationBtn.setText(_translate("Dialog", "Start Animation"))
        self.stepLeftBtn.setText(_translate("Dialog", "Step Left"))
        self.stepRightBtn.setText(_translate("Dialog", "Step Right"))
        self.labelSpeed.setText(_translate("Dialog", "Animation Speed:"))
        self.sliderLbl.setText(_translate("Dialog", "3 Steps/Sec"))

    def display_file_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Please enter a filename that is stored in the mazes folder.')
        msg.setWindowTitle("Error")
        msg.exec_()

    def display_file_success(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("File Load Sucessful")
        msg.setWindowTitle("Success")
        msg.exec_()


    def loadBtn_click(self):
        filename = self.fileTextBox.text() # get the filename input from the text box
        if not os.path.exists(os.path.join("mazes", filename)) or not filename:
            self.display_file_error()
        else:
            self.display_file_success()
            self.statusLabel.setText("File Loaded...")
            self.showMazeBtn.show()

    def showMazeBtn_click(self):
        self.algGroupBox.show()
        self.maze_sim = Maze_Sim(os.path.join("mazes", self.fileTextBox.text()))
        self.maze_sim.main()
        self.statusLabel.setText("Maze has been drawn...")

    def speed_slider_change(self):
        self.sliderLbl.setText(str(self.speedSlider.value()) + "Steps/Sec")
        if self.startAnimationBtn.text() == "Stop Animation":
            update_time = 1000 / self.speedSlider.value()
            self.timer.start(update_time)

    
    def solveBtn_click(self):
        self.timer.stop()
        self.startAnimationBtn.setText("Start Animation")
        self.maze = maze_generate.maze(os.path.join("mazes", self.fileTextBox.text()))
        current_time = round(time.time() * 1000)  #get current time in millis
        self.get_alg_result() # get the result of the algorithm, saves to self.closed_set
        elapsed_time = round(time.time() * 1000) - current_time
        self.solveTimeLbl.setText("Solve Time: " + str(elapsed_time / 1000.0) + " sec")
        self.ctrl_groupBox.show()
        self.statusLabel.setText("Algorithm Solved using " + self.selected_alg)
        self.maze_sim.closed_set = self.closed_set # pass the solved set to the GUI for animations
        self.cur_step = 0
        self.maze_sim.reset()
        
            

    def algorithmSelection_change(self):
        self.selected_alg = self.algorithmCboBox.currentText()

    def startBtn_click(self):
        if self.startAnimationBtn.text() == "Start Animation":
            update_time = 1000 / self.speedSlider.value()
            self.timer.start(update_time)
            self.startAnimationBtn.setText("Stop Animation")
        else:
            self.timer.stop()
            self.startAnimationBtn.setText("Start Animation")


    def update_solve_status(self):
        if self.cur_step == len(self.closed_set):
            self.statusLabel.setText("Target found; Reachable in "+ str(len(self.closed_set)) + " steps.")

        else:
            self.statusLabel.setText("Not found: Step " + str(self.cur_step) + "/" + str(len(self.closed_set)))
    
    def stepLeftBtn_click(self):
        if self.cur_step > 0:
            self.cur_step -= 1
            self.maze_sim.step(-1)
            self.update_solve_status()
            
    
    def stepRightBtn_click(self):
        if self.cur_step < len(self.closed_set):
            self.cur_step += 1
            self.maze_sim.step(1)
            self.update_solve_status()

    def get_alg_result(self):
        if self.selected_alg == "BFS":
            self.closed_set = BFS(self.maze)
            print("BFS")
        elif self.selected_alg == "Dijkstras":
            self.closed_set = Dijkstra(self.maze)
            print("Dijkstras")
        elif self.selected_alg == "DFS":
            self.closed_set = DFS(self.maze)
            print("DFS")
        elif self.selected_alg == "IDS":
            self.closed_set = IDS(self.maze)
            print("IDS")
        elif self.selected_alg == "A*":
            self.closed_set = Astar(self.maze)
            print("A*")
    
    
    

            
class Maze_Sim(object):
    def __init__(self, file_path):
        self.maze = maze_generate.maze(file_path)


        self.NUMBER_OF_BLOCKS_WIDE = len(self.maze.maze[0])
        self.NUMBER_OF_BLOCKS_HIGH = len(self.maze.maze)
        self.BLOCK_HEIGHT = round((constants.SCREEN_HEIGHT)/self.NUMBER_OF_BLOCKS_HIGH)
        self.BLOCK_WIDTH = round((constants.SCREEN_WIDTH)/self.NUMBER_OF_BLOCKS_WIDE)
        self.surface = None
        self.cur_step = 0
        self.closed_set = None

    def initialize_gui(self):
        pygame.init()
        surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Maze solver")
        surface.fill(constants.WHITE)
        return surface


    def reset(self):
        self.cur_step = 0
        self.main()
        self.maze.reset()



    def draw_maze(self,surface, maze):
        for i in range(len(maze.maze)):
            for j in range(len(maze.maze[0])):
                maze_node = pygame.Rect(j * self.BLOCK_WIDTH, i * self.BLOCK_HEIGHT, self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
                pygame.draw.rect(surface, self.get_node_color(maze.maze[i][j]), maze_node)





    def step(self, step_num):
        # step_num == -1 = step left, 1 = step right
        if self.cur_step + step_num >= 0 and self.cur_step + step_num <= len(self.closed_set): #make sure we are not out of bounds
            cur_node = self.closed_set[self.cur_step]
            color = None
            if step_num == 1:
                color = constants.GREEN
            else:
                color = constants.WHITE

            path_node = pygame.Rect(cur_node.y * self.BLOCK_WIDTH, cur_node.x * self.BLOCK_HEIGHT, self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
            pygame.draw.rect(self.surface, color, path_node)
            self.draw_grid(self.surface, self.maze)
            pygame.display.update()
            self.cur_step += step_num
        
    def start_animation(self, selected_alg):
        

        for node in self.closed_set:
            path_node = pygame.Rect(node.y * self.BLOCK_WIDTH, node.x * self.BLOCK_HEIGHT, self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
            pygame.draw.rect(self.surface, constants.GREEN, path_node)
            pygame.display.update()
            time.sleep(0.1)
        self.maze.reset()
        self.draw_maze(self.surface, self.maze)

    def get_alg_result(self, selected_alg):
        closed_set = None
        if selected_alg == "BFS":
            closed_set = BFS(self.maze)
            print("BFS")
        elif selected_alg == "Dijkstras":
            closed_set = Dijkstra(self.maze)
            print("Dijkstras")
        elif selected_alg == "DFS":
            closed_set = DFS(self.maze)
            print("DFS")
        elif selected_alg == "IDS":
            closed_set = IDS(self.maze)
            print("IDS")
        elif selected_alg == "A*":
            closed_set = Astar(self.maze)
            print("A*")
        return closed_set
            



    def get_node_color(self,node: Node):
        tile_color = constants.BLACK
        if node.nodetype == "open":
            tile_color = constants.WHITE
        elif node.nodetype == "start":
            tile_color = constants.ORANGE
        elif node.nodetype == "end":
            tile_color = constants.GREEN
        return tile_color


    def show_maze(self,surface,maze):
        self.initialize_gui()
        pygame.draw.rect(surface, constants.GREEN, (constants.SCREEN_WIDTH, 0 ,50,50))
        self.draw_maze(surface, maze)
        self.draw_grid(surface, maze)
        pygame.display.update()



    def draw_grid(self,surface, maze):
        for i in range(len(maze.maze[0])):
            new_height = round(i * self.BLOCK_HEIGHT)
            new_width = round(i * self.BLOCK_WIDTH)
            pygame.draw.line(surface, constants.BLACK, (0, new_height), (round(constants.SCREEN_WIDTH), new_height), 1)
            pygame.draw.line(surface, constants.BLACK, (new_width, 0), (new_width, constants.SCREEN_HEIGHT), 1)


    def main(self):
        self.surface = self.initialize_gui()
        self.show_maze(self.surface,self.maze)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Main_Menu()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

