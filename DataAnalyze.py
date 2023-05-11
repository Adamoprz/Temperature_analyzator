import pandas as pd
import os

"""Config - define the localization of the config file"""
config = str(os.getcwd()) + '\\config.ini'



class DataAnalyze:
    """Class DataAnalyze responsible to read data from sensors into using Pandas. """

    def __init__(self) -> None:
        self.data = "1\n2\n3\n4\n5\n"
        self.data1 = ''
        self.find_el = 0
        self.df = {}
        f = open(config, 'r')
        self.path_files = str(f.readline())
        self.week = 10
        self.number = None

    def read_files(self, sensor: str) -> None:
        src = self.path_files
        self.df[sensor] = pd.read_csv(f"{src}/{sensor}.dat", sep=',', names=["Date", "Temperature" ])
        self.df[sensor]['Date_new'] = pd.to_datetime(self.df[sensor]['Date'], format="%Y-%m-%d %H:%M")