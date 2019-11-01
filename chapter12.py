#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:12:40 2019

@author: timxing
"""

import random


def SetUpEmptyGrid():
    Grid = [[0 for i in range(2)] for i in range(2)]
    return Grid


def RandomlyDistributeCards(Grid):
    for Number in range(1, 3):
        x, y = GetEmptyGridPosition(Grid)
        Grid[x][y] = Number
        x, y = GetEmptyGridPosition(Grid)
        Grid[x][y] = Number
    return Grid


def GetEmptyGridPosition(Grid):
    while True:
        x = random.randint(0,1)
        y = random.randint(0,1)
        if Grid[x][y] == 0:
            break
    return x, y


def SetUpPlayers():
    Points = [0, 0]
    ThisPlayer = 1
    return Points, ThisPlayer


def GetPlayersCoordinates(Grid):
    while True:
        Coordinates1 = input('Input Coordinates(x and y): ').split()
        if Grid[int(Coordinates1[0])][int(Coordinates1[1])] > 0:
            break
    DisplayGrid(int(Coordinates1[0]), int(Coordinates1[1]), Grid)
    while True:
        Coordinates2 = input('Input Coordinates(x and y): ').split()
        if Grid[int(Coordinates2[0])][int(Coordinates2[1])] > 0 and Coordinates1 != Coordinates2:
            break
    return Coordinates1, Coordinates2


def DisplayGrid(x, y, Grid):
    for i in range(2):
        print('')
        for j in range(2):
            if i == x and j == y:
                print(Grid[i][j], end='')
            elif Grid[i][j] == 0:
                print(' ', end='')
            else:
                print('?',end='')


def TestForMatch(x1, y1, x2, y2, Grid, Points, ThisPlayer):
    if Grid[x1][y1] == Grid[x2][y2]:
        Grid[x1][y1] = 0
        Grid[x2][y2] = 0
        Points[ThisPlayer - 1] += 1
    return Points, Grid
    
    
def SwapPlayers(ThisPlayer):
    print('')
    if ThisPlayer == 1:
        print("Player2's turn")
        ThisPlayer = 2
    else:
        print("Player1's turn")
        ThisPlayer = 1
    return ThisPlayer


def TestForEndGame(Points):
    if Points[0] + Points[1] == 2:
        return True
    return False


def OutPutResult(Points):
    print('')
    print('GameOver')
    print('Player1: ', Points[0])
    print('Player2: ', Points[1])
    

def Main():
    Grid = SetUpEmptyGrid()
    Grid = RandomlyDistributeCards(Grid)
    Points, ThisPlayer = SetUpPlayers()
    while True:
        Coordinates1, Coordinates2 = GetPlayersCoordinates(Grid)
        DisplayGrid(int(Coordinates2[0]), int(Coordinates2[1]), Grid)
        Points, Grid = TestForMatch(int(Coordinates1[0]), int(Coordinates1[1]), int(Coordinates2[0]), int(Coordinates2[1]), Grid, Points, ThisPlayer)
        if TestForEndGame(Points):
            return OutPutResult(Points)
        ThisPlayer = SwapPlayers(ThisPlayer)
            



Main()