from PySide6.QtWidgets import (QApplication, QSpinBox, QDoubleSpinBox, QLineEdit, QPushButton,
        QLabel, QComboBox, QRadioButton, QButtonGroup, QWidget, QGridLayout)
from PySide6.QtGui import QDoubleValidator
#from GUI_calc import is_input
import math, time
from GUI_calc_HEXA import HEXA_calc, origin_calc, ascent_calc

#Dot Damage 0.5秒周期
class SecondWindow(QWidget):
    def __init__(self, parent_window, parent=None):
        super().__init__()

        #スキル平均の最終ダメージ増加量
        #アセント
        #ステータスをダメージに反映
        
    # ウィンドウサイズを指定（px単位）
        windowWidth = 1300  # ウィンドウの横幅
        windowHeight = 500  # ウィンドウの高さ
    # ウィンドウサイズの変更
        self.resize(windowWidth, windowHeight)
        self.setFixedSize(1300, 500)
        self.main_window_ref = parent_window
        #self.move(40, 100)

        self.job = [
                "Hero",           "Paladin",        "DarkNight",      "SoulMaster",     "Aran",
                "DemonSlayer",    "DemonAvenger",   "Kaiser",         "Hayato",         "Zero",
                "Michael",        "Blaster",        "Adel",          "IceLightning",   "FirePoison",
                "Bishop",         "FlameWizard",    "BattleMage",     "Evan",           "Luminous",
                "Kanna",          "Kinesis",        "Illium",         "Lara",           "Lynn",
                "Bowmaster",      "Crossbowmaster", "Pathfinder",     "Windshooter",    "WildHunter",
                "Mercedes",       "Cain",           "Shadow",         "KnightLord",     "DualBlade",
                "NightWalker",    "Zenon",          "PhantomThief",   "Cadena",         "Torakage",
                "Kali",           "Viper",          "Captain",        "CannonShooter",  "Striker",
                "Mechanic",       "HiddenMoon",     "AngelicBuster",  "Arc"
        ]


        self.HEXA_skill_mastery = {
                    "Hero": {
                         "mastery1_skill":  {"skill_1": {"name": "Raging Blow", "damage": 356,  "number_o_t": 4, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Enhanced "
                                                                 "Raging Blow", "damage": 410,  "number_o_t": 4, "add":10, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Rising Rage", "damage": 181,  "number_o_t": 8, "add": 4, "add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Raging Blow", "damage": 32,   "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Beam Blade",  "damage": 334,  "number_o_t": 5, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Final Blade", "damage": 530,  "number_o_t": 5, "add": 8, "add_attack": 1, "ct": 4, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Rending Edge","damage": 132,  "number_o_t": 3, "add": 5, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Cry Valhalla","damage": 334,  "number_o_t": 5, "add": 6, "add_attack": 12,"ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_2": {"name": "Puncture"    ,"damage": 530,  "number_o_t": 4, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "Final Attack","damage": 132,  "number_o_t": 3, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 61,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }                             
                        },
                    "Paladin": {
                         "mastery1_skill":  {"skill_1": {"name": "Blast",       "damage": 390,  "number_o_t": 10,"add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Divine "
                                                                 "Judgment",    "damage": 783,  "number_o_t": 10,"add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 20,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Divine "
                                                                 "Charge",      "damage": 463,  "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Divine Mark", "damage": 488,  "number_o_t": 7, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Falling "
                                                                 "Justice",     "damage": 911,  "number_o_t": 6, "add": 20,"add_attack": 15,"ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Heaven's "
                                                                 "Hammer",      "damage": 179,  "number_o_t": 0, "add": 9, "add_attack": 1, "ct": 14,"dam": 0, "boss_dam": 30,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Blast",       "damage": 22,   "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Divine "
                                                                 "Judgment",    "damage": 236,  "number_o_t": 0, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Final Attack","damage": 102,  "number_o_t": 2, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 65,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Rising "
                                                                 "Justice",     "damage": 625,  "number_o_t": 6, "add": 15,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "DarkNight": {
                         "mastery1_skill":  {"skill_1": {"name": "Gungnir's "
                                                                 "Descent",     "damage": 245,  "number_o_t": 12,"add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 40,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Dark Impale", "damage": 307,  "number_o_t": 6, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Dark Bident", "damage": 354,  "number_o_t": 7, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Nightshade "
                                                                 "Explosion",   "damage": 402,  "number_o_t": 12,"add": 12,"add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 30,"fainal_dam": 0, "def_a": 60,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Gungnir's "
                                                                 "Descent",     "damage": 58,   "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Revenge of "
                                                                 "the Evil Eye","damage": 90,   "number_o_t": 5, "add": 2, "add_attack": 1, "ct": 14,"dam": 0, "boss_dam": 30,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Final Attack","damage": 88,   "number_o_t": 2, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 65,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Evil Eye "
                                                                 "Shock",       "damage": 700,  "number_o_t": 7, "add": 29,"add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Nightshade "
                                                                 "Explosion",   "damage": 46,   "number_o_t": 0, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Revenge of "
                                                                 "the Evil Eye","damage": 8,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Evil Eye's "
                                                                 "Punishment",  "damage": 16.5, "number_o_t": 0, "add":1.3,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "SoulMaster": {
                         "mastery1_skill":  {"skill_1": {"name": "Luna Divide", "damage": 540,  "number_o_t": 6, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Solar Slash", "damage": 540,  "number_o_t": 6, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Equinox "
                                                                 "Power",       "damage": 3600, "number_o_t": 5, "add":100,"add_attack": 1, "ct": 20,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Cosmic Shower","damage": 305,  "number_o_t": 3, "add": 15,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Cosmic Burst","damage": 500,  "number_o_t": 4, "add": 20,"add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Equinox "
                                                                 "Slash",       "damage": 267,  "number_o_t": 6, "add": 7, "add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Equinox "
                                                                 "Power II",    "damage": 377,  "number_o_t": 5, "add": 17,"add_attack": 12,"ct": 20,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Cosmic Shower","damage": 12,   "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Cosmic Burst","damage": 18,   "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "Aran": {
                         "mastery1_skill":  {"skill_1": {"name": "Beyond Blade","damage": 443,  "number_o_t": 15,"add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 30,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Finisher - "
                                                                "Hunter's Prey","damage": 892,  "number_o_t": 22,"add": 15,"add_attack": 10,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Beyond Blade","damage": 48,   "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Hyper Finisher"
                                                               " - Last Stand", "damage": 875,  "number_o_t": 10,"add": 28,"add_attack": 10,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Adrenaline "
                                                                 "Overload",    "damage": 726,  "number_o_t": 10,"add": 16,"add_attack": 6, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Final Attack","damage": 201,  "number_o_t": 3, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 61,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Permafrost",  "damage": 566,  "number_o_t": 4, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "DemonSlayer": {
                         "mastery1_skill":  {"skill_1": {"name": "Demon "
                                                                 "Impact",      "damage": 487,  "number_o_t": 6, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 45,"fainal_dam": 40,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Demon Chain", "damage": 639,  "number_o_t": 6, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 45,"fainal_dam": 40,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Demon Lash",  "damage": 216.5,"number_o_t": 6, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Demonic "
                                                                 "Spear",       "damage": 355,  "number_o_t": 6, "add": 5, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Demonic "
                                                    "Spear[Demon Awakening]",   "damage": 510,  "number_o_t": 6, "add": 10,"add_attack": 1, "ct": 3, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Infernal "
                                                                 "Concussion",  "damage": 324,  "number_o_t": 5, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Demon Impact","damage": 12,   "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Demon Chain", "damage": 32,   "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Demon Cry",   "damage": 575,  "number_o_t": 7, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Dark"
                                                                "Metamorphosis","damage": 713,  "number_o_t": 4, "add": 13,"add_attack": 1, "ct": 0, "dam": 45,"boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_3": {"name": "Demon Impact","damage": 0.5,  "number_o_t": 0, "add":0.5,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Demon Chain", "damage": 521,  "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Cerberus"
                                                                 "Chomp",       "damage": 495,  "number_o_t": 6, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 50,"fainal_dam": 0, "def_a": 50,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Cerberus "
                                                    "Chomp: Teeth of Tartarus", "damage": 317,  "number_o_t": 7, "add": 7, "add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Demonic"
                                                                 "Plume",       "damage":1142,  "number_o_t": 7, "add": 22,"add_attack": 5, "ct": 20,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "DemonAvenger": {
                         "mastery1_skill":  {"skill_1": {"name": "Nether "
                                                                 "Shield",      "damage": 521,  "number_o_t": 16,"add": 11,"add_attack": 3, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Execution",   "damage": 603,  "number_o_t": 4, "add": 13,"add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 35,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Lunar Slash", "damage": 708,  "number_o_t": 3, "add": 15,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Maximal "
                                                                 "Exceed",      "damage": 1530, "number_o_t": 7, "add": 30,"add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Thousand "
                                                                 "Swords",      "damage": 552,  "number_o_t": 8, "add": 12,"add_attack": 1, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Infernal "
                                                                 "Exceed",      "damage": 231,  "number_o_t": 2, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 80,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Execution",   "damage": 92,   "number_o_t": 0, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Kaiser": {
                         "mastery1_skill":  {"skill_1": {"name": "Gigas Wave",  "damage": 406,  "number_o_t": 9, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Gigas Wave"
                                                                 "[Final Form]","damage": 406,  "number_o_t": 11,"add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Blade Burst", "damage": 540,  "number_o_t": 5, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Tempest "
                                                                 "Blades",      "damage": 543,  "number_o_t": 4, "add": 8, "add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "Tempest "
                                                        "Blades[Final Form]",   "damage": 543,  "number_o_t": 5, "add": 8, "add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Inferno "
                                                                 "Breath",      "damage": 1701, "number_o_t": 14,"add": 51,"add_attack": 1, "ct": 19,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Ultimate "
                                                         "Inferno Breath",      "damage": 1103, "number_o_t": 8, "add": 33,"add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Wing Beat",   "damage": 220,  "number_o_t":2.67,"add":6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Stone Dragon","damage": 440,  "number_o_t": 3, "add": 10,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Gigas Wave",  "damage": 17,   "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Draco Surge", "damage": 23,   "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "Hayato": {
                         "mastery1_skill":  {"skill_1": {"name": "[Shinsoku] "
                                                         "Mist Slash",          "damage": 224,  "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "[Shinsoku] "
                                                         "Afterimage Slash",    "damage": 527,  "number_o_t": 10,"add": 7, "add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "[Shinsoku] Crescent Moon Cut",    
                                                                                "damage": 705,  "number_o_t": 10,"add": 5, "add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "[Shinsoku] Silent Arc",            
                                                                                "damage": 303,  "number_o_t": 10,"add": 3, "add_attack": 5, "ct": 20,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "[Battou] Dark Moon Cut",       
                                                                                "damage": 476,  "number_o_t": 10,"add": 6, "add_attack": 10,"ct": 20,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "[Battou] Full Moon's Rage",      
                                                                                "damage": 378,  "number_o_t": 12,"add": 8, "add_attack": 16,"ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Zero": {
                         "mastery1_skill":  {"skill_1": {"name": "Giga Crash",  "damage": 244,  "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Falling Star","damage": 204,  "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name":"Groundbreaker","damage": 371,  "number_o_t": 10,"add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "Wind Cutter", "damage": 178,  "number_o_t": 7, "add": 3, "add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_5": {"name": "Wind Striker","damage": 239,  "number_o_t": 8, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "Storm Break", "damage": 330,  "number_o_t": 10,"add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_7": {"name": "Time Piece",  "damage": 976,  "number_o_t": 4, "add": 16,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Spin Driver", "damage": 291,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Wheel Wind",  "damage": 220,  "number_o_t": 2, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Rolling Cross","damage": 397, "number_o_t": 12,"add": 7, "add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "Rolling "
                                                                 "Assault",     "damage": 412,  "number_o_t": 12,"add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Flash Cut",   "damage": 230,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Throwing "
                                                                 "Weapon",      "damage": 357,  "number_o_t": 4, "add": 7, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Flash Assault","damage": 163, "number_o_t": 5, "add": 3, "add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Blade Ring",  "damage": 290,  "number_o_t": 9, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Rising Slash","damage": 220,  "number_o_t": 6, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Air Raid",    "damage": 345,  "number_o_t": 6, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Moon Strike", "damage": 133,  "number_o_t": 6, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Piercing "
                                                                 "Thrust",      "damage": 188,  "number_o_t": 6, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name":"Shadow Strike","damage": 215,  "number_o_t": 8, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "Shadow Rain", "damage": 900,  "number_o_t": 14,"add": 25,"add_attack": 1, "ct":300,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_7": {"name": "Resonance",   "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_8": {"name": "Giga Crash",  "damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_9": {"name": "Falling Star","damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_10":{"name":"Groundbreaker","damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_11":{"name":"Wind Cutter",  "damage": 12,   "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_12":{"name":"Wind Cutter "
                                                                  "Swirlingr",  "damage": 11,   "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_13":{"name":"Wind Striker", "damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_14":{"name":"Storm Break ", "damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "Michael": {
                         "mastery1_skill":  {"skill_1": {"name": "Radiant Cross","damage": 594, "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Radiant Cross"
                                                                 "- Assault",   "damage": 356,  "number_o_t": 10,"add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Royal Guard", "damage": 648,  "number_o_t": 4, "add": 18,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Install Shield","damage": 251,"number_o_t": 4, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Charging Light","damage": 917,"number_o_t": 10,"add": 27,"add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Charging Light"
                                                                 "[Blade]",       "damage": 254,"number_o_t": 8, "add": 9, "add_attack": 5, "ct": 35,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Offensive "
                                                                 "Defense",     "damage": 669,  "number_o_t": 5, "add": 24,"add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Final Attack","damage": 106,  "number_o_t": 4, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 76,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Soul Majesty","damage": 773,  "number_o_t": 6, "add": 28,"add_attack": 1, "ct":120,"dam": 15,"boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Blaster": {
                         "mastery1_skill":  {"skill_1": {"name": "Magnum Punch","damage": 597,  "number_o_t": 3, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Double Blast","damage": 506,  "number_o_t": 4, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Bunker Buster "
                                                                 "Explosion",   "damage": 725,  "number_o_t": 8, "add": 15,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Burst "
                                                                 "Pile Bunker", "damage": 500,  "number_o_t": 10,"add": 10,"add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Revolving "
                                                                 "Cannon Mastery","damage":381, "number_o_t": 1, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability":100,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Hammer Smash","damage": 332,  "number_o_t": 6, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Shotgun Punch","damage": 199, "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Magnum Punch","damage": 15.4, "number_o_t": 0, "add":2.4,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Double Blast","damage": 10.55,"number_o_t": 0,"add":2.05,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Revolving "
                                                                 "Cannon",      "damage": 298,  "number_o_t": 4, "add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Ballistic "
                                                                 "Hurricane",   "damage": 1389, "number_o_t": 5, "add": 39,"add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Adel": {
                         "mastery1_skill":  {"skill_1": {"name": "Cleave",      "damage": 402,  "number_o_t": 6, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Enhanced "
                                                                 "Cleave",      "damage": 309,  "number_o_t": 7, "add": 9, "add_attack": 3, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Magic "
                                                                 "Dispatch",    "damage": 488,  "number_o_t": 3, "add": 8, "add_attack": 5, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Aetherial "
                                                                 "Arms",        "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Hunting "
                                                                 "Decree",      "damage": 394,  "number_o_t": 2, "add": 14,"add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Plummet",     "damage": 583,  "number_o_t": 6, "add": 8, "add_attack": 1, "ct":1.5,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Impale",      "damage": 368,  "number_o_t": 6, "add": 8, "add_attack": 1, "ct": 7, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Resonance "
                                                                 "Rush",        "damage": 427,  "number_o_t": 6, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_3": {"name": "Noble "
                                                                 "Summons",     "damage": 622,  "number_o_t": 4, "add": 12,"add_attack": 0, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_4": {"name": "Aether "
                                                                 "Bloom",       "damage": 723,  "number_o_t": 8, "add": 13,"add_attack": 8, "ct": 20,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Cleave",      "damage": 11,   "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Aether Forge","damage": 788,  "number_o_t": 1, "add": 8, "add_attack": 6,"ct":0.25,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Reign of "
                                                                 "Destruction", "damage": 555,  "number_o_t": 4, "add": 5, "add_attack": 2, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Shardbreaker","damage": 2755, "number_o_t": 6, "add": 30,"add_attack": 3, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "IceLightning": {
                         "mastery1_skill":  {"skill_1": {"name": "Chain "
                                                                 "Lightning",   "damage": 248,  "number_o_t": 10,"add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Current Zone","damage": 82,   "number_o_t": 2, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Frozen Orb",  "damage": 271,  "number_o_t": 20,"add":203,"add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Blizzard",    "damage": 340,  "number_o_t": 12,"add": 10,"add_attack": 1, "ct": 45,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Final Attack","damage": 255,  "number_o_t": 1, "add": 29,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 70,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Lightning Orb","damage": 11,  "number_o_t": 0,"add":15/29,"add_attack": 1,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Lightning Orb"
                                                                 "Finish",       "damage": 75,  "number_o_t": 0, "add":2,  "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Lightning Orb","damage": 170, "number_o_t": 15,"add": 3, "add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Cryo Shock",  "damage": 713,  "number_o_t": 15,"add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name":"Thunder Sphere","damage":413,  "number_o_t": 3, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Elquines",    "damage": 143,  "number_o_t": 3, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Cryo Shock",  "damage": 107,  "number_o_t": 0, "add": 20,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "FirePoison": {
                         "mastery1_skill":  {"skill_1": {"name": "Flame Sweep", "damage": 239,  "number_o_t": 7, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "the giant "
                                            "flame have an ember[explosion]",   "damage": 143,  "number_o_t": 8, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Flame Haze",  "damage": 219,  "number_o_t": 15,"add": 4, "add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Mist Eruption","damage": 128, "number_o_t": 10,"add": 3, "add_attack": 5, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam":170,"def_a": 45,"is_skill": True, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Ignite",      "damage": 46,   "number_o_t": 3, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Ifrit",       "damage": 170,  "number_o_t": 3, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Inferno Aura","damage": 452,  "number_o_t": 2, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Creeping "
                                                                 "Toxin",       "damage": 220,  "number_o_t": 1, "add": 3, "add_attack": 10,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Meteor Shower","damage": 352, "number_o_t": 12,"add": 12,"add_attack": 1, "ct": 50,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Megiddo Flame","damage": 341, "number_o_t": 5, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Megiddo Flame"
                                                            "[mode Explosion]",  "damage": 252, "number_o_t": 3, "add": 7, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Final Attack","damage": 238,  "number_o_t": 1, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 65,"passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Bishop": {
                         "mastery1_skill":  {"skill_1": {"name": "Angel Ray",   "damage": 239,  "number_o_t": 14,"add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Angel of "
                                                                 "Judgment",    "damage": 559,  "number_o_t": 10,"add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Big Bang",    "damage": 530,  "number_o_t": 4, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Holy Explosion","damage":454,  "number_o_t": 6, "add": 9, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Triumph "
                                                                 "Feather",     "damage": 396,  "number_o_t": 4, "add": 6, "add_attack": 1, "ct": 4, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name":"Angelic Wrath","damage": 276,  "number_o_t": 7, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_2": {"name":"Fountain of "
                                                                "Vengeance",    "damage": 194,  "number_o_t": 5, "add": 4, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Bahamut",     "damage": 198,  "number_o_t": 3, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Angel Ray",   "damage": 5.5,  "number_o_t": 0, "add":0.5,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Angel of "
                                                                 "Judgment",    "damage": 6,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Genesis",     "damage": 361,  "number_o_t": 10,"add": 16,"add_attack": 1, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Heaven's Door","damage": 573,  "number_o_t": 10,"add": 8, "add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Final Attack","damage": 202,  "number_o_t": 1, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 65,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "FlameWizard": {
                         "mastery1_skill":  {"skill_1": {"name": "Orbital Flame "
                                                                 "[Normal]",    "damage": 411,  "number_o_t": 2, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Orbital Flame "
                                                                 "[Enhanced]",  "damage": 646,  "number_o_t": 2, "add": 1, "add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Orbital Flame "
                                                          "[Normal, Flame Fox]","damage": 731,  "number_o_t": 2, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "Orbital Flame "
                                                        "[Enhanced, Flame Fox]","damage": 916,  "number_o_t": 2, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Blazing Extinction [Blazing Lion]",            
                                                                                "damage": 653,  "number_o_t": 4, "add": 13,"add_attack": 4, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Blazing Extinction [Flame Fox]",            
                                                                                "damage": 424,  "number_o_t": 12,"add": 14,"add_attack": 10,"ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Orbital "
                                                                 "Explosion",   "damage": 98,   "number_o_t": 3, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Phoenix Drive "
                                                               "[Blazing Lion]","damage": 529,  "number_o_t": 2, "add": 29,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name":"Phoenix Drive "
                                                               "[Flame Fox]",   "damage": 756,  "number_o_t": 2, "add": 16,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name":"",             "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Towering Inferno [Blazing Lion]",            
                                                                                "damage": 355,  "number_o_t": 10,"add": 5, "add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Towering Inferno [Flame Fox]",            
                                                                                "damage": 699,  "number_o_t": 12,"add": 10,"add_attack": 3, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "BattleMage": {
                         "mastery1_skill":  {"skill_1": {"name": "Condemnation","damage": 524,  "number_o_t": 12,"add": 14,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Condemnation "
                                                                 "[enhanced]",  "damage": 837,  "number_o_t": 14,"add": 22,"add_attack": 1, "ct": 4, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Finishing "
                                                                 "Blow",        "damage": 376,  "number_o_t": 6, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 22,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Sweeping "
                                                                 "Staff",       "damage": 371,  "number_o_t": 5, "add": 11,"add_attack": 1, "ct": 13,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "Ambassador "
                                                                 "Scythe",      "damage": 50,   "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Dark Shock",  "damage": 171,  "number_o_t": 4, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Dark Brand",  "damage": 482,  "number_o_t": 4, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 20,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Dark Pentacle","damage": 610,  "number_o_t": 6, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 20,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Dark Genesis","damage": 600,  "number_o_t": 8, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Dark Genesis: "
                                                                 "Death Whip",  "damage": 163,  "number_o_t": 10,"add": 3, "add_attack": 6, "ct": 36,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Final Attack","damage": 285,  "number_o_t": 1, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 80,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Dark Brand",  "damage": 1,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "Evan": {
                         "mastery1_skill":  {"skill_1": {"name": "Mana Burst",  "damage": 323,  "number_o_t": 4, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Thunder "
                                                                 "Circle",      "damage": 469,  "number_o_t": 5, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Dragon Flash","damage": 558,  "number_o_t": 4, "add": 8, "add_attack": 7, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Thunder Flash","damage": 1430, "number_o_t": 9, "add": 30,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Wind Flash",  "damage": 526,  "number_o_t": 10,"add": 6, "add_attack": 7, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-35,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Earth Circle","damage": 469,  "number_o_t": 5, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Dragon Dive", "damage": 363,  "number_o_t": 3, "add": 11,"add_attack": 7, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Earth Dive",  "damage": 1143, "number_o_t": 10,"add": 33,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Thunder Dive","damage": 383,  "number_o_t": 4, "add": 7, "add_attack": 8, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Wind Circle", "damage": 469,  "number_o_t": 5, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Dragon Breath","damage": 273,  "number_o_t": 5, "add": 8, "add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Earth Breath","damage": 303,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Wind Breath", "damage": 235,  "number_o_t": 6, "add": 12,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Magic Debris","damage": 149,  "number_o_t": 1, "add": 14,"add_attack":2.5,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "Dragon Spark","damage": 209,  "number_o_t": 1, "add": 14,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability":100,"passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Luminous": {
                         "mastery1_skill":  {"skill_1": {"name": "Ender",       "damage": 492,  "number_o_t": 7, "add": 7, "add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 45,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Reflection",  "damage": 491,  "number_o_t": 4, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Darkness",    "damage": 855,  "number_o_t": 5, "add": 25,"add_attack": 1, "ct": 2, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Ender",       "damage": 43,   "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Apocalypse",  "damage": 420,  "number_o_t": 7, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Eternal "
                                                                 "Light",       "damage": 630,  "number_o_t": 7, "add": 25,"add_attack": 1, "ct": 2, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Twilight "
                                                                 "Nova",        "damage": 470,  "number_o_t": 7, "add": 40,"add_attack": 3, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Twilight "
                                                         "Nova[Equilibrium]",   "damage": 400,  "number_o_t": 7, "add": 25,"add_attack": 4, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Kanna": {
                         "mastery1_skill":  {"skill_1": {"name": "Soul-Shatter "
                                                          "Talisman: Dance",    "damage": 284,  "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Heart-Wreck "
                                                                   "Talisman",  "damage": 286,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Summon Oni",  "damage": 437,  "number_o_t": 6, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "[Order] "
                                                         "Spinning Strike",     "damage": 376,  "number_o_t": 8, "add": 6, "add_attack": 12,"ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "[Order] "
                                                         "Pulverizing Strike",  "damage": 560,  "number_o_t": 12,"add": 10,"add_attack": 12,"ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Summon Tengu","damage": 893,  "number_o_t": 12,"add": 13,"add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 100,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Shade-Fletched"
                                                         " Arrow",              "damage": 254,  "number_o_t": 8, "add": 4, "add_attack": 6, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 50,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name":"Summon Orochi"
                                                         "[Dance of Poison]",   "damage": 468,  "number_o_t": 12,"add": 5, "add_attack": 2, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Summon Orochi"
                                                         "[Poison]",            "damage": 91,   "number_o_t": 1, "add": 1, "add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Summon Orochi"
                                                         "[Shadow Cleave]",     "damage": 631,  "number_o_t": 8, "add": 11,"add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "[Order] "
                                                         "Execute",             "damage": 508,  "number_o_t": 14,"add": 8, "add_attack": 12,"ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 30,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Kinesis": {
                         "mastery1_skill":  {"skill_1": {"name": "Ultimate - "
                                                                 "Metal Press", "damage": 760,  "number_o_t": 10,"add": 15,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Psychic Grab","damage": 507,  "number_o_t": 5, "add": 17,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Ultimate - "
                                                                 "Psychic Shot","damage": 504,  "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Ultimate - "
                                                                 "Trainwreck",  "damage": 234,  "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Ultimate - "
                                                                 "B.P.M.",      "damage": 193,  "number_o_t": 7, "add": 3, "add_attack": 1, "ct":0.5,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Kinetic "
                                                                 "Combo",       "damage": 386,  "number_o_t": 1, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 70,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Illium": {
                         "mastery1_skill":  {"skill_1": {"name": "Radiant "
                                                                 "Javelin",     "damage": 435,  "number_o_t": 3, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Radiant "
                                                            "Enchanted Javelin","damage": 435,  "number_o_t": 3, "add": 5, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Winged Javelin","damage":751,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name":"Winged "
                                                             "Enchanted Javelin","damage": 751, "number_o_t": 6, "add": 6, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Reaction - "
                                                                 "Destruction", "damage": 797,  "number_o_t": 6, "add": 12,"add_attack": 2, "ct": 4, "dam": 0, "boss_dam": 20,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Reaction - "
                                                                 "Domination",  "damage": 567,  "number_o_t": 5, "add": 12,"add_attack": 1, "ct": 4, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Vortex Wings","damage": 1620, "number_o_t": 15,"add": 20,"add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Enchanted "
                                                                 "Javelin",     "damage": 54,   "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Ex",          "damage": 272,  "number_o_t": 40,"add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Machina",     "damage": 387,  "number_o_t": 4, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Crystal Skill "
                                                                 "- Deus",      "damage": 561,  "number_o_t": 10,"add": 31,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Longinus "
                                                                 "Spear",       "damage": 978,  "number_o_t": 14,"add": 28,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 20,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Umbral "
                                                                 "Brand III",   "damage": 220,  "number_o_t": 0, "add": 20,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_3": {"name":"Longinus Zone","damage": 1066, "number_o_t": 5, "add": 16,"add_attack": 4, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Radiant "
                                      "Javelin   Radiant Enchanted Javelin",    "damage": 1,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "Lara": {
                         "mastery1_skill":  {"skill_1": {"name": "Essence "
                                                                 "Sprinkle",    "damage": 492,  "number_o_t": 4, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Mountain Kid","damage": 80,   "number_o_t": 0, "add": 20,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Mountain Seeds","damage":80,   "number_o_t": 0, "add": 20,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Dragon Vein "
                                                                 "Eruption",    "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Eruption: "
                                                                "Heaving River","damage": 791,  "number_o_t": 5, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Eruption: "
                                                                 "Whirlwind",   "damage": 516,  "number_o_t": 5, "add": 6, "add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Eruption: "
                                                                 "Sunrise Well","damage": 770,  "number_o_t": 6, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_5": {"name": "Eruption: Sunrise Well[Volcanic Bomb]",
                                                                                "damage": 472,  "number_o_t": 3, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_6": {"name": "Eruption: "
                                                                 "Sunrise Well[Volcanic Bomb duration]",
                                                                                "damage": 137,  "number_o_t": 1, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Dragon Vein "
                                                                "Absorption",   "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Absorption: "
                                                    "River Puddle Douse",       "damage": 572,  "number_o_t": 10,"add": 5, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Absorption: "
                                                                "Fierce Wind",  "damage": 273,  "number_o_t": 3, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Absorption: "
                                                                "Sunlit Grain", "damage": 293,  "number_o_t": 6, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}                                
                                            ,"skill_5": {"name": "Eruption",    "damage": 6,    "number_o_t": 0, "add":0.5,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Wakeup Call", "damage": 715,  "number_o_t": 4, "add": 15,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Eruption, Absorption",            
                                                                                "damage": 1,    "number_o_t": 0, "add":0.5,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Lynn": {
                         "mastery1_skill":  {"skill_1": {"name": "Strike",      "damage": 340,  "number_o_t": 6, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Sneak Attack","damage": 700,  "number_o_t": 8, "add": 20,"add_attack": 1, "ct": 2, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Raid",        "damage": 1894, "number_o_t": 15,"add": 34,"add_attack": 1, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Peck",        "damage": 904,  "number_o_t": 6, "add": 24,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "[Focus] Heal","damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_2": {"name": "[Focus] "
                                                         "Forest Protection",   "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_3": {"name": "Mother "
                                                         "Nature's Touch",      "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Bowmaster": {
                         "mastery1_skill":  {"skill_1": {"name": "Hurricane",   "damage": 372,  "number_o_t": 1, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Shootout Mode","damage": 489,  "number_o_t": 1, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Arrow Stream","damage": 436,  "number_o_t": 5, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Arrow Blaster","damage": 240,  "number_o_t": 1, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Advanced Final Attack",            
                                                                                "damage": 117,  "number_o_t": 1, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Quiver "
                                                                 "Cartridge",   "damage": 297,  "number_o_t": 1, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Phoenix",     "damage": 511,  "number_o_t": 1, "add": 16,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Extra Quiver "
                                                                 "Cartridge",   "damage": 784,  "number_o_t": 1, "add": 29,"add_attack": 50,"ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Speed Mirage","damage": 636,  "number_o_t": 4, "add": 21,"add_attack": 1, "ct": 1, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Gritty Gust", "damage": 367,  "number_o_t": 12,"add": 7, "add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Crossbowmaster": {
                         "mastery1_skill":  {"skill_1": {"name": "Snipe",       "damage": 496,  "number_o_t": 9, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Empowered "
                                                                 "Snipe",       "damage": 490,  "number_o_t": 10,"add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "Ultimate "
                                                                 "Snipe",       "damage": 258,  "number_o_t": 10,"add": 3, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Piercing "
                                                                 "Arrow",       "damage": 381,  "number_o_t": 5, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Empowered "
                                                               "Piercing Arrow","damage": 467,  "number_o_t": 10,"add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Ultimate "
                                                               "Piercing Arrow","damage": 477,  "number_o_t": 6, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Piercing "
                                                        "Arrow[passive]",       "damage": 3,    "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Empowered "
                                                        "Piercing Arrow[passive]","damage": 5,  "number_o_t": 0, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            ,"skill_6": {"name": "Ultimate "
                                                        "Piercing Arrow[passive]","damage": 2,  "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Frostprey",   "damage": 335,  "number_o_t": 3, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Bolt Burst",  "damage": 477,  "number_o_t": 7, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Piercing "
                                                        "Arrow[passive]",       "damage": 4,    "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Empowered "
                                                        "Piercing Arrow[passive]","damage": 8,  "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "Empowered "
                                                   "Piercing Arrow[passive][add]","damage": 4,  "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            ,"skill_5": {"name": "Ultimate "
                                                        "Piercing Arrow[passive]","damage": 5,  "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            ,"skill_5": {"name": "Ultimate "
                                                   "Piercing Arrow[passive][add]","damage": 3,  "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            }#addダメージpassive
                        ,"mastery4_skill":  {"skill_1": {"name": "Final Attack","damage": 224,  "number_o_t": 1, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 60,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "High Speed "
                                                                 "Shot",        "damage": 378,  "number_o_t": 9, "add": 6, "add_attack": 6, "ct": 40,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Piercing "
                                                        "Arrow[passive]",       "damage": 1,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Empowered "
                                                        "Piercing Arrow[passive]","damage": 1,  "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            ,"skill_5": {"name": "Ultimate "
                                                        "Piercing Arrow[passive]","damage": 1,  "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            }
                        },
                    "Pathfinder": {
                         "mastery1_skill":  {"skill_1": {"name": "Cardinal "
                                                                    "Burst",    "damage": 638,  "number_o_t": 5, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Bountiful "
                                                            "Burst",            "damage": 243,  "number_o_t": 3, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Cursed Arrows","damage": 122,  "number_o_t": 4, "add": 2,"add_attack":16.34,"ct":20,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Cardinal " 
                                                           "Deluge",            "damage": 330,  "number_o_t": 5, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Bountiful "
                                                           "Deluge",            "damage": 188,  "number_o_t": 3, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 45,"passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Glyph of "
                                                      "Impalement",             "damage": 949,  "number_o_t": 6, "add": 29,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Ancient "
                                                          "Impact",             "damage": 1611, "number_o_t": 10,"add": 34,"add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Cardinal "
                                                         "Torrent",             "damage": 610,  "number_o_t": 5, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name":"Ancient Astra","damage": 364,  "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name":"Ancient Astra"
                                                                 " (Deluge)",   "damage": 455,  "number_o_t": 6, "add": 5, "add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_6": {"name":"Ancient Astra"
                                                                 " (Burst)",    "damage": 1609, "number_o_t": 10,"add": 19,"add_attack": 1, "ct": 90,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_7": {"name": "Ancient Astra"
                                                                 " (Torrent)",  "damage": 424,  "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name":"Combo Assault","damage": 562,  "number_o_t": 7, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Combo Assault"
                                                                 " (Deluge)",   "damage": 683,  "number_o_t": 7, "add": 8, "add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "Combo Assault"
                                                                 " (Burst)",    "damage": 810,  "number_o_t": 10,"add": 36,"add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "Combo Assault"
                                                                 " (Torrent)",  "damage": 683,  "number_o_t": 7, "add": 8, "add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_5": {"name": "Shadow Raven","damage": 440,  "number_o_t": 1, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_6": {"name":"Manifest Curse","damage": 409, "number_o_t": 1, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            }
                        },
                    "Windshooter": {
                         "mastery1_skill":  {"skill_1": {"name": "Song of "
                                                                 "Heaven",      "damage": 575,  "number_o_t": 1, "add": 20,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Trifling "
                                                                 "Wind",        "damage": 314,  "number_o_t": 1, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 50,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Trifling "
                                                            "Wind[enhanced]",   "damage": 443,  "number_o_t": 1, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 20,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Storm "
                                                                 "Bringer",     "damage": 707,  "number_o_t": 1, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 45,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Fairy Spiral","damage": 422,  "number_o_t": 5, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Monsoon",     "damage": 473,  "number_o_t": 12,"add": 8, "add_attack": 1, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Storm Whim",  "damage": 616,  "number_o_t": 1, "add": 11,"add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Anemoi",      "damage": 950,  "number_o_t": 15,"add": 27,"add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "WildHunter": {
                         "mastery1_skill":  {"skill_1": {"name": "Wild Arrow "
                                                                 "Blast",       "damage": 385,  "number_o_t": 1, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 10,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Wild Arrow "
                                                             "Blast [Mounted]", "damage": 200,  "number_o_t": 2, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Swipe",       "damage": 526,  "number_o_t": 4, "add": 6, "add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Wild Lure",   "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_3": {"name":"Dash 'n Slash","damage": 561,  "number_o_t": 2, "add": 6, "add_attack": 1, "ct": 7, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Dash 'n Slash "
                                                                 "[Mounted]",   "damage": 561,  "number_o_t": 2, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Sonic Roar",  "damage": 554,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "Jaguar Soul", "damage": 346,  "number_o_t": 12,"add": 4, "add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_7": {"name": "Jaguar "
                                                                 "Rampage",     "damage": 498,  "number_o_t": 15,"add": 6, "add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_8": {"name": "Exploding "
                                                                 "Arrows",      "damage": 443,  "number_o_t": 11,"add": 7, "add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Summon "
                                                                 "Jaguar",      "damage": 438,  "number_o_t": 1, "add": 8, "add_attack": 1, "ct": 1, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Another Bite","damage": 204,  "number_o_t": 1, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability":100,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Hunting "
                                                   "Assistant Unit",            "damage": 165,  "number_o_t": 6, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Drill Salvo", "damage": 478,  "number_o_t": 1, "add": 9, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Final Attack", "damage": 418,  "number_o_t": 1, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 71,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Mercedes": {
                         "mastery1_skill":  {"skill_1": {"name": "Ishtar's "
                                                                 "Ring",        "damage": 351,  "number_o_t": 2, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Ishtar's "
                                                                 "Mark",        "damage": 356,  "number_o_t": 3, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Wrath of "
                                                                 "Enlil",       "damage": 560,  "number_o_t": 10,"add": 10,"add_attack": 1, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Wrath of "
                                                        "Enlil: Spirit Enchant","damage": 616,  "number_o_t": 10,"add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name":"Spikes Royale","damage": 707,  "number_o_t": 4, "add": 12,"add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name":"Spikes Royale:"
                                                         " Spirit Enchant",     "damage": 754,  "number_o_t": 4, "add": 14,"add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Leaf Tornado","damage": 519,  "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "Leaf Tornado: "
                                                         "Spirit Enchant",      "damage": 599,  "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}                                            
                                            ,"skill_7": {"name": "Ishtar's "
                                                                 "Mark",        "damage": 31,   "number_o_t": 0, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": True}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Unicorn "
                                                         "Spike",               "damage": 619,  "number_o_t": 6, "add": 11,"add_attack": 1, "ct": 9, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_2": {"name": "Gust Dive",   "damage": 572,  "number_o_t": 4, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Stunning "
                                                                 "Strikes",     "damage": 600,  "number_o_t": 4, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Ishtar's "
                                                                 "Ring",        "damage": 1,    "number_o_t": 0,"add":0.65,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Elemental "
                                                                 "Knights",     "damage": 238,  "number_o_t": 1, "add": 3, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Final "
                                                                 "Attack",      "damage": 229,  "number_o_t": 2, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 76,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Cain": {
                         "mastery1_skill":  {"skill_1": {"name": "Falling Dust","damage": 504,  "number_o_t": 8, "add": 14,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "[Possess] "
                                                                 "Falling Dust","damage": 566,  "number_o_t": 10,"add": 16,"add_attack": 1, "ct": 14,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "[Execute] "
                                                                "Poison Needle","damage": 391,  "number_o_t": 8, "add": 11,"add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "[Execute] "
                                          "Poison Needle[consecutive attack]",  "damage": 330,  "number_o_t": 1, "add": 10,"add_attack": 1, "ct": 15, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Strike "
                                                                 "Arrow",       "damage": 409,  "number_o_t": 5, "add": 9, "add_attack": 1, "ct": 1, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "[Possess] "
                                                                "Strike Arrow", "damage": 614,  "number_o_t": 8, "add": 14,"add_attack": 1, "ct": 1, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Scattering "
                                                                 "Shot",        "damage": 274,  "number_o_t": 4, "add": 6, "add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "[Possess] "
                                                              "Scattering Shot","damage": 431,  "number_o_t": 4, "add": 11,"add_attack": 7, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "[Execute] "
                                                              "Tearing Knife",  "damage": 513,  "number_o_t": 7, "add": 13,"add_attack": 1, "ct":4.5,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "[Execute] "
                                                                 "Chain Sickle","damage": 322,  "number_o_t": 6, "add": 7, "add_attack": 1, "ct": 7, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Dragon Fang", "damage": 292,  "number_o_t": 4, "add": 5, "add_attack": 3, "ct": 3, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Shaft Break", "damage": 290,  "number_o_t": 3, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "(Possess) "
                                                                 "Shaft Break", "damage": 463,  "number_o_t": 3, "add": 11,"add_attack": 1, "ct": 11,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "(Execute) "
                                                                "Phantom Blade","damage": 426,  "number_o_t": 6, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Lasting "
                                                                 "Grudge",      "damage": 275,  "number_o_t": 4, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Death's "
                                                                 "Blessing",    "damage": 330,  "number_o_t": 10,"add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Chasing Shot", "damage": 386,  "number_o_t": 6, "add": 10,"add_attack": 3, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Unseen "
                                                                 "Sniper",      "damage": 211,  "number_o_t": 10,"add": 6, "add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "(Possess/"
                                                    "Execute) Unseen Sniper",   "damage": 316,  "number_o_t": 12,"add": 8, "add_attack": 15,"ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Death's "
                                                                 "Blessing",    "damage": 36,   "number_o_t": 0, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Shadow": {
                         "mastery1_skill":  {"skill_1": {"name": "Assassinate", "damage": 279,  "number_o_t": 6, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Pulverize",   "damage": 306,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Meso "
                                                         "Explosion",           "damage": 155,  "number_o_t": 2, "add": 5, "add_attack": 15,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Meso "
                                                    "Explosion[Blood Money]",   "damage": 155,  "number_o_t": 2, "add": 5, "add_attack": 15,"ct": 0, "dam": 0, "boss_dam": 40,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Dark Flare",  "damage": 406,  "number_o_t": 1, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Cruel Stab",  "damage": 286,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Assassinate", "damage": 13,   "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Pulverize",   "damage": 13,   "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Sudden Raid", "damage": 539,  "number_o_t": 7, "add": 9, "add_attack": 1, "ct": 14,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Shadow Veil", "damage": 874,  "number_o_t": 1, "add": 14,"add_attack": 2, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Covert Edge", "damage": 92,   "number_o_t": 2, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 60,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Shadow Edge", "damage": 100,  "number_o_t": 1, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability":100,"passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "KnightLord": {
                         "mastery1_skill":  {"skill_1": {"name": "Quad Star",   "damage": 547,  "number_o_t": 4, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Enhanced Quad "
                                                                 "Star",        "damage": 700,  "number_o_t": 4, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Assassin's "
                                                                 "Mark",        "damage": 383,  "number_o_t": 1, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 65,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Dark Flare",  "damage": 409,  "number_o_t": 1, "add": 14,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Showdown",    "damage": 793,  "number_o_t": 2, "add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Showdown"
                                                              "[Shurikens]",    "damage": 28,   "number_o_t": 6, "add":  1,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "Darkness "
                                                                 "Shuriken",    "damage": 695,  "number_o_t": 6, "add": 25,"add_attack": 5, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Quad Star",   "damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Sudden Raid", "damage": 559,  "number_o_t": 7, "add": 9, "add_attack": 1, "ct": 14,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Death Star",  "damage": 447,  "number_o_t": 7, "add": 17,"add_attack": 1, "ct": 14,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Death Star: "
                                                            "Rampant[enhances]","damage": 519,  "number_o_t": 7, "add": 11,"add_attack": 1, "ct": 14,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "Assassin's "
                                                                 "Mark",        "damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "DualBlade": {
                         "mastery1_skill":  {"skill_1": {"name": "Phantom Blow","damage": 356,  "number_o_t": 6, "add": 6, "add_attack": 11,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 40,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Asura's "
                                                                 "Anger",       "damage": 617,  "number_o_t": 6, "add": 17,"add_attack": 11,"ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a":100,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Phantom Blow","damage": 48,   "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Blade Clone", "damage": 306,  "number_o_t": 1, "add": 6, "add_attack": 1, "ct": 0, "dam": 10,"boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Mortality",   "damage": 280,  "number_o_t": 6, "add": 5, "add_attack": 4, "ct": 1, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Blade Fury",  "damage": 377,  "number_o_t": 5, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Fury Jet",    "damage": 387,  "number_o_t": 6, "add": 7, "add_attack": 1, "ct":5.6,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Sudden Raid", "damage": 672,  "number_o_t": 7, "add": 12,"add_attack": 1, "ct": 14,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_4": {"name": "Phantom Blow","damage": 13,   "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Mortality",   "damage": 110,  "number_o_t": 0, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "NightWalker": {
                         "mastery1_skill":  {"skill_1": {"name": "Quintuple "
                                                                 "Star",        "damage": 272,  "number_o_t": 4, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_2": {"name": "Quintuple "
                                              "Star [Jet Black Throwing Stars]","damage": 272,  "number_o_t": 4, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": True}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Shadow Bat",  "damage": 910,  "number_o_t": 1, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 50,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Ravenous Bat","damage": 748,  "number_o_t": 2, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability":100,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Dark Omen",   "damage": 414,  "number_o_t": 6, "add": 14,"add_attack":3.3,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Dark Omen"
                                                         "[active Shadow Bat]", "damage": 332,  "number_o_t": 2, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Dominion",    "damage": 1101, "number_o_t": 10,"add": 31,"add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 20,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_2": {"name": "Abyssal "
                                                                 "Darkness",    "damage": 195,  "number_o_t": 6, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Zenon": {
                         "mastery1_skill":  {"skill_1": {"name": "Mecha Purge: "
                                                                 "Snipe",       "damage": 394,  "number_o_t": 7, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 40,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Mecha Purge: "
                                                                 "Execute",     "damage": 243,  "number_o_t": 7, "add": 3, "add_attack": 3, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Mecha Purge: "
                                                                 "Bombardment", "damage": 452,  "number_o_t": 5, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Mecha Purge: "
                                                                 "Fire",        "damage": 452,  "number_o_t": 7, "add": 7, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Hypogram "
                                                            "Field: Penetrate", "damage": 250,  "number_o_t": 2, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Hypogram "
                                                        "Field: Force Field",   "damage": 710,  "number_o_t": 2, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Hypogram "
                                                            "Field: Support",   "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_4": {"name": 
                                                            "Triangulation",    "damage": 265,  "number_o_t": 3, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Salvo System","damage": 307,  "number_o_t": 2, "add": 9, "add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Aegis System","damage": 324,  "number_o_t": 2, "add": 9, "add_attack": 7, "ct": 2, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Orbital "
                                                                 "Cataclysm",   "damage": 1411, "number_o_t": 7, "add": 40,"add_attack": 1, "ct": 50,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_4": {"name": "Mecha Purge: "
                                                                 "Snipe",       "damage": 17,   "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Mecha Purge: "
                                                                 "Execute",     "damage": 1,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Beam Dance",  "damage": 290,  "number_o_t": 1, "add": 6, "add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Memory Dance","damage": 123,  "number_o_t": 7, "add": 3, "add_attack": 6, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "PhantomThief": {
                         "mastery1_skill":  {"skill_1": {"name": "Tempest",     "damage": 502,  "number_o_t": 4, "add": 12,"add_attack": 6, "ct": 18,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 20,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Mille "
                                                                 "Aiguilles",   "damage": 311,  "number_o_t": 3, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Mille "
                                                        "Aiguilles: Fortune",   "damage": 409,  "number_o_t": 6, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Fate Shuffle","damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Carte Noir",  "damage": 282,  "number_o_t": 1, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability":100,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Swerve Card", "damage": 1006, "number_o_t": 1, "add": 16,"add_attack": 5, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Rose Carte "
                                                         "Finale",              "damage": 207,  "number_o_t": 6, "add": 7, "add_attack": 7, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "La Mort "
                                                                 "Carte",       "damage": 915,  "number_o_t": 0, "add": 15,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Carte Noir",  "damage": 1,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Cadena": {
                         "mastery1_skill":  {"skill_1": {"name": "Chain Arts: "
                                                                 "Thrash 1",    "damage": 155,  "number_o_t": 2, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Chain Arts: "
                                                                 "Thrash 2",    "damage": 415,  "number_o_t": 5, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Shockwave "
                                                                 "Damage",      "damage": 468,  "number_o_t": 10,"add": 18,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Muscle "
                                                                 "Memory",      "damage": 457,  "number_o_t": 4, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 11,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Summon "
                                                                 "Scimitar",    "damage": 530,  "number_o_t": 5, "add": 11,"add_attack": 1, "ct": 4, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Summon "
                                                                 "Claw",        "damage": 561,  "number_o_t": 4, "add": 11,"add_attack": 1, "ct": 3, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Summon "
                                                                 "Shuriken",    "damage": 530,  "number_o_t": 1, "add": 11,"add_attack": 2, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Summon Spiked"
                                                                 " Bat 1",      "damage": 365,  "number_o_t": 12,"add": 7, "add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Summon Spiked"
                                                                 " Bat 2",      "damage": 493,  "number_o_t": 13,"add": 10,"add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "Summon Spiked"
                                                                 " Bat 3",      "damage": 725,  "number_o_t": 14,"add": 15,"add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}                                        
                                            ,"skill_7": {"name": "Chain Arts: "
                                                                 "Crush",       "damage": 561,  "number_o_t": 15,"add": 14,"add_attack": 1, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Summon "
                                                                 "Shotgun 1",   "damage": 621,  "number_o_t": 7, "add": 11,"add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Summon "
                                                                 "Shotgun 2",   "damage": 547,  "number_o_t": 7, "add": 10,"add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Summon "
                                                                 "Shotgun 3",   "damage": 497,  "number_o_t": 7, "add": 9, "add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Summon "
                                                                 "Daggers",     "damage": 541,  "number_o_t": 8, "add": 9, "add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Summon Decoy "
                                                                 "Bomb",        "damage": 652,  "number_o_t": 6, "add": 12,"add_attack": 1, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "Summon Brick","damage": 596,  "number_o_t": 7, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_7": {"name": "Chain Arts: "
                                                                 "Beatdown",    "damage": 334,  "number_o_t": 2, "add": 6, "add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_8": {"name": "Chain Arts: "
                                                            "Beatdown Strike",  "damage": 1101, "number_o_t": 15,"add": 21,"add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 80,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_9": {"name": "Chain Arts: "
                                                  "Beatdown Strike Shockwave",  "damage": 667,  "number_o_t": 4, "add": 12,"add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 80,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_10":{"name": "Veteran "
                                                                 "Shadowdealer","damage": 280,  "number_o_t": 3, "add": 5, "add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Torakage": {
                         "mastery1_skill":  {"skill_1": {"name": "Heaven: "
                                                         "Consuming Flames",    "damage": 410,  "number_o_t": 6, "add": 5, "add_attack": 1, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Heaven: "
                                                "Consuming Flames [Enhanced]",  "damage": 607,  "number_o_t": 6, "add": 7, "add_attack": 1, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Consuming "
                                                         "Flames (Clone/True)", "damage": 410,  "number_o_t": 6, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Consuming "
                                            "Flames (Clone/True) [Enhanced]",   "damage": 607,  "number_o_t": 6, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Earth: Stone "
                                                                 "Tremor",      "damage": 476,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_6": {"name": "Earth: Stone "
                                                         "Tremor [Enhanced]",   "damage": 749,  "number_o_t": 6, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_7": {"name": "Stone Tremor "
                                                         "(Clone/True)",        "damage": 476,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_8": {"name": "Stone Tremor "
                                                     "(Clone/True) [Enhanced]", "damage": 820,  "number_o_t": 6, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_9": {"name": "Humanity: "
                                                         "Gold-Banded Cudgel",  "damage": 281,  "number_o_t": 10,"add": 6, "add_attack": 1, "ct": 11,"dam": 0, "boss_dam": 30,"fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_10":{"name": "Humanity: "
                                                "Gold-Banded Cudgel [Enhanced]","damage": 435,  "number_o_t": 10,"add": 10,"add_attack": 1, "ct": 11,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_11":{"name": "Universal "
                                                                 "Harmony",     "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 5, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Heaven: Iron "
                                                                 "Fan Gale",    "damage": 304,  "number_o_t": 5, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Heaven: Iron "
                                                        "Fan Gale [Enhanced]",  "damage": 465,  "number_o_t": 5, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Iron Fan "
                                                         "Gale (Clone/True)",   "damage": 304,  "number_o_t": 5, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Iron Fan "
                                                "Gale (Clone/True) [Enhanced]", "damage": 465,  "number_o_t": 5, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Earth: "
                                                    "Ground-Shattering Wave",   "damage": 460,  "number_o_t": 4, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Earth: "
                                            "Ground-Shattering Wave [Enhanced]","damage": 699,  "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": 
                                        "Ground-Shattering Wave (Clone/True)",  "damage": 460,  "number_o_t": 4, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": 
                            "Ground-Shattering Wave (Clone/True) [Enhanced]",   "damage": 699,  "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Humanity: "
                                                         "As-You-Will Fan",     "damage": 626,  "number_o_t": 5, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Humanity: "
                                                "As-You-Will Fan [Enhanced]",   "damage": 969,  "number_o_t": 5, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Talisman: "
                                                                 "Clone",       "damage": 270,  "number_o_t": 4, "add": 4,"add_attack":5.965,"ct":0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Talisman: "
                                                        "Seeking Ghost Flame",  "damage": 276,  "number_o_t": 10,"add": 6, "add_attack":0.55,"ct":0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Scroll: Star "
                                                                 "Vortex",      "damage": 320,  "number_o_t": 6, "add": 5, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Scroll: "
                                                         "Butterfly Dream",     "damage": 449,  "number_o_t": 5, "add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 10,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Kali": {
                         "mastery1_skill":  {"skill_1": {"name": "Arts: "
                                                                 "Flurry",      "damage": 324,  "number_o_t": 7, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Arts: "
                                                                 "Crescentum",  "damage": 540,  "number_o_t": 4, "add": 15,"add_attack": 5, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Void Rush",   "damage": 254,  "number_o_t": 4, "add": 4, "add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Void Blitz",  "damage": 190,  "number_o_t": 5, "add": 5, "add_attack": 4, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Hex: "
                                                                "Chakram Split","damage": 268,  "number_o_t": 5, "add": 8, "add_attack": 4, "ct": 14,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Hex: Chakram "
                                                                 "Sweep",       "damage": 775,  "number_o_t": 7, "add": 19,"add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Hex: Chakram "
                                                                 "Fury",        "damage": 612,  "number_o_t": 10,"add": 16,"add_attack": 1, "ct": 10,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Death "
                                                                 "Blossom",     "damage": 544,  "number_o_t": 6, "add": 14,"add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Resonate",    "damage": 303,  "number_o_t": 3, "add": 3, "add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Deceiving "
                                                                 "Blade",       "damage": 438,  "number_o_t": 2, "add": 8, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Viper": {
                         "mastery1_skill":  {"skill_1": {"name": "Octopunch",   "damage": 339,  "number_o_t": 10,"add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Super "
                                                                 "Octopunch",   "damage": 183,  "number_o_t": 3, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Sea Serpent", "damage": 483,  "number_o_t": 8, "add": 13,"add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"Sea Serpent's "
                                                                "Rage",         "damage": 444,  "number_o_t": 9, "add": 14,"add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 20,"def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Nautilus "
                                                                 "Strike",      "damage": 511,  "number_o_t": 7, "add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Final Attack","damage": 216,  "number_o_t": 2, "add": 11,"add_attack": 1, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability":100,"passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Serpent "
                                                                 "Scale",       "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Serpent "
                                                                 "Assault",     "damage": 473,  "number_o_t": 6, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Raging "
                                                         "Serpent Assault",     "damage": 476,  "number_o_t": 7, "add": 13,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Sea "
                                                         "Serpent's Rage",      "damage": 79,   "number_o_t": 0, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Hook Bomber", "damage": 627,  "number_o_t": 4, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Super "
                                                         "Octopunch ",          "damage": 17,   "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Super "
                                                         "Octopunch Shockwave", "damage": 12,   "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Octopunch",   "damage": 13,   "number_o_t": 0, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "Captain": {
                         "mastery1_skill":  {"skill_1": {"name": "Rapid Fire",  "damage": 436,  "number_o_t": 1, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Rapid Fire "
                                                         "[Shootout Mode]",     "damage": 210,  "number_o_t": 4, "add": 3, "add_attack":1.67,"ct":0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Majestic "
                                                                 "Presence",    "damage": 29,   "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Broadside",   "damage": 550,  "number_o_t": 3, "add": 10,"add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Firing "
                                                         "Orders is active",    "damage": 550,  "number_o_t": 3, "add": 10,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Brain "
                                                                 "Scrambler",   "damage": 1195, "number_o_t": 13,"add": 17,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 60,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Condemnation","damage": 860,  "number_o_t": 13,"add": 14,"add_attack": 2, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 60,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Eight-Legs "
                                                                 "Easton",      "damage": 732,  "number_o_t": 4, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Firing "
                                                                 "Orders",      "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Scurvy "
                                                                 "Summons",     "damage": 530,  "number_o_t": 3, "add": 15,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Siege "
                                                                 "Bomber",      "damage": 354,  "number_o_t": 2, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Ugly Bomb",   "damage": 455,  "number_o_t": 12,"add": 5, "add_attack": 1, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Nautilus "
                                                                 "Strike",      "damage": 633,  "number_o_t": 7, "add": 8, "add_attack": 1, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "CannonShooter": {
                         "mastery1_skill":  {"skill_1": {"name": "Cannon "
                                                                 "Barrage",     "damage": 863,  "number_o_t": 4, "add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 30,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Cannon "
                                                                 "Bazooka",     "damage": 608,  "number_o_t": 4, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Monkey "
                                                                 "Mortar",      "damage": 1129, "number_o_t": 5, "add": 19,"add_attack": 1, "ct": 4, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Anchors Away","damage": 587,  "number_o_t": 1, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Nautilus "
                                                                 "Strike",      "damage": 567,  "number_o_t": 7, "add": 5, "add_attack": 1, "ct": 30,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Rolling "
                                                                 "Rainbow",     "damage": 698,  "number_o_t": 5, "add": 38,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Max Cannon "
                                                                 "Rainbow",     "damage": 724,  "number_o_t": 5, "add": 44,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Cannon "
                                                                 "Barrage",     "damage": 4,    "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Monkey "
                                                                 "Militia",     "damage": 365,  "number_o_t": 1, "add": 25,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Monkey Fury", "damage": 198,  "number_o_t": 3, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Monkey Fury"
                                                                 "[dot]",       "damage": 220,  "number_o_t": 1, "add": 4, "add_attack": 1, "ct": 0, "dam":1622.5,"boss_dam":0,"fainal_dam":0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "explodes",    "damage": 198,  "number_o_t": 3, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Striker": {
                         "mastery1_skill":  {"skill_1": {"name": "Annihilate",  "damage": 354,  "number_o_t": 7, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Thunder "
                                                                 "Bolt",        "damage": 206,  "number_o_t": 3, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "massive "
                                                        "thunderbolt",          "damage": 166,  "number_o_t": 5, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 40,"fainal_dam": 0, "def_a": 20,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Thunderbolt", "damage": 341,  "number_o_t": 5, "add": 0, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Thunder "
                                                         "Slash",               "damage": 371,  "number_o_t": 5, "add": 6, "add_attack": 1, "ct": 6, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Lightning "
                                                "Strike's Massive Thunderbolt", "damage": 99,   "number_o_t": 0, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Typhoon",     "damage": 396,  "number_o_t": 5, "add": 15,"add_attack": 1, "ct": 12,"dam":262,"boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Deep Rising", "damage": 945,  "number_o_t": 7, "add": 15,"add_attack": 1, "ct": 45,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Sea Wave",    "damage": 430,  "number_o_t": 5, "add": 20,"add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Deep "
                                                         "Reinforcement",       "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": True,  "add_effect": False}
                                            ,"skill_3": {"name": "Annihilate",  "damage": 18,   "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Mechanic": {
                         "mastery1_skill":  {"skill_1": {"name": "Heavy Salvo "
                                                                 "Plus",        "damage": 426,  "number_o_t": 4, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name":"AP Salvo Plus","damage": 338,  "number_o_t": 6, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name":"Homing Beacon","damage": 405,  "number_o_t": 1, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Distortion "
                                                                 "Bomb",        "damage": 459,  "number_o_t": 2, "add": 9, "add_attack": 2, "ct": 8, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Intense "
                                                         "Distortion Bomb",     "damage": 805,  "number_o_t": 3, "add": 15,"add_attack": 1, "ct": 25,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Robo "
                                                                 "Launcher RM7","damage": 402,  "number_o_t": 1, "add": 7, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Rock 'n "
                                                                 "Shock",       "damage": 718,  "number_o_t": 1, "add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Bots 'n Tots","damage": 535,  "number_o_t": 3, "add": 10,"add_attack": 1, "ct": 3, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Robo "
                                                            "Conversion: CB-P1","damage": 824,  "number_o_t": 8, "add": 14,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": True,  "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "AP Salvo "
                                                                 "Plus's 2nd",  "damage": 102,  "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        },
                    "HiddenMoon": {
                         "mastery1_skill":  {"skill_1": {"name": "Spirit Claw", "damage": 301,  "number_o_t": 12,"add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Fox Spirints","damage": 265,  "number_o_t": 2, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Spirit CLow", "damage": 11,   "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Fox Marble "
                                                                 "Fusion",      "damage": 41,   "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Dragonvein "
                                                                 "Fist",        "damage": 256,  "number_o_t": 12,"add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Death Mark",  "damage": 677,  "number_o_t": 8, "add": 19,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Dusk Blow",   "damage": 1516, "number_o_t": 20,"add": 31,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Soul "
                                                                 "Splitter",    "damage": 314,  "number_o_t": 0, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Spirit "
                                                         "Frenzy",              "damage": 412,  "number_o_t": 8, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Spirit "
                                                                 "Incarnation", "damage": 61,   "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Spirit Clow", "damage": 17,   "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "AngelicBuster": {
                         "mastery1_skill":  {"skill_1": {"name": "Trinity",     "damage": 612,  "number_o_t": 7, "add": 12,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 15,"is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Soul Seeker", "damage": 345,  "number_o_t": 7, "add": 3, "add_attack":1.7,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Soul Seeker "
                                                                 "Expert",      "damage": 241.5,"number_o_t": 7, "add":2.25,"add_attack":1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Trinity",     "damage": 18,   "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Superme "
                                                                 "Supernova",   "damage": 360,  "number_o_t": 4, "add": 26,"add_attack": 18,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Trinity",     "damage": 24,   "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Celestial "
                                                                 "Roar",        "damage": 645,  "number_o_t": 4, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Encore "
                                                                 "Ribbon",      "damage": 209,  "number_o_t": 4, "add": 19,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 80,"passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
                    "Arc": {
                         "mastery1_skill":  {"skill_1": {"name": "Basic Charge "
                                                                 "Drive",       "damage": 799,  "number_o_t": 3, "add": 14,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Scarlet Charge "
                                                                 "Drive",       "damage": 494,  "number_o_t": 3, "add": 9, "add_attack": 1, "ct": 3, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Gust Charge "
                                                                 "Drive",       "damage": 556,  "number_o_t": 6, "add": 11,"add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Abyssal Charge "
                                                                 "Drive",       "damage": 481,  "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Awakened "
                                                                 "Abyss",       "damage": 996,  "number_o_t": 3, "add": 16,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "Grievous "
                                                                 "Wound",       "damage": 847,  "number_o_t": 6, "add": 17,"add_attack": 1, "ct": 3, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Insatiable "
                                                                 "Hunger",      "damage": 860,  "number_o_t": 7, "add": 16,"add_attack": 1, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Unbridled "
                                                                 "Chaos",       "damage": 779,  "number_o_t": 12,"add": 14,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "Vengeful "
                                                                 "Hate",        "damage": 163,  "number_o_t": 0, "add": 13,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_5": {"name": "Unstoppable "
                                             "Impulse, Tenacious Instinct",     "damage": 171,  "number_o_t": 0, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "Vengeful "
                                                                 "Hate",        "damage": 732,  "number_o_t": 8, "add": 7, "add_attack": 1, "ct": 12,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Blissful "
                                                                 "Restraint",   "damage": 736,  "number_o_t": 6, "add": 16,"add_attack": 1, "ct":120,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Endless "
                                                                 "Agony",       "damage": 402,  "number_o_t": 3, "add": 6, "add_attack": 6, "ct": 60,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "Ominous "
                                                                 "Nightmare",   "damage": 607,  "number_o_t": 7, "add": 12,"add_attack": 1, "ct": 2, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "Ominous "
                                                                 "Dream",       "damage": 623,  "number_o_t": 7, "add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "Impending "
                                                                 "Death",       "damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": True,  "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },

                    "job": {
                         "mastery1_skill":  {"skill_1": {"name": "mastery1",    "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"name": "mastery2",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"name": "mastery3",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"name": "mastery4",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_2": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_3": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            ,"skill_4": {"name": "",            "damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "f_Probability": 0, "passive": False, "buf": False, "add_effect": False}
                                            }
                        },
        }

        #持続 1秒あたり2回で1秒のダメージで表記






        self.HEXA_mastery_add = {
                 "Hero": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill": {"Puncture": {"damage": 292,  "number_o_t": 4, "add": 3, "add_attack": 30,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Aran": {
                         "mastery1_skill":   {"Beyond "
                                               "Blade": {"damage": 456,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 4, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Kaiser": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"Tempest "
                                              "Blades": {"damage": 2640, "number_o_t": 10,"add": 40,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Tempest "
                                  "Blades[Final Form]": {"damage": 2640, "number_o_t": 10,"add": 40,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Hayato": {
                         "mastery1_skill":  {"[Shinsoku] "
                                    "Afterimage Slash": {"damage": 618,  "number_o_t": 12,"add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                    },
                    "Zero": {
                         "mastery1_skill":   {"Falling "
                                                "Star": {"damage": 204,  "number_o_t": 3, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                      ,"Groundbreaker": {"damage": 260,  "number_o_t": 10,"add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                    ,"Groundbreaker_2": {"damage": 340,  "number_o_t": 1, "add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                        ,"Wind Cutter": {"damage": 117,  "number_o_t": 2, "add": 2, "add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                       ,"Storm Break" : {"damage": 330,  "number_o_t": 4, "add": 5, "add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                     ,"Storm Break_2" : {"damage": 214,  "number_o_t": 1, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                           }
                        ,"mastery2_skill":  {"Rolling "
                                               "Cross": {"damage": 462,  "number_o_t": 3, "add": 12,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Rolling "
                                             "Assault": {"damage": 458,  "number_o_t": 4, "add": 18,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {
                                          "Blade Ring": {"damage": 123,  "number_o_t": 4, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"Air Raid":{"damage": 345,  "number_o_t": 9, "add": 3, "add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                      ,"Shadow Strike": {"damage": 340,  "number_o_t": 1, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Blaster": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"Bunker Buster "
                                         "Explosion"  : {"damage": 440,  "number_o_t": 4, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Adel": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Aether "
                                               "Bloom": {"damage": 723,  "number_o_t": 8, "add": 13,"add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-25,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "FlameWizard": {
                         "mastery1_skill":  {"Orbital Flame "
                                 "[Normal, Flame Fox]": {"damage": 446,  "number_o_t": 4, "add": 6, "add_attack": 9, "ct": 15,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Phoenix Drive [Blazing Lion]": {"damage": 529,  "number_o_t": 2, "add": 29,"add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-50,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Phoenix Drive [Flame Fox]": {"damage": 756,  "number_o_t": 2, "add": 16,"add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-50,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "BattleMage": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"Sweeping "
                                             "Staff"  : {"damage": 323,  "number_o_t": 5, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "IceLightning": {
                         "mastery1_skill":{  "skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Lightning Orb"
                                                      : {"damage": 269,  "number_o_t": 15,"add": 5, "add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "FirePoison": {
                         "mastery1_skill":{  "Flame Sweep"
                                                      : {"damage": 261,  "number_o_t": 1, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"Flame Haze"
                                                      : {"damage": 540,  "number_o_t": 1, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Ifrit"  : {"damage": 157,  "number_o_t": 15,"add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                       ,"Inferno Aura": {"damage": 500,  "number_o_t": 1, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"Creeping "
                                               "Toxin": {"damage": 224,  "number_o_t": 4, "add": 4, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                      ,"Megiddo Flame": {"damage": 341,  "number_o_t": 5, "add": 11,"add_attack": 10,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-55,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                    ,"Megiddo Flame_2": {"damage": 777,  "number_o_t": 1, "add": 7, "add_attack": 1, "ct": 20,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Evan": {
                         "mastery1_skill":{"Mana Burst": {"damage": 364,  "number_o_t": 4, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Illium": {
                         "mastery1_skill":   {"Radiant "
                                             "Javelin": {"damage": 142,  "number_o_t": 2, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                     ,"Winged Javelin": {"damage": 259,  "number_o_t": 3, "add": 4, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Crystal Skill "
                                              "- Deus": {"damage": 104,  "number_o_t": 40,"add": 6, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Lara": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {
                                            "Eruption: Sunrise Well": 
                                                        {"damage": 455,  "number_o_t": 1, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Eruption: Sunrise Well[Volcanic Bomb]": 
                                                        {"damage": 472,  "number_o_t": 3, "add": 7, "add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-10,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Absorption: "
                                        "Sunlit Grain": {"damage": 293,  "number_o_t": 6, "add": 3, "add_attack": 4, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-40,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"Wakeup Call": 
                                                        {"damage": 715,  "number_o_t": 4, "add": 15,"add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-40,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Crossbowmaster": {
                         "mastery1_skill":{
                                     "Empowered Snipe": {"damage": 323,  "number_o_t": 5, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                     ,"Ultimate Snipe": {"damage": 323,  "number_o_t": 5, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {
                             "Ultimate Piercing Arrow": {"damage": 324,  "number_o_t": 10,"add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                  ,"Empowered Piercing Arrow[passive]": {"damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": True,  "buf": False}
                   ,"Ultimate Piercing Arrow[passive]": {"damage": 2,    "number_o_t": 0, "add": 2, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": True,  "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  { 
                   "Empowered Piercing Arrow[passive]": {"damage": 4,    "number_o_t": 0, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": True,  "buf": False}
                   ,"Ultimate Piercing Arrow[passive]": {"damage": 3,    "number_o_t": 0, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": True,  "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {                   
                   "Empowered Piercing Arrow[passive]": {"damage": 1,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": True,  "buf": False}
                   ,"Ultimate Piercing Arrow[passive]": {"damage": 1,    "number_o_t": 0, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": True,  "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Pathfinder": {
                         "mastery1_skill":  {"Bountiful "
                                               "Burst": {"damage": 243,  "number_o_t": 3, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-30,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"Bountiful "
                                              "Deluge": {"damage": 188,  "number_o_t": 3, "add": 3, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-30,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Ancient Astra"
                                           " (Deluge)": {"damage": 273,  "number_o_t": 2, "add": 3, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 30,"passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {
                                       "Combo Assault": {"damage": 637,  "number_o_t": 5, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                             ,"Combo Assault (Deluge)": {"damage": 729,  "number_o_t": 5, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                              ,"Combo Assault (Burst)": {"damage": 728,  "number_o_t": 7, "add": 32,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                            ,"Combo Assault (Torrent)": {"damage": 729,  "number_o_t": 5, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Windshooter": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Monsoon": {"damage": 220,  "number_o_t": 1, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"Anemoi":  {"damage": 980,  "number_o_t": 10,"add": 31,"add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "WildHunter": {
                         "mastery1_skill":   {"Wild Arrow "
                                     "Blast [Mounted]": {"damage": 241,  "number_o_t": 10,"add": 6, "add_attack": 1, "ct":1.2,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Mercedes": {
                         "mastery1_skill":   {"Ishtar's "
                                                "Mark": {"damage": 457,  "number_o_t": 8, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"Ishtar's "
                                                "Mark": {"damage": 46,   "number_o_t": 0, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": True, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Cain": {
                         "mastery1_skill":   {"[Possess] "
                                        "Falling Dust": {"damage": 407,  "number_o_t": 15,"add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                      ,"Poison Needle": {"damage": 289,  "number_o_t": 8, "add": 9, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"Strike "
                                               "Arrow": {"damage": 367,  "number_o_t": 5, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                             ,"[Execute] Chain Sickle": {"damage": 291,  "number_o_t": 14,"add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"[Execute] "
                   "Poison Needle[consecutive attack]": {"damage": 257,  "number_o_t": 10,"add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {
                                         "Shaft Break": {"damage": 240,  "number_o_t": 10,"add": 5, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                              ,"(Possess) Shaft Break": {"damage": 522,  "number_o_t": 10,"add": 12,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                   ,"(Possess) Shaft Break[whirlwind]": {"damage": 93,   "number_o_t": 3, "add": 2, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Shadow": {
                         "mastery1_skill":   {
                                         "Assassinate": {"damage": 516,  "number_o_t": 6, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 50,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                          ,"Pulverize": {"damage": 603,  "number_o_t": 6, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 50,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Showdown"
                                         "[Shurikens]": {"damage": 28,   "number_o_t": 6, "add": 1, "add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":-50,"def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {
                                         "Sudden Raid": {"damage": 216,  "number_o_t": 1, "add": 1, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "KnightLord": {
                         "mastery1_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"Showdown":{"damage": 28,   "number_o_t": 6, "add": 1, "add_attack": 6, "ct": 5, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {
                                         "Sudden Raid": {"damage": 239,  "number_o_t": 1, "add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                      ,"Death Star: Rampant[enhances]": {"damage": 303,  "number_o_t": 7, "add": 14,"add_attack": 6, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "DualBlade": {
                         "mastery1_skill":   {
                                             "skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"Sudden Raid"
                                                      : {"damage": 387,  "number_o_t": 1, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "NightWalker": {
                         "mastery1_skill":   {"Quintuple "
                                                "Star": {"damage": 1088, "number_o_t": 1, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Quintuple "
                     "Star [Jet Black Throwing Stars]": {"damage": 213,  "number_o_t": 7, "add": 3, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Zenon": {
                         "mastery1_skill":   {
                                       "Triangulation": {"damage": 133,  "number_o_t": 4, "add": 3, "add_attack": 4, "ct":1.5,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "PhantomThief": {
                         "mastery1_skill":   {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"Rose Carte "
                                              "Finale": {"damage": 228,  "number_o_t": 2, "add": 8, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                         ,"Carte Noir": {"damage": 15,   "number_o_t": 0, "add": 15,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Cadena": {
                         "mastery1_skill":   {"Summon "
                                            "Shuriken": {"damage": 800,  "number_o_t": 3, "add": 17,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"Chain Arts: "
                                     "Beatdown Strike": {"damage": 550,  "number_o_t": 10,"add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Torakage": {
                         "mastery1_skill":   {"Heaven: "
                         "Consuming Flames [Enhanced]": {"damage": 511,  "number_o_t": 5, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                        ,"Earth: Stone "
                                   "Tremor [Enhanced]": {"damage": 527,  "number_o_t": 5, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                 ,"Humanity: "
                                  "Gold-Banded Cudgel": {"damage": 511,  "number_o_t": 8, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                      ,"Humanity: "
                       "Gold-Banded Cudgel [Enhanced]": {"damage": 798,  "number_o_t": 8, "add": 18,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 30,"fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
              ,"Humanity: "
               "Gold-Banded Cudgel [Enhanced][energy]": {"damage": 506,  "number_o_t": 8, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 30,"fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Viper": {
                         "mastery1_skill":   {"Super "
                                           "Octopunch": {"damage": 339,  "number_o_t": 10,"add": 4, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Captain": {
                         "mastery1_skill":   {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"Scurvy "
                                             "Summons": {"damage": 265,  "number_o_t": 4, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "CannonShooter": {
                         "mastery1_skill":   {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {
                                        "Anchors Away": {"damage": 810,  "number_o_t": 1, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Mechanic": {
                         "mastery1_skill":   {
                                       "AP Salvo Plus": {"damage": 187,  "number_o_t": 3, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Intense "
                                     "Distortion Bomb": {"damage": 1323, "number_o_t": 15,"add": 23,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "HiddenMoon": {
                         "mastery1_skill":   {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {
                                          "Death Mark": {"damage": 281,  "number_o_t": 1, "add": 7, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                          ,"Dusk Blow": {"damage": 373,  "number_o_t": 11,"add": 8, "add_attack": 8, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
                    "Arc": {
                         "mastery1_skill":   {"Basic Charge "
                                               "Drive": {"damage": 515,  "number_o_t": 2, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Scarlet Charge "
                                               "Drive": {"damage": 301,  "number_o_t": 5, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Gust Charge "
                                               "Drive": {"damage": 321,  "number_o_t": 4, "add": 6, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Abyssal Charge "
                                               "Drive": {"damage": 572,  "number_o_t": 6, "add": 11,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Abyssal Charge "
                                         "Drive[cast]": {"damage": 93,   "number_o_t": 2, "add": 2, "add_attack": 2, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"Blissful "
                                           "Restraint": {"damage": 610,  "number_o_t": 3, "add": 10,"add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Blissful "
                               "Restraint[Explosions]": {"damage": 259,  "number_o_t": 7, "add": 4, "add_attack": 8, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"Endless "
                                               "Agony": {"damage": 249,  "number_o_t": 10,"add": 3, "add_attack": 12,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },


                    "job": {
                         "mastery1_skill":   {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery2_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }

                        ,"mastery3_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        ,"mastery4_skill":  {"skill_1": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_2": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_3": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            ,"skill_4": {"damage": 0,    "number_o_t": 0, "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False, "Probability": 0, "passive": False, "buf": False}
                                            }
                        },
        }


        self.HEXA_skill_enhance = {
                 "Hero": {
                         "enhance1_skill":  {"skill_1": {"name": "Burning Soul Blade" }}
                        ,"enhance2_skill":  {"skill_1": {"name": "Instinctual Combo"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Worldreaver"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Sword Illusion"}}
                        },
                 "Paladin": {
                         "enhance1_skill":  {"skill_1": {"name": "Divine Echo"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Hammers of the Righteous"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Grand Guardian"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Mighty Mjolnir"}}
                        },
                 "DarkNight": {
                         "enhance1_skill":  {"skill_1": {"name": "Spear of Darkness"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Radiant Evil"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Calamitous Cyclone"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Darkness Aura"}}
                        },
                 "SoulMaster": {
                         "enhance1_skill":  {"skill_1": {"name": "Cosmos"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Rift of Damnation"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Soul Eclipse"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Flare Slash"}}
                        },
                 "Aran": {
                         "enhance1_skill":  {"skill_1": {"name": "Finisher - Adrenaline Surge"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Maha's Carnage"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Final Beyond Blade - White Tiger"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Blizzard Tempest"}}
                        },
                 "DemonSlayer": {
                         "enhance1_skill":  {"skill_1": {"name": "Demon Awakening"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Spirit of Rage"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Orthrus"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Demon Bane"}}
                        },
                 "DemonAvenger": {
                         "enhance1_skill":  {"skill_1": {"name": "Demonic Frenzy"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Demonic Blast"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Dimensional Sword"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Revenant"}}
                        },
                 "Kaiser": {
                         "enhance1_skill":  {"skill_1": {"name": "Nova Guardians"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Bladefall"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Draco Surge"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Dragonflare"}}
                        },
                 "Hayato": {
                         "enhance1_skill":  {"skill_1": {"name": "Shogetsu Form"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "[Shinsoku] Crashing Tide"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "[Shinsoku] Light Cutter"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "[Battou] Wailing Heavens"}}
                        },
                 "Zero": {
                         "enhance1_skill":  {"skill_1": {"name": "Chrono Break"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Twin Blades of Time"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Shadow Flash"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Ego Weapon"}}
                        },
                 "Michael": {
                         "enhance1_skill":  {"skill_1": {"name": "Shield of Light"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Sword of Light"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Radiant Soul"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Light of Courage"}}
                        },
                 "Blaster": {
                         "enhance1_skill":  {"skill_1": {"name": "Rocket Punch"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Gatling Punch"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Bullet Blast"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Afterimage Shock"}}
                        },
                 "Adel": {
                         "enhance1_skill":  {"skill_1": {"name": "Ruin"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Infinity Blade"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Legacy Restoration"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Storm"}}
                        },
                 "IceLightning": {
                         "enhance1_skill":  {"skill_1": {"name": "Ice Age"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Bolt Barrage"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Spirit of Snow"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Jupiter Thunder"}}
                        },
                 "FirePoison": {
                         "enhance1_skill":  {"skill_1": {"name": "DoT Punisher"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Poison Nova"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Elemental Fury"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Poison Chain"}}
                        },
                 "Bishop": {
                         "enhance1_skill":  {"skill_1": {"name": "Benediction"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Angel of Balance"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Peacemaker"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Divine Punishment"}}
                        },
                "FlameWizard": {
                         "enhance1_skill":  {"skill_1": {"name": "Orbital Inferno"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Savage Flame"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Inferno Sphere"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Salamander Mischief"}}
                        },
                 "Battle Mage": {
                         "enhance1_skill":  {"skill_1": {"name": "Aura Scythe"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Altar of Annihilation"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Grim Harvest"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Abyssal Lightning"}}
                        },
                 "Evan": {
                         "enhance1_skill":  {"skill_1": {"name": "Elemental Barrag"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Dragon Slam"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Elemental Radiance"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Spiral of Mana"}}
                        },
                 "Luminous": {
                         "enhance1_skill":  {"skill_1": {"name": "Gate of Light"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Aether Conduit"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Baptism of Light and Darkness"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Liberation Orb"}}
                        },
                 "Kanna": {
                         "enhance1_skill":  {"skill_1": {"name": "Hakumenkonmou Juubi"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Unleash the Radiant Flame"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Unleash Black-Winged Destruction"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Unleash Soul-Searing Venom'"}}
                        },
                 "Kinesis": {
                         "enhance1_skill":  {"skill_1": {"name": "Psychic Tornado"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Ultimate - Mind Over Matter"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Ultimate - Psychic Shockwave"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Law of Gravity"}}
                        },
                 "Illium": {
                         "enhance1_skill":  {"skill_1": {"name": "Crystal Ignition"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Templar Knight"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Crystalline Spirit"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Crystal Gate"}}
                        },
                 "Lara": {
                         "enhance1_skill":  {"skill_1": {"name": "Big Stretch"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Land's Connection"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Surging Essence"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Winding Mountain Ridge"}}
                        },
                 "Lynn": {
                         "enhance1_skill":  {"skill_1": {"name": "Beast's Rage"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Beak Strike"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "[Focus] Awaken Boost"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Nature's Grace"}}
                        },
                 "Bowmaster": {
                         "enhance1_skill":  {"skill_1": {"name": "Storm of Arrows"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Inhuman Speed"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Quiver Barrage"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Silhouette Mirage"}}
                        },
                 "Crossbowmaster": {
                         "enhance1_skill":  {"skill_1": {"name": "Perfect Shot"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Split Shot"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Surge Bolt"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Repeating Crossbow Cartridge"}}
                        },
                 "Pathfinder": {
                         "enhance1_skill":  {"skill_1": {"name": "Nova Blast"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Raven Tempest/Fury of the Wild Tempest"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Obsidian Barrier"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Relic Unbound"}}
                        },
                 "Windshooter": {
                         "enhance1_skill":  {"skill_1": {"name": "Howling Gale"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Merciless Winds"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Gale Barrier"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Vortex Sphere"}}
                        },
                "WildHunter": {
                         "enhance1_skill":  {"skill_1": {"name": "Jaguar Storm"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Primal Fury"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Primal Grenade"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Wild Arrow Blast Type X"}}
                        },
                 "Mercedes": {
                         "enhance1_skill":  {"skill_1": {"name": "Spirit of Elluel"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Sylvidia's Flight"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Irkalla's Wrath"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Royal Knights"}}
                        },
                 "Cain": {
                         "enhance1_skill":  {"skill_1": {"name": "Dragon Burst"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Fatal Blitz"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Thanatos Descent"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Grip of Agony"}}
                        },
                 "Shadow": {
                         "enhance1_skill":  {"skill_1": {"name": "Shadow Assault"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Trickblade"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Sonic Blow"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Slash Shadow Formation"}}
                        },
                 "KnightLord": {
                         "enhance1_skill":  {"skill_1": {"name": "Throwing Star Barrage"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Shurrikane"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Dark Lord's Omen"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Throw Blasting"}}
                        },
                 "DualBlade": {
                         "enhance1_skill":  {"skill_1": {"name": "Blade Storm"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Blades of Destiny"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Blade Tornado"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Haunted Edge"}}
                        },
                 "NightWalker": {
                         "enhance1_skill":  {"skill_1": {"name": "Shadow Spear"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Greater Dark Servant"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Shadow Bite"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Rapid Throw"}}
                        },
                 "Zenon": {
                         "enhance1_skill":  {"skill_1": {"name": "Omega Blaster"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Core Overload"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Hypogram Field: Fusion"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Photon Ray"}}
                        },
                 "PhantomThief": {
                         "enhance1_skill":  {"skill_1": {"name": "Luck of the Draw"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Ace in the Hole"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Phantom's Mark"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Rift Break"}}
                        },
                 "Cadena": {
                         "enhance1_skill":  {"skill_1": {"name": "Chain Arts: Void Strike"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Apocalypse Cannon"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Chain Arts: Maelstrom"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Muscle Memory Finale"}}
                        },
                 "Torakage": {
                         "enhance1_skill":  {"skill_1": {"name": "Sage: Clone Rampage"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Scroll: Tiger of Songyu"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Sage: Wrath of Gods"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Sage: Three Paths Apparition"}}
                        },
                 "Kali": {
                         "enhance1_skill":  {"skill_1": {"name": "Hex: Pandemonium"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Void Burst"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Arts: Astra"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Resonate: Ultimatum"}}
                        },
                 "Viper": {
                         "enhance1_skill":  {"skill_1": {"name": "Lightning Form"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Lord of the Deep"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Serpent Vortex"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Howling Fist"}}
                        },
                 "Captain": {
                         "enhance1_skill":  {"skill_1": {"name": "Bullet Barrage"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Target Lock"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Nautilus Assault"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Death Trigger"}}
                        },
                 "CannonShooter": {
                         "enhance1_skill":  {"skill_1": {"name": "Cannon of Mass Destruction"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "The Nuclear Option"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Monkey Business"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Poolmaker"}}
                        },
                 "Striker": {
                         "enhance1_skill":  {"skill_1": {"name": "Lightning Cascade"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Shark Torpedo"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Lightning God Spear Strike"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Lightning Spear Multistrike"}}
                        },
                 "Mechanic": {
                         "enhance1_skill":  {"skill_1": {"name": "Doomsday Device"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Mobile Missile Battery"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Full Metal Barrage"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Mecha Carrier"}}
                        },
                 "HiddenMoon": {
                         "enhance1_skill":  {"skill_1": {"name": "Fox God Flash"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Spiritgate"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "True Spirit Claw"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Smashing Multipunch"}}
                        },
                 "AngelicBuster": {
                         "enhance1_skill":  {"skill_1": {"name": "Sparkle Burst"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Superstar Spotlight"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Mighty Mascot"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Trinity Fusion"}}
                        },
                 "Arc": {
                         "enhance1_skill":  {"skill_1": {"name": "Abyssal Recall"}}
                        ,"enhance2_skill":  {"skill_1": {"name": "Infinity Spell"}}
                        ,"enhance3_skill":  {"skill_1": {"name": "Devious Nightmare/Devious Dream"}}
                        ,"enhance4_skill":  {"skill_1": {"name": "Endlessly Starving Beast"}}
                        },
                 
                 "job": {
                         "enhance1_skill":  {"skill_1": {"name": ""}}
                        ,"enhance2_skill":  {"skill_1": {"name": ""}}
                        ,"enhance3_skill":  {"skill_1": {"name": ""}}
                        ,"enhance4_skill":  {"skill_1": {"name": ""}}
                        },
        }

        #FAINAL ATACK 確率xダメージ
        job = [
                "Kali",           "Viper",          "Captain",        "CannonShooter",  "Striker",
                "Mechanic",       "HiddenMoon",     "AngelicBuster",  "Arc",            "Ren"
        ]


        self.HEXA_skill_origin = {
                "Hero": {
                         "origin_skill":    {"skill_1": {"name":"Spirit Calibur","damage": 240,  "number_o_t": 14,"add": 8, "add_attack": 33,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 238,  "number_o_t": 15,"add": 8, "add_attack": 48,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },
                "Paladin": {
                         "origin_skill":    {"skill_1": {"name":"Sacred Bastion","damage": 410,  "number_o_t": 9, "add": 13, "add_attack": 28,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 460,  "number_o_t": 14,"add": 15, "add_attack": 17,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },
                "DarkNight": {
                         "origin_skill":    {"skill_1": {"name":"Dead Space",    "damage": 620,  "number_o_t": 6, "add": 20, "add_attack": 6, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 542,  "number_o_t": 14,"add": 17, "add_attack": 58,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },
                "SoulMaster": {
                         "origin_skill":    {"skill_1": {"name":"Astral Blitz",  "damage": 1085, "number_o_t": 48,"add": 35, "add_attack": 5, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 1076, "number_o_t": 24,"add": 34, "add_attack": 7, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 10,"def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Aran": {
                         "origin_skill":    {"skill_1": {"name":"Endgame",       "damage": 775,  "number_o_t": 14,"add": 25, "add_attack": 50,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 837,  "number_o_t": 15,"add": 27, "add_attack": 30,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "DemonSlayer": {
                         "origin_skill":    {"skill_1": {"name":"Nightmare",     "damage": 1550, "number_o_t": 4, "add": 50, "add_attack": 6, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 919,  "number_o_t": 7, "add": 29, "add_attack": 46,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 50,"def_a": 0, "is_skill": False}                                            
                                            ,"skill_2": {"name":"Nightmare",     "damage": 1156, "number_o_t": 7, "add": 50, "add_attack": 66,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "DemonAvenger": {
                         "origin_skill":    {"skill_1": {"name":"Requiem",       "damage": 620,  "number_o_t": 10,"add": 20, "add_attack": 50,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 646,  "number_o_t": 14,"add": 21, "add_attack": 46,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Requiem",       "damage": 1168, "number_o_t": 12,"add": 30, "add_attack": 66,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Kaiser": {
                         "origin_skill":    {"skill_1": {"name":"Nova Triumphant","damage":1226, "number_o_t": 8, "add": 39, "add_attack": 14,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 981,  "number_o_t": 13,"add": 32, "add_attack": 47,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Hayato": {
                         "origin_skill":    {"skill_1": {"name":"Jin Quick Draw","damage": 430,  "number_o_t": 15,"add": 10, "add_attack": 15,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 10,"def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 359,  "number_o_t":120,"add": 0,  "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 10,"def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Jin Quick Draw","damage": 481,  "number_o_t": 15,"add": 11, "add_attack": 60,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Zero": {
                         "origin_skill":    {"skill_1": {"name":"End Time",      "damage": 733,  "number_o_t": 6, "add": 23, "add_attack": 17,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 733,  "number_o_t": 8, "add": 23, "add_attack": 22,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"End Time",      "damage": 734,  "number_o_t": 14,"add": 24, "add_attack": 32,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Michael": {
                         "origin_skill":    {"skill_1": {"name":"Durendal",      "damage": 775,  "number_o_t": 7, "add": 25, "add_attack": 6, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 712,  "number_o_t": 6, "add": 22, "add_attack": 30,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Durendal",      "damage": 708,  "number_o_t": 14,"add": 23, "add_attack": 24,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Blaster": {
                         "origin_skill":   {"skill_1": {"name":"Final Destroyer","damage": 775,  "number_o_t": 10,"add": 25, "add_attack": 43,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 796,  "number_o_t": 14,"add": 26, "add_attack": 30,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Adel": {
                         "origin_skill":    {"skill_1": {"name":"Maestro",       "damage": 703,  "number_o_t": 10,"add": 23, "add_attack": 29,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 703,  "number_o_t": 57,"add": 23, "add_attack": 14,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "IceLightning": {
                         "origin_skill":  {"skill_1": {"name":"Frozen Lightning","damage": 409,  "number_o_t": 7, "add": 14, "add_attack": 32,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 412,  "number_o_t": 12,"add": 14, "add_attack": 24,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                          ,"skill_2": {"name":"Frozen Lightning","damage": 868,  "number_o_t": 15,"add": 28, "add_attack": 15,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "FirePoison": {
                         "origin_skill":    {"skill_1": {"name":"Infernal Venom","damage": 279,  "number_o_t": 12,"add": 9,  "add_attack":680,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 269,  "number_o_t": 15,"add": 9,  "add_attack": 42,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Bishop": {
                         "origin_skill":    {"skill_1": {"name":"Holy Advent",   "damage": 280,  "number_o_t": 8, "add": 10, "add_attack": 25,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 243,  "number_o_t": 12,"add": 8,  "add_attack": 35,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "FlameWizard": {
                         "origin_skill":    {"skill_1": {"name":"Eternity",      "damage": 1085, "number_o_t": 10,"add": 35, "add_attack": 38,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 1902, "number_o_t": 13,"add": 62, "add_attack": 60,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "BattleMage": {
                         "origin_skill":    {"skill_1": {"name":"Crimson Pact",  "damage": 931,  "number_o_t": 11,"add": 29, "add_attack": 48,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 1471, "number_o_t": 14,"add": 48, "add_attack": 22,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Evan": {
                         "origin_skill":    {"skill_1": {"name":"Zodiac Burst",  "damage": 598,  "number_o_t": 15,"add": 18, "add_attack": 24,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 558,  "number_o_t": 27,"add": 18, "add_attack": 15,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Luminous": {
                         "origin_skill":    {"skill_1":{"name":"Harmonic Paradox","damage":1550, "number_o_t": 7, "add": 50, "add_attack": 7, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 784,  "number_o_t": 7 ,"add": 26, "add_attack": 39,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Kanna": {
                         "origin_skill":    {"skill_1": {"name":"Hakumenkonmou Juubi",              
                                                                                 "damage": 430,  "number_o_t": 12,"add": 10, "add_attack": 25,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 355,  "number_o_t": 5, "add": 5,  "add_attack": 5, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Hakumenkonmou Juubi"
                                                                                ,"damage": 1135, "number_o_t": 15,"add": 15, "add_attack": 62,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Kinesis": {
                         "origin_skill":    {"skill_1": {"name":"From Another Realm",              
                                                                                 "damage": 821,  "number_o_t": 15,"add": 26, "add_attack": 12,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 832,  "number_o_t": 13,"add": 26, "add_attack": 44,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Illium": {
                         "origin_skill":    {"skill_1": {"name":"Mytocrystal Expanse",              
                                                                                 "damage": 620,  "number_o_t": 8, "add": 20, "add_attack": 12,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 692,  "number_o_t": 10,"add": 22, "add_attack": 13,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Mytocrystal Expanse"
                                                                                ,"damage": 775,  "number_o_t": 15,"add": 25, "add_attack": 16,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Lara": {
                         "origin_skill":    {"skill_1": {"name":"Universe in Bloom",  
                                                                                 "damage": 1085, "number_o_t": 7, "add": 35, "add_attack": 8, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 718,  "number_o_t": 14,"add": 23, "add_attack": 64,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Lynn": {
                         "origin_skill":    {"skill_1": {"name":"Source Flow",   "damage": 558,  "number_o_t": 12,"add": 18, "add_attack": 54,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 0,    "number_o_t": 0, "add": 0,  "add_attack": 0, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Bowmaster": {
                         "origin_skill":    {"skill_1": {"name":"Ascendant Shadow",              
                                                                                 "damage": 729,  "number_o_t": 14,"add": 24, "add_attack": 39,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 789,  "number_o_t": 8, "add": 26, "add_attack": 7, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Crossbowmaster": {
                         "origin_skill":    {"skill_1": {"name":"Final Aim",     "damage": 806,  "number_o_t": 7, "add": 26, "add_attack": 35,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 869,  "number_o_t": 13,"add": 29, "add_attack": 35,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Pathfinder": {
                         "origin_skill":    {"skill_1": {"name":"Forsaken Relic","damage": 801,  "number_o_t": 9, "add": 26, "add_attack": 24,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 791,  "number_o_t": 14,"add": 26, "add_attack": 30,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Forsaken Relic"
                                                                                ,"damage": 671,  "number_o_t": 45,"add": 21, "add_attack": 3, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 15,"def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Windshooter": {
                         "origin_skill":    {"skill_1": {"name":"Mistral Spring","damage": 858,  "number_o_t": 10,"add": 28, "add_attack": 13,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 0,    "number_o_t": 0, "add": 0,  "add_attack": 0, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "WildHunter": {
                         "origin_skill":    {"skill_1": {"name":"Nature's Truth",              
                                                                                 "damage": 1022, "number_o_t": 7, "add": 32, "add_attack": 12,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 1085, "number_o_t": 14,"add": 35, "add_attack": 23,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Nature's Truth"
                                                                                ,"damage": 1022, "number_o_t": 60,"add": 32, "add_attack": 15, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Mercedes": {
                         "origin_skill":    {"skill_1": {"name":"Unfading Glory","damage": 434,  "number_o_t": 10,"add": 14, "add_attack": 36,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 435,  "number_o_t": 15,"add": 15, "add_attack": 28,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Cain": {
                         "origin_skill":    {"skill_1": {"name":"Total Annihilation",              
                                                                                 "damage": 310,  "number_o_t": 8, "add": 10, "add_attack": 26,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 372,  "number_o_t": 14,"add": 12, "add_attack": 12,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Shadow": {
                         "origin_skill":    {"skill_1": {"name":"Halve Cut",     "damage": 496,  "number_o_t": 6, "add": 16, "add_attack": 23,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 405,  "number_o_t": 6, "add": 13, "add_attack": 32,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Halve Cut"
                                                                                ,"damage": 444,  "number_o_t": 7, "add": 14, "add_attack": 55,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "KnightLord": {
                         "origin_skill":    {"skill_1": {"name":"Life and Death","damage": 600,  "number_o_t": 7, "add": 20, "add_attack": 33,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 607,  "number_o_t": 42,"add": 19, "add_attack": 15,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "DualBlade": {
                         "origin_skill":    {"skill_1": {"name":"Karma Blade",   "damage": 496,  "number_o_t": 5, "add": 16, "add_attack": 6, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 465,  "number_o_t": 7, "add": 15, "add_attack": 20,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Karma Blade"
                                                                                ,"damage": 1135, "number_o_t": 7, "add": 20, "add_attack": 25,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "NightWalker": {
                         "origin_skill":    {"skill_1": {"name":"Silence",       "damage": 481,  "number_o_t": 12,"add": 16, "add_attack": 34,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 465,  "number_o_t": 12,"add": 15, "add_attack":150,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Zenon": {
                         "origin_skill":    {"skill_1": {"name":"Artificial Evolution",              
                                                                                 "damage": 362,  "number_o_t": 7, "add": 12, "add_attack": 31,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 558,  "number_o_t": 30,"add": 18, "add_attack": 16,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "PhantomThief": {
                         "origin_skill":    {"skill_1": {"name":"Defying Fate",  "damage": 403,  "number_o_t": 15,"add": 13, "add_attack": 57,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 321,  "number_o_t": 15,"add": 11, "add_attack": 60,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Cadena": {
                         "origin_skill":    {"skill_1": {"name":"Chain Arts: "
                                                         "Grand Arsenal",        "damage": 352,  "number_o_t": 8, "add": 12, "add_attack": 54,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 382,  "number_o_t": 9, "add": 12, "add_attack": 17,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Chain Arts: "
                                                         "Grand Arsenal"   ,     "damage": 403,  "number_o_t": 60,"add": 13, "add_attack": 14,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Torakage": {
                         "origin_skill":    {"skill_1": {"name":"Sage: Apotheosis",              
                                                                                 "damage": 520,  "number_o_t": 8, "add": 17, "add_attack": 10,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 631,  "number_o_t": 15,"add": 21, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Sage: Apotheosis"
                                                        ,                        "damage": 555,  "number_o_t": 14,"add": 18, "add_attack": 61,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Kali": {
                         "origin_skill":    {"skill_1": {"name":"Hex: Sandstorm","damage": 393,  "number_o_t": 15,"add": 13, "add_attack": 6, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 424,  "number_o_t": 10,"add": 14, "add_attack": 13,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Hex: Sandstorm"
                                                        ,                        "damage": 414,  "number_o_t": 14,"add": 14, "add_attack": 34,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":30, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "Viper": {
                         "origin_skill":    {"skill_1": {"name":"Unleash "
                                                         "Neptunus",             "damage": 713,  "number_o_t": 13,"add": 23, "add_attack": 4, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 589,  "number_o_t": 15,"add": 19, "add_attack": 22,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Captain": {
                         "origin_skill":    {"skill_1": {"name":"The Dreadnought",              
                                                                                 "damage": 661,  "number_o_t": 12,"add": 21, "add_attack": 52,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 775,  "number_o_t": 8, "add": 25, "add_attack": 30,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "CannonShooter": {
                         "origin_skill":    {"skill_1": {"name":"Super Cannon "
                                                         "Explosion",            "damage": 992,  "number_o_t": 4, "add": 32, "add_attack": 68,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 1147, "number_o_t": 5, "add": 37, "add_attack": 52,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Striker": {
                         "origin_skill":    {"skill_1": {"name":"Thunder Wall "
                                                         "Sea Wave",             "damage": 723,  "number_o_t": 5, "add": 23, "add_attack": 32,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 703,  "number_o_t": 7, "add": 23, "add_attack": 62,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Mechanic": {
                         "origin_skill":    {"skill_1": {"name":"Ground Zero",   "damage": 1054, "number_o_t": 8, "add": 34, "add_attack": 10,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 1023, "number_o_t": 15,"add": 33, "add_attack": 32,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Ground Zero",
                                                                                 "damage": 1488, "number_o_t": 15,"add": 48, "add_attack": 60,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":30, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "HiddenMoon": {
                         "origin_skill":    {"skill_1": {"name":"Advent of the Fox",              
                                                                                 "damage": 310,  "number_o_t": 11,"add": 10, "add_attack": 28,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 403,  "number_o_t": 13,"add": 13, "add_attack": 28,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            ,"skill_2": {"name":"Advent of the Fox",
                                                                                 "damage": 434,  "number_o_t": 14,"add": 14, "add_attack": 30,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam":30, "def_a": 0, "is_skill": True,  "opt": False}
                                            }
                        },                    
                "AngelicBuster": {
                         "origin_skill":    {"skill_1": {"name":"Grand Finale",  "damage": 346,  "number_o_t": 9, "add": 12, "add_attack": 12,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 355,  "number_o_t": 14,"add": 12, "add_attack": 38,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
                "Arc": {
                         "origin_skill":    {"skill_1": {"name":"Primordial Abyss",              
                                                                                 "damage": 579,  "number_o_t": 14,"add": 18, "add_attack": 68,"ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 889,  "number_o_t": 15,"add": 29, "add_attack": 60,"ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    

                     "job": {
                         "origin_skill":    {"skill_1": {"name":"",              "damage": 0,    "number_o_t": 0, "add": 0,  "add_attack": 0, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at": {                         "damage": 0,    "number_o_t": 0, "add": 0,  "add_attack": 0, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False}
                                            }
                        },                    
        }

        self.HEXA_skill_ascent = {
                 "Hero": {
                         "ascent_skill":    {"skill_1": {"name": "Ultrasonic "
                                                                 "Slash",       "damage": 1433, "number_o_t": 24, "add":237,"add_attack": 15,"ct":360,"dam": 0, "boss_dam": 40, "fainal_dam": 0, "def_a": 60, "is_skill": True,  "opt": False}
                                            ,"adi_at" : {"name": "",            "damage": 0,    "number_o_t": 0,  "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False}
                                            }
                        },
                 "Paladin": {
                         "ascent_skill":    {"skill_1": {"name": ""
                                                                 "",       "damage": 0,        "number_o_t": 0,  "add": 0, "add_attack": 1, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at" : {"name": "",       "damage": 0,        "number_o_t": 0,  "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False}
                                            }
                        },
                 "DarkNight": {
                         "ascent_skill":    {"skill_1": {"name": ""
                                                                 "",       "damage": 0,        "number_o_t": 0,  "add": 0, "add_attack": 1, "ct":360,"dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": True,  "opt": False}
                                            ,"adi_at" : {"name": "",       "damage": 0,        "number_o_t": 0,  "add": 0, "add_attack": 1, "ct": 0, "dam": 0, "boss_dam": 0, "fainal_dam": 0, "def_a": 0, "is_skill": False, "opt": False}
                                            }
                        },
        }

        #呼び出し　 self.HEXA_skill["Hero"][mastery][skill]["name"]


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
        #self.label_ascent = QLabel(self)
        #self.label_ascent.setText("アセントスキル")


        self.label_space1 = QLabel(self)
        self.label_space1.setText("マスタリー")
        self.label_space2 = QLabel(self)
        self.label_space2.setText("強化コア")
        self.label_space3 = QLabel(self)
        self.label_space3.setText("スキルコア")
        self.label_LV = QLabel(self)
        self.label_LV.setText("Lv")


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

        #self.label_ascent_sp = QSpinBox(self)
        #self.label_ascent_sp.setValue(0)
        #self.label_ascent_sp.setMaximum(30)

        #self.label_ascent_fd_sp = QSpinBox(self)
        #self.label_ascent_fd_sp.setValue(0)
        #self.label_ascent_fd_sp.setMaximum(30)

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

        #self.ascent_dam_li = QLineEdit()
        #self.ascent_dam_li.setReadOnly(True)
        #self.ascent_fd_li = QLineEdit()
        #self.ascent_fd_li.setReadOnly(True)


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

        #self.ascent_dam_butt = QPushButton(self)
        #self.ascent_dam_butt.setText("ASCENT : ダメージ")
        #self.ascent_fd_dam_butt = QPushButton(self)
        #self.ascent_fd_dam_butt.setText("ASCENT : 最終ダメージ")


    #コンボックス
        self.combobox = QComboBox(self)
        self.combobox.setEditable(False)
        self.combobox.setFixedSize(200, 30)
        #self.combobox.addItem("job")
        self.combobox.addItem(self.main_window_ref.select_job)

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
        #layout.addWidget(self.label_ascent, 14,0)

    #スピンボックス
        layout.addWidget(self.label_LV, 1,1)
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
        #layout.addWidget(self.label_ascent_sp, 14,1)

        layout.addWidget(self.label_mastery1_fd_sp, 7,4)
        layout.addWidget(self.label_mastery2_fd_sp, 8,4)
        layout.addWidget(self.label_mastery3_fd_sp, 9,4)
        layout.addWidget(self.label_mastery4_fd_sp, 10,4)

        layout.addWidget(self.label_origin_fd_sp, 13,4)
        #layout.addWidget(self.label_ascent_fd_sp, 15,4)


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
        #layout.addWidget(self.ascent_li, 14,2)

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
        #layout.addWidget(self.ascent_dam_li, 14,5)
        #layout.addWidget(self.ascent_fd_li, 15,5)



    #ダメージ計算ボタン
        layout.addWidget(self.mastery1_dam_butt, 2,3)
        layout.addWidget(self.mastery2_dam_butt, 3,3)
        layout.addWidget(self.mastery3_dam_butt, 4,3)
        layout.addWidget(self.mastery4_dam_butt, 5,3)
        layout.addWidget(self.origin_dam_butt, 12,3)
        #layout.addWidget(self.ascent_dam_butt, 14,3)


        layout.addWidget(self.mastery1_fd_dam_butt, 7,3)
        layout.addWidget(self.mastery2_fd_dam_butt, 8,3)
        layout.addWidget(self.mastery3_fd_dam_butt, 9,3)
        layout.addWidget(self.mastery4_fd_dam_butt, 10,3)
        layout.addWidget(self.origin_fd_dam_butt, 13,3)
        #layout.addWidget(self.ascent_fd_dam_butt, 15,3)


            
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

        self.boss_damage            = 0
        self.damage                 = 0
        self.def_a                  = 0
        self.fainal_dam_skill = 0

        #初期化
        self.attack_damage = is_input(0)
        self.dam_calc
        self.format_damage()

        self.level_dia_c = (1.1)
        self.attack_damage = is_input(self.attack_damage_li.text().strip())
        self.skill_set()

        self.hexa_calc = HEXA_calc()
        self.mastery_name = "name"

    #計算処理
        self.mastery1_dam_butt.pressed.connect(self.mastery1_fd_calc)
        self.mastery2_dam_butt.pressed.connect(self.mastery2_fd_calc)
        self.mastery3_dam_butt.pressed.connect(self.mastery3_fd_calc)
        self.mastery4_dam_butt.pressed.connect(self.mastery4_fd_calc)

        #マスタリー最終ダメージ
        self.mastery1_fd_dam_butt.pressed.connect(self.mastery1_fd_calc)
        self.mastery2_fd_dam_butt.pressed.connect(self.mastery2_fd_calc)
        self.mastery3_fd_dam_butt.pressed.connect(self.mastery3_fd_calc)
        self.mastery4_fd_dam_butt.pressed.connect(self.mastery4_fd_calc)

        #origin
        self.origin_dam_butt.pressed.connect(self.origin_fd_calc)
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
        self.label_mastery1_sp.valueChanged.connect(lambda: self.is_input_mastery1(self.label_mastery1_sp.value()-1))
        self.label_mastery2_sp.valueChanged.connect(lambda: self.is_input_mastery2(self.label_mastery2_sp.value()-1))
        self.label_mastery3_sp.valueChanged.connect(lambda: self.is_input_mastery3(self.label_mastery3_sp.value()-1))
        self.label_mastery4_sp.valueChanged.connect(lambda: self.is_input_mastery4(self.label_mastery4_sp.value()-1))

        self.mastery1_combo.activated.connect(lambda: self.is_input_mastery1(self.label_mastery1_sp.value()-1))
        self.mastery2_combo.activated.connect(lambda: self.is_input_mastery2(self.label_mastery2_sp.value()-1))
        self.mastery3_combo.activated.connect(lambda: self.is_input_mastery3(self.label_mastery3_sp.value()-1))
        self.mastery4_combo.activated.connect(lambda: self.is_input_mastery4(self.label_mastery4_sp.value()-1))

        #enhance
        self.label_enhancement1_sp.valueChanged.connect(self.is_input_enhance1)
        self.label_enhancement2_sp.valueChanged.connect(self.is_input_enhance2)
        self.label_enhancement3_sp.valueChanged.connect(self.is_input_enhance3)
        self.label_enhancement4_sp.valueChanged.connect(self.is_input_enhance4)

        #origin
        self.label_origin_sp.valueChanged.connect(lambda: self.is_input_origin(self.label_origin_sp.value()-1))

        #ascent
        #self.label_ascent_sp.valueChanged.connect(self.is_input_ascent)

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
        
    def is_input_mastery(self, skill_level, n):
        self.mastery = skill_level
        self.hexa_calc = HEXA_calc()
        self.hexa_calc.select_job = self.select_job

        dic = self.HEXA_skill_mastery
        dic_add = self.HEXA_mastery_add

        mastery_skill = "mastery" + n + "_skill"
        combo = getattr(self, f"mastery{n}_combo")
        
        Index=combo.currentIndex()
        skill = "skill_" + str(Index+1)
        self.hexa_calc.input_set(dic, mastery_skill, skill, dic_add)

        self.hexa_calc.input_mastery(self.mastery)
        if(self.hexa_calc.add_effect):
            self.hexa_calc.input_add()


    def is_input_mastery1(self, skill_level):
        self.hexa_calc = HEXA_calc()
        self.hexa_calc.select_job = self.select_job
        self.is_input_mastery(skill_level, "1")

        self.mastery1_li.setText(self.hexa_calc.text)
        self.boss_damage     = self.hexa_calc.boss_dam/100
        self.damage             = self.hexa_calc.dam/100
        self.def_a           = self.hexa_calc.def_a/100
        self.skill_dam_m1       = self.hexa_calc.damage/100
        self.skill_dam_m1_add   = self.hexa_calc.damage_add/100
        self.numb_t_m1          = self.hexa_calc.attack_num
        self.numb_t_m1_add      = self.hexa_calc.attack_num_add
        self.fainal_dam_skill   = self.hexa_calc.fainal_dam

    def is_input_mastery2(self, skill_level):
        self.hexa_calc = HEXA_calc()
        self.hexa_calc.select_job = self.select_job
        self.is_input_mastery(skill_level, "2")
        

        self.mastery_name = self.hexa_calc.name
        if(self.mastery_name == "Triumph Feather"):
            self.mastery2_li.setText(self.hexa_calc.text + "  6枚の羽[5枚 最終ダメージ減少]")
        else:
            self.mastery2_li.setText(self.hexa_calc.text)

        self.boss_damage     = self.hexa_calc.boss_dam/100
        self.damage             = self.hexa_calc.dam/100
        self.def_a           = self.hexa_calc.def_a/100
        self.skill_dam_m2 = self.hexa_calc.damage/100
        self.skill_dam_m2_add = self.hexa_calc.damage_add/100
        self.numb_t_m2    = self.hexa_calc.attack_num
        self.numb_t_m2_add    = self.hexa_calc.attack_num_add
        self.fainal_dam_skill = self.hexa_calc.fainal_dam

    def is_input_mastery3(self, skill_level):
        self.hexa_calc = HEXA_calc()
        self.hexa_calc.select_job = self.select_job
        self.is_input_mastery(skill_level, "3")


        self.mastery3_li.setText(self.hexa_calc.text)
        self.boss_damage     = self.hexa_calc.boss_dam/100
        self.damage             = self.hexa_calc.dam/100
        self.def_a           = self.hexa_calc.def_a/100
        self.skill_dam_m3 = self.hexa_calc.damage/100
        self.skill_dam_m3_add = self.hexa_calc.damage_add/100
        self.numb_t_m3    = self.hexa_calc.attack_num
        self.numb_t_m3_add    = self.hexa_calc.attack_num_add
        self.fainal_dam_skill = self.hexa_calc.fainal_dam

    def is_input_mastery4(self, skill_level):
        self.hexa_calc = HEXA_calc()
        self.hexa_calc.select_job = self.select_job
        self.is_input_mastery(skill_level, "4")


        self.mastery4_li.setText(self.hexa_calc.text)
        self.boss_damage     = self.hexa_calc.boss_dam/100
        self.damage             = self.hexa_calc.dam/100
        self.def_a           = self.hexa_calc.def_a/100
        self.skill_dam_m4 = self.hexa_calc.damage/100
        self.skill_dam_m4_add = self.hexa_calc.damage_add/100
        self.numb_t_m4    = self.hexa_calc.attack_num
        self.numb_t_m4_add    = self.hexa_calc.attack_num_add
        self.fainal_dam_skill = self.hexa_calc.fainal_dam


    def is_input_enhance(self, enhance):

        self.enhancement = enhance
        enhancement_fi_dam = (
            10 + self.enhancement
        )
        if(self.enhancement>=10): 
            enhancement_fi_dam+=5
        if(self.enhancement>=20):
            enhancement_fi_dam+=5
        if(self.enhancement>=30):
            enhancement_fi_dam+=10
        if(self.enhancement==0):
            enhancement_fi_dam=0
        self.enhancement_fi_dam = enhancement_fi_dam
        self.enhancement_text = "最終ダメージ: " + str(self.enhancement_fi_dam) +"%"


    def is_input_enhance1(self):
        enhance1_name = self.HEXA_skill_enhance[self.select_job]["enhance1_skill"]["skill_1"]["name"] 
        enhance = self.label_enhancement1_sp.value()
        self.is_input_enhance(enhance)
        self.enhancement1_li.setText(self.enhancement_text)
        
        #Hayato
        if(enhance1_name == "Shogetsu Form Boost"):
            enhancement_fi = 101 + round(enhance*0.3)
            text = "持続時間: " + str(30 + round(enhance*0.34)) + "秒"
            text = text + "  最終ダメージ: " +str(enhancement_fi)+"%"
            text = text + "  防御率無視: " + str(50+enhance)+"%"
            self.enhancement1_li.setText(text)

        #Zero
        if(enhance1_name == "Chrono Break"):
            text = ("クロノブレイク" + self.enhancement_text)
            enhancement_fi = 37 + round(enhance*0.3)
            text = text + "  最終ダメージ: " +str(enhancement_fi)+"%"
            self.enhancement1_li.setText(text)
            
        #Bishop
        if(enhance1_name == "Benediction"):
            text = ("ビショップの")
            enhancement_fi = 2 + round(enhance*0.5)
            text = text + "最終ダメージ: " +str(enhancement_fi)+"%"
            text=  text + "  [passive]全ステータス: " +str(round(enhance*3))
            self.enhancement1_li.setText(text)

        #WildHunter
        if(enhance1_name == "Jaguar Storm"):          
            enhancement_fi = 210 + round(enhance*5)
            text = "最終ダメージ: " +str(enhancement_fi)+"%"
            self.enhancement1_li.setText(text)

        #Mercedes
        if(enhance1_name == "Spirit of Elluel"):          
            enhancement_fi = round(60.5 + enhance*0.5)
            text = self.enhancement_text + "  Spirits最終ダメージ: " +str(enhancement_fi)+"%"
            self.enhancement1_li.setText(text)
            
        #Torakage
        if(enhance1_name == "Sage: Clone Rampage"):          
            enhancement_fi = round(440 + enhance*0.17)
            text = "クローンの暴走が有効な間ダメージ: " +str(enhancement_fi)+"%"
            self.enhancement1_li.setText(text)
            
        #Striker
        if(enhance1_name == "Lightning Cascade"):          
            enhancement_fi = round(27.83 + enhance*12)
            text = self.enhancement_text + "  Viperの最終ダメージ: " +str(enhancement_fi)+"%"
            self.enhancement1_li.setText(text)
                    
    def is_input_enhance2(self):
        enhance2_name = self.HEXA_skill_enhance[self.select_job]["enhance2_skill"]["skill_1"]["name"] 
        enhance = self.label_enhancement2_sp.value()
        self.is_input_enhance(enhance)
        self.enhancement2_li.setText(self.enhancement_text)
        
        #kanna
        if(enhance2_name == "Unleash the Radiant Flame"):
            enhancement_fi = 30 
            if(enhance>=10):
                enhancement_fi +=1
            if(enhance>=20):
                enhancement_fi +=2
            if(enhance>=30):
                enhancement_fi +=2
            text = "最終ダメージ: " +str(enhancement_fi)+"%"
            text=  text + "  持続時間: " +str(round(30.66+enhance*0.34))
            self.enhancement2_li.setText(text)
        
        #NightWalker
        if(enhance2_name == "Greater Dark Servant"):
            enhancement_fi = 55 + round(enhance*1)
            text = "最終ダメージ: " +str(enhancement_fi)+"%"
            dure = 56 + round(enhance*0.3)
            text = text + "  持続時間: " + str(dure)
            self.enhancement2_li.setText(text)     
            
        #Arc
        if(enhance2_name == "Infinity Spell"):
            enhancement_fi = round(enhance*7)
            text = "Impending Death Damage During Infinity Spell:ダメージ: " +str(enhancement_fi)+"%"
            self.enhancement2_li.setText(text)     
            
    def is_input_enhance3(self):
        enhance3_name = self.HEXA_skill_enhance[self.select_job]["enhance3_skill"]["skill_1"]["name"] 
        enhance = self.label_enhancement3_sp.value()
        self.is_input_enhance(enhance)
        self.enhancement3_li.setText(self.enhancement_text)
        
        #Lynn        
        if(enhance3_name == "[Focus] Awaken Boost"):
            text = ("Awaken Boostの効果を受けている間")
            enhancement_fi = 10
            
            if(enhance>=9):
                enhancement_fi += 1
            elif(enhance>=19):
                enhancement_fi += 2
            elif(enhance>=29):
                enhancement_fi += 1
            elif(enhance>=30):
                enhancement_fi += 1
                
            text = text + "最終ダメージ: " +str(enhancement_fi)+"%"
            text=  text + "  [passive]全ステータス: " +str(round(enhance*3))
            self.enhancement3_li.setText(text)
            
        #NightWalker
        if(enhance3_name == "Shadow Bite"):
            enhancement_fi = 3 
            if(enhance>=9):
                enhancement_fi += 1
            elif(enhance>=17):
                enhancement_fi += 1
            elif(enhance>=25):
                enhancement_fi += 1
            text = self.enhancement_text + "Shadow Biteで倒した敵ごとに最終ダメージ: " +str(enhancement_fi)+"%"
            ct = 14 - round(enhance*0.16)
            text = text + "  ct: " + str(ct)
            self.enhancement2_li.setText(text)

    def is_input_enhance4(self):
        enhance4_name = self.HEXA_skill_enhance[self.select_job]["enhance4_skill"]["skill_1"]["name"] 
        enhance = self.label_enhancement4_sp.value()
        self.is_input_enhance(enhance)
        self.enhancement4_li.setText(self.enhancement_text)
        
        #Lynn        
        if(enhance4_name == "Nature's Grace"):
            text=  "  [passive]全ステータス: " +str(round(enhance*3))
            self.enhancement4_li.setText(text)
        


    def is_input_origin(self, skill_level):

        self.hexa_calc = origin_calc()
        self.hexa_calc.select_job = self.select_job
        dic = self.HEXA_skill_origin

        self.origin = skill_level

        #skill
        self.hexa_calc.input_set_origin(dic)
        self.hexa_calc.input_origin(self.origin)
        self.origin_li.setText(self.hexa_calc.text) 
        
        self.boss_dam_origin = 0
        self.damage          = 0
        self.def_a_origin    = 0
        self.skill_dam_origin = self.hexa_calc.damage_origin/100
        self.skill_dam_origin_add = self.hexa_calc.damage_add/100
        self.numb_t_origin    = self.hexa_calc.attack_num
        self.numb_t_origin_add = self.hexa_calc.attack_num_add
        
        if(self.hexa_calc.skill2_damage_origin != 0):
            self.skill2_dam_origin = self.hexa_calc.skill2_damage_origin/100
            self.skill2_numb_t_origin    = self.hexa_calc.skill2_attack_num_origin

        if(self.origin>=10):
            self.def_a_origin       = 20
        if(self.origin>=20):
            self.boss_dam_origin    = 30
        if(self.origin>=30):
            self.def_a_origin       = 30
        
        self.boss_damage            = (self.hexa_calc.boss_dam + self.boss_dam_origin)/100
        self.damage                 = 0
        self.def_a                  = (self.hexa_calc.def_a + self.def_a_origin)/100
        self.fainal_dam_origin      = 0

    def is_input_ascent(self):
        damage_ascent = 0
        attack_num = 0
        damage_ascent_add = 0
        attack_num_add = 0
        self.hexa_calc = ascent_calc()
        self.hexa_calc.select_job = self.select_job
        dic = self.HEXA_skill_ascent

        damage_ascent_add = 0
        attack_num_add = 0

        self.ascent = self.label_ascent_sp.value() -1


        #skill
        self.hexa_calc.input_set_ascent(dic)
        self.hexa_calc.input_ascent(damage_ascent,
                                    self.ascent)


        self.ascent_li.setText(self.hexa_calc.text) 


        self.boss_damage_ascent = 0
        self.def_a_ascent = 0
        self.skill_dam_ascent = damage_ascent/100
        self.skill_dam_ascent_add = damage_ascent_add/100
        self.numb_t_ascent    = attack_num
        self.numb_t_ascent_add = attack_num_add
        self.fainal_dam_origin = 0


        self.mastery1_calc()
        self.mastery2_calc()
        self.mastery3_calc()
        self.mastery4_calc()

    def skill_set(self):

        self.mastery1_combo.clear()
        self.mastery2_combo.clear()
        self.mastery3_combo.clear()
        self.mastery4_combo.clear()
    
        #マスタリーSET
        i=1
        while(self.HEXA_skill_mastery.get(self.select_job, {}).get("mastery1_skill", {}).get("skill_" + str(i), {}).get("is_skill") == True):
            if(self.HEXA_skill_mastery.get(self.select_job, {}).get("mastery1_skill", {}).get("skill_" + str(i), {}).get("is_skill") == True):
                add_text = [self.HEXA_skill_mastery[self.select_job]["mastery1_skill"]["skill_" + str(i)]["name"]]
                self.mastery1_combo.addItems(add_text)
            i+=1


        i=1
        while(self.HEXA_skill_mastery.get(self.select_job, {}).get("mastery2_skill", {}).get("skill_" + str(i), {}).get("is_skill") == True):
            if(self.HEXA_skill_mastery.get(self.select_job, {}).get("mastery2_skill", {}).get("skill_" + str(i), {}).get("is_skill") == True):
                add_text = [self.HEXA_skill_mastery[self.select_job]["mastery2_skill"]["skill_" + str(i)]["name"]]
                self.mastery2_combo.addItems(add_text)
            i+=1
         
         
        i=1
        while(self.HEXA_skill_mastery.get(self.select_job, {}).get("mastery3_skill", {}).get("skill_" + str(i), {}).get("is_skill") == True):
            if(self.HEXA_skill_mastery.get(self.select_job, {}).get("mastery3_skill", {}).get("skill_" + str(i), {}).get("is_skill") == True):
                add_text = [self.HEXA_skill_mastery[self.select_job]["mastery3_skill"]["skill_" + str(i)]["name"]]
                self.mastery3_combo.addItems(add_text)
            i+=1


        i=1
        while(self.HEXA_skill_mastery.get(self.select_job, {}).get("mastery4_skill", {}).get("skill_" + str(i), {}).get("is_skill") == True):
            if(self.HEXA_skill_mastery.get(self.select_job, {}).get("mastery4_skill", {}).get("skill_" + str(i), {}).get("is_skill") == True):
                add_text = [self.HEXA_skill_mastery[self.select_job]["mastery4_skill"]["skill_" + str(i)]["name"]]
                self.mastery4_combo.addItems(add_text)
            i+=1



        #強化コアSET
        self.label_enhancement1.setText(str(self.HEXA_skill_enhance[self.select_job]["enhance1_skill"]["skill_1"]["name"]))
        self.label_enhancement2.setText(str(self.HEXA_skill_enhance[self.select_job]["enhance2_skill"]["skill_1"]["name"]))
        self.label_enhancement3.setText(str(self.HEXA_skill_enhance[self.select_job]["enhance3_skill"]["skill_1"]["name"]))
        self.label_enhancement4.setText(str(self.HEXA_skill_enhance[self.select_job]["enhance4_skill"]["skill_1"]["name"]))

        #スキルコア
            #origin
        self.label_origin.setText(str(self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["name"]))

    def mastery_calc(self, skill_dam_m, numb_t_m,  skill_dam_m_add, numb_t_m_add):
        self.attack_damage = 0
        damage = 0
        self.calc(skill_dam_m, numb_t_m)
        damage = self.attack_damage

        #add_damage
        if(self.attack_damage > 0):
            self.calc(skill_dam_m_add, numb_t_m_add)
            self.attack_damage += damage


        self.format_damage()


    def mastery1_calc(self):
        self.mastery_calc(self.skill_dam_m1,self.numb_t_m1, self.skill_dam_m1_add,self.numb_t_m1_add)
        
        self.format_damage()
        self.mastery1_dam_li.setText(self.damage_text)

    def mastery2_calc(self):
        self.mastery_calc(self.skill_dam_m2,self.numb_t_m2, self.skill_dam_m2_add,self.numb_t_m2_add)
        
        #Bishop
        if(self.mastery_name == "Triumph Feather"):
            skill_dam   = 396 + 6*self.mastery
            numb_t      = 4
            skill_dam   = skill_dam/100
            i=0
            damage = self.attack_damage
            self.attack_damage=0
            self.fainal_dam_skill = -50
            while(i<5):
                self.calc(skill_dam, numb_t)
                damage += self.attack_damage
                i+=1
            if(i==5):   
                self.attack_damage = damage
        
        self.format_damage()
        self.mastery2_dam_li.setText(self.damage_text)

    def mastery3_calc(self):
        self.mastery_calc(self.skill_dam_m3,self.numb_t_m3, self.skill_dam_m3_add,self.numb_t_m3_add)
        
        self.format_damage()
        self.mastery3_dam_li.setText(self.damage_text)

    def mastery4_calc(self):
        self.mastery_calc(self.skill_dam_m4,self.numb_t_m4, self.skill_dam_m4_add,self.numb_t_m4_add)
        
        self.format_damage()
        self.mastery4_dam_li.setText(self.damage_text)



    def origin_calc(self):
        self.attack_damage = 0
        damage = 0

        origin_name = self.HEXA_skill_origin[self.select_job]["origin_skill"]["skill_1"]["name"] 
        
        self.calc(self.skill_dam_origin,self.numb_t_origin)
        damage = self.attack_damage
        
        skill_2_data = self.HEXA_skill_origin.get(self.select_job, {}).get("origin_skill", {}).get("skill_2")
        if skill_2_data:
            self.calc(self.skill2_dam_origin, self.skill2_numb_t_origin)
            damage = self.attack_damage + damage
        else:
            pass
        #add_damage
        self.calc(self.skill_dam_origin_add, self.numb_t_origin_add)
        damage = self.attack_damage + damage


        #Bishop
        if(origin_name == "Holy Advent"):
            #Archangel of Balance
            skill_dam   = 254 + 9*self.origin
            numb_t      = 14*20
            ct          = 3
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #Avenging Archangel 
            skill_dam   = 268 + 8*self.origin
            numb_t      = 12*12
            ct          = 5
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #Archangel of Benevolence
            skill_dam   = 310 + 10*self.origin
            numb_t      = 12*15
            ct          = 4
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            
        #Illium
        if(origin_name == "Mytocrystal Expanse"):
            #infinite mytocrystals
            skill_dam   = 992 + 32*self.origin
            numb_t      = 15*20
            ct          = 1
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #Mytocrystal Crystals 
            skill_dam   = 620 + 20*self.origin
            numb_t      = 50*8
            ct          = 2
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage

        #Pathfinder
        if(origin_name == "Forsaken Relic"):
            skill_dam   = 837 + 27*self.origin
            numb_t      = 5*60
            ct          = 0.5
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage

        #Windshooter
        if(origin_name == "Mistral Spring"):
            #Spirit Arrows
            skill_dam   = 682 + 22*self.origin
            numb_t      = 5*13*12
            ct          = 3
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #Excited Spirit Arrows
            skill_dam   = 744 + 24*self.origin
            numb_t      = 6*5*12
            ct          = 3
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #Strong Spirit Arrows
            skill_dam   = 666 + 21*self.origin
            numb_t      = 7*3*12
            ct          = 3
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage

        #Mercedes
        if(origin_name == "Unfading Glory"):
            #精霊王形態
            skill_dam   = 1156 + 36*self.origin
            numb_t      = 15*20
            ct          = 3
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #強化された攻撃
            skill_dam   = 744 + 24*self.origin
            numb_t      = 15*4*30
            ct          = 2
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage

        #Cain
        if(origin_name == "Total Annihilation"):
            #マリスの領土
            skill_dam   = 483 + 8*self.origin
            numb_t      = 15
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #デスの祝福
            skill_dam   = 589 + 19*self.origin
            numb_t      = 15*2*150
            ct          = 0.2
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage

        #DualBlade
        if(origin_name == "Karma Blade"):
            #業火の神はカルマブレードを完全に消費するか持続時間が終了すると顕現
            skill_dam   = 578 + 18*self.origin
            numb_t      = 7*30
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage

        #Viper
        if(origin_name == "Unleash Neptunus"):
            #1
            skill_dam   = 897 + 27*(self.origin-1)
            numb_t      = 12
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #2
            skill_dam   = 930 + 30*(self.origin-1)
            numb_t      = 13
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #3
            skill_dam   = 992 + 32*(self.origin-1)
            numb_t      = 15
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #4
            skill_dam   = 992 + 32*(self.origin-1)
            numb_t      = 15
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #5
            skill_dam   = 1136 + 36*(self.origin-1)
            numb_t      = 15
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage

        #AngelicBuster
        if(origin_name == "Grand Finale"):
            #Balloons
            skill_dam   = 340 + 5*(self.origin)
            numb_t      = 25
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #Cheering Balloons
            skill_dam   = 433 + 8*(self.origin)
            numb_t      = 7
            ct          = 0
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage
            #Cheering Balloons 2-
            skill_dam   = 433 + 8*(self.origin)
            numb_t      = 7*20
            ct          = 0
            self.fainal_dam_skill = -43
            self.calc(skill_dam, numb_t)
            damage      = self.attack_damage + damage

        self.attack_damage = damage
        self.format_damage()
        self.origin_dam_li.setText(self.damage_text)
        


    def mastery_fd_calc(self, mastery_fd, mastery, n):
        self.mastery_fd = mastery_fd
        mastery_skill = "mastery" + n + "_skill"
        is_input = getattr(self, f"is_input_mastery{n}")
        is_input(self.mastery_fd)
        
        mastery_calc = getattr(self, f"mastery{n}_calc")
        mastery_calc()
        damage_fd = self.attack_damage  

        self.mastery = mastery
        is_input(self.mastery)
        mastery_calc()
        damage = self.attack_damage


        skill_dam = getattr(self, f"skill_dam_m{n}")
        if(damage_fd!=0 and skill_dam !=0):
            fd = ((damage_fd/damage)*100) - 100
        else:
            fd=0
        fd = round(fd, 3)
        mastery_fd_li = getattr(self, f"mastery{n}_fd_li")
        mastery_fd_li.setText("最終ダメージの増加量: " + str(fd))

    
    def mastery1_fd_calc(self):
        self.mastery_fd_calc(self.label_mastery1_fd_sp.value() -1, self.label_mastery1_sp.value() -1,  "1")

    def mastery2_fd_calc(self):
        self.mastery_fd_calc(self.label_mastery2_fd_sp.value() -1, self.label_mastery2_sp.value() -1,  "2")

    def mastery3_fd_calc(self):
        self.mastery_fd_calc(self.label_mastery3_fd_sp.value() -1, self.label_mastery3_sp.value() -1,  "3")

    def mastery4_fd_calc(self):
        self.mastery_fd_calc(self.label_mastery4_fd_sp.value() -1, self.label_mastery4_sp.value() -1,  "4")

    def origin_fd_calc(self):
        self.attack_damage = 0
        damage = 0

        self.origin_fd = self.label_origin_fd_sp.value() -1
        self.is_input_origin(self.origin_fd)
        self.origin_calc()
        damage_fd = self.attack_damage

        self.origin = self.label_origin_sp.value() -1
        self.is_input_origin(self.origin)
        self.origin_calc()
        damage = self.attack_damage


        if(damage_fd!=0 and self.skill_dam_m1 !=0):
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

    def dam_calc(self, skill_dam):
           
        #damage   
        self.damage      = self.main_window_ref.damage + self.damage
        #BossDam    
        self.boss_damage = self.main_window_ref.boss_damage + self.boss_damage
        mons_def = (1-self.main_window_ref.mons_def*(1-self.main_window_ref.def_a))
        
        #防御率無視
        out_def_att = (
            1-self.main_window_ref.mons_def*(1-self.main_window_ref.mons_def)*(1-self.def_a)
            )
        monsdef = round(out_def_att*100, 2)

        #最終ダメージ
        self.fainal_dam = (
            (1+self.main_window_ref.fainal_dam)*(1+self.fainal_dam_skill/100)-1
            )
        
        self.skill_dam = skill_dam
        #print(self.mons_def)

        self.attack_damage = (
        self.main_window_ref.wepon_coe * (self.main_window_ref.main_st*4 + self.main_window_ref.sub_st) * (self.main_window_ref.a_ma/100) *(1 + self.damage + self.boss_damage) * (1-(self.main_window_ref.element_def_const-self.main_window_ref.element_ig)) *
        (1.35 + self.main_window_ref.crit_dam) * self.skill_dam * (mons_def) * (1 + self.fainal_dam) * self.main_window_ref.profic )

        self.fainal_dam_skill = 0

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
