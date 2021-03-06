import webbrowser
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window
from kivy.metrics import dp, sp
import mysql.connector
import hashlib


db = mysql.connector.connect(
    host="172.104.148.212",
    user="daviid",
    passwd="Ubuntob0I!",
    database="Tfw",
    auth_plugin="mysql_native_password"
)
mycursor = db.cursor(buffered=True)


class username1:
    def __init__(self, name="Guest"):
        self.__name=name


    def setname(self, name):
        print("name was set" + name)
        self.__name=name

    def getname(self):
        return self.__name

class LoginPage(Screen):

    def get_username(self):
        return self.ids.login.text

    def if_active(self, state):
        r_user = self.ids.rem_user
        r_pass = self.ids.rem_pass

        if state:
            r_pass.disabled = False

        else:
            r_pass.disabled = True
            r_pass.active = False

    def verify_credentials(self):

        user = self.ids.login
        pwd = self.ids.passw
        info = self.ids.info
        r_user = self.ids.rem_user
        r_pass = self.ids.rem_pass
        username = user.text
        password = pwd.text

        userfile = open("user.txt", "w")
        userfile.write(username)
        userfile.close()

        hash_object = hashlib.sha256(password.encode('utf-8'))
        hashedpw = hash_object.hexdigest()

        mycursor.execute("SELECT * FROM Users WHERE username = '"+username+"' AND password = '"+hashedpw+"'")
        results = mycursor.fetchall()

        if results and results[0][2] == 1:
            for i in results:
                print("Welcome "+i[0])
                info.text = ''
                if not r_user.active:
                    self.ids.login.text = ""
                if not r_pass.active:
                    self.ids.passw.text = ""

                self.manager.current = "admin"

            return ""
        elif results:
            for i in results:
                us1 = username1()
                us1.setname(i[0])


                print("Welcome "+i[0])
                info.text = ''
                if not r_user.active:
                    self.ids.login.text = ""
                if not r_pass.active:
                    self.ids.passw.text = ""
                self.manager.current = "user"

            return ""

        if username == '' or password == '':
            info.text = '[color=#FF0000]Username and/ or Password required[/color]'
        else:
            info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'


class UserPage(Screen):

    def openWarriorTracker(self):
        webbrowser.open("https://www.warriortracker.com/")

    def getUsername(self):
        with open("user.txt") as f:
            contents = f.read()
            self.ids.label1.text = "Velkommen " + str(contents)


class WarriorsManualPage(Screen):
    pass


class WarriorsManualPage1(Screen):
    pass


class WarriorsManualPage2(Screen):
    pass


class WarriorsManualPage3(Screen):
    pass


class WarriorsManualPage4(Screen):
    pass


class ExercisesPage(Screen):
    pass


class ExercisesPage1(Screen):
    pass


class ExercisesPage2(Screen):
    pass


class ExercisesPage3(Screen):
    pass


class ExercisesPage4(Screen):
    pass


class ExercisesPage5(Screen):
    pass


class StatsPage(Screen):
    pass


class EvalPage(Screen):
    pass


class LeaderboardPage(Screen):
    pass


class KneegrabPage(Screen):
    pass
'''    def savePR(self):
        labelknee = self.ids.prknee
        labelarm = self.ids.prarms
        lblarm = self.ids.lblarm
        lblknee= self.ids.lblknee
        username = open("user.txt").read()

        mycursor.execute("SELECT UserId From Users WHERE Username='"+username+"'")
        results = mycursor.fetchone()

        mycursor.execute("SELECT * From Prs WHERE UserId='" + str(results[0]) + "'")
        results1 = mycursor.fetchone()

        if results1:
            if labelarm.text == '':
                labelarm.text = lblarm.text
            if labelknee.text == '':
                labelknee.text = lblknee.text
            mycursor.execute("UPDATE Prs SET KneePR='"+(str(labelknee.text))+"', ArmPR='"+(str(labelarm.text))+"' WHERE Userid = '"+str(results[0])+"'")
            db.commit()
            kbp = KneegrabPage()
            lblarm.text = kbp.loadArmPR()
            lblknee.text = kbp.loadKneePR()

        if not results1:
            if labelarm.text == '':
                labelarm.text = "0"
            if labelknee.text == '':
                labelknee.text = "0"
            mycursor.execute("INSERT INTO Prs  VALUES (%s,%s,%s)",
                         (int(labelknee.text),int(labelarm.text), results[0]))
            db.commit()
            kbp = KneegrabPage()
            lblarm.text = kbp.loadArmPR()
            lblknee.text = kbp.loadKneePR()


    def loadArmPR(self):

        username = open("user.txt").read()
        mycursor.execute("SELECT UserId From Users WHERE Username='"+username+"'")
        userid = mycursor.fetchone()

        mycursor.execute("SELECT ArmPR From Prs WHERE UserId='" + str(userid[0]) + "'")
        results1 = mycursor.fetchone()

        return str(results1[0])

    def loadKneePR(self):
        username = open("user.txt").read()
        mycursor.execute("SELECT UserId From Users WHERE Username='"+username+"'")
        userid = mycursor.fetchone()

        mycursor.execute("SELECT KneePR From Prs WHERE UserId='" + str(userid[0]) + "'")
        results1 = mycursor.fetchone()

        return str(results1[0])

'''

class AdminPage(Screen):
    def dostuff(self):
        print("IT WORKS YES")

    def get_count(self):
        mycursor.execute("SELECT Count(*) FROM Users")
        results = mycursor.fetchone()[0]
        return "Current user count= " + str(results)


