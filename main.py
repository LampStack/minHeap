from tempfile import TemporaryDirectory
import networkx as nx
import matplotlib.pyplot as plt
import os
os.system('CLS')

class MinHeap :

    heapArray = []
    size = 0

    def __init__(self, file_path) -> None:
        with open(file_path, 'r') as my_file :
            temp_list = list(my_file.read().replace("\n", ' ').split())
        words_list = []
        for word in temp_list:
            if word not in words_list and len(word) >= 3 :
                words_list.append(word)
        self.heapArray = [''] * 1000
        for word in words_list :
            self.add(word)


    def rightChild(self, node) -> int :
        return (2 * node) + 1


    def leftChild(self, node) -> int :
        return 2 * node


    def parent(self, node) -> int :
        return node//2


    def add(self, word) -> None :
        self.size += 1 # change current size
        self.heapArray[self.size] = word # add new word in the last of our list
        temp = self.size
        while self.heapArray[temp] < self.heapArray[self.parent(temp)] :
            self.heapArray[temp], self.heapArray[self.parent(temp)] = self.heapArray[self.parent(temp)], self.heapArray[temp] # swap node with parent
            temp = self.parent(temp)


    def isLeaf(self, node):
        if self.heapArray[self.leftChild(node)] == '' and self.heapArray[self.rightChild(node)] == '' :
            return True
        return False


    def treeSort(self, node) -> None :
        if not self.isLeaf(node) : # check that this node is not a leaf
            if self.heapArray[node] > self.heapArray[self.leftChild(node)] or self.heapArray[node] > self.heapArray[self.rightChild(node)] : # chech that this node is not less than its childrens
                if self.heapArray[self.leftChild(node)] < self.heapArray[self.rightChild(node)] : # swap the node with its left child and call treeSort for left child
                    self.heapArray[node], self.heapArray[self.leftChild(node)] = self.heapArray[self.leftChild(node)], self.heapArray[node]
                    self.treeSort(self.leftChild(node))
                else : # swap the node with its right child and call treeSort for right child
                    self.heapArray[node], self.heapArray[self.rightChild(node)] = self.heapArray[self.rightChild(node)], self.heapArray[node]
                    self.treeSort(self.rightChild(node))


    def remove(self) -> None :
        self.heapArray[1] = self.heapArray[self.size] # change the first node (root) to last leaf
        self.heapArray[self.size] = '' # empty the last leaf
        self.size -= 1 # set a new size for tree
        self.treeSort(1) # use sort method to sort the tree


    def showGUI(self) -> None :
        G = nx.DiGraph()
        for i in range(1, (self.size//2) + 1 ): # from 1 to the last parent !
            if self.heapArray[self.leftChild(i)] != '':
                G.add_edge(self.heapArray[i], self.heapArray[self.leftChild(i)]) # parent and left
            if self.heapArray[self.rightChild(i)] != '':
                G.add_edge(self.heapArray[i], self.heapArray[self.rightChild(i)]) # parent and right
        nx.draw_networkx(G)
        plt.show() #show GUI tree


    def showWords(self) -> None :
        wordsArray = [] # Add parent and childs sorted in a list
        for i in range(1, (self.size//2) + 1 ): # from 1 to the last parent !
            if self.heapArray[i] not in wordsArray : wordsArray.append(self.heapArray[i])
            if self.heapArray[self.leftChild(i)] != '' and self.heapArray[self.leftChild(i)] not in wordsArray :
                wordsArray.append(self.heapArray[self.leftChild(i)])
            if self.heapArray[self.rightChild(i)] != '' and self.heapArray[self.rightChild(i)] not in wordsArray :
                wordsArray.append(self.heapArray[self.rightChild(i)])
        print("*** WORDS LIST ***")
        for word in wordsArray :
            print(word, end="\t")


my_tree = MinHeap('data.txt')
# my_tree.add('tree')
# my_tree.remove()
# my_tree.showGUI()
# my_tree.showWords()
