#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:31:27 2020

@author: clementmutez
"""



'''Fait par Clément Mutez et Noel Nakhle'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model



def SolveSimpleSudoku4(matrice):
    #Create the model
    model=cp_model.CpModel()
    
    ######## Create the variable #########
    entier = 0
    for colonne in range(0,4):
       for ligne in range(0,4):
           # Si il y a un 0, on créer une variable int du model compris 
           # entre 1 et 4
           if matrice[colonne][ligne] == 0:
               matrice[colonne][ligne] = model.NewIntVar(1, 4, '')
           # Sinon on créer une variable int du model égale a la valeur de la
           # matrice (ici on appel cette valeur entier)
           else:
               entier = matrice[colonne][ligne]
               matrice[colonne][ligne] = model.NewIntVar(entier, entier, '')
           
    
    ####### Define the constraint #######
    #contrainte de colonne:
    listetemp =[]
    #on place toutes les valeurs d'une colonne dans une liste
    #on repete l'operation pour toutes les colonnes
    for colonne in range(0,4):
        for ligne in range (0,4):
            listetemp.append(matrice[colonne][ligne])
        #cette fonction permet de dire :tous les élements de la liste doivent
        #etre different
        model.AddAllDifferent(listetemp)
        listetemp.clear()
        
    #contrainte de ligne:
    #pareil que colonnes mais version ligne
    listetemp =[]
    for ligne in range (0,4):
        for colonne in range (0,4):
            listetemp.append(matrice[colonne][ligne])
        model.AddAllDifferent(listetemp)
        listetemp.clear()
    
    #contrainte carré:
    listetemp1 =[]
    listetemp2 = []
    listetemp3 = []
    listetemp4 = []
    #permet de stocker les 4 differents carrées dans une liste chacun
    j = 0
    for i in range (0,4):
        if (i < 2 ):
            listetemp1.append(matrice[i][j])
            listetemp1.append(matrice[i][j+1])
            listetemp4.append(matrice[i][j+2])
            listetemp4.append(matrice[i][j+3])
        else:
            listetemp2.append(matrice[i][j])
            listetemp2.append(matrice[i][j+1])
            listetemp3.append(matrice[i][j+2])
            listetemp3.append(matrice[i][j+3])
    model.AddAllDifferent(listetemp1)
    model.AddAllDifferent(listetemp2)
    model.AddAllDifferent(listetemp3)
    model.AddAllDifferent(listetemp4)
    
    
    ######## Call the sover #########
    solver=cp_model.CpSolver()
    status=solver.Solve(model)
    ####### Display first solution #####
    if status == cp_model.FEASIBLE:
        #on affiche le resultat
        print('Matrice solution : \n')
        colonne = 0
        for ligne in range(0,4):
            print(solver.Value(matrice[colonne][ligne]), 
                  solver.Value(matrice[colonne+1][ligne]), 
                  solver.Value(matrice[colonne+2][ligne]), 
                  solver.Value(matrice[colonne+3][ligne]))
    print()

def SolveSimpleSudoku(matrice):
    #Create the model
    model=cp_model.CpModel()
    
    ######## Create the variable #########
    entier = 0
    for colonne in range(0,9):
       for ligne in range(0,9):
           # Si il y a un 0, on créer une variable int du model compris 
           # entre 1 et 9
           if matrice[colonne][ligne] == 0:
               matrice[colonne][ligne] = model.NewIntVar(1, 9, '')
           # Sinon on créer une variable int du model égale a la valeur de la
           # matrice (ici on appel cette valeur entier)
           else:
               entier = matrice[colonne][ligne]
               matrice[colonne][ligne] = model.NewIntVar(entier, entier, '')
               
    ####### Define the constraint #######
    #contrainte de colonne:
    listetemp =[]
    #on place toutes les valeurs d'une colonne dans une liste
    #on repete l'operation pour toutes les colonnes
    for colonne in range(0,9):
        for ligne in range (0,9):
            listetemp.append(matrice[colonne][ligne])
        model.AddAllDifferent(listetemp)
        listetemp.clear()
        
    #contrainte de ligne:
    #pareil que colonnes mais version ligne
    listetemp =[]
    for ligne in range (0,9):
        for colonne in range (0,9):
            listetemp.append(matrice[colonne][ligne])
        model.AddAllDifferent(listetemp)
        listetemp.clear()
    
    #contrainte carré:
    #on creer une liste de liste qui stockera les élements d'un carré
    #que devront etre différents
    listetemp =[[],[],[],[],[],[],[],[],[]]
    j = 0
    compteur = 0
    for i in range (0,9):
        if (i < 3):
            compteur = 0
        elif (i < 6):
            compteur = 3
        else:
            compteur = 6
        listetemp[compteur].append(matrice[i][j])
        listetemp[compteur].append(matrice[i][j+1])
        listetemp[compteur].append(matrice[i][j+2])
        
        listetemp[compteur+1].append(matrice[i][j+3])
        listetemp[compteur+1].append(matrice[i][j+4])
        listetemp[compteur+1].append(matrice[i][j+5])
        
        listetemp[compteur+2].append(matrice[i][j+6])
        listetemp[compteur+2].append(matrice[i][j+7])
        listetemp[compteur+2].append(matrice[i][j+8])
        
    #tous les elements de chaque carrés doivent etre différent
    for i in range (0,9):
        model.AddAllDifferent(listetemp[i])
    
    ######## Call the sover #########
    solver=cp_model.CpSolver()
    status=solver.Solve(model)
    print('Une solution est : \n')
    ####### Display first solution #####
    #on affiche la solution
    if status == cp_model.FEASIBLE:
        colonne = 0
        for ligne in range(0,9):
            print(solver.Value(matrice[colonne][ligne]),
                  solver.Value(matrice[colonne+1][ligne]),
                  solver.Value(matrice[colonne+2][ligne]), '|', 
                  solver.Value(matrice[colonne+3][ligne]),
                  solver.Value(matrice[colonne+4][ligne]),
                  solver.Value(matrice[colonne+5][ligne]), '|', 
                  solver.Value(matrice[colonne+6][ligne]),
                  solver.Value(matrice[colonne+7][ligne]),
                  solver.Value(matrice[colonne+8][ligne]))
            if ((ligne == 2) | (ligne == 5)):
                print('- - - - - - - - - - -')
    print()

def CreateSudoku():
    #Create the model
    model=cp_model.CpModel()
    
    ######## Create the variable #########
    #on creer la matrice que l'on va par la suite modifier
    matrice = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    #permet de créer toutes les contraintes
    for colonne in range(0,9):
       for ligne in range(0,9):
           matrice[colonne][ligne] = model.NewIntVar(1, 9, '')
    
    ####### Define the constraint #######
    #contrainte de colonne:
    #pareil qu'avant
    listetemp =[]
    for colonne in range(0,9):
        for ligne in range (0,9):
            listetemp.append(matrice[colonne][ligne])
        model.AddAllDifferent(listetemp)
        listetemp.clear()
        
    #contrainte de ligne:
    #pareil qu'avant
    listetemp =[]
    for ligne in range (0,9):
        for colonne in range (0,9):
            listetemp.append(matrice[colonne][ligne])
        model.AddAllDifferent(listetemp)
        listetemp.clear()
    
    #contrainte carré:
    #pareil qu'avant
    listetemp =[[],[],[],[],[],[],[],[],[]]
    j = 0
    compteur = 0
    for i in range (0,9):
        if (i < 3):
            compteur = 0
        elif (i < 6):
            compteur = 3
        else:
            compteur = 6
        listetemp[compteur].append(matrice[i][j])
        listetemp[compteur].append(matrice[i][j+1])
        listetemp[compteur].append(matrice[i][j+2])
        
        listetemp[compteur+1].append(matrice[i][j+3])
        listetemp[compteur+1].append(matrice[i][j+4])
        listetemp[compteur+1].append(matrice[i][j+5])
        
        listetemp[compteur+2].append(matrice[i][j+6])
        listetemp[compteur+2].append(matrice[i][j+7])
        listetemp[compteur+2].append(matrice[i][j+8])
        
        
    for i in range (0,9):
        model.AddAllDifferent(listetemp[i])
    
    ######## Call the sover #########
    solver=cp_model.CpSolver()
    status=solver.Solve(model)
    ####### Display first solution #####
    #on affiche la solution
    if status == cp_model.FEASIBLE:
        print('Sudoku de base :')
        print()
        colonne = 0
        for ligne in range(0,9):
            print(solver.Value(matrice[colonne][ligne]),
                  solver.Value(matrice[colonne+1][ligne]),
                  solver.Value(matrice[colonne+2][ligne]), '|', 
                  solver.Value(matrice[colonne+3][ligne]),
                  solver.Value(matrice[colonne+4][ligne]),
                  solver.Value(matrice[colonne+5][ligne]), '|', 
                  solver.Value(matrice[colonne+6][ligne]),
                  solver.Value(matrice[colonne+7][ligne]),
                  solver.Value(matrice[colonne+8][ligne]))
            if ((ligne == 2) | (ligne == 5)):
                print('- - - - - - - - - - -')
        print()
        print('Quel est le niveau du sudoku ?')
        print('Tapez 1 pour debutant, 2 pour facile, 3 pour moyen,',
              '4 pour difficile, 5 pour très difficile')
        reponse = int(input())
        print()
        #17 cases
        if (reponse == 5):
            print('17 cases affichées \n')
            colonne = 0
            for ligne in range(0,8):
                print(solver.Value(matrice[colonne][ligne]),'0' ,'0', '|', 
                    '0','0','0', '|', 
                    solver.Value(matrice[colonne+6][ligne]),'0','0')
                if ((ligne == 2) | (ligne == 5)):
                    print('- - - - - - - - - - -')
            ligne += 1
            print('0','0' ,'0', '|', 
                    '0','0',solver.Value(matrice[colonne+5][ligne]), '|', 
                    '0','0','0')
        #26 cases            
        if (reponse == 4):
            print('26 cases affichées \n')
            colonne = 0
            for ligne in range(0,8):
                print('0','0',solver.Value(matrice[colonne+2][ligne]), '|', 
                      solver.Value(matrice[colonne+3][ligne]),'0','0', '|', 
                      '0',solver.Value(matrice[colonne+7][ligne]),'0')
                if ((ligne == 2) | (ligne == 5)):
                    print('- - - - - - - - - - -')
            ligne += 1
            print('0',solver.Value(matrice[colonne+1][ligne]),'0', '|', 
                    '0','0',solver.Value(matrice[colonne+5][ligne]), '|', 
                    '0','0','0')
        #33 cases
        if (reponse == 3):
           print('33 cases affichées \n')
           colonne = 0
           for ligne in range(0,8):
               print(solver.Value(matrice[colonne][ligne]),'0','0', '|', 
                     solver.Value(matrice[colonne+3][ligne]),'0',
                     solver.Value(matrice[colonne+5][ligne]), '|', 
                     '0',solver.Value(matrice[colonne+7][ligne]),'0')
               if ((ligne == 2) | (ligne == 5)):
                   print('- - - - - - - - - - -')
           ligne += 1
           print('0',solver.Value(matrice[colonne+1][ligne]),'0', '|', 
                    '0','0','0', '|', 
                    '0','0','0')
         #40 cases   
        if (reponse == 2):
            print('40 cases affichées \n')
            colonne = 0
            for ligne in range(0,8):
                print(solver.Value(matrice[colonne][ligne]),'0',
                      solver.Value(matrice[colonne+2][ligne]), '|', 
                      '0',solver.Value(matrice[colonne+4][ligne]),'0', '|', 
                      solver.Value(matrice[colonne+6][ligne]),
                      solver.Value(matrice[colonne+7][ligne]),'0')
                if ((ligne == 2) | (ligne == 5)):
                    print('- - - - - - - - - - -')
            ligne += 1
            print('0','0','0', '|', 
                    '0','0','0', '|', 
                    '0','0','0')
        #50 cases
        if (reponse == 1):
            print('50 cases affichées \n')
            colonne = 0
            for ligne in range(0,8):
                print(solver.Value(matrice[colonne][ligne]),
                      solver.Value(matrice[colonne+1][ligne]),'0', '|', 
                      solver.Value(matrice[colonne+3][ligne]),'0',
                      solver.Value(matrice[colonne+5][ligne]), '|', 
                      '0',solver.Value(matrice[colonne+7][ligne]),
                      solver.Value(matrice[colonne+8][ligne]))
                if ((ligne == 2) | (ligne == 5)):
                    print('- - - - - - - - - - -')
            ligne += 1
            print('0',solver.Value(matrice[colonne+1][ligne]),'0', '|', 
                    '0','0',solver.Value(matrice[colonne+5][ligne]), '|', 
                    '0','0','0')


def PartieI4cases():
    matrice = [[2,0,0,3], [0,0,2,0], [0,2,3,1], [1,3,4,0]]
    print('Matrice de base : \n')
    colonne = 0
    for ligne in range (0,4):
        print(matrice[colonne][ligne], matrice[colonne+1][ligne],
              matrice[colonne+2][ligne], matrice[colonne+3][ligne])
    print('\n')
    SolveSimpleSudoku4(matrice)
    
def PartieI9cases():
    matriceb = [[0,0,0,6,0,0,9,0,0],[0,9,0,0,8,0,7,0,4],[6,0,1,3,4,9,0,0,0],
                [1,0,7,5,9,0,0,0,2],[9,0,4,0,0,0,1,0,5],[8,0,0,0,7,1,4,0,3],
                [0,0,0,4,5,2,8,0,9],[2,0,9,0,3,0,0,4,0],[0,0,5,0,0,6,0,0,0]]
    print('Sudoku de base : \n')
    colonne = 0
    for ligne in range(0,9):
        print(matriceb[colonne][ligne],matriceb[colonne+1][ligne],
              matriceb[colonne+2][ligne], '|', 
              matriceb[colonne+3][ligne],matriceb[colonne+4][ligne],
              matriceb[colonne+5][ligne], '|', 
              matriceb[colonne+6][ligne],matriceb[colonne+7][ligne],
              matriceb[colonne+8][ligne])
        if ((ligne == 2) | (ligne == 5)):
            print('- - - - - - - - - - -')
    print()
    SolveSimpleSudoku(matriceb)
    
#execute the program
if __name__=='__main__' :
    #Partie 1 avec un soduko a 4 cases
    print('Partie I, 4 cases \n')
    PartieI4cases()
    
    #Partie 1 avec un soduko a 9 cases
    print('Partie I, 9 cases \n')
    PartieI9cases()

    #Partie 2 création d'un soduko:
    print('Partie II \n')
    CreateSudoku()

    