class CreateUserPage(Screen):

    def create_user(self):
        user = self.ids.createuser_username
        pwd = self.ids.createuser_password
        verifypwd = self.ids.createuser_verifypassword
        info = self.ids.info_create_user
        username = user.text
        password = pwd.text
        verifypassword = verifypwd.text

        mycursor.execute("SELECT * FROM Users WHERE username = '" +username+"'")
        results = mycursor.fetchall()

        if results:
            info.text = '[color=#FF0000]Username already exists![/color]'
        if not results:
            if verifypassword == password:
                mycursor.execute("INSERT INTO Users (username, password, admin_rights) VALUES (%s,%s,%s)", (username, hashlib.sha256(password.encode('utf-8')).hexdigest(), True))
                db.commit()
                info.text = '[color=#00FF00]User Created![/color]'
            else:
                info.text = '[color=#FF0000]Passwords discrepancy![/color]'


class DeleteUserPage(Screen):
    def delete_user(self):
        user = self.ids.del_username
        username = user.text
        info = self.ids.info_delete_user
        mycursor.execute("SELECT * FROM Users WHERE username = '" +username+"'")
        results = mycursor.fetchall()

        if results:
            mycursor.execute("DELETE FROM Users WHERE username = '" +username+"'")
            db.commit()
            info.text = '[color=#00FF00]'+username+' has been removed![/color]'

        else:
            info.text = '[color=#FF0000]' +username+ ' not found![/color]'

class UpdateUserPage(Screen):

    def update_user(self):
        user = self.ids.createuser_username
        pwd = self.ids.createuser_password
        verifypwd = self.ids.createuser_verifypassword
        info = self.ids.info_create_user
        username = user.text
        password = pwd.text
        verifypassword = verifypwd.text

        mycursor.execute("SELECT * FROM Users WHERE username = '" +username+"'")
        results = mycursor.fetchall()

        if results:
            info.text = '[color=#FF0000]Username already exists![/color]'
        if not results:
            if verifypassword == password:
                mycursor.execute("INSERT INTO Users (username, password, admin_rights) VALUES (%s,%s,%s)", (username, hashlib.sha256(password.encode('utf-8')).hexdigest(), True))
                db.commit()
                info.text = '[color=#00FF00]User Created![/color]'
            else:
                info.text = '[color=#FF0000]Passwords discrepancy![/color]'


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)

    def on_key(self, window, key, *args):
        if key == 27:  # the esc key
            if self.current_screen.name == "login_page":
                return False  # exit the app from this page
            elif self.current_screen.name == "admin":
                self.current = "login_page"
                return True  # do not exit the app
            elif self.current_screen.name == "user":
                self.current = "login_page"
                return True  # do not exit the app
            elif self.current_screen.name == "create_user_page":
                self.current = "admin"
                return True  # do not exit the app
            elif self.current_screen.name == "delete_user_page":
                self.current = "admin"
                return True  # do not exit the app
            elif self.current_screen.name == "update_user_page":
                self.current = "admin"
                return True  # do not exit the app
            elif self.current_screen.name == "KneegrabPage":
                self.current = "user"
                return True  # do not exit the app
            elif self.current_screen.name == "WarriorsManualPage":
                self.current = "user"
                return True  # do not exit the app
            elif self.current_screen.name == "WarriorsManualPage1":
                self.current = "WarriorsManualPage"
                return True  # do not exit the app
            elif self.current_screen.name == "WarriorsManualPage2":
                self.current = "WarriorsManualPage"
                return True  # do not exit the app
            elif self.current_screen.name == "WarriorsManualPage3":
                self.current = "WarriorsManualPage"
                return True  # do not exit the app
            elif self.current_screen.name == "WarriorsManualPage4":
                self.current = "WarriorsManualPage"
                return True  # do not exit the app
            elif self.current_screen.name == "ExercisesPage":
                self.current = "user"
                return True  # do not exit the app
            elif self.current_screen.name == "ExercisesPage1":
                self.current = "ExercisesPage"
                return True  # do not exit the app
            elif self.current_screen.name == "ExercisesPage2":
                self.current = "ExercisesPage"
                return True  # do not exit the app
            elif self.current_screen.name == "ExercisesPage3":
                self.current = "ExercisesPage"
                return True  # do not exit the app
            elif self.current_screen.name == "ExercisesPage4":
                self.current = "ExercisesPage"
                return True  # do not exit the app
            elif self.current_screen.name == "ExercisesPage5":
                self.current = "ExercisesPage"
                return True  # do not exit the app
            elif self.current_screen.name == "StatsPage":
                self.current = "user"
                return True  # do not exit the app



class TFWApp(App):

    def builder(self):
        pass


if __name__ == '__main__':
    TFWApp().run()









#mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Users (username VARCHAR(20) NOT NULL, password VARCHAR(100) NOT NULL, admin_rights boolean NOT NULL, userID int PRIMARY KEY AUTO_INCREMENT)")


#mycursor.execute("INSERT INTO Users (username, password, admin_rights) VALUES (%s,%s,%s)", ("Daviid9400", hashedpw2, True))
#db.commit()


#engine = create_engine('mysql+mysqlconnector://daviid:Ubuntob0I!@172.104.148.212/Tfw')

#connection = engine.raw_connection()

#mycursor = connection.cursor()





  # hash_object = hashlib.sha256(password.encode('utf-8'))
      #  hashedpw = hash_object.hexdigest()