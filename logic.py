from PyQt6.QtWidgets import *
from gui import *
from csv import *
import algorithms
import time


class Logic(QMainWindow, Ui_window):
    '''
    Class to conatian the logic for the user interface
    '''

    def __init__(self) -> None:
        '''
        Method to set the inital positions of widgets, values of variables, and connect buttons to functions
        '''
        super().__init__()

        self.setupUi(self)
        self.searchingUi()
        self.fileUi()
        self.__fileName = ''

        self.buttonSubmit.clicked.connect(lambda : self.submit())
        self.buttonClear.clicked.connect(lambda : self.erase())
        self.radioSearching.clicked.connect(lambda : self.searchingUi())
        self.radioSorting.clicked.connect(lambda : self.sortingUi())
        self.radioManual.clicked.connect(lambda : self.manualUi())
        self.radioFile.clicked.connect(lambda : self.fileUi())
        self.buttonFile.clicked.connect(lambda : self.selectFile())

    def sortingUi(self) -> None:
        '''
        Method to change the layout of user interface to match the sorting option
        '''
        self.radioLinear.hide()
        self.radioBinary.hide()
        self.inputValue.hide()

        self.labelOutputType.setText("Sort Type")
        
        self.radioBubble.show()
        self.radioSelection.show()
        self.radioInsertion.show()
        self.radioAscending.show()
        self.radioDescending.show()

    def searchingUi(self) -> None:
        '''
        Method to change the layout of user interface to match the searching option
        '''
        self.radioBubble.hide()
        self.radioSelection.hide()
        self.radioInsertion.hide()
        self.radioAscending.hide()
        self.radioDescending.hide()

        self.labelOutputType.setText("Search Value")
        self.radioLinear.show()
        self.radioBinary.show()
        self.inputValue.show()
    
    def manualUi(self) -> None:
        '''
        Method to change the layout of user interface to match the manual input option
        '''
        self.buttonFile.hide()
        self.labelFile.hide()
        self.inputList.show()

    def fileUi(self) -> None:
        '''
        Method to change the layout of user interface to match the file input option
        '''
        self.inputList.hide()
        self.buttonFile.show()
        self.labelFile.show()

    def selectFile(self) -> None:
        '''
        Method to cleanse the input of choosing a file
        '''
        try:
            temp = self.fileSelector.getOpenFileName(caption = 'Open file', filter = "Text files (*.txt *.csv)")[0]
            tempFile = open(temp)

            charIndex = len(temp) - 1
            while(temp[charIndex] != '/'):
                charIndex -= 1
            shortHandFileName = temp[(charIndex + 1):]

            self.labelFile.setText(f'Current File:\n{shortHandFileName}')
            self.__fileName = temp
            tempFile.close()

        except:
            if self.__fileName != '':
                charIndex = len(self.__fileName) - 1
                while(self.__fileName[charIndex] != '/'):
                    charIndex -= 1
                shortHandFileName = self.__fileName[(charIndex + 1):]
            else:
                shortHandFileName = 'None'

            self.labelFile.setText(f'Could not Open File\nCurrent File:\n{shortHandFileName}')
        
    def submit(self) -> None:
        '''
        Method to check inputs and give the result of the selected values
        '''
        
        if self.dropDownDelimiter.currentIndex() == 0:
            delimiter = ','
        elif self.dropDownDelimiter.currentIndex() == 1:
            delimiter = '\n'
        elif self.dropDownDelimiter.currentIndex() == 2:
            delimiter = ';'
        elif self.dropDownDelimiter.currentIndex() == 3:
            delimiter = ' '

        if self.radioManual.isChecked():
            if self.inputList.toPlainText() == '':
                self.labelOutput.setText('Please input list')
                return
            list = self.inputList.toPlainText().strip().split(sep = delimiter)
        
        elif self.radioFile.isChecked():
            try:
                inputFile = open(self.__fileName)
                contents = inputFile.read().strip()
                inputFile.close()
                if contents == '':
                    self.labelOutput.setText('The entered file is empty')
                    return
                list = [item for item in contents.split(sep = delimiter)]

            except:
                self.labelOutput.setText('Please select input file')
                return
        
        try:
            newList = []
            for item in list:
                item.strip()
                if not (item.isspace() or item == ''):
                    newList.append(float(item))
            isNum = True
        
        except:
            newList = [item.strip().lower() for item in list]
            isNum = False
        
        if self.radioSearching.isChecked():
            searchValue = self.inputValue.toPlainText().strip()

            if self.inputValue.toPlainText() == '':
                self.labelOutput.setText('Enter Search Value')
                return
            elif isNum:
                try:
                    searchValue = float(searchValue)
                except:
                    self.labelOutput.setText('Search value must match the lists type')
        
        elif self.radioDescending.isChecked():
            ascending = False
        elif self.radioAscending.isChecked():
            ascending = True

        startTime = time.time()

        if self.radioSearching.isChecked() and self.radioLinear.isChecked():
            finalIndex = algorithms.linearSearch(newList, searchValue)
            if finalIndex == -1:
                self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nItem not found')
            else:
                self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nItem found at index: {finalIndex}')

        elif self.radioSearching.isChecked() and self.radioBinary.isChecked():
            finalIndex = algorithms.binarySearch(newList, searchValue)
            if finalIndex == -1:
                self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nItem not found')
            else:
                self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nItem found at index: {finalIndex}')

        elif self.radioSorting.isChecked() and self.radioBubble.isChecked():
            sortedList = algorithms.bubbleSort(newList, ascending)
            with open('output.csv', 'a') as outputFile:
                pen = writer(outputFile)
                pen.writerow(sortedList)
                if isNum:
                    self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nSorted list appended to file output.csv')
                else:
                    self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nSorted list appended to file output.csv\n\nWarning: input read as text not number. If this is\nnot correct, make sure input is only numbers\n(e.g. 1000 not 1,000)')

        elif self.radioSorting.isChecked() and self.radioSelection.isChecked():
            sortedList = algorithms.selectionSort(newList, ascending)
            with open('output.csv', 'a') as outputFile:
                pen = writer(outputFile)
                pen.writerow(sortedList)
                if isNum:
                    self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nSorted list appended to file output.csv')
                else:
                    self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nSorted list appended to file output.csv\n\nWarning: input read as text not number. If this is\nnot correct, make sure input is only numbers\n(e.g. 1000 not 1,000)')

        elif self.radioSorting.isChecked() and self.radioInsertion.isChecked():
            sortedList = algorithms.insertionSort(newList, ascending)
            with open('output.csv', 'a') as outputFile:
                pen = writer(outputFile)
                pen.writerow(sortedList)
                if isNum:
                    self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nSorted list appended to file output.csv')
                else:
                    self.labelOutput.setText(f'Operation completed in {(time.time() - startTime):.6f} seconds.\nSorted list appended to file output.csv\n\nWarning: input read as text not number. If this is\nnot correct, make sure input is only numbers\n(e.g. 1000 not 1,000)')
    def erase(self) -> None:
        '''
        Method to reset the user interface to the default values
        '''
        self.inputList.clear()
        self.inputValue.clear()

        self.__fileName = ''

        self.radioLinear.setChecked(True)
        self.radioBinary.setChecked(False)
        self.radioSelection.setChecked(False)
        self.radioBubble.setChecked(False)
        self.radioInsertion.setChecked(True)
        self.radioManual.setChecked(False)
        self.radioFile.setChecked(True)
        self.radioDescending.setChecked(False)
        self.radioAscending.setChecked(True)
        self.radioSorting.setChecked(False)
        self.radioSearching.setChecked(True)

        self.labelFile.setText('')
        self.labelOutput.setText('')
        self.labelOutputType.setText('')

        self.inputList.hide()
        self.buttonFile.show()

        self.dropDownDelimiter.setCurrentIndex(0)

        self.fileUi()
        self.searchingUi()
        
        