
import os
import csv
import pandas as pd
import xml.etree.ElementTree as ET
import mysql.connector as mc

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

cols = [
    'producent',
    'przekatna',
    'rozdzielczosc',
    'matryca',
    'dotykowy',
    'procesor',
    'rdzeni',
    'MHz',
    'RAM',
    'dysk',
    'typ',
    'grafika',
    'GDDR',
    'system',
    'naped',
    'empty'
]

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setGeometry(100, 100, 1200, 700)

        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.pushLoadCsv = QtWidgets.QPushButton(self)
        self.pushLoadCsv.setText("Load Csv")
        self.pushLoadCsv.clicked.connect(self.on_pushLoadCsv_clicked)
        

        self.pushWriteCsv = QtWidgets.QPushButton(self)
        self.pushWriteCsv.setText("Write Csv")
        self.pushWriteCsv.clicked.connect(self.on_pushWriteCsv_clicked)

        self.pushLoadXml = QtWidgets.QPushButton(self)
        self.pushLoadXml.setText("Load Xml")
        self.pushLoadXml.clicked.connect(self.on_pushLoadXml_clicked)
        
        self.pushWriteXml = QtWidgets.QPushButton(self)
        self.pushWriteXml.setText("Write Xml")
        self.pushWriteXml.clicked.connect(self.on_pushWriteXml_clicked)

        self.pushImportDb = QtWidgets.QPushButton(self)
        self.pushImportDb.setText("Import DB")
        self.pushImportDb.clicked.connect(self.on_pushImportDb_clicked)

        self.pushExportDb = QtWidgets.QPushButton(self)
        self.pushExportDb.setText("Export DB")
        self.pushExportDb.clicked.connect(self.on_pushExportDb_clicked)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutHorizontal = QtWidgets.QHBoxLayout(self)
        self.layoutVertical.addLayout(self.layoutHorizontal)
        self.layoutHorizontal.addWidget(self.pushLoadCsv)
        self.layoutHorizontal.addWidget(self.pushWriteCsv)
        self.layoutHorizontal.addWidget(self.pushLoadXml)
        self.layoutHorizontal.addWidget(self.pushWriteXml)
        self.layoutHorizontal.addWidget(self.pushImportDb)
        self.layoutHorizontal.addWidget(self.pushExportDb)
        self.layoutVertical.addWidget(self.tableView)
        


    
    def loadCsv(self):
        fileName, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Csv", ".", "Csv Files (*.txt)")
    
        with open(fileName, "r", newline='') as fileInput:

             csvReader = csv.reader(fileInput, delimiter=';', quotechar='|')
             print(type(csvReader))

             for row in csvReader: 
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                    
                ]
                self.model.appendRow(items)

    def writeCsv(self):
        fileName, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Open Csv", ".", "Csv Files (*.txt)")
        
        with open(fileName, "w", newline='') as fileOutput:
            writer = csv.writer(fileOutput, delimiter=';', quotechar='|')
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                writer.writerow(fields)

    def loadXml(self):
        fileName, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Xml", ".", "Xml Files (*.xml)")
        
        df = pd.read_xml(fileName)

        rows = df.values.tolist()
        head=df.columns

        with open('pom.txt', 'w', newline='') as f:
      
            write = csv.writer(f, delimiter=';', quotechar='|')
            write.writerow(head)
            write.writerows(rows)
        

        with open('pom.txt', "r", newline='') as fileInput:
            csvReader = csv.reader(fileInput, delimiter=';', quotechar='|')

            for row in csvReader:  
                items = [
                    QtGui.QStandardItem(field)
                    for field in row     
                ]
                self.model.appendRow(items)
        os.remove("pom.txt")
    
    def writeXml(self):
        fileName, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Open Xml", ".", "Xml Files (*.xml)")

        df = pd.DataFrame(columns=cols)
        for row in range(self.model.rowCount()):
            for col in range(self.model.columnCount()):
                df.at[row, cols[col]] = self.model.item(row, col).text()
        df.to_xml(fileName, index=False)
    

    def select_data(self):
        try:
            i=0
            d=0

            mydb = mc.connect(
 
                host="localhost",
                user="root",
                password="",
                database="integracja"
            )
 
            mycursor = mydb.cursor()
 
            mycursor.execute("SELECT * FROM katalog")
            result = mycursor.fetchall()
            #self.tableView.setRowCount(0)
            
            for row_number, row_data in enumerate(result):
                i+=1
                items = [
                    QtGui.QStandardItem(str(field))
                    for field in row_data
                ]
               
                for rowNumber in range(1, self.model.rowCount()):
                    fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(0,16)
                    ]
                    #print(fields[0])
                    #print(row_data[0])
                    if (str(fields[0])==str(row_data[0])) :
                        d+=1
                self.model.appendRow(items)
            if(d>0):
                d+=1
                
                
            QMessageBox.information(self, "Import", "Data imported from Database \nFound: \n"+str(i)+" Records \n"+str(d)+" Duplicates")
            #print(i, d)
 
        except mc.Error as e:
            print("Error")

    def insert_data(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="integracja"
            )
 
            mycursor = mydb.cursor()
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(0,16)
                ]
            
                sql = "INSERT INTO katalog VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                #print(sql,fields)
                mycursor.execute(sql, fields)
 
            mydb.commit()
            print("Data Inserted")
            QMessageBox.information(self, "Export", "Data exported to Database")
 
        except mc.Error as e:
            print("Error Inserting Data")
            QMessageBox.information(self, "Export", "Error! Data not exported to Database")


    @QtCore.pyqtSlot()
    def on_pushWriteCsv_clicked(self):
        self.writeCsv()
        
    @QtCore.pyqtSlot()
    def on_pushLoadCsv_clicked(self):
        self.loadCsv()

    @QtCore.pyqtSlot()
    def on_pushLoadXml_clicked(self):
        self.loadXml()

    @QtCore.pyqtSlot()
    def on_pushWriteXml_clicked(self):
        self.writeXml()

    @QtCore.pyqtSlot()
    def on_pushImportDb_clicked(self):
        self.select_data()

    @QtCore.pyqtSlot()
    def on_pushExportDb_clicked(self):
        self.insert_data()
    

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('CSV Editor')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())
    