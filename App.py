import tkinter as tk
import tkinter.font as tkFont
from datetime import datetime
from tkinter import *
import threading
import matplotlib.pyplot as plt
from DataAnalyze import *
from tkinter.ttk import Style

class App:
    """Class App used to generate Window, Generate the plot"""
    def __init__(self, root):
        self.sensor_names = {'01': 'X1', '02': 'X2', '03': 'X3', '04': 'X4', '05': 'X5', '06': 'X6', '07': 'Y1',
                             '08': 'Y2', '09': 'Y3', '10': 'Z1', '11': 'Z2', '12': 'Z3', '13': 'Head', '14': '14',
                             '15': '15', '16': '16'}
        self.if_result = False
        self.if_found_in_database = False
        # setting title
        root.title("Analiza danych")
        # setting window size
        width = 600
        height = 640
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.checkbox_dict = {}
        for i in range(1, 17, 1):
            self.checkbox_dict[i] = 1
        self.range_time = 0
        self.breakops = False

        GButton_186 = tk.Button(root)
        GButton_186["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_186["font"] = ft
        GButton_186["fg"] = "#000000"
        GButton_186["justify"] = "center"
        GButton_186["text"] = "Sprawdz Dobowy Wzrost"
        GButton_186.place(x=5, y=260, width=160, height=30)
        GButton_186["command"] = self.GButton_186_command_

        GButton_187 = tk.Button(root)
        GButton_187["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_187["font"] = ft
        GButton_187["fg"] = "#000000"
        GButton_187["justify"] = "center"
        GButton_187["text"] = "Sprawdz Godzinowy Wzrost"
        GButton_187.place(x=5, y=290, width=160, height=30)
        GButton_187["command"] = self.GButton_187_command_

        GButton_390 = tk.Button(root)
        GButton_390["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_390["font"] = ft
        GButton_390["fg"] = "#000000"
        GButton_390["justify"] = "center"
        GButton_390["text"] = "Generuj wykres"
        GButton_390.place(x=5, y=230, width=160, height=30)
        GButton_390["command"] = self.GButton_390_command

        self.GMessage_953 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GMessage_953["font"] = ft
        self.GMessage_953["fg"] = "#333333"
        self.GMessage_953["justify"] = "center"
        self.GMessage_953["text"] = ""
        self.GMessage_953.place(x=120, y=350, width=338, height=300)

        self.GCheckBox_145 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheckBox_145["font"] = ft
        self.GCheckBox_145["fg"] = "#333333"
        self.GCheckBox_145["justify"] = "center"
        self.GCheckBox_145["text"] = "Analizuj do daty"
        self.GCheckBox_145.place(x=310, y=215, width=110, height=40)
        self.GCheckBox_145["offvalue"] = "0"
        self.GCheckBox_145["onvalue"] = "1"
        self.CheckVar17 = IntVar()
        self.GCheckBox_145["variable"] = self.CheckVar17
        self.GCheckBox_145["command"] = self.GCheckBox_145_command

        self.GCheck_1 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_1["font"] = ft
        self.GCheck_1["fg"] = "#333333"
        self.GCheck_1["justify"] = "center"
        self.GCheck_1["text"] = "01"
        self.GCheck_1.place(x=10, y=90, width=30, height=25)
        self.GCheck_1["offvalue"] = "0"
        self.GCheck_1["onvalue"] = "1"
        self.CheckVar1 = IntVar()
        self.GCheck_1["variable"] = self.CheckVar1
        self.GCheck_1.select()
        self.GCheck_1["command"] = self.GCheck_1_command

        self.GCheck_2 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_2["font"] = ft
        self.GCheck_2["fg"] = "#333333"
        self.GCheck_2["justify"] = "center"
        self.GCheck_2["text"] = "02"
        self.GCheck_2.place(x=40, y=90, width=30, height=25)
        self.GCheck_2["offvalue"] = "0"
        self.GCheck_2["onvalue"] = "1"
        self.CheckVar2 = IntVar()
        self.GCheck_2["variable"] = self.CheckVar2
        self.GCheck_2.select()
        self.GCheck_2["command"] = self.GCheck_2_command

        self.GCheck_3 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_3["font"] = ft
        self.GCheck_3["fg"] = "#333333"
        self.GCheck_3["justify"] = "center"
        self.GCheck_3["text"] = "03"
        self.GCheck_3.place(x=70, y=90, width=30, height=25)
        self.GCheck_3["offvalue"] = "0"
        self.GCheck_3["onvalue"] = "1"
        self.CheckVar3 = IntVar()
        self.GCheck_3["variable"] = self.CheckVar3
        self.GCheck_3.select()
        self.GCheck_3["command"] = self.GCheck_3_command

        self.GCheck_4 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_4["font"] = ft
        self.GCheck_4["fg"] = "#333333"
        self.GCheck_4["justify"] = "center"
        self.GCheck_4["text"] = "04"
        self.GCheck_4.place(x=100, y=90, width=30, height=25)
        self.GCheck_4["offvalue"] = "0"
        self.GCheck_4["onvalue"] = "1"
        self.CheckVar4 = IntVar()
        self.GCheck_4["variable"] = self.CheckVar4
        self.GCheck_4.select()
        self.GCheck_4["command"] = self.GCheck_4_command

        self.GCheck_5 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_5["font"] = ft
        self.GCheck_5["fg"] = "#333333"
        self.GCheck_5["justify"] = "center"
        self.GCheck_5["text"] = "05"
        self.GCheck_5.place(x=130, y=90, width=30, height=25)
        self.GCheck_5["offvalue"] = "0"
        self.GCheck_5["onvalue"] = "1"
        self.CheckVar5 = IntVar()
        self.GCheck_5["variable"] = self.CheckVar5
        self.GCheck_5.select()
        self.GCheck_5["command"] = self.GCheck_5_command

        self.GCheck_6 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_6["font"] = ft
        self.GCheck_6["fg"] = "#333333"
        self.GCheck_6["justify"] = "center"
        self.GCheck_6["text"] = "06"
        self.GCheck_6.place(x=160, y=90, width=30, height=25)
        self.GCheck_6["offvalue"] = "0"
        self.GCheck_6["onvalue"] = "1"
        self.CheckVar6 = IntVar()
        self.GCheck_6["variable"] = self.CheckVar6
        self.GCheck_6.select()
        self.GCheck_6["command"] = self.GCheck_6_command

        self.GCheck_7 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_7["font"] = ft
        self.GCheck_7["fg"] = "#333333"
        self.GCheck_7["justify"] = "center"
        self.GCheck_7["text"] = "07"
        self.GCheck_7.place(x=190, y=90, width=30, height=25)
        self.GCheck_7["offvalue"] = "0"
        self.GCheck_7["onvalue"] = "1"
        self.CheckVar7 = IntVar()
        self.GCheck_7["variable"] = self.CheckVar7
        self.GCheck_7.select()
        self.GCheck_7["command"] = self.GCheck_7_command

        self.GCheck_8 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_8["font"] = ft
        self.GCheck_8["fg"] = "#333333"
        self.GCheck_8["justify"] = "center"
        self.GCheck_8["text"] = "08"
        self.GCheck_8.place(x=220, y=90, width=30, height=25)
        self.GCheck_8["offvalue"] = "0"
        self.GCheck_8["onvalue"] = "1"
        self.CheckVar8 = IntVar()
        self.GCheck_8["variable"] = self.CheckVar8
        self.GCheck_8.select()
        self.GCheck_8["command"] = self.GCheck_8_command

        self.GCheck_9 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_9["font"] = ft
        self.GCheck_9["fg"] = "#333333"
        self.GCheck_9["justify"] = "center"
        self.GCheck_9["text"] = "09"
        self.GCheck_9.place(x=250, y=90, width=30, height=25)
        self.GCheck_9["offvalue"] = "0"
        self.GCheck_9["onvalue"] = "1"
        self.CheckVar9 = IntVar()
        self.GCheck_9["variable"] = self.CheckVar9
        self.GCheck_9.select()
        self.GCheck_9["command"] = self.GCheck_9_command

        self.GCheck_10 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_10["font"] = ft
        self.GCheck_10["fg"] = "#333333"
        self.GCheck_10["justify"] = "center"
        self.GCheck_10["text"] = "10"
        self.GCheck_10.place(x=280, y=90, width=30, height=25)
        self.GCheck_10["offvalue"] = "0"
        self.GCheck_10["onvalue"] = "1"
        self.CheckVar10 = IntVar()
        self.GCheck_10["variable"] = self.CheckVar10
        self.GCheck_10.select()
        self.GCheck_10["command"] = self.GCheck_10_command

        self.GCheck_11 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_11["font"] = ft
        self.GCheck_11["fg"] = "#333333"
        self.GCheck_11["justify"] = "center"
        self.GCheck_11["text"] = "11"
        self.GCheck_11.place(x=310, y=90, width=30, height=25)
        self.GCheck_11["offvalue"] = "0"
        self.GCheck_11["onvalue"] = "1"
        self.CheckVar11 = IntVar()
        self.GCheck_11["variable"] = self.CheckVar11
        self.GCheck_11.select()
        self.GCheck_11["command"] = self.GCheck_11_command

        self.GCheck_12 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_12["font"] = ft
        self.GCheck_12["fg"] = "#333333"
        self.GCheck_12["justify"] = "center"
        self.GCheck_12["text"] = "12"
        self.GCheck_12.place(x=340, y=90, width=30, height=25)
        self.GCheck_12["offvalue"] = "0"
        self.GCheck_12["onvalue"] = "1"
        self.CheckVar12 = IntVar()
        self.GCheck_12["variable"] = self.CheckVar12
        self.GCheck_12.select()
        self.GCheck_12["command"] = self.GCheck_12_command

        self.GCheck_13 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_13["font"] = ft
        self.GCheck_13["fg"] = "#333333"
        self.GCheck_13["justify"] = "center"
        self.GCheck_13["text"] = "13"
        self.GCheck_13.place(x=370, y=90, width=30, height=25)
        self.GCheck_13["offvalue"] = "0"
        self.GCheck_13["onvalue"] = "1"
        self.CheckVar13 = IntVar()
        self.GCheck_13["variable"] = self.CheckVar13
        self.GCheck_13.select()
        self.GCheck_13["command"] = self.GCheck_13_command

        self.GCheck_14 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_14["font"] = ft
        self.GCheck_14["fg"] = "#333333"
        self.GCheck_14["justify"] = "center"
        self.GCheck_14["text"] = "14"
        self.GCheck_14.place(x=400, y=90, width=30, height=25)
        self.GCheck_14["offvalue"] = "0"
        self.GCheck_14["onvalue"] = "1"
        self.CheckVar14 = IntVar()
        self.GCheck_14["variable"] = self.CheckVar14
        self.GCheck_14.select()
        self.GCheck_14["command"] = self.GCheck_14_command

        self.GCheck_15 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_15["font"] = ft
        self.GCheck_15["fg"] = "#333333"
        self.GCheck_15["justify"] = "center"
        self.GCheck_15["text"] = "15"
        self.GCheck_15.place(x=430, y=90, width=30, height=25)
        self.GCheck_15["offvalue"] = "0"
        self.GCheck_15["onvalue"] = "1"
        self.CheckVar15 = IntVar()
        self.GCheck_15["variable"] = self.CheckVar15
        self.GCheck_15.select()
        self.GCheck_15["command"] = self.GCheck_15_command

        self.GCheck_16 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GCheck_16["font"] = ft
        self.GCheck_16["fg"] = "#333333"
        self.GCheck_16["justify"] = "center"
        self.GCheck_16["text"] = "16"
        self.GCheck_16.place(x=460, y=90, width=30, height=25)
        # self.GCheck_16["offvalue"] = "0"
        # self.GCheck_16["onvalue"] = "1"

        self.CheckVar16 = IntVar()
        self.GCheck_16["variable"] = self.CheckVar16
        self.GCheck_16.select()
        self.GCheck_16["command"] = self.GCheck_16_command

        self.GLabel_01 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_01["font"] = ft
        self.GLabel_01["fg"] = "#333333"
        self.GLabel_01["justify"] = "center"
        self.GLabel_01["text"] = "-"
        self.GLabel_01.place(x=10, y=130, width=30, height=25)

        self.GLabel_02 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_02["font"] = ft
        self.GLabel_02["fg"] = "#333333"
        self.GLabel_02["justify"] = "center"
        self.GLabel_02["text"] = "-"
        self.GLabel_02.place(x=40, y=130, width=30, height=25)

        self.GLabel_03 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_03["font"] = ft
        self.GLabel_03["fg"] = "#333333"
        self.GLabel_03["justify"] = "center"
        self.GLabel_03["text"] = "-"
        self.GLabel_03.place(x=70, y=130, width=30, height=25)

        self.GLabel_04 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_04["font"] = ft
        self.GLabel_04["fg"] = "#333333"
        self.GLabel_04["justify"] = "center"
        self.GLabel_04["text"] = "-"
        self.GLabel_04.place(x=100, y=130, width=30, height=25)

        self.GLabel_05 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_05["font"] = ft
        self.GLabel_05["fg"] = "#333333"
        self.GLabel_05["justify"] = "center"
        self.GLabel_05["text"] = "-"
        self.GLabel_05.place(x=130, y=130, width=30, height=25)

        self.GLabel_06 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_06["font"] = ft
        self.GLabel_06["fg"] = "#333333"
        self.GLabel_06["justify"] = "center"
        self.GLabel_06["text"] = "-"
        self.GLabel_06.place(x=160, y=130, width=30, height=25)

        self.GLabel_07 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_07["font"] = ft
        self.GLabel_07["fg"] = "#333333"
        self.GLabel_07["justify"] = "center"
        self.GLabel_07["text"] = "-"
        self.GLabel_07.place(x=190, y=130, width=30, height=25)

        self.GLabel_08 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_08["font"] = ft
        self.GLabel_08["fg"] = "#333333"
        self.GLabel_08["justify"] = "center"
        self.GLabel_08["text"] = "-"
        self.GLabel_08.place(x=220, y=130, width=30, height=25)

        self.GLabel_09 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_09["font"] = ft
        self.GLabel_09["fg"] = "#333333"
        self.GLabel_09["justify"] = "center"
        self.GLabel_09["text"] = "-"
        self.GLabel_09.place(x=250, y=130, width=30, height=25)

        self.GLabel_10 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_10["font"] = ft
        self.GLabel_10["fg"] = "#333333"
        self.GLabel_10["justify"] = "center"
        self.GLabel_10["text"] = "-"
        self.GLabel_10.place(x=280, y=130, width=30, height=25)

        self.GLabel_11 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_11["font"] = ft
        self.GLabel_11["fg"] = "#333333"
        self.GLabel_11["justify"] = "center"
        self.GLabel_11["text"] = "-"
        self.GLabel_11.place(x=310, y=130, width=30, height=25)

        self.GLabel_12 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_12["font"] = ft
        self.GLabel_12["fg"] = "#333333"
        self.GLabel_12["justify"] = "center"
        self.GLabel_12["text"] = "-"
        self.GLabel_12.place(x=340, y=130, width=30, height=25)

        self.GLabel_13 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_13["font"] = ft
        self.GLabel_13["fg"] = "#333333"
        self.GLabel_13["justify"] = "center"
        self.GLabel_13["text"] = "-"
        self.GLabel_13.place(x=370, y=130, width=30, height=25)

        self.GLabel_14 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_14["font"] = ft
        self.GLabel_14["fg"] = "#333333"
        self.GLabel_14["justify"] = "center"
        self.GLabel_14["text"] = "-"
        self.GLabel_14.place(x=400, y=130, width=30, height=25)

        self.GLabel_15 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_15["font"] = ft
        self.GLabel_15["fg"] = "#333333"
        self.GLabel_15["justify"] = "center"
        self.GLabel_15["text"] = "-"
        self.GLabel_15.place(x=430, y=130, width=30, height=25)

        self.GLabel_16 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_16["font"] = ft
        self.GLabel_16["fg"] = "#333333"
        self.GLabel_16["justify"] = "center"
        self.GLabel_16["text"] = "-"
        self.GLabel_16.place(x=460, y=130, width=30, height=25)

        self.GLineEdit_805 = tk.Entry(root)
        self.GLineEdit_805["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_805["font"] = ft
        self.GLineEdit_805["fg"] = "#333333"
        self.GLineEdit_805["justify"] = "center"
        a = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.GLineEdit_805.insert(0, str(a))
        self.GLineEdit_805.place(x=170, y=260, width=129, height=30)

        self.GMessage_317 = tk.Message(root)
        ft = tkFont.Font(family='Arial', size=9)
        self.GMessage_317["font"] = ft
        self.GMessage_317["fg"] = "#333333"
        self.GMessage_317["justify"] = "center"
        self.GMessage_317["text"] = "Podaj date do analizy"
        self.GMessage_317.place(x=190, y=220, width=90, height=40)

        self.GButton_657 = tk.Button(root)
        self.GButton_657["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=14)
        self.GButton_657["font"] = ft
        self.GButton_657["fg"] = "#000000"
        self.GButton_657["justify"] = "center"
        self.GButton_657["text"] = "Pobierz Dane"
        self.GButton_657.place(x=200, y=30, width=150, height=30)
        self.GButton_657["command"] = self.GButton_657_command_

        self.rframe = Frame(root)

        self.rframe.pack()
        self.rframe.place(x=430, y=220, width=110, height=110)

        self.v = StringVar(self.rframe, "4")
        self.style = Style(self.rframe)
        self.style.configure("TRadiobutton",
                             foreground="black", font=("arial", 10, "bold"))
        # Dictionary to create multiple buttons
        self.values = {"Dzień ": 1,
                       "Tydzień": 2,
                       "Miesiąc": 3,
                       "Pełny zakres": 4}

        for (text, value) in self.values.items():
            Radiobutton(self.rframe, text=text, variable=self.v,
                        value=value, command=self.GRadio_313_command).pack(side=TOP, ipady=4, anchor='w')

    def GButton_186_command_(self):
        threading.Thread(target=self.GButton_186_command).start()

    def GButton_186_command(self):

        a = 'Dobowy wzrost wynosi: \n'

        for key in self.data1.df.keys():
            if self.checkbox_dict[int(key)]:
                tab1 = self.data1.df[key]["Temperature"]
                length1 = len(tab1)
                temp = length1
                if self.if_found_in_database and self.CheckVar17.get():
                    if temp != 0:
                        length1 = self.number
                time = self.range_time
                w = length1 - time
                data1 = self.data1.df[key]["Date_new"][w]
                if self.range_time == 0:
                    w = 0
                x = []
                count = 0

                while (w + 24 * 60 <= length1):
                    x.append(max(self.data1.df[key]["Temperature"][w:w + 24 * 60]) - min(
                        self.data1.df[key]["Temperature"][w:w + 24 * 60]))
                    count += 1
                    w += 1
                a1 = f'Dla czujnika {self.sensor_names[key]} wynosi: {max(x):.2f}'
                a = str(a) + str(a1) + str('\n')
                self.GMessage_953["text"] = a

    def GButton_187_command_(self):
        threading.Thread(target=self.GButton_187_command).start()

    def GButton_187_command(self):
        a = 'Godzinowy wzrost wynosi: \n'
        for key in self.data1.df.keys():
            if self.checkbox_dict[int(key)]:
                tab1 = self.data1.df[key]["Temperature"]
                length1 = len(tab1)
                temp = length1
                if self.if_found_in_database and self.CheckVar17.get():
                    # print("ok")
                    if temp != 0:
                        length1 = self.number
                time = self.range_time
                w = length1 - time
                if self.range_time == 0:
                    w = 0
                x = []
                count = 0

                while (w + 60 <= length1):
                    x.append(max(self.data1.df[key]["Temperature"][w:w + 60]) - min(
                        self.data1.df[key]["Temperature"][w:w + 60]))
                    count += 1
                    w += 1

                # print(f'maks godzinowy czujnik {key} wynosi {max(x):.2f}')
                a1 = f'dla czujnika {self.sensor_names[key]} wynosi: {max(x):.2f}'
                a = str(a) + str(a1) + str('\n')
                self.GMessage_953["text"] = a

    def stop(self):
        self.breakops = True

    def threading(function):
        # Call work function
        t1 = Thread(target=function)
        t1.start()

    def GButton_390_command(self):
        self.show_plot()

    def GCheck_1_command(self):
        self.checkbox_dict[1] = self.CheckVar1.get()

    def GCheck_2_command(self):
        self.checkbox_dict[2] = self.CheckVar2.get()

    def GCheck_3_command(self):
        self.checkbox_dict[3] = self.CheckVar3.get()

    def GCheck_4_command(self):
        self.checkbox_dict[4] = self.CheckVar4.get()

    def GCheck_5_command(self):
        self.checkbox_dict[5] = self.CheckVar5.get()

    def GCheck_6_command(self):
        self.checkbox_dict[6] = self.CheckVar6.get()

    def GCheck_7_command(self):
        self.checkbox_dict[7] = self.CheckVar7.get()

    def GCheck_8_command(self):
        self.checkbox_dict[8] = self.CheckVar8.get()

    def GCheck_9_command(self):
        self.checkbox_dict[9] = self.CheckVar9.get()

    def GCheck_10_command(self):
        self.checkbox_dict[10] = self.CheckVar10.get()

    def GCheck_11_command(self):
        self.checkbox_dict[11] = self.CheckVar11.get()

    def GCheck_12_command(self):
        self.checkbox_dict[12] = self.CheckVar12.get()

    def GCheck_13_command(self):
        self.checkbox_dict[13] = self.CheckVar13.get()

    def GCheck_14_command(self):
        self.checkbox_dict[14] = self.CheckVar14.get()

    def GCheck_15_command(self):
        self.checkbox_dict[15] = self.CheckVar15.get()

    def GCheck_16_command(self):
        self.checkbox_dict[16] = self.CheckVar16.get()

    def GCheckBox_145_command(self):
        if_from_date = self.CheckVar17.get()
        a = self.GLineEdit_805.get()
        b = datetime.strptime(a, "%Y-%m-%d %H:%M")
        self.if_found_in_database = False
        for enum, x in enumerate(self.data1.df['01']["Date"]):

            if str(b)[:16] == str(x)[:16]:
                self.if_found_in_database = True
                self.number = enum
        if not self.if_found_in_database:
            messagebox.showerror("Popraw Date", "Daty nie odnaleziono \n Wpisz Poprawna date")

    def GButton_657_command(self):

        self.data1 = DataAnalyze()
        if self.if_result == True:
            self.reset()
        # del dialog
        # del data1
        # self.data1.read_files(self.src, self.dialog.folder)
        sensors = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']

        for element in sensors:
            self.data1.read_files(element)
            if element[0:2] == '01':
                self.GLabel_01["text"] = 'OK'
            if element[0:2] == '02':
                self.GLabel_02["text"] = 'OK'
            if element[0:2] == '03':
                self.GLabel_03["text"] = 'OK'
            if element[0:2] == '04':
                self.GLabel_04["text"] = 'OK'
            if element[0:2] == '05':
                self.GLabel_05["text"] = 'OK'
            if element[0:2] == '06':
                self.GLabel_06["text"] = 'OK'
            if element[0:2] == '07':
                self.GLabel_07["text"] = 'OK'
            if element[0:2] == '08':
                self.GLabel_08["text"] = 'OK'
            if element[0:2] == '09':
                self.GLabel_09["text"] = 'OK'
            if element[0:2] == '10':
                self.GLabel_10["text"] = 'OK'
            if element[0:2] == '11':
                self.GLabel_11["text"] = 'OK'
            if element[0:2] == '12':
                self.GLabel_12["text"] = 'OK'
            if element[0:2] == '13':
                self.GLabel_13["text"] = 'OK'
            if element[0:2] == '14':
                self.GLabel_14["text"] = 'OK'
            if element[0:2] == '15':
                self.GLabel_15["text"] = 'OK'
            if element[0:2] == '16':
                self.GLabel_16["text"] = 'OK'
        self.if_result = True
        self.GButton_657["text"] = 'Pobierz ponownie'
        self.GLineEdit_805.delete(0, 'end')
        # w = self.data1.df[16]["Date_new"]
        w = self.data1.df['01']["Date_new"][len(self.data1.df['01']["Date_new"]) - 1]
        self.GLineEdit_805.insert(0, w.strftime("%Y-%m-%d %H:%M"))

    def GButton_657_command_(self):
        threading.Thread(target=self.GButton_657_command).start()

    def GRadio_313_command(self):
        range_time = {1: 24 * 60, 2: 7 * 24 * 60, 3: 30 * 24 * 60, 4: 0}
        self.range_time = range_time[int(self.v.get())]

    def GRadio_532_command(self):
        pass

    def GRadio_94_command(self):
        pass

    def update_check_dict(self, sensor_ifselect):
        pass

    def reset(self):

        self.GLabel_01["text"] = '-'
        self.GLabel_02["text"] = '-'
        self.GLabel_03["text"] = '-'
        self.GLabel_04["text"] = '-'
        self.GLabel_05["text"] = '-'
        self.GLabel_06["text"] = '-'
        self.GLabel_07["text"] = '-'
        self.GLabel_08["text"] = '-'
        self.GLabel_09["text"] = '-'
        self.GLabel_10["text"] = '-'
        self.GLabel_11["text"] = '-'
        self.GLabel_12["text"] = '-'
        self.GLabel_13["text"] = '-'
        self.GLabel_14["text"] = '-'
        self.GLabel_15["text"] = '-'
        self.GLabel_16["text"] = '-'

    def show_plot(self):
        for key in self.data1.df.keys():
            if self.checkbox_dict[int(key)]:
                temp = len(self.data1.df[key]["Date_new"])
                if self.if_found_in_database and self.CheckVar17.get():
                    if temp != 0:
                        temp = self.number
                if self.range_time == 0:
                    self.range_time = temp
                plt.plot(self.data1.df[key]["Date_new"][temp - self.range_time:temp],
                         self.data1.df[key]["Temperature"][temp - self.range_time:temp],
                         label=self.sensor_names[key])

        plt.ylabel('Temperatura')
        plt.ylim(15, 25)
        plt.legend(fontsize=5, loc='lower left')
        plt.axhline(y=19, color='blue', linestyle='-', linewidth=0.5)
        plt.axhline(y=21, color='red', linestyle='-', linewidth=0.5)
        plt.gcf().autofmt_xdate()
        plt.show()
