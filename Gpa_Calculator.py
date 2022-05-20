from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


def gpa_calc(number):
    if 90 <= number <= 100:
        return "4.00"
    elif 85 <= number < 90:
        return "3.70"
    elif 80 <= number < 85:
        return "3.30"
    elif 75 <= number < 80:
        return "3.00"
    elif 70 <= number < 75:
        return "2.70"
    elif 65 <= number < 70:
        return "2.30"
    elif 60 <= number < 65:
        return "2.00"
    elif 57 <= number < 60:
        return "1.70"
    elif 55 <= number < 57:
        return "1.30"
    elif 52 <= number < 55:
        return "1.00"
    elif 50 <= number < 52:
        return "0.70"
    elif 0 <= number < 50:
        return "0.00"


class WelcomeScreen(Screen):
    def get_pressed(self):
        self.manager.get_screen("MenuScreen").ids.back_image.source = 'data/icons/back.png'


class MenuScreen(Screen):
    def pressed(self):
        self.ids.back_image.source = 'data/icons/back2.png'

    def cse_pressed(self):
        self.manager.get_screen("CseGPA").ids.back_image_cse.source = 'data/icons/back.png'

    def mat_pressed(self):
        self.manager.get_screen("MatGPA").ids.back_image_cse.source = 'data/icons/back.png'

    def phy_pressed(self):
        self.manager.get_screen("PhyGPA").ids.back_image_cse.source = 'data/icons/back.png'

    def eng_pressed(self):
        self.manager.get_screen("EngGPA").ids.back_image_cse.source = 'data/icons/back.png'


class CseCGPA(Screen):
    nam = ObjectProperty(None)
    stu_id = ObjectProperty(None)
    mid = ObjectProperty(None)
    lab = ObjectProperty(None)
    quiz_1 = ObjectProperty(None)
    quiz_2 = ObjectProperty(None)
    quiz_3 = ObjectProperty(None)
    attendance = ObjectProperty(None)
    final = ObjectProperty(None)
    result = ObjectProperty(None)
    btn = ObjectProperty(None)

    button_flag = True

    def pressed_cse(self):
        self.ids.back_image_cse.source = 'data/icons/back2.png'
        self.manager.get_screen("MenuScreen").ids.back_image.source = 'data/icons/back.png'


    def calculate(self):
        if self.button_flag:
            try:
                number = float(self.mid.text)+float(self.lab.text)+float(self.attendance.text)+float(self.final.text)
                list_of_quiz = [float(self.quiz_1.text), float(self.quiz_2.text), float(self.quiz_3.text)]
                list_of_quiz.sort(reverse=True)
                quiz = (list_of_quiz[0]+list_of_quiz[1])
                self.result.text = f"Name: {self.nam.text}\nID: {self.stu_id.text}\nNumber: {number+quiz}\nGPA: {gpa_calc(number+quiz)}"
            except:
                self.result.text = "Wrong Input"

            self.btn.text = "Calculate Next"
            self.button_flag = False
        else:
            self.nam.text = ""
            self.stu_id.text = ""
            self.lab.text = ""
            self.quiz_1.text = ""
            self.quiz_2.text = ""
            self.quiz_3.text = ""
            self.attendance.text = ""
            self.mid.text = ""
            self.final.text = ""
            self.result.text = ""
            self.btn.text = "Calculate"
            self.button_flag = True


class MatCGPA(Screen):
    nam = ObjectProperty(None)
    stu_id = ObjectProperty(None)
    mid = ObjectProperty(None)
    lab = ObjectProperty(None)
    quiz_1 = ObjectProperty(None)
    quiz_2 = ObjectProperty(None)
    quiz_3 = ObjectProperty(None)
    attendance = ObjectProperty(None)
    final = ObjectProperty(None)
    result = ObjectProperty(None)
    btn = ObjectProperty(None)

    button_flag = True

    def pressed_mat(self):
        self.ids.back_image_cse.source = 'data/icons/back2.png'
        self.manager.get_screen("MenuScreen").ids.back_image.source = 'data/icons/back.png'

    def calculate_mat(self):
        if self.button_flag:
            try:
                number = ((float(self.mid.text)/250)*20) + float(self.lab.text)+float(self.attendance.text)+((float(self.final.text)/300)*30)
                list_of_quiz = [float(self.quiz_1.text), (float(self.quiz_2.text)/20)*25, (float(self.quiz_3.text)/15)*25]
                list_of_quiz.sort(reverse=True)
                quiz = (list_of_quiz[0]+list_of_quiz[1])/2
                self.result.text = f"Name: {self.nam.text}\nID: {self.stu_id.text}\nNumber: {number+quiz}\nGPA: {gpa_calc(number+quiz)}"
            except:
                self.result.text = "Wrong Input"

            self.btn.text = "Calculate Next"
            self.button_flag = False
        else:
            self.nam.text = ""
            self.stu_id.text = ""
            self.lab.text = ""
            self.quiz_1.text = ""
            self.quiz_2.text = ""
            self.quiz_3.text = ""
            self.attendance.text = ""
            self.mid.text = ""
            self.final.text = ""
            self.result.text = ""
            self.btn.text = "Calculate"
            self.button_flag = True


