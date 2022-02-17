import  sys

import  pymysql

from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QMenu,QAbstractItemView
from mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt,QPoint

from addstaff import Ui_add_staff

from alter_display_staff import Ui_alter_display_staff



from login import  Ui_login
from admin import  Ui_admin
from add_admin import  Ui_add_admin
from alter_admin import  Ui_alter_admin
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

        if txt!='Mange HR Guys':
            for singer_obj in self.content.children():
                #print("初始",singer_obj)
                if(isinstance(singer_obj,QtWidgets.QLabel)==False and isinstance(singer_obj,QtWidgets.QGridLayout)==False):
                    grid.removeWidget(singer_obj)
                    singer_obj.deleteLater()
                    sip.delete(singer_obj)
        else:
            self.label1.hide()
            self.label2.hide()

        if txt == 'Add HR Guys':
            self.label1.hide()
            self.label2.hide()
            self.add_staff_page = add_staff()
            grid.addWidget(self.add_staff_page)
        elif txt =='HR Guys Info':
            self.label1.hide()
            self.label2.hide()
            self.alter_display_staff_page = alter_display_staff()
            grid.addWidget(self.alter_display_staff_page)
            obj={}
            # 打开数据库
            dbn = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
            cursor = dbn.cursor()
            try:
                cursor.execute(" select staff.s_no,staff.s_name,department.d_invation ,staff.s_quote from staff, department where  department.d_no = staff.s_no order by convert (staff.s_no,signed)")
                results = cursor.fetchall()
                print(results)

                for row in results:
                    sno = row[0]
                    sname = row[1]
                    dname = row[2]
                    squote=row[3]
                    oldrow = self.alter_display_staff_page.tableWidget.rowCount()


                    self.alter_display_staff_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 1, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 2, item)

                    item = QTableWidgetItem(squote)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 3, item)


                   
            except:
                print("error")
        
        
  
        elif txt=="Mange HR_ADM":
            self.label1.hide()
            self.label2.hide()
            self.admin_table = admin()
            grid.addWidget(self.admin_table)

            cursor = db.cursor()
            try:
                cursor.execute("select s_no,pwd from admin_table order by convert (s_no,signed)")
                results = cursor.fetchall()
                #print(results)
                for row in results:
                    sno = row[0]
                    pwd = row[1]
                    oldrow = self.admin_table.tableWidget.rowCount()

                    self.admin_table.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(sno)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_table.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(pwd)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_table.tableWidget.setItem(oldrow, 1, item)
            except:
                print("error")
       

        


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
                QMessageBox.information(self,"Atttion","Wrong！",QMessageBox.Yes)
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
        sex = self.sex.currentText()
        birth = self.birth.text()
        tel = self.tel.text()
        address = self.address.text()
        quot = self.quot.text()
        email = self.email.text()
        identity = self.identity.text()
        



           

        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        cursor = db.cursor()
        try:
                #获取下一个sno
                sql = "select max(convert(s_no,signed)) from staff"
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
                
                
                
              
               

                sql = "insert into staff (s_no,s_name,s_firstname,s_sex,s_birth,s_email,s_company,s_quote,s_password) \
                                  values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                      (newsno, name, identity,sex, birth, email, address,quot,tel )
                print(sql)
                cursor.execute(sql)
                
              

               
                QMessageBox.information(self, "Atttion", "Suessuful!", QMessageBox.Yes)
                db.commit()

        except Exception as e:
                print(e)
                print("error1")


    def clearAll(self):
        self.name.clear()
        self.address.clear()
        self.tel.clear()
        self.email.clear()
        self.identity.clear()
    
        self.sex.setCurrentText("-Please Choice")
        self.quot.clear()
       
        self.birth.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
      


   

