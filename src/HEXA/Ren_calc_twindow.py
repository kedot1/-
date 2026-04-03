from PySide6.QtWidgets import (QApplication, QSpinBox, QDoubleSpinBox, QLineEdit, QPushButton,
        QLabel, QComboBox, QRadioButton, QButtonGroup, QWidget, QGridLayout)
from PySide6.QtGui import QDoubleValidator
#from GUI_calc import is_input
import math, time

#Dot Damage 0.5秒周期
class SecondWindow(QWidget):
    def __init__(self, parent_window, parent=None):
        super().__init__()

        self.setWindowTitle("HEXA")
    # ウィンドウサイズを指定（px単位）
        windowWidth = 1300  # ウィンドウの横幅
        windowHeight = 500  # ウィンドウの高さ
    # ウィンドウサイズの変更
        self.resize(windowWidth, windowHeight)
        self.setFixedSize(1300, 500)
        self.main_window_ref = parent_window
        #self.move(40, 100)

        self.job = [
               "Ren"
        ]


        self.HEXA_skill_mastery = {
                    "Ren": {
                         "mastery1_skill":  {"skill_1": {"name": "梅花剣・本招："
                                                                 "旋斬・陸",     "damage": 202,  "number_o_t": 5, "add": 3, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "蠎魂剣・本招："
                                                                 "霊撃・陸",     "damage": 833,  "number_o_t": 4, "add": 13,"add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "蠎魂剣・弐招："
                                                                 "連斬・陸",     "damage": 238,  "number_o_t": 2, "add": 3, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 62,"passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "蠎魂降臨・陸", "damage": 858,  "number_o_t": 5, "add": 18,"add_attack": 2, "ct": 20,"boss_dam": 0, "def_a": 20,"is_skill": True,  "opt": False,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "蠎魂剣・絶技："
                                                                 "裂地・陸",     "damage": 860,  "number_o_t": 5, "add": 10,"add_attack": 1, "ct": 20,"boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "蠎魂剣・絶技："
                                                                 "蠎呑・陸",     "damage": 1380, "number_o_t": 9, "add": 30,"add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "蠎魂剣・絶技："
                                                                 "無量劫・陸",   "damage": 407,  "number_o_t": 7, "add": 7, "add_attack": 8, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "梅花剣・弐招："
                                                                 "砕梅・陸",     "damage": 122,  "number_o_t": 3, "add": 2, "add_attack": 5, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "梅花剣・参招："
                                                                 "鋭刃・陸",     "damage": 250,  "number_o_t": 7, "add": 4, "add_attack": 10,"ct": 30,"boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }                             
                        },
                 "job": {
                         "mastery1_skill":  {"skill_1": {"name": "mastery1",    "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "mastery2",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "mastery3",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "mastery4",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        },
        }

        self.HEXA_mastery_add = {
                 "Ren": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"蠎魂剣・本招："
                                             "霊撃・陸": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "Probability": 35,"passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"蠎魂剣・絶技："
                                             "無量劫・陸": {"damage":270,   "number_o_t": 3, "add": 5, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": False,  "Probability": 0, "passive": False, "buf": False, "duration": 5}
                                            ,"蠎魂剣・絶技："
                                             "裂地・陸": {"damage": 915,  "number_o_t": 7, "add": 15,"add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"梅花剣・弐招："
                                             "砕梅・陸": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "Probability": 35, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
        }


        self.HEXA_skill_enhance = {
                 "Ren": {
                         "enhance1_skill":  {"skill_1": {"name": "梅花剣・絶技：万里香" }
                                            }
                        ,"enhance2_skill":  {"skill_1": {"name": "蠎魂覚醒"}
                                            }
                        ,"enhance3_skill":  {"skill_1": {"name": "梅花剣・絶技：殲舞"}
                                            }
                        ,"enhance4_skill":  {"skill_1": {"name": "蠎魂剣・絶技：心剣"}
                                            }
                        },
                 "job": {
                         "enhance1_skill":  {"skill_1": {"name": "enhance1",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"enhance2_skill":  {"skill_1": {"name": "enhance2",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"enhance3_skill":  {"skill_1": {"name": "enhance3",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"enhance4_skill":  {"skill_1": {"name": "enhance4",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        },
        }

        self.HEXA_skill_origin = {
                 "Ren": {
                         "origin_skill":    {"skill_1": {"name": "蒼龍破天剣・"
                                                                 "昇天",         "damage": 775,  "number_o_t": 58,"add": 25,"add_attack": 12,"ct":360,"boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 1085, "number_o_t": 27,"add": 35,"add_attack": 15,"ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },
        }

        self.HEXA_skill_ascent = {
                 "Ren": {
                         "ascent_skill":    {"skill_1": {"name": "一梅落花・"
                                                                 "天悲人寂",     "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "boss_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False}
                                            }
                        },
        }

        #呼び出し　 self.HEXA_skill["Hero"]["mastery1_skill"]["skill_1"]["name"]


    # (レイアウト)
        layout = QGridLayout(self)
        self.setLayout(layout)


    # スキルを表示するメソッド
        self.mastery1_combo = QComboBox()
        self.mastery1_combo.addItem("マスタリー1")
        self.mastery2_combo = QComboBox()
        self.mastery2_combo.addItem("マスタリー2")
        self.mastery3_combo = QComboBox()
        self.mastery3_combo.addItem("マスタリー3")
        self.mastery4_combo = QComboBox()
        self.mastery4_combo.addItem("マスタリー4")

        self.label_enhancement1 = QLabel(self)
        self.label_enhancement1.setText("強化コア1")
        self.label_enhancement2 = QLabel(self)
        self.label_enhancement2.setText("強化コア2")
        self.label_enhancement3 = QLabel(self)
        self.label_enhancement3.setText("強化コア3")
        self.label_enhancement4 = QLabel(self)
        self.label_enhancement4.setText("強化コア4")
        self.label_origin = QLabel(self)
        self.label_origin.setText("オリジンスキル")
        self.label_ascent = QLabel(self)
        self.label_ascent.setText("アセントスキル")


        self.label_space1 = QLabel(self)
        self.label_space1.setText("マスタリー")
        self.label_space2 = QLabel(self)
        self.label_space2.setText("強化コア")
        self.label_space3 = QLabel(self)
        self.label_space3.setText("スキルコア")


    #スピンボックス_スキルレベル

        self.label_mastery1_sp = QSpinBox(self)
        self.label_mastery1_sp.setValue(0)
        self.label_mastery1_sp.setMaximum(30)
        self.label_mastery2_sp = QSpinBox(self)
        self.label_mastery2_sp.setValue(0)
        self.label_mastery2_sp.setMaximum(30)
        self.label_mastery3_sp = QSpinBox(self)
        self.label_mastery3_sp.setValue(0)
        self.label_mastery3_sp.setMaximum(30)
        self.label_mastery4_sp = QSpinBox(self)
        self.label_mastery4_sp.setValue(0)
        self.label_mastery4_sp.setMaximum(30)

        self.label_mastery1_fd_sp = QSpinBox(self)
        self.label_mastery1_fd_sp.setValue(0)
        self.label_mastery1_fd_sp.setMaximum(30)
        self.label_mastery2_fd_sp = QSpinBox(self)
        self.label_mastery2_fd_sp.setValue(0)
        self.label_mastery2_fd_sp.setMaximum(30)
        self.label_mastery3_fd_sp = QSpinBox(self)
        self.label_mastery3_fd_sp.setValue(0)
        self.label_mastery3_fd_sp.setMaximum(30)
        self.label_mastery4_fd_sp = QSpinBox(self)
        self.label_mastery4_fd_sp.setValue(0)
        self.label_mastery4_fd_sp.setMaximum(30)


        self.label_enhancement1_sp = QSpinBox(self)
        self.label_enhancement1_sp.setValue(0)
        self.label_enhancement1_sp.setMaximum(30)
        self.label_enhancement2_sp = QSpinBox(self)
        self.label_enhancement2_sp.setValue(0)
        self.label_enhancement2_sp.setMaximum(30)
        self.label_enhancement3_sp = QSpinBox(self)
        self.label_enhancement3_sp.setValue(0)
        self.label_enhancement3_sp.setMaximum(30)
        self.label_enhancement4_sp = QSpinBox(self)
        self.label_enhancement4_sp.setValue(0)
        self.label_enhancement4_sp.setMaximum(30)

        self.label_origin_sp = QSpinBox(self)
        self.label_origin_sp.setValue(0)
        self.label_origin_sp.setMaximum(30)

        self.label_origin_fd_sp = QSpinBox(self)
        self.label_origin_fd_sp.setValue(0)
        self.label_origin_fd_sp.setMaximum(30)

        self.label_ascent_sp = QSpinBox(self)
        self.label_ascent_sp.setValue(0)
        self.label_ascent_sp.setMaximum(30)

        self.label_mastery1_sp.setMinimumWidth(40)
    #LineEdit
        self.mastery1_li   = QLineEdit()
        self.mastery1_li.setMinimumWidth(300)

        self.mastery2_li   = QLineEdit()
        self.mastery3_li   = QLineEdit()
        self.mastery4_li = QLineEdit()


        self.enhancement1_li = QLineEdit()
        self.enhancement2_li = QLineEdit()
        self.enhancement3_li = QLineEdit()
        self.enhancement4_li = QLineEdit()
        self.enhancement4_li.setReadOnly(True)

        self.origin_li = QLineEdit()
        self.ascent_li = QLineEdit()

        self.attack_damage_li = QLineEdit()
        self.attack_damage_li.setReadOnly(True)
        self.stat_li = QLineEdit()
        self.stat_li.setReadOnly(True)
        self.combatstat_li = QLineEdit()
        self.combatstat_li.setReadOnly(True)

        self.mastery1_dam_li = QLineEdit()
        self.mastery1_dam_li.setReadOnly(True)
        self.mastery2_dam_li = QLineEdit()
        self.mastery2_dam_li.setReadOnly(True)
        self.mastery3_dam_li = QLineEdit()
        self.mastery3_dam_li.setReadOnly(True)
        self.mastery4_dam_li = QLineEdit()
        self.mastery4_dam_li.setReadOnly(True)

        self.mastery1_fd_li   = QLineEdit()
        self.mastery2_fd_li   = QLineEdit()
        self.mastery3_fd_li   = QLineEdit()
        self.mastery4_fd_li   = QLineEdit()


        self.origin_dam_li = QLineEdit()
        self.origin_dam_li.setReadOnly(True)
        self.origin_fd_li = QLineEdit()
        self.origin_fd_li.setReadOnly(True)


    #ボタン
        self.mastery1_dam_butt = QPushButton(self)
        self.mastery1_dam_butt.setText("マスタリー1 : ダメージ")

        self.mastery2_dam_butt = QPushButton(self)
        self.mastery2_dam_butt.setText("マスタリー2 : ダメージ")

        self.mastery3_dam_butt = QPushButton(self)
        self.mastery3_dam_butt.setText("マスタリー3 : ダメージ")

        self.mastery4_dam_butt = QPushButton(self)
        self.mastery4_dam_butt.setText("マスタリー4 : ダメージ")


        self.mastery1_fd_dam_butt = QPushButton(self)
        self.mastery1_fd_dam_butt.setText("マスタリー1 : 最終ダメージ")
        self.mastery2_fd_dam_butt = QPushButton(self)
        self.mastery2_fd_dam_butt.setText("マスタリー2 : 最終ダメージ")
        self.mastery3_fd_dam_butt = QPushButton(self)
        self.mastery3_fd_dam_butt.setText("マスタリー3 : 最終ダメージ")
        self.mastery4_fd_dam_butt = QPushButton(self)
        self.mastery4_fd_dam_butt.setText("マスタリー4 : 最終ダメージ")


        self.origin_dam_butt = QPushButton(self)
        self.origin_dam_butt.setText("ORIGIN : ダメージ")

        self.origin_fd_dam_butt = QPushButton(self)
        self.origin_fd_dam_butt.setText("ORIGIN : 最終ダメージ")


    #コンボックス
        self.combobox = QComboBox(self)
        self.combobox.setEditable(False)
        self.combobox.setFixedSize(200, 30)
        #self.combobox.addItem("job")
        self.combobox.addItem("Ren")

    #ボタン
        #self.calc_dam_butt = QPushButton(self)
        #self.calc_dam_butt.setText("計算: ダメージ")

        #self.stat_butt = QPushButton(self)
        #self.stat_butt.setText("計算: 表記ステータス")
        #self.combatstat_butt = QPushButton(self)
        #self.combatstat_butt.setText("計算: 戦闘力          ")
    #Grid　追加
        layout.addWidget(self.combobox, 0,0)
        layout.addWidget(self.label_space1,    1,0)
        layout.addWidget(self.mastery1_combo, 2,0)
        layout.addWidget(self.mastery2_combo,  3,0)
        layout.addWidget(self.mastery3_combo, 4,0)
        layout.addWidget(self.mastery4_combo, 5,0)
        layout.addWidget(self.label_space2,    6,0)
        layout.addWidget(self.label_enhancement1, 7,0)
        layout.addWidget(self.label_enhancement2, 8,0)
        layout.addWidget(self.label_enhancement3, 9,0)
        layout.addWidget(self.label_enhancement4, 10,0)
        layout.addWidget(self.label_space3, 11,0)
        layout.addWidget(self.label_origin, 12,0)
        layout.addWidget(self.label_ascent, 14,0)

    #スピンボックス
        layout.addWidget(self.label_mastery1_sp, 2,1)
        layout.addWidget(self.label_mastery2_sp,  3,1)
        layout.addWidget(self.label_mastery3_sp, 4,1)
        layout.addWidget(self.label_mastery4_sp, 5,1)
        #layout.addWidget(self.label_space, 6,1)
        layout.addWidget(self.label_enhancement1_sp, 7,1)
        layout.addWidget(self.label_enhancement2_sp, 8,1)
        layout.addWidget(self.label_enhancement3_sp, 9,1)
        layout.addWidget(self.label_enhancement4_sp, 10,1)
        #layout.addWidget(self.label_space, 11,1)
        layout.addWidget(self.label_origin_sp, 12,1)
        layout.addWidget(self.label_ascent_sp, 14,1)

        layout.addWidget(self.label_mastery1_fd_sp, 7,4)
        layout.addWidget(self.label_mastery2_fd_sp, 8,4)
        layout.addWidget(self.label_mastery3_fd_sp, 9,4)
        layout.addWidget(self.label_mastery4_fd_sp, 10,4)

        layout.addWidget(self.label_origin_fd_sp, 13,4)


    #数値入力ボックス　の追加
        layout.addWidget(self.mastery1_li, 2,2)
        layout.addWidget(self.mastery2_li, 3,2)
        layout.addWidget(self.mastery3_li, 4,2)
        layout.addWidget(self.mastery4_li, 5,2)
        #layout.addWidget(self.label_space, 6,2)
        layout.addWidget(self.enhancement1_li, 7,2)
        layout.addWidget(self.enhancement2_li, 8,2)
        layout.addWidget(self.enhancement3_li, 9,2)
        layout.addWidget(self.enhancement4_li, 10,2)
        #layout.addWidget(self.label_space, 11,2)
        layout.addWidget(self.origin_li, 12,2)
        layout.addWidget(self.ascent_li, 14,2)

        layout.addWidget(self.mastery1_dam_li, 2,5)
        layout.addWidget(self.mastery2_dam_li, 3,5)
        layout.addWidget(self.mastery3_dam_li, 4,5)
        layout.addWidget(self.mastery4_dam_li, 5,5)

        layout.addWidget(self.mastery1_fd_li, 7,5)
        layout.addWidget(self.mastery2_fd_li, 8,5)
        layout.addWidget(self.mastery3_fd_li, 9,5)
        layout.addWidget(self.mastery4_fd_li, 10,5)

        layout.addWidget(self.origin_dam_li, 12,5)
        layout.addWidget(self.origin_fd_li, 13,5)


    #ダメージ計算ボタン
        layout.addWidget(self.mastery1_dam_butt, 2,3)
        layout.addWidget(self.mastery2_dam_butt, 3,3)
        layout.addWidget(self.mastery3_dam_butt, 4,3)
        layout.addWidget(self.mastery4_dam_butt, 5,3)
        layout.addWidget(self.origin_dam_butt, 12,3)

        layout.addWidget(self.mastery1_fd_dam_butt, 7,3)
        layout.addWidget(self.mastery2_fd_dam_butt, 8,3)
        layout.addWidget(self.mastery3_fd_dam_butt, 9,3)
        layout.addWidget(self.mastery4_fd_dam_butt, 10,3)
        layout.addWidget(self.origin_fd_dam_butt, 13,3)

            
    #オプション


    #QT Style
        labelStyle = """QLabel {
            font-size: 16px;
        }"""

        lineStyle = """
            QLineEdit {
                border: 0.4px solid Gray; /* ピクセルの青い枠線 */
                border-radius: 3px;   /* 角を丸くする */
                padding: 2px;         /* テキストと枠線の間隔 */
                font-size: 16px;      /* フォントサイズ */
                font-family: Arial;   /* フォント */
            }
            QLineEdit:focus {
                border: 1px solid "#3D6DEB"; /* フォーカス時の枠線 */
            }
        """
    #STyleの適用
        #label.setStyleSheet(labelStyle)
        #self.wepon_coe_li.setStyleSheet(lineStyle)

        self.setLayout(layout)

    #職業選択処理
        self.select_job = self.combobox.currentText()
        self.combobox.currentTextChanged.connect(self.combo_set)

    #数値変更で変数の数値を変更する

        #self.wepon_coe = is_input(1.44)
        #self.wepon_coe_li.textChanged.connect(lambda new_text: self.is_input_str('wepon_coe', False, new_text))

        #値の設定
        self.boss_damage_m1 = 0
        self.def_a_m1 = 0
        self.skill_dam_m1 = 0 
        self.numb_t_m1 = 0
        self.fainal_dam_m1 = 0

        self.skill_dam_m2 = 0 
        self.numb_t_m2 = 0

        self.skill_dam_m3 = 0 
        self.numb_t_m3 = 0

        self.skill_dam_m4 = 0 
        self.numb_t_m4 = 0

        self.skill_dam_origin = 0 
        self.numb_t_origin = 0
        self.skill_dam_origin_add = 0
        self.numb_t_origin_add = 0


        #初期化
        self.attack_damage = is_input(0)
        self.dam_calc
        self.format_damage()

        self.level_dia_c = (1.1)
        self.attack_damage = is_input(self.attack_damage_li.text().strip())
        self.skill_set()

    #計算処理
        self.mastery1_dam_butt.pressed.connect(self.mastery1_calc)
        self.mastery2_dam_butt.pressed.connect(self.mastery2_calc)
        self.mastery3_dam_butt.pressed.connect(self.mastery3_calc)
        self.mastery4_dam_butt.pressed.connect(self.mastery4_calc)

        #マスタリー最終ダメージ
        self.mastery1_fd_dam_butt.pressed.connect(self.mastery1_fd_calc)
        self.mastery2_fd_dam_butt.pressed.connect(self.mastery2_fd_calc)
        self.mastery3_fd_dam_butt.pressed.connect(self.mastery3_fd_calc)
        self.mastery4_fd_dam_butt.pressed.connect(self.mastery4_fd_calc)

        #origin
        self.origin_dam_butt.pressed.connect(self.origin_calc)
        #最終ダメージ
        self.origin_fd_dam_butt.pressed.connect(self.origin_fd_calc)


    #timer
        start_time = time.perf_counter()
        #self.format_damage()
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        #print(f"処理にかかった時間: {elapsed_time:.8f} 秒")


    #connect!
        self.combobox.activated.connect(self.skill_set)

        #mastery
        self.label_mastery1_sp.valueChanged.connect(self.is_input_mastery1)
        self.label_mastery2_sp.valueChanged.connect(self.is_input_mastery2)
        self.label_mastery3_sp.valueChanged.connect(self.is_input_mastery3)
        self.label_mastery4_sp.valueChanged.connect(self.is_input_mastery4)

        self.mastery1_combo.activated.connect(self.is_input_mastery1)
        self.mastery2_combo.activated.connect(self.is_input_mastery2)
        self.mastery3_combo.activated.connect(self.is_input_mastery3)
        self.mastery4_combo.activated.connect(self.is_input_mastery4)

        #enhance
        self.label_enhancement1_sp.valueChanged.connect(self.is_input_enhance)
        self.label_enhancement2_sp.valueChanged.connect(self.is_input_enhance)
        self.label_enhancement3_sp.valueChanged.connect(self.is_input_enhance)
        self.label_enhancement4_sp.valueChanged.connect(self.is_input_enhance)

        #origin
        self.label_origin_sp.valueChanged.connect(self.is_input_origin)


    def combo_set(self):
        self.select_job = self.combobox.currentText()

        #self.label_mastery1.setText("マスタリー1")
        #self.label_mastery2.setText("マスタリー2")
        #self.label_mastery3.setText("マスタリー3")
        #self.label_mastery4.setText("マスタリー4")

        self.label_enhancement1.setText("強化コア1")
        self.label_enhancement2.setText("強化コア2")
        self.label_enhancement3.setText("強化コア3")
        self.label_enhancement4.setText("強化コア4")

        self.label_origin.setText("オリジンスキル")
        self.label_ascent.setText("アセントスキル")

    def is_input_mastery1(self):
        #旋斬　0.15
        self.mastery1 = self.label_mastery1_sp.value() -1
        damage1 = (self.HEXA_skill_mastery[self.select_job]["mastery1_skill"]["skill_1"]["damage"] 
            + self.mastery1 * self.HEXA_skill_mastery[self.select_job]["mastery1_skill"]["skill_1"]["add"] 
        )
        attack_num = self.HEXA_skill_mastery[self.select_job]["mastery1_skill"]["skill_1"]["number_o_t"]
        self.mastery1_li.setText("ダメージ:" + str(damage1) + "  攻撃回数:" + str(attack_num))

        self.boss_damage_m1 = 0
        self.def_a_m1 = 0
        self.skill_dam_m1 = damage1/100
        self.numb_t_m1    = attack_num
        self.fainal_dam_m1 = 0

    def is_input_mastery2(self):
        self.mastery2 = self.label_mastery2_sp.value() -1

        #self.HEXA_mastery_add

        damage2 = (self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_1"]["damage"] 
            + self.mastery2 * self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_1"]["add"] 
        )
        Probability = self.HEXA_mastery_add[self.select_job]["mastery2_skill"]["蠎魂剣・本招：霊撃・陸"]["Probability"]

        attack_num = self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_1"]["number_o_t"]
        if(self.select_job == "Ren"):
            self.mastery2_li.setText("ダメージ:" + str(damage2) + "  攻撃回数:" + str(attack_num) + "  梅花剣技を受けた敵の位置で35%の確率で発動")

        if(self.mastery2_combo.currentIndex()==1):
            damage2 = (self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["damage"] 
                + self.mastery2 * self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["add"] 
            )
            attack_num = self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["number_o_t"]
            f_at = self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["f_Probability"]


            if(self.select_job == "Ren"):
                self.mastery2_li.setText("ダメージ:" + str(damage2) + "  攻撃回数:" + str(attack_num) + "  [FainalAttack]追加攻撃確率:" +str(f_at))

        self.boss_damage_m2 = 0
        self.def_a_m2 = 0
        self.skill_dam_m2 = damage2/100
        self.numb_t_m2    = attack_num
        self.fainal_dam_m1 = 0

    def is_input_mastery3(self):
        damage3_add = 0
        attack_num_add = 0

        self.mastery3 = self.label_mastery3_sp.value() -1
        damage3 = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["damage"] 
            + self.mastery3 * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["add"] 
        )
        attack_num = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["number_o_t"]
            * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["add_attack"]
        )
        self.mastery3_li.setText("ダメージ:" + str(damage3) + "  攻撃回数:" + str(attack_num))


        if(self.mastery3_combo.currentIndex()==1):
            damage3 = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_2"]["damage"] 
                + self.mastery3 * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_2"]["add"] 
            )
            attack_num = self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_2"]["number_o_t"]
            
            damage3_add = (self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：裂地・陸"]["damage"]
                + self.mastery3 * self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：裂地・陸"]["add"] 
            )
            attack_num_add = self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：裂地・陸"]["number_o_t"]

    
            self.mastery3_li.setText("ダメージ:" + str(damage3) + "  攻撃回数:" + str(attack_num)
                                    + "  AddAtack:" + str(damage3_add) + "  攻撃回数:" + str(attack_num_add))


        if(self.mastery3_combo.currentIndex()==2):
            damage3 = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_3"]["damage"] 
                + self.mastery3 * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_3"]["add"] 
            )
            attack_num = self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_3"]["number_o_t"]
            self.mastery3_li.setText("ダメージ:" + str(damage3) + "  攻撃回数:" + str(attack_num))



        #"蠎魂剣・絶技：無量劫・陸"
        if(self.mastery3_combo.currentIndex()==3):
            damage3 = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["damage"] 
                + self.mastery3 * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["add"] 
            )
            attack_num = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["number_o_t"]
                * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["add_attack"]
            )
            damage3_add = (self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：無量劫・陸"]["damage"]
                + self.mastery3 * self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：無量劫・陸"]["add"] 
            )
            attack_num_add = (self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：無量劫・陸"]["number_o_t"]
                * (5/0.5))
            self.mastery3_li.setText("ダメージ:" + str(damage3) + "  攻撃回数:" + str(attack_num)
                                    + "  AddAtack :" + str(damage3_add) + "  攻撃回数:" + str(attack_num_add))
        
        #self.mastery3_li.setText(str(self.mastery3_combo.currentIndex()))
        self.boss_damage_m3 = 0
        self.def_a_m3 = 0
        self.skill_dam_m3 = damage3/100
        self.skill_dam_m3_add = damage3_add/100
        self.numb_t_m3    = attack_num
        self.numb_t_m3_add    = attack_num_add
        self.fainal_dam_m3 = 0

    def is_input_mastery4(self):
        damage4_add = 0
        attack_num_add = 0
        self.mastery4 = self.label_mastery4_sp.value() -1

        #"梅花剣・弐招：砕梅・陸"
        damage4 = (self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["damage"] 
            + self.mastery4 * self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["add"] 
        )
        attack_num = (self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["number_o_t"]
            * self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["add_attack"]
        )
        p_b = self.HEXA_mastery_add[self.select_job]["mastery4_skill"]["梅花剣・弐招：砕梅・陸"]["Probability"]

        self.mastery4_li.setText("ダメージ:" + str(damage4) + "  攻撃回数:" + str(attack_num) + "  追加攻撃確率" + str(p_b) + "%")


        #"梅花剣・弐招：砕梅・陸"
        if(self.mastery4_combo.currentIndex()==1):
            damage4 = (self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["damage"] 
                + self.mastery4 * self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["add"] 
            )
            attack_num = (self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["number_o_t"]
                * self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["add_attack"]
            )
            self.mastery4_li.setText("ダメージ:" + str(damage4) + "  攻撃回数:" + str(attack_num))
            


        self.boss_damage_m4 = 0
        self.def_a_m4 = 0
        self.skill_dam_m4 = damage4/100
        self.skill_dam_m4_add =damage4_add/100
        self.numb_t_m4    = attack_num
        self.numb_t_m4_add = attack_num_add
        self.fainal_dam_m4 = 0


    def is_input_enhance(self):

        self.enhancement1 = self.label_enhancement1_sp.value()
        enhancement1_fi_dam = (
            10 + self.enhancement1 
        )
        if(self.enhancement1>=10): 
            enhancement1_fi_dam+=5
        if(self.enhancement1>=20):
            enhancement1_fi_dam+=5
        if(self.enhancement1>=30):
            enhancement1_fi_dam+=10
        if(self.enhancement1==0):
            enhancement1_fi_dam=0
        text = "最終ダメージ: " + str(enhancement1_fi_dam)
        self.enhancement1_li.setText(text)


        self.enhancement2 = self.label_enhancement2_sp.value()
        enhancement2_fi_dam = (
            10 + self.enhancement2 
        )
        if(self.enhancement2>=10): 
            enhancement2_fi_dam+=5
        if(self.enhancement2>=20):
            enhancement2_fi_dam+=5
        if(self.enhancement2>=30):
            enhancement2_fi_dam+=10
        if(self.enhancement2==0):
            enhancement2_fi_dam=0
        text = "最終ダメージ: " + str(enhancement2_fi_dam)
        self.enhancement2_li.setText(text)


        self.enhancement3 = self.label_enhancement3_sp.value()
        enhancement3_fi_dam = (
            10 + self.enhancement3 
        )
        if(self.enhancement3>=10): 
            enhancement3_fi_dam+=5
        if(self.enhancement3>=20):
            enhancement3_fi_dam+=5
        if(self.enhancement3>=30):
            enhancement3_fi_dam+=10
        if(self.enhancement3==0):
            enhancement3_fi_dam=0
        text = "最終ダメージ: " + str(enhancement3_fi_dam)
        self.enhancement3_li.setText(text)


        self.enhancement4 = self.label_enhancement4_sp.value()
        enhancement4_fi_dam = (
            10 + self.enhancement4 
        )
        if(self.enhancement4>=10): 
            enhancement4_fi_dam+=5
        if(self.enhancement4>=20):
            enhancement4_fi_dam+=5
        if(self.enhancement4>=30):
            enhancement4_fi_dam+=10
        if(self.enhancement4==0):
            enhancement4_fi_dam=0
        text = "最終ダメージ: " + str(enhancement4_fi_dam)
        self.enhancement4_li.setText(text)

    def is_input_origin(self):
        damage_origin_add = 0
        attack_num_add = 0

        self.origin = self.label_origin_sp.value() -1
        damage_origin = (self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["damage"] 
            + self.origin * self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["add"] 
        )
        attack_num = (self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["number_o_t"]
                     *  self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["add_attack"]
        )
        
        damage_origin_add = (self.HEXA_skill_origin[self.select_job]["origin_skill"]["adi_at"]["damage"] 
            + self.origin * self.HEXA_skill_origin[self.select_job]["origin_skill"]["adi_at"]["add"] 
        )
        attack_num_add = (self.HEXA_skill_origin[self.select_job]["origin_skill"]["adi_at"]["number_o_t"]
                     *  self.HEXA_skill_origin[self.select_job]["origin_skill"]["adi_at"]["add_attack"]
        )

        
        self.origin_li.setText("ダメージ:" + str(damage_origin) + "  攻撃回数:" + str(attack_num)
                                 + "  Add Atack:" + str(damage_origin_add) + "  攻撃回数:" + str(attack_num_add)
        )

        self.boss_damage_origin = 0
        self.def_a_origin = 0
        self.skill_dam_origin = damage_origin/100
        self.skill_dam_origin_add = damage_origin_add/100
        self.numb_t_origin    = attack_num
        self.numb_t_origin_add = attack_num_add
        self.fainal_dam_origin = 0

    def is_calc_boss(self):
        self.mastery1_calc()
        self.mastery2_calc()
        self.mastery3_calc()
        self.mastery4_calc()

    def skill_set(self):
        self.select_job
        self.select_job = self.combobox.currentText()

        self.mastery1_combo.clear()
        self.mastery2_combo.clear()
        self.mastery3_combo.clear()
        self.mastery4_combo.clear()
    
        #マスタリーSET
        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery1_skill"]["skill_1"]["name"]]
        self.mastery1_combo.addItems(add_text)
        
        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_1"]["name"]]
        self.mastery2_combo.addItems(add_text)
        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["name"]]
        self.mastery2_combo.addItems(add_text)

        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["name"]]
        self.mastery3_combo.addItems(add_text)
        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_2"]["name"]]
        self.mastery3_combo.addItems(add_text)
        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_3"]["name"]]
        self.mastery3_combo.addItems(add_text)
        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["name"]]
        self.mastery3_combo.addItems(add_text)

        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["name"]]
        self.mastery4_combo.addItems(add_text)
        add_text = [self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["name"]]
        self.mastery4_combo.addItems(add_text)

        #強化コアSET
        self.label_enhancement1.setText(str(self.HEXA_skill_enhance[self.select_job]["enhance1_skill"]["skill_1"]["name"]))
        self.label_enhancement2.setText(str(self.HEXA_skill_enhance[self.select_job]["enhance2_skill"]["skill_1"]["name"]))
        self.label_enhancement3.setText(str(self.HEXA_skill_enhance[self.select_job]["enhance3_skill"]["skill_1"]["name"]))
        self.label_enhancement4.setText(str(self.HEXA_skill_enhance[self.select_job]["enhance4_skill"]["skill_1"]["name"]))

        #スキルコア
            #origin
        self.label_origin.setText(str(self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["name"]))


    def combatstat_calc(self):
        self.setUpdatesEnabled(False)
        wepon_coe = is_input(self.wepon_coe_li.text().strip())
        main_st = is_input(self.main_st_li.text().strip())
        sub_st = is_input(self.sub_st_li.text().strip())
        a_ma = is_input(self.a_ma_li.text().strip())
        damage = is_input(self.damage_li.text().strip())
        crit_dam = is_input(self.crit_dam_li.text().strip())
        fainal_dam = is_input(self.fainal_dam_li.text().strip())

        #%から数値に
        damage /= 100
        fainal_dam /= 100
        crit_dam /= 100

        stat = (
            (main_st*4 + sub_st) * (a_ma/100) * (1 + damage) *
            (1.35 + crit_dam) * (1 + fainal_dam))

        stat = round(stat)

        stat = str(stat)
        stat_length = len(stat)

        if stat_length > 8 :
            stat_text = ("戦闘力: " + stat[:stat_length-8] + "億"
            + stat[stat_length-8:stat_length-4] + "万"
            + stat[stat_length-4:])
            print(stat_text)
        elif stat_length > 4 :
            stat_text = ("戦闘力: " + stat[:stat_length-4] + "万"
            + stat[stat_length-4:])
            print(stat_text)
        else :
            stat_text = ("戦闘力: " + str(stat))
            print(stat_text)

        self.combatstat_li.setText(stat_text)
        self.combatstat_li.repaint()
        self.setUpdatesEnabled(True)

    def stat_calc(self):
        self.setUpdatesEnabled(False)
        wepon_coe = is_input(self.wepon_coe_li.text().strip())
        main_st = is_input(self.main_st_li.text().strip())
        sub_st = is_input(self.sub_st_li.text().strip())
        a_ma = is_input(self.a_ma_li.text().strip())
        damage = is_input(self.damage_li.text().strip())
        fainal_dam = is_input(self.fainal_dam_li.text().strip())
        profic = is_input(self.profic_li.text().strip())

        #%から数値に
        damage /= 100
        fainal_dam /= 100
        profic /= 100


        stat = (
            wepon_coe * (main_st*4 + sub_st) * (a_ma/100) * (1 + damage) *
            (1 + fainal_dam) * profic)

        stat = round(stat)

        stat = str(stat)
        stat_length = len(stat)

        if stat_length > 8 :
            stat_text = ("ステータス火力: " + stat[:stat_length-8] + "億"
            + stat[stat_length-8:stat_length-4] + "万"
            + stat[stat_length-4:])
            print(stat_text)
        elif stat_length > 4 :
            stat_text = ("ステータス火力: " + stat[:stat_length-4] + "万"
            + stat[stat_length-4:])
            print(stat_text)
        else :
            stat_text = ("ステータス火力: " + str(stat))
            print(stat_text)

        self.stat_li.setText(stat_text)
        self.stat_li.repaint()
        self.setUpdatesEnabled(True)


    def mastery1_calc(self):
        self.calc(self.skill_dam_m1,self.numb_t_m1)
        #self.print_check()
        self.mastery1_dam_li.setText(self.damage_text)

    def mastery2_calc(self):
        self.calc(self.skill_dam_m2,self.numb_t_m2)
        self.mastery2_dam_li.setText(self.damage_text)

    def mastery3_calc(self):
        self.calc(self.skill_dam_m3,self.numb_t_m3)
        damage = self.attack_damage

        #add_damage
        if(self.mastery3_combo.currentIndex()==1):
            self.calc(self.skill_dam_m3_add,self.numb_t_m3_add)
            self.attack_damage += damage

        #DOT 10回
        self.format_damage()
        self.mastery3_dam_li.setText(self.damage_text)

    def mastery4_calc(self):
        self.calc(self.skill_dam_m4,self.numb_t_m4)

        self.mastery4_dam_li.setText(self.damage_text)

    def origin_calc(self):
        self.calc(self.skill_dam_origin,self.numb_t_origin)
        damage = self.attack_damage

        #add_damage
        self.calc(self.skill_dam_origin_add,self.numb_t_origin_add)
        self.attack_damage += damage

        self.origin_dam_li.setText(self.damage_text)

    
    def mastery1_fd_calc(self):
        self.is_input_mastery1()
        self.mastery1_calc()
        self.mastery1_fd = self.label_mastery1_fd_sp.value() -1

        self.calc(self.skill_dam_m1,self.numb_t_m1)
        damage = self.attack_damage

        self.mastery1 = self.label_mastery1_sp.value() -1
        damage1 = (self.HEXA_skill_mastery[self.select_job]["mastery1_skill"]["skill_1"]["damage"] 
            + self.mastery1_fd * self.HEXA_skill_mastery[self.select_job]["mastery1_skill"]["skill_1"]["add"] 
        )
        attack_num = self.HEXA_skill_mastery[self.select_job]["mastery1_skill"]["skill_1"]["number_o_t"]

        damage1 = damage1/100
        self.calc(damage1,attack_num)
        damage_fd = self.attack_damage
        if(self.attack_damage!=0 and self.skill_dam_m1 !=0):
            fd = ((damage_fd/damage)*100) - 100
        else:
            fd=0
        fd = round(fd, 3)
        self.mastery1_fd_li.setText("最終ダメージの増加量: " + str(fd))

    def mastery2_fd_calc(self):
        self.is_input_mastery2()
        self.mastery2_calc()
        self.mastery2_fd = self.label_mastery2_fd_sp.value() -1

        self.calc(self.skill_dam_m2,self.numb_t_m2)
        damage = self.attack_damage

        damage2 = (self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_1"]["damage"] 
            + self.mastery2_fd * self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_1"]["add"] 
        )
        Probability = self.HEXA_mastery_add[self.select_job]["mastery2_skill"]["蠎魂剣・本招：霊撃・陸"]["Probability"]

        attack_num = self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_1"]["number_o_t"]

        if(self.mastery2_combo.currentIndex()==1):
            damage2 = (self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["damage"] 
                + self.mastery2_fd * self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["add"] 
            )
            attack_num = self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["number_o_t"]
            f_at = self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_2"]["f_Probability"]

        damage2 = damage2/100
        self.calc(damage2,attack_num)
        damage_fd = self.attack_damage
        if(self.attack_damage!=0 and self.skill_dam_m2 !=0):
            fd = ((damage_fd/damage)*100) - 100
        else:
            fd=0
        fd = round(fd, 3)
        self.mastery2_fd_li.setText("最終ダメージの増加量: " + str(fd))

    def mastery3_fd_calc(self):
        self.is_input_mastery3()
        self.mastery3_calc()
        self.mastery3_fd = self.label_mastery3_fd_sp.value() -1

        self.calc(self.skill_dam_m3,self.numb_t_m3)
        damage = self.attack_damage


        damage3 = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["damage"] 
            + self.mastery3_fd * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["add"] 
        )
        attack_num = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["number_o_t"]
            * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_1"]["add_attack"]
        )


        if(self.mastery3_combo.currentIndex()==1):
            damage3 = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_2"]["damage"] 
                + self.mastery3_fd * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_2"]["add"] 
            )
            attack_num = self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_2"]["number_o_t"]
            
            damage3_add = (self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：裂地・陸"]["damage"]
                + self.mastery3_fd * self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：裂地・陸"]["add"] 
            )
            attack_num_add = self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：裂地・陸"]["number_o_t"]

    
            self.mastery3_li.setText("ダメージ:" + str(damage3) + "  攻撃回数:" + str(attack_num)
                                    + "  AddAtack:" + str(damage3_add) + "  攻撃回数:" + str(attack_num_add))


        if(self.mastery3_combo.currentIndex()==2):
            damage3 = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_3"]["damage"] 
                + self.mastery3_fd * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_3"]["add"] 
            )
            attack_num = self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_3"]["number_o_t"]
            self.mastery3_li.setText("ダメージ:" + str(damage3) + "  攻撃回数:" + str(attack_num))



        #"蠎魂剣・絶技：無量劫・陸"
        if(self.mastery3_combo.currentIndex()==3):
            damage3 = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["damage"] 
                + self.mastery3_fd * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["add"] 
            )
            attack_num = (self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["number_o_t"]
                * self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_4"]["add_attack"]
            )
            damage3_add = (self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：無量劫・陸"]["damage"]
                + self.mastery3_fd * self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：無量劫・陸"]["add"] 
            )
            attack_num_add = (self.HEXA_mastery_add[self.select_job]["mastery3_skill"]["蠎魂剣・絶技：無量劫・陸"]["number_o_t"]
                * (5/0.5))
            self.mastery3_li.setText("ダメージ:" + str(damage3) + "  攻撃回数:" + str(attack_num)
                                    + "  AddAtack :" + str(damage3_add) + "  攻撃回数:" + str(attack_num_add))

      
        #add_damage
        if(self.mastery3_combo.currentIndex()==1):
            self.calc(self.skill_dam_m3_add,self.numb_t_m3_add)
            self.attack_damage += damage


        damage3 = damage3/100
        self.calc(damage3,attack_num)
        damage_fd = self.attack_damage
        if(self.attack_damage!=0 and self.skill_dam_m3 !=0):
            fd = ((damage_fd/damage)*100) - 100
        else:
            fd=0
        fd = round(fd, 3)
        self.mastery3_fd_li.setText("最終ダメージの増加量: " + str(fd))

    def mastery4_fd_calc(self):
        self.is_input_mastery4()
        self.mastery4_calc()
        self.mastery4_fd = self.label_mastery4_fd_sp.value() -1

        self.calc(self.skill_dam_m4,self.numb_t_m4)
        damage = self.attack_damage

        #"梅花剣・弐招：砕梅・陸"
        damage4 = (self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["damage"] 
            + self.mastery4_fd * self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["add"] 
        )
        attack_num = (self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["number_o_t"]
            * self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_1"]["add_attack"]
        )
        p_b = self.HEXA_mastery_add[self.select_job]["mastery4_skill"]["梅花剣・弐招：砕梅・陸"]["Probability"]

        #"梅花剣・弐招：砕梅・陸"
        if(self.mastery4_combo.currentIndex()==1):
            damage4 = (self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["damage"] 
                + self.mastery4_fd * self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["add"] 
            )
            attack_num = (self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["number_o_t"]
                * self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_2"]["add_attack"]
            )


        damage4 = damage4/100
        self.calc(damage4,attack_num)
        damage_fd = self.attack_damage
        if(self.attack_damage!=0 and self.skill_dam_m4 !=0):
            fd = ((damage_fd/damage)*100) - 100
        else:
            fd=0
        fd = round(fd, 3)
        self.mastery4_fd_li.setText("最終ダメージの増加量: " + str(fd))

    def origin_fd_calc(self):
        self.is_input_origin()
        self.origin_calc()
        damage = self.attack_damage


        self.origin_fd = self.label_origin_fd_sp.value() -1

        damage_origin = (self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["damage"] 
            + self.origin_fd * self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["add"] 
        )
        attack_num = (self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["number_o_t"]
                     *  self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["add_attack"]
        )
        
        damage_origin_add = (self.HEXA_skill_origin[self.select_job]["origin_skill"]["adi_at"]["damage"] 
            + self.origin_fd * self.HEXA_skill_origin[self.select_job]["origin_skill"]["adi_at"]["add"] 
        )
        attack_num_add = (self.HEXA_skill_origin[self.select_job]["origin_skill"]["adi_at"]["number_o_t"]
                     *  self.HEXA_skill_origin[self.select_job]["origin_skill"]["adi_at"]["add_attack"]
        )


        damage_origin = damage_origin/100
        damage_origin_add = damage_origin_add/100
        self.calc(damage_origin,attack_num)
        damage_fd = self.attack_damage
        #add_damage
        self.calc(damage_origin_add, attack_num_add)
        damage_fd +=self.attack_damage

        if(self.attack_damage!=0 and self.skill_dam_origin !=0):
            fd = ((damage_fd/damage)*100) - 100
        else:
            fd=0
        fd = round(fd, 3)
        self.origin_fd_li.setText("最終ダメージの増加量: " + str(fd))



    def calc(self, skill_dam, numb_t):
        #is_input(self.main_window_ref.main_st)


        start_time = time.perf_counter()
        self.setUpdatesEnabled(False)

        arorn_is  = self.main_window_ref.arca_ra.isChecked()
        if(arorn_is == True):
            mons_ageru_higai  = self.main_window_ref.higai_li
            mons_ukeru_dam = 1.0
        else:
            mons_ukeru_dam  = self.main_window_ref.ukerudam_li
            mons_ageru_higai = 1.0
        #print(mons_ukeru_dam)
        #///////////////////
        self.dam_calc(skill_dam)
        #print(self.attack_damage)
        #print(self.level_dia_c)
        if(self.attack_damage<0):
            self.attack_damage = 0
        else:
            self.attack_damage = self.attack_damage * self.main_window_ref.level_dia_c * mons_ageru_higai * mons_ukeru_dam
            self.attack_damage = self.attack_damage*numb_t
            self.attack_damage = round(self.attack_damage)
        #print(self.attack_damage)
        self.format_damage()
        #print(self.damage_text)
        #self.print_check()
        #attack_damage = attack_damage * self.level_dia_c * mons_ageru_higai * mons_ukeru_dam
        #self.attack_damage_li.setText(self.damage_text)
        self.attack_damage_li.repaint()
        self.setUpdatesEnabled(True)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        #print(f"処理にかかった時間: {elapsed_time:.8f} 秒")

    def dam_calc(self, damage):
        self.boss_damage = self.main_window_ref.boss_damage
        mons_def = (1-self.main_window_ref.mons_def*(1-self.main_window_ref.def_a))
        self.skill_dam = damage
        self.fainal_dam = self.main_window_ref.fainal_dam
        #print(self.mons_def)

        self.attack_damage = (
        self.main_window_ref.wepon_coe * (self.main_window_ref.main_st*4 + self.main_window_ref.sub_st) * (self.main_window_ref.a_ma/100) *(1 + self.main_window_ref.damage + self.boss_damage) * (1-(self.main_window_ref.element_def_const-self.main_window_ref.element_ig)) *
        (1.35 + self.main_window_ref.crit_dam) * self.skill_dam * (mons_def) * (1 + self.fainal_dam) * self.main_window_ref.profic )


    def format_damage(self):
        #print(self.attack_damage)
        attack_damage = self.attack_damage
        attack_damage = str(attack_damage)
        attack_damage_length = len(attack_damage)
        #print(attack_damage)
        if attack_damage_length > 8 :
            damage_text = ("攻撃時のダメージ: " + attack_damage[:attack_damage_length-8] + "億"
            + attack_damage[attack_damage_length-8:attack_damage_length-4] + "万"
            + attack_damage[attack_damage_length-4:])
            #print(damage_text)
        elif attack_damage_length > 4 :
            damage_text = ("攻撃時のダメージ: " + attack_damage[:attack_damage_length-4] + "万"
            + attack_damage[attack_damage_length-4:])
            #print(damage_text)
        else :
            damage_text = ("攻撃時のダメージ: " + str(attack_damage))
            #print(damage_text)
        if(attack_damage=='0'):
            damage_text = ("攻撃時のダメージ")
        self.damage_text = damage_text


    def print_check(self):
        print(self.main_window_ref.wepon_coe)
        print(self.main_window_ref.main_st)
        print(self.main_window_ref.sub_st)
        print(self.main_window_ref.a_ma)
        print(self.main_window_ref.damage)
        print(self.main_window_ref.boss_damage)
        #print(element_def)
        print(self.main_window_ref.element_ig)
        print(self.main_window_ref.crit_dam)
        print(self.skill_dam_m1)
        print(self.mons_def)
        print(self.main_window_ref.def_a)
        print(self.main_window_ref.fainal_dam)
        print(self.main_window_ref.profic)
        print(self.main_window_ref.level_dia_c)
        #print(mons_ukeru_dam)
        print(self.attack_damage)
        print(" ")


    def is_input_str(self, set_value: str, per_dec: bool, new_text: str):
        if not new_text:
            new_value = 0.0
        else:
            try:
                new_value = float(new_text)
            except ValueError:
                return

        if(per_dec):
            new_value = new_value/100
        setattr(self, set_value, new_value)
        #print(new_value)


def is_input(input_num):
    try:
        return float(input_num)
    except ValueError:
        return 0

def is_input_int(setco, input_num):
    try:
        return int(input_num)
    except ValueError:
        return 0
