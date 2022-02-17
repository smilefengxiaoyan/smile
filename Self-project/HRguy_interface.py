from email import message
import  sys
from tkinter import PanedWindow
import  pymysql
import time

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QAction,QMenu,QAbstractItemView
from mainWindowg import Ui_MainWindow
from PyQt5.QtCore import Qt,QPoint

from invainfor import Ui_alter_display_staff


from addstaff import Ui_add_staff

from PyQt5.QtGui import QCursor

from functools import partial
from loging import  Ui_login
import sip





#主界面
class staff_Admin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(staff_Admin, self).__init__()
        self.setupUi(self)
        grid = QtWidgets.QGridLayout()
        self.content.setLayout(grid)

    def test(self):
        self.label1.show()
        self.label2.show()
        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        txt = self.treeWidget.currentItem().text(0)
        grid = self.content.layout()

        if txt!='Mange my Work':
            for singer_obj in self.content.children():
            
                if(isinstance(singer_obj,QtWidgets.QLabel)==False and isinstance(singer_obj,QtWidgets.QGridLayout)==False):
                    grid.removeWidget(singer_obj)
                    singer_obj.deleteLater()
                    sip.delete(singer_obj)
        else:
            self.label1.hide()
            self.label2.hide()

        if txt == 'Send invatation':
            self.label1.hide()
            self.label2.hide()
            self.add_staff_page = add_staff()
            grid.addWidget(self.add_staff_page)
        elif txt =='Team List':
            self.label1.hide()
            self.label2.hide()
            self.alter_display_staff_page = alter_display_staff()
            grid.addWidget(self.alter_display_staff_page)
            obj={}
            # 打开数据库
            dbn = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
            cursor = dbn.cursor()
            try:
                cursor.execute(" select inva.s_vo,inva.s_name,inva.s_subject from inva order by inva.s_vo")
                results = cursor.fetchall()
                print(results)

                for row in results:
                    sno = row[0]
                    sname = row[1]
                    ssub = row[2]
                   
                    oldrow = self.alter_display_staff_page.tableWidget.rowCount()


                    self.alter_display_staff_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 1, item)

                    item = QTableWidgetItem(ssub)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 2, item)

                    

                    
                   
            except:
                print("error")
        elif txt=='Upload my info':
            self.label1.hide()
            self.label2.hide()
            self.delete_staff_page = delete_staff()
            grid.addWidget(self.delete_staff_page)
            obj={}
            # 打开数据库
            cursor = db.cursor()
            try:
                cursor.execute(" select staff.s_no,staff.s_name,department.d_name from staff, department,sp where sp.s_no = staff.s_no and department.d_no = sp.d_no order by convert (staff.s_no,signed)")
                results = cursor.fetchall()
                #print(results)

                for row in results:
                    sno = row[0]
                    sname = row[1]
                    dname = row[2]
                    oldrow = self.delete_staff_page.tableWidget.rowCount()
                    self.delete_staff_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_staff_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_staff_page.tableWidget.setItem(oldrow, 1, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_staff_page.tableWidget.setItem(oldrow, 2, item)
                    
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                   
                    obj[strbtn].setStyleSheet("text-decoration: underline")
                    self.delete_staff_page.one = partial(self.delete_staff_page.btnclicked, obj[strbtn])
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.delete_staff_page.tableWidget.setCellWidget(oldrow, 3, obj[strbtn])
                    obj[strbtn].clicked.connect(self.delete_staff_page.one)

            except:
                print("error")
        

#登陆
class login(QtWidgets.QDialog,Ui_login):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)

    def jump(self):
        sno = self.sno.text()
        pwd = self.pwd.text()
        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        cursor = db.cursor()
        try:
           # print(sno)
            sql = "select count(*) from admin_table where s_no='%s' and pwd='%s'"%(sno,pwd)
            cursor.execute(sql)
            result = cursor.fetchone()
            #print(result)
            count = result[0]
            if count==0:
                QMessageBox.information(self,"Atttion","Wrong id or password！",QMessageBox.Yes)
            else:

                self.close()
                self.my_staffAdmin = staff_Admin()
                self.my_staffAdmin.show()

        except:
            print("error")

class add_staff(QtWidgets.QWidget,Ui_add_staff):
    def __init__(self):
        super(add_staff, self).__init__()
        self.setupUi(self)
       
        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        cursor = db.cursor()

    def addInfo(self):

        #sno = self.no.text()
        name = self.name.text()
        message = self.message.text()
        von = self.von.text()
        zu = self.zu.text()
        sub = self.sub.text()
        
      

        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        cursor = db.cursor()
        try:
                #获取下一个sno
                sql = "select max(convert(s_vo,signed)) from inva"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
                maxsno = result[0]
                if maxsno == None:
                    newsno = 1
                else:
                    newsno = maxsno + 1
                print(newsno)

                needstr = ''
                if len(str(newsno)) < 6:
                    need = 6 - len(str(newsno))
                    print(need)
                    for i in range(need):
                        needstr += '0'
                newsno = needstr + str(newsno)
                
                
                sql = "insert into inva (s_vo,s_from,s_to,s_subject,s_message,s_name) \
                                  values ('%s','%s','%s','%s','%s','%s')" % \
                      (newsno, von, zu,sub, message, name )
                print(sql)
                
                
                QMessageBox.information(self, "提示", "添加成功!", QMessageBox.Yes)
                db.commit()

        except Exception as e:
                print(e)
                print("error1")


    def clearAll(self):
        self.name.clear()
        self.von.clear()
        self.zu.clear()
        self.sub.clear()
        self.message.clear()
       
class alter_display_staff(QtWidgets.QWidget,Ui_alter_display_staff):
    def __init__(self):
        super(alter_display_staff, self).__init__()
        self.setupUi(self)
    #查看详情按钮
    def btnclicked(self,btn):
        x = btn.frameGeometry().x()
        y = btn.frameGeometry().y()
        index = self.tableWidget.indexAt(QPoint(x, y))
        row = index.row()
        #row = self.tableWidget.currentRow()
        print(row)
        sno = self.tableWidget.item(row,0).text()#获取工号

        for singer_obj in self.parent().children():
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj

        #print(grid)
        content = self.parent()
        for singer_obj in content.children():
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False):
                singer_obj.hide()

        content.alter_staff_page = alter_staff()

        grid.addWidget(content.alter_staff_page)

        # 打开数据库
        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        cursor = db.cursor()
        try:
            #读取基本信息
            cursor.execute(" select * from inva where s_vo='%s'"%(sno))
            result = cursor.fetchone()
            print(result)

            sno = result[0]
            sname = result[5]
          
            


           


           


            content.alter_staff_page.no.setText(str(sno))
            content.alter_staff_page.name.setText(sname)
    
            

        except:
            print("error")



  

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = login()
    login_window.show()
    sys.exit(app.exec_())