class admin(QtWidgets.QWidget,Ui_admin):
    def __init__(self):
        super(admin, self).__init__()
        self.setupUi(self)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
    #产生右键触发菜单
    def generateMenu(self, pos):
        print(pos)
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        menu = QMenu()
        item1 = menu.addAction("Add admin")
        item2 = menu.addAction("delete Admin")
        item3 = menu.addAction("change password")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        
        if action == item1:  # 添加
            self.add_admin_page = add_admin(self)
            self.add_admin_page.show()
        elif action == item2:  # 删除
            row = self.tableWidget.currentRow()
            sno = self.tableWidget.item(row, 0).text()  # 获取工号
            if sno == "1":
                print("Run")
                reply = QMessageBox.information(self, "提示", "该用户为超级管理员！无法删除！", QMessageBox.Yes )
            elif row!=0:
                reply = QMessageBox.information(self, "提示", "您是否确定要删除该管理员?", QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
                    cursor = db.cursor()
                    try:
                        sql = "delete from admin_table where s_no = '%s'"%(sno)
                        cursor.execute(sql)
                        db.commit()
                        row = self.tableWidget.currentRow()
                        self.tableWidget.removeRow(row)
                    except:
                        print("error")

        if action == item3:  # 修改
            row = self.tableWidget.currentRow()
            sno = self.tableWidget.item(row, 0).text()  # 获取工号

            self.alter_admin_page = alter_admin(self)
            self.alter_admin_page.show()
            self.alter_admin_page.sno.setText(sno)
            db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
            cursor = db.cursor()
            try:
                sql = "select pwd from admin_table where s_no = '%s'" % (sno)
                cursor.execute(sql)
                result = cursor.fetchone()
                pwd = result[0]
                self.alter_admin_page.pwd.setText(pwd)
                #self.alter_profess_page.no.setText(pno)
                # print(result)
            except:
                print("error1")


        else:
            return

class add_admin(QtWidgets.QWidget,Ui_add_admin):
    def __init__(self,professAdmin):
        super(add_admin,self).__init__()
        self.setupUi(self)
        self.profess_admin = professAdmin

        self.staff.addItem("-请选择")
        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        cursor = db.cursor()
        try:
            sql = "select s_no,s_name from staff"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                sno = row[0]
                sname = row[1]
                staffstr = sno+'-'+sname
                self.staff.addItem(staffstr)
        except:
            print("error")
    #添加按钮
    def add(self):
        staffstr = self.staff.currentText()
        sta = staffstr.split('-')[1]
        pwd  = self.pwd.text()
        if sta == '请选择' or pwd=='':
            QMessageBox.information(self,"提示","请正确填写信息！",QMessageBox.Yes)
        else:
            sno = staffstr.split('-')[0]
            db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
            cursor = db.cursor()
            try:
                sql = "select count(*) from admin_table where s_no='%s'" % (sno)
                cursor.execute(sql)
                result = cursor.fetchone()
                count= result[0]
                if count==0:#不是管理员
                    sql = "insert into admin_table values('%s','%s')" % (sno, pwd)
                    status = cursor.execute(sql)
                    db.commit()
                    if status == 1:
                        self.rewrite()
                    reply = QMessageBox.information(self, "提示", "添加成功！", QMessageBox.Yes)
                    if reply == QMessageBox.Yes:
                        self.close()
                else:#已经是管理员
                    QMessageBox.information(self,"提示","该员工已是管理员",QMessageBox.Yes)
                    self.staff.setCurrentText("-请选择")
                    self.pwd.clear()
            except:
                print("error")
    #重写表格
    def rewrite(self):

        professA = self.profess_admin
        rows = professA.tableWidget.rowCount()
        # print(rows)
        i = rows
        while i > 0:
            professA.tableWidget.removeRow(i)
            i = i - 1

        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute("select s_no,pwd from admin_table order by convert(s_no,signed)")
            results = cursor.fetchall()
            #print("hello", results)

            for row in results:
                sno = row[0]
                pwd = row[1]
                oldrow = professA.tableWidget.rowCount()
                print('oldrow=', oldrow)
                professA.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(sno)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 0, item)

                item = QTableWidgetItem(pwd)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 1, item)

        except:
            print("error")

class alter_admin(QtWidgets.QWidget,Ui_alter_admin):
    def __init__(self,professAdmin):
        super(alter_admin, self).__init__()
        self.setupUi(self)
        self.profess_admin = professAdmin
    #保存按钮
    def save(self):
        sno = self.sno.text()
        pwd = self.pwd.text()
        if pwd == '':
            QMessageBox.information(self, "提示", "请正确填写密码!", QMessageBox.Yes)

        else:
            db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
            cursor = db.cursor()
            try:
                print(pwd,sno)
                sql = "update admin_table set pwd='%s' where s_no='%s'"%(pwd,sno)
                status = cursor.execute(sql)
                db.commit()
                if status == 1:
                    self.rewirte()
                reply = QMessageBox.information(self, "提示", "保存成功！", QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    self.close()
            except:
                print("error2")
    #重写按钮
    def rewirte(self):
        professA = self.profess_admin
        rows = professA.tableWidget.rowCount()
        i = rows
        while i > 0:
            professA.tableWidget.removeRow(i)
            i = i - 1

        db = pymysql.connect(host="localhost",user="root",password= "root1234",db="personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute("select s_no,pwd from admin_table order by convert(s_no,signed)")
            results = cursor.fetchall()
            for row in results:
                sno = row[0]
                pwd = row[1]
                oldrow = professA.tableWidget.rowCount()
                #print('oldrow=', oldrow)
                professA.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(sno)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 0, item)

                item = QTableWidgetItem(pwd)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 1, item)

        except:
            print("error")


    def __init__(self):
        super(find_check, self).__init__()
        self.setupUi(self)
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
            cursor.execute(" select * from staff where s_no='%s'"%(sno))
            result = cursor.fetchone()
            print(result)

            sno = result[0]
            sname = result[1]
            sex= result[2]
            birth = result[3]
            identity = result[4]
            tel = result[5]
            email = result[6]
            isMarried = result[7]
            address = result[8]




            
      

           

            content.alter_staff_page.no.setText(str(sno))
            content.alter_staff_page.name.setText(sname)
            content.alter_staff_page.sex.setCurrentText(sex)
            content.alter_staff_page.birth.setDate(QtCore.QDate(birth))
            content.alter_staff_page.address.setText(address)
            content.alter_staff_page.tel.setText(tel)
            content.alter_staff_page.isMarried.setCurrentText(isMarried)
            content.alter_staff_page.identity.setText(identity)
            content.alter_staff_page.email.setText(email)
        

        except:
            print("error")

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = login()
    login_window.show()
    sys.exit(app.exec_())