class PhyCGPA(Screen):
    nam = ObjectProperty(None)
    stu_id = ObjectProperty(None)
    mid = ObjectProperty(None)
    lab = ObjectProperty(None)
    quiz_1 = ObjectProperty(None)
    quiz_2 = ObjectProperty(None)
    quiz_3 = ObjectProperty(None)
    attendance = ObjectProperty(None)
    final = ObjectProperty(None)
    result = ObjectProperty(None)
    btn = ObjectProperty(None)

    button_flag = True

    def pressed_phy(self):
        self.ids.back_image_cse.source = 'data/icons/back2.png'
        self.manager.get_screen("MenuScreen").ids.back_image.source = 'data/icons/back.png'

    def calculate_phy(self):
        if self.button_flag:
            try:
                number = ((float(self.mid.text)/40)*20) + float(self.lab.text)+float(self.attendance.text)+float(self.final.text)
                number += float(self.ids.report.text)
                list_of_quiz = [float(self.quiz_1.text), float(self.quiz_2.text), float(self.quiz_3.text), float(self.ids.quiz4.text), float(self.ids.quiz5.text)]
                list_of_quiz.sort(reverse=True)
                quiz = (list_of_quiz[0]+list_of_quiz[1]+list_of_quiz[2]+list_of_quiz[3])/4
                self.result.text = f"Name: {self.nam.text}\nID: {self.stu_id.text}\nNumber: {number+quiz}\nGPA: {gpa_calc(number+quiz)}"
            except:
                self.result.text = "Wrong Input"

            self.btn.text = "Calculate Next"
            self.button_flag = False
        else:
            self.nam.text = ""
            self.stu_id.text = ""
            self.lab.text = ""
            self.quiz_1.text = ""
            self.quiz_2.text = ""
            self.quiz_3.text = ""
            self.ids.quiz4.text = ""
            self.ids.quiz5.text = ""
            self.ids.report.text = ""
            self.attendance.text = ""
            self.mid.text = ""
            self.final.text = ""
            self.result.text = ""
            self.btn.text = "Calculate"
            self.button_flag = True


class EngCGPA(Screen):
    nam = ObjectProperty(None)
    stu_id = ObjectProperty(None)
    mid = ObjectProperty(None)
    lab = ObjectProperty(None)
    quiz_1 = ObjectProperty(None)
    quiz_2 = ObjectProperty(None)
    quiz_3 = ObjectProperty(None)
    attendance = ObjectProperty(None)
    final = ObjectProperty(None)
    result = ObjectProperty(None)
    btn = ObjectProperty(None)

    button_flag = True

    def pressed_eng(self):
        self.ids.back_image_cse.source = 'data/icons/back2.png'
        self.manager.get_screen("MenuScreen").ids.back_image.source = 'data/icons/back.png'

    def calculate(self):
        if self.button_flag:
            try:
                number = float(self.mid.text) + float(self.ids.act_pre.text)+float(self.attendance.text)+float(self.final.text)
                number += float(self.ids.journal_pre.text) + float(self.ids.lis_quiz.text)+float(self.ids.debate.text)
                number += float(self.ids.assign.text) + float(self.ids.journal_ent.text) + float(self.ids.dls.text)
                list_of_quiz = [float(self.quiz_1.text), float(self.quiz_2.text), float(self.quiz_3.text), float(self.ids.quiz4.text)]
                list_of_quiz.sort(reverse=True)
                quiz = (list_of_quiz[0]+list_of_quiz[1]+list_of_quiz[2])/3
                self.result.text = f"Name: {self.nam.text}\nID: {self.stu_id.text}\nNumber: {number+quiz}\nGPA: {gpa_calc(number+quiz)}"
            except:
                self.result.text = "Wrong Input"

            self.btn.text = "Calculate Next"
            self.button_flag = False
        else:
            self.ids.debate.text = ""
            self.nam.text = ""
            self.stu_id.text = ""
            self.quiz_1.text = ""
            self.quiz_2.text = ""
            self.quiz_3.text = ""
            self.ids.quiz4.text = ""
            self.ids.act_pre.text = ""
            self.ids.assign.text = ""
            self.ids.dls.text = ""
            self.ids.journal_pre.text = ""
            self.ids.journal_ent.text = ""
            self.ids.lis_quiz.text = ""
            self.attendance.text = ""
            self.mid.text = ""
            self.final.text = ""
            self.result.text = ""
            self.btn.text = "Calculate"
            self.button_flag = True


class Manager(ScreenManager):
    pass


kv = Builder.load_file("Gpa_Calculator.kv")


class GPA_CalculatorApp(App):  # takes the func name as default for title bar
    # App class (using parent class constructor)
    def build(self):  #
        Window.clearcolor = (61/255, 61/255, 61/255, 1)
        return kv  # returning a class


if __name__ == "__main__":
    GPA_CalculatorApp().run(

    )