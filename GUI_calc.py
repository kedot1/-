import PySide6
from PySide6.QtWidgets import (QApplication, QSpinBox, QDoubleSpinBox, QLineEdit, QPushButton,
        QLabel, QComboBox, QRadioButton, QButtonGroup, QWidget, QGridLayout)
from PySide6.QtGui import QDoubleValidator, QColor,  QPalette
from PySide6.QtCore import QLocale, Qt
import os
import sys
import math, time
import GUI_calc_swindow
import Ren_calc_twindow, HEXA_calc_twindow

QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseOpenGLES)
# 1. 既存の QApplication インスタンスがあるかチェック
app = QApplication.instance()

# 2. なければ新しいインスタンスを作成する
#if app is None:
#    app = QApplication(sys.argv)

# PySide6のアプリ本体（ユーザがコーディングしていく部分）
class MainWindow(QWidget):              # ウィンドウ系クラスを継承すること
    def __init__(self, parent=None):    # parentは他にウィンドウを表示させる場合に指定する
        super().__init__(parent)        # 継承元クラス（ここではQWidget）を初期化


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
                "Mechanic",       "HiddenMoon",     "AngelicBuster",  "Arc",            "Ren"
        ]

        self.job_wepon_coe = {
                "Hero":1.44,          "Paladin":1.34,       "DarkNight":1.49,     "SoulMaster":1.34,    "Aran":1.49,
                "DemonSlayer":1.2,    "DemonAvenger":1.3,   "Kaiser":1.34,        "Hayato":1.25,        "Zero":1.34,
                "Michael":1.24,       "Blaster":1.7,        "Adel":1.3,           "IceLightning":1.2,   "FirePoison":1.2,
                "Bishop":1.2,         "FlameWizard":1.2,    "BattleMage":1.2,     "Evan":1.2,           "Luminous":1.2,
                "Kanna":1.35,         "Kinesis":1.2,        "Illium":1.2,         "Lara":1.2,           "Lynn":1.34,
                "Bowmaster":1.3,      "Crossbowmaster":1.35,"Pathfinder":1.3,     "Windshooter":1.3,    "WildHunter":1.35,
                "Mercedes":1.3,       "Cain":1.3,           "Shadow":1.3,         "KnightLord":1.75,    "DualBlade":1.3,
                "NightWalker":1.75,   "Zenon":1.3125,       "PhantomThief":1.3,   "Cadena":1.3,         "Torakage":1.3,
                "Kali":1.3,           "Viper":1.7,          "Captain":1.5,        "CannonShooter":1.5,  "Striker":1.7,
                "Mechanic":1.5,       "HiddenMoon":1.7,     "AngelicBuster":1.7,  "Arc":1.7,            "Ren" :1.3
        }

        self.job_profic = {
                "Hero":90,           "Paladin":91,       "DarkNight":90,      "SoulMaster":90,     "Aran":90,
                "DemonSlayer":90,    "DemonAvenger":90,   "Kaiser":90,         "Hayato":99,        "Zero":90,
                "Michael":90,        "Blaster":90,        "Adel":90,           "IceLightning":95,  "FirePoison":95,
                "Bishop":95,        "FlameWizard":95,   "BattleMage":95,    "Evan":95,          "Luminous":95,
                "Kanna":95,         "Kinesis":90,        "Illium":90,         "Lara":95,          "Lynn":95,
                "Bowmaster":85,     "Crossbowmaster":90, "Pathfinder":85,    "Windshooter":85,   "WildHunter":85,
                "Mercedes":85,      "Cain":85,           "Shadow":95,         "KnightLord":85,    "DualBlade":90,
                "NightWalker":90,    "Zenon":90,          "PhantomThief":90,   "Cadena":90,         "Torakage":90,
                "Kali":90,           "Viper":90,          "Captain":85,       "CannonShooter":85, "Striker":90,
                "Mechanic":85,      "HiddenMoon":90,     "AngelicBuster":95, "Arc":90,             "Ren": 90
        }


    # ウィンドウタイトル
        self.setWindowTitle("dam_calc_GUImode...")
    # ウィンドウサイズを指定（px単位）
        windowWidth = 1300  # ウィンドウの横幅
        windowHeight = 500  # ウィンドウの高さ
    # ウィンドウサイズの変更
        self.resize(windowWidth, windowHeight)
        self.setFixedSize(1300, 500)

    #別window
        self.s_window_open = QPushButton("Tools")
        self.t_window_open = QPushButton("HEXA")
        #self.setCentralWidget(self.s_window_open())

    # (レイアウト)
        layout = QGridLayout(self)
        self.setLayout(layout)


    # ラベルを表示するメソッド
        self.label_wepon_coe = QLabel(self)
        self.label_wepon_coe.setText("武器係数")

        self.label_main_st = QLabel(self)
        self.label_main_st.setText("メインステータス")
        self.label_main_st_ba = QLabel(self)
        self.label_main_st_ba.setText("   基本数値")
        self.label_main_st_per = QLabel(self)
        self.label_main_st_per.setText("  %数値")
        self.label_main_st_n_per = QLabel(self)
        self.label_main_st_n_per.setText("  %未適用")

        self.label_sub_st = QLabel(self)
        self.label_sub_st.setText("サブステータス")
        self.label_sub_st_ba = QLabel(self)
        self.label_sub_st_ba.setText("   基本数値")
        self.label_sub_st_per = QLabel(self)
        self.label_sub_st_per.setText("  %数値")
        self.label_sub_st_n_per = QLabel(self)
        self.label_sub_st_n_per.setText("  %未適用")
        
        self.label_a_ma = QLabel(self)
        self.label_a_ma.setText("a/ma")
        self.label_a_ma_ba = QLabel(self)
        self.label_a_ma_ba.setText("   基本数値")
        self.label_a_ma_per = QLabel(self)
        self.label_a_ma_per.setText("  %数値")
        self.label_a_ma_n_per = QLabel(self)
        self.label_a_ma_n_per.setText("  %未適用")
        
        self.label_damage = QLabel(self)
        self.label_damage.setText("ダメージ")
        self.label_boss_damage = QLabel(self)
        self.label_boss_damage.setText("ボスダメージ")
        self.label_element_ig = QLabel(self)
        self.label_element_ig.setText("属性耐性無視")
        self.label_boss_def = QLabel(self)
        self.label_boss_def.setText("ボス:防御率")
        self.label_crit = QLabel(self)
        self.label_crit.setText("クリティカル率: 100%")
        self.label_crit_dam = QLabel(self)
        self.label_crit_dam.setText("クリティカルダメージ")
        self.label_skill_dam = QLabel(self)
        self.label_skill_dam.setText("スキルダメージ")
        self.label_t = QLabel(self)
        self.label_t.setText("スキル攻撃回数")
        self.label_def_a = QLabel(self)
        self.label_def_a.setText("防御率無視")
        self.label_skill_def_a = QLabel(self)
        self.label_skill_def_a.setText("SKILL防御率無視")
        self.label_final_dam = QLabel(self)
        self.label_final_dam.setText("最終ダメージ")
        self.label_profic = QLabel(self)
        self.label_profic.setText("熟練度")

        self.label_level = QLabel(self)
        self.label_level.setText("レベル補正")
        self.label_arcane_symbol = QLabel(self)
        self.label_arcane_symbol.setText("アーケインシンボル")
        self.label_arpaca = QLabel(self)
        self.label_arpaca.setText("%")
        self.label_authentic_symbol = QLabel(self)
        self.label_authentic_symbol.setText("オーセンティックシンボル")

    #LineEdit
        self.wepon_coe_li = QLineEdit()
        w_l_v = QDoubleValidator()
        w_l_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        w_l_v.setTop(10.00)
        w_l_v.setDecimals(2)
        self.wepon_coe_li.setValidator(w_l_v)
        self.wepon_coe_li.setText("1.44")

        self.main_st_li = QLineEdit()
        st_l_v = QDoubleValidator()
        st_l_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        st_l_v.setTop(100000)
        st_l_v.setDecimals(0)
        self.main_st_li.setValidator(st_l_v)
        self.main_st_ba_li = QLineEdit()
        self.main_st_ba_li.setValidator(st_l_v)
        self.main_st_ba_li.setFixedWidth(40)
        self.main_st_per_li = QLineEdit()
        self.main_st_per_li.setValidator(st_l_v)
        self.main_st_per_li.setFixedWidth(40)
        self.main_st_n_per_li = QLineEdit()
        self.main_st_n_per_li.setValidator(st_l_v)
        self.main_st_n_per_li.setFixedWidth(40)

        self.sub_st_li = QLineEdit()
        self.sub_st_li.setValidator(st_l_v)
        self.sub_st_ba_li = QLineEdit()
        self.sub_st_ba_li.setValidator(st_l_v)
        self.sub_st_ba_li.setFixedWidth(40)
        self.sub_st_per_li = QLineEdit()
        self.sub_st_per_li.setValidator(st_l_v)
        self.sub_st_per_li.setFixedWidth(40)              
        self.sub_st_n_per_li = QLineEdit()
        self.sub_st_n_per_li.setValidator(st_l_v)
        self.sub_st_n_per_li.setFixedWidth(40)

        self.a_ma_li = QLineEdit()
        self.a_ma_li.setValidator(st_l_v)
        self.a_ma_ba_li = QLineEdit()
        self.a_ma_ba_li.setValidator(st_l_v)
        self.a_ma_ba_li.setFixedWidth(40)
        self.a_ma_per_li = QLineEdit()
        self.a_ma_per_li.setValidator(st_l_v)
        self.a_ma_per_li.setFixedWidth(40)
        self.a_ma_n_per_li = QLineEdit()
        self.a_ma_n_per_li.setValidator(st_l_v)
        self.a_ma_n_per_li.setFixedWidth(40)

        self.damage_li = QLineEdit()
        dam_v = QDoubleValidator()
        dam_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        dam_v.setTop(1000)
        dam_v.setDecimals(0)
        self.damage_li.setValidator(dam_v)

        self.boss_damage_li = QLineEdit()
        self.boss_damage_li.setValidator(dam_v)

        self.element_ig_li = QLineEdit()
        el_v = QDoubleValidator()
        el_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        el_v.setTop(100)
        el_v.setDecimals(0)
        self.element_ig_li.setValidator(el_v)

        self.crit_li = QLineEdit()
        self.crit_li.setText("100")
        self.crit_li.setReadOnly(True)

        self.crit_dam_li = QLineEdit()
        self.crit_dam_li.setValidator(dam_v)

        self.skill_dam_li = QLineEdit()
        sd_v = QDoubleValidator()
        sd_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        sd_v.setTop(10000)
        sd_v.setDecimals(0)
        self.skill_dam_li.setValidator(sd_v)

        self.numb_t_li = QLineEdit()
        nut_v = QDoubleValidator()
        nut_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        nut_v.setTop(100)
        nut_v.setDecimals(0)
        self.numb_t_li.setValidator(nut_v)

        self.def_a_li = QLineEdit()
        def_v = QDoubleValidator()
        def_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        def_v.setTop(100)
        def_v.setDecimals(2)
        self.def_a_li.setValidator(def_v)

        self.skill_de_att_li = QLineEdit()
        self.skill_de_att_li.setValidator(def_v)

        self.fainal_dam_li = QLineEdit()
        f_v = QDoubleValidator()
        f_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        f_v.setTop(1000)
        f_v.setDecimals(2)
        self.fainal_dam_li.setValidator(f_v)

        self.profic_li = QLineEdit()
        profic_v = QDoubleValidator()
        profic_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        profic_v.setTop(100)
        profic_v.setDecimals(2)
        self.profic_li.setValidator(profic_v)
        self.profic_li.setText("90")

        self.attack_damage_li = QLineEdit()
        self.attack_damage_li.setReadOnly(True)

        self.stat_li = QLineEdit()
        self.stat_li.setReadOnly(True)
        self.combatstat_li = QLineEdit()
        self.combatstat_li.setReadOnly(True)
    #コンボックス
        self.combobox = QComboBox(self)
        self.combobox.setEditable(False)
        self.combobox.setFixedSize(200, 30)
        self.combobox.addItem("Hero")
        self.combobox.addItem("Paladin")
        self.combobox.addItem("DarkNight")
        self.combobox.addItem("SoulMaster")
        self.combobox.addItem("Aran")
        self.combobox.addItem("DemonSlayer")
        self.combobox.addItem("DemonAvenger")
        self.combobox.addItem("Kaiser")
        self.combobox.addItem("Hayato")
        self.combobox.addItem("Zero")
        self.combobox.addItem("Michael")
        self.combobox.addItem("Blaster")
        self.combobox.addItem("Adel")
        self.combobox.addItem("IceLightning")
        self.combobox.addItem("FirePoison")
        self.combobox.addItem("Bishop")
        self.combobox.addItem("FlameWizard")
        self.combobox.addItem("BattleMage")
        self.combobox.addItem("Evan")
        self.combobox.addItem("Luminous")
        self.combobox.addItem("Kanna")
        self.combobox.addItem("Kinesis")
        self.combobox.addItem("Illium")
        self.combobox.addItem("Lara")
        self.combobox.addItem("Lynn")
        self.combobox.addItem("Bowmaster")
        self.combobox.addItem("Crossbowmaster")
        self.combobox.addItem("Pathfinder")
        self.combobox.addItem("Windshooter")
        self.combobox.addItem("WildHunter")
        self.combobox.addItem("Mercedes")
        self.combobox.addItem("Cain")
        self.combobox.addItem("Shadow")
        self.combobox.addItem("KnightLord")
        self.combobox.addItem("DualBlade")
        self.combobox.addItem("NightWalker")
        self.combobox.addItem("Zenon")
        self.combobox.addItem("PhantomThief")
        self.combobox.addItem("Cadena")
        self.combobox.addItem("Torakage")
        self.combobox.addItem("Kali")
        self.combobox.addItem("Viper")
        self.combobox.addItem("Captain")
        self.combobox.addItem("CannonShooter")
        self.combobox.addItem("Striker")
        self.combobox.addItem("Mechanic")
        self.combobox.addItem("HiddenMoon")
        self.combobox.addItem("AngelicBuster")
        self.combobox.addItem("Arc")
        self.combobox.addItem("Ren")


    #スピンボックス
        self.level_sp = QSpinBox(self)
        self.level_sp.setMinimum(-5)
        self.level_sp.setMaximum(+5)
        self.level_sp.setValue(0)
        self.level_li = QLineEdit()
        self.level_li.setText("1.1")
        self.level_li.hide()
        self.level_sp.valueChanged.connect(self.level_dia)



        self.arca_sp = QSpinBox(self)
        self.arca_sp.setMinimum(-500)
        self.arca_sp.setMaximum(+1000)
        self.arca_sp.setValue(100)
        self.arca_sp.valueChanged.connect(self.arca_dia)



        self.aut_sp = QSpinBox(self)
        self.aut_sp.setMinimum(-500)
        self.aut_sp.setMaximum(+1000)
        self.aut_sp.setValue(0)
        self.aut_sp.valueChanged.connect(self.aut_dia)


    #Zero
        self.al_ra = QRadioButton("Alpha")
        self.be_ra = QRadioButton("Beta")
        self.al_ra.setChecked(False)

        self.albe_group = QButtonGroup(self)
        self.albe_group.addButton(self.al_ra)
        self.albe_group.addButton(self.be_ra)
    #arca/aut
        self.arca_ra = QRadioButton("アーケイン")
        self.aut_ra = QRadioButton("オーセンティック")
        self.arca_ra.setChecked(True)

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.arca_ra)
        self.button_group.addButton(self.aut_ra)
    #ボス防御率
        self.boss_def = QComboBox(self)
        self.boss_def.setEditable(False)
        self.boss_def.addItem("300")
        self.boss_def.addItem("330")
        self.boss_def.addItem("380")

    #ボタン
        self.calc_dam_butt = QPushButton(self)
        self.calc_dam_butt.setText("計算: ダメージ")

        self.stat_butt = QPushButton(self)
        self.stat_butt.setText("計算: 表記ステータス")
        self.combatstat_butt = QPushButton(self)
        self.combatstat_butt.setText("計算: 戦闘力          ")
    #Grid　追加
        layout.addWidget(self.combobox, 0,0)
        layout.addWidget(self.label_wepon_coe, 1,0)

        layout.addWidget(self.label_main_st,  2,0)
        layout.addWidget(self.label_main_st_ba,  2,2)
        layout.addWidget(self.label_main_st_per,  2,4)
        layout.addWidget(self.label_main_st_n_per,  2,6)

        layout.addWidget(self.label_sub_st, 3,0)
        layout.addWidget(self.label_sub_st_ba, 3,2)
        layout.addWidget(self.label_sub_st_per, 3,4)
        layout.addWidget(self.label_sub_st_n_per, 3,6)
        
        layout.addWidget(self.label_a_ma, 4,0)
        layout.addWidget(self.label_a_ma_ba, 4,2)
        layout.addWidget(self.label_a_ma_per, 4,4)
        layout.addWidget(self.label_a_ma_n_per, 4,6)
        
        layout.addWidget(self.label_damage, 5,0)
        layout.addWidget(self.label_boss_damage, 6,0)
        layout.addWidget(self.label_element_ig, 7,0)
        layout.addWidget(self.label_boss_def, 8,0)
        layout.addWidget(self.label_crit, 9,0)
        layout.addWidget(self.label_crit_dam, 10,0)
        layout.addWidget(self.label_skill_dam,11,0)
        layout.addWidget(self.label_t,12,0)
        layout.addWidget(self.label_def_a,13,0)
        layout.addWidget(self.label_skill_def_a,14,0)
        layout.addWidget(self.label_final_dam,15,0)
        layout.addWidget(self.label_profic,16,0)
        layout.addWidget(self.calc_dam_butt,17,0)
        layout.addWidget(self.stat_butt,16,8)
        layout.addWidget(self.combatstat_butt,17,8)

    #数値入力ボックス　の追加
        layout.addWidget(self.wepon_coe_li, 1,1)

        layout.addWidget(self.main_st_li, 2,1)
        layout.addWidget(self.main_st_ba_li, 2,3)
        layout.addWidget(self.main_st_per_li, 2,5)
        layout.addWidget(self.main_st_n_per_li, 2,7)
        
        layout.addWidget(self.sub_st_li, 3,1)
        layout.addWidget(self.sub_st_ba_li, 3,3)
        layout.addWidget(self.sub_st_per_li, 3,5)
        layout.addWidget(self.sub_st_n_per_li, 3,7)
        
        layout.addWidget(self.a_ma_li, 4,1)
        layout.addWidget(self.a_ma_ba_li, 4,3)
        layout.addWidget(self.a_ma_per_li, 4,5)
        layout.addWidget(self.a_ma_n_per_li, 4,7)

        layout.addWidget(self.damage_li, 5,1)
        layout.addWidget(self.boss_damage_li, 6,1)
        layout.addWidget(self.element_ig_li, 7,1)
        layout.addWidget(self.boss_def, 8,1)
        layout.addWidget(self.crit_li, 9,1)
        layout.addWidget(self.crit_dam_li, 10,1)
        layout.addWidget(self.skill_dam_li, 11,1)
        layout.addWidget(self.numb_t_li, 12,1)
        layout.addWidget(self.def_a_li, 13,1)
        layout.addWidget(self.skill_de_att_li, 14,1)
        layout.addWidget(self.fainal_dam_li, 15,1)
        layout.addWidget(self.profic_li, 16,1)
        layout.addWidget(self.attack_damage_li, 17,1)
        layout.addWidget(self.stat_li, 16,9)
        layout.addWidget(self.combatstat_li, 17,9)

    #オプション
        layout.addWidget(self.label_level, 1,8)
        layout.addWidget(self.level_sp, 1,9)
        layout.addWidget(self.label_arcane_symbol, 2,8)
        layout.addWidget(self.arca_sp, 2,9)
        layout.addWidget(self.label_arpaca, 2,10)
        layout.addWidget(self.label_authentic_symbol, 3,8)
        layout.addWidget(self.aut_sp, 3,9)

        layout.addWidget(self.arca_ra, 4,8)
        layout.addWidget(self.aut_ra, 4,9)

        layout.addWidget(self.al_ra, 5,8)
        layout.addWidget(self.be_ra, 5,9)

        layout.addWidget(self.s_window_open, 6,8)
        layout.addWidget(self.t_window_open, 6,9)

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

        self.wepon_coe_li.setStyleSheet(lineStyle)
        self.main_st_li.setStyleSheet(lineStyle)
        self.sub_st_li.setStyleSheet(lineStyle)
        self.a_ma_li.setStyleSheet(lineStyle)
        self.damage_li.setStyleSheet(lineStyle)
        self.boss_damage_li.setStyleSheet(lineStyle)
        self.element_ig_li.setStyleSheet(lineStyle)
        self.crit_li.setStyleSheet(lineStyle)
        self.crit_dam_li.setStyleSheet(lineStyle)
        self.skill_dam_li.setStyleSheet(lineStyle)
        self.numb_t_li.setStyleSheet(lineStyle)
        self.def_a_li.setStyleSheet(lineStyle)
        self.skill_de_att_li.setStyleSheet(lineStyle)
        self.fainal_dam_li.setStyleSheet(lineStyle)
        self.profic_li.setStyleSheet(lineStyle)
        self.attack_damage_li.setStyleSheet(lineStyle)

        self.boss_def.setStyleSheet(lineStyle)

        self.setLayout(layout)

    #職業選択処理
        #select_job = self.combobox.currentText()
        #wepon_coe_li.setText(str(job_wepon_coe[select_job]))
        #profic_li.SSSsetText(str(job_profic[select_job]))

        self.combobox.activated.connect(self.combo_set)

    #ZERO_アルファ_ベータ選択
        self.al_ra.setEnabled(False)
        self.be_ra.setEnabled(False)
        self.al_ra.clicked.connect(lambda: on_radio_al())
        self.be_ra.clicked.connect(lambda: on_radio_be())

        def on_radio_al():
            if (self.select_job == "Zero"):
                self.wepon_coe_li.setText("1.34")
        def on_radio_be():
            if (self.select_job == "Zero"):
                self.wepon_coe_li.setText("1.49")

    #arca/aut 選択処理
        self.arca_ra.clicked.connect(lambda: arca_set())
        self.aut_ra.clicked.connect(lambda: arca_set())

        def arca_set():
            arca_aut = 1
        def aut_set():
            arca_aut = 2

    #数値変更で変数の数値を変更する

        self.main_st_ba_li.textChanged.connect(self.per_main_st)
        self.sub_st_ba_li.textChanged.connect(self.per_sub_st)
        self.a_ma_ba_li.textChanged.connect(self.per_a_ma)

        self.main_st_per_li.textChanged.connect(self.per_main_st)
        self.sub_st_per_li.textChanged.connect(self.per_sub_st)
        self.a_ma_per_li.textChanged.connect(self.per_a_ma)

        self.main_st_n_per_li.textChanged.connect(self.per_main_st)
        self.sub_st_n_per_li.textChanged.connect(self.per_sub_st)
        self.a_ma_n_per_li.textChanged.connect(self.per_a_ma)

        self.wepon_coe = is_input(1.44)
        self.wepon_coe_li.textChanged.connect(lambda new_text: self.is_input_str('wepon_coe', False, new_text))

        self.main_st = is_input(self.main_st_li.text().strip())
        self.main_st_li.textChanged.connect(lambda new_text: self.is_input_str('main_st', False,  new_text))

        self.sub_st = is_input(self.sub_st_li.text().strip())
        self.sub_st_li.textChanged.connect(lambda new_text: self.is_input_str('sub_st', False, new_text))

        self.a_ma = is_input(self.a_ma_li.text().strip())
        self.a_ma_li.textChanged.connect(lambda new_text: self.is_input_str('a_ma', False, new_text))

        self.damage = is_input(self.damage_li.text().strip())
        self.damage_li.textChanged.connect(lambda new_text: self.is_input_str('damage', True, new_text))

        self.boss_damage= is_input(self.boss_damage_li.text().strip())
        self.boss_damage_li.textChanged.connect(lambda new_text: self.is_input_str('boss_damage', True, new_text))

        self.element_ig = is_input(self.element_ig_li.text().strip())
        self.element_ig_li.textChanged.connect(lambda new_text: self.is_input_str('element_ig', True, new_text))

        self.crit_dam = is_input(self.crit_dam_li.text().strip())
        self.crit_dam_li.textChanged.connect(lambda new_text: self.is_input_str('crit_dam', True, new_text))

        self.skill_dam = is_input(self.skill_dam_li.text().strip())
        self.skill_dam_li.textChanged.connect(lambda new_text: self.is_input_str('skill_dam', True, new_text))

        self.numb_t = is_input(self.numb_t_li.text().strip())
        self.numb_t_li.textChanged.connect(lambda new_text: self.is_input_str('numb_t', False, new_text))

        self.def_a = is_input(self.def_a_li.text().strip())
        self.def_a_li.textChanged.connect(self.def_calc)

        self.skill_de_att = is_input(self.skill_de_att_li.text().strip())
        self.skill_de_att_li.textChanged.connect(self.def_calc)

        self.fainal_dam = is_input(self.fainal_dam_li.text().strip())
        self.fainal_dam_li.textChanged.connect(lambda new_text: self.is_input_str('fainal_dam', True, new_text))

        self.profic = is_input(0.9)
        self.profic_li.textChanged.connect(lambda new_text: self.is_input_str('profic', True, new_text))

        self.mons_def = is_input(3.0)
        self.boss_def.currentTextChanged.connect(lambda new_text: self.is_input_str('mons_def', True, new_text))

        self.higai_li  = is_input(1.0)
        self.ukerudam_li   = is_input(1.0)

        self.select_job = "Hero"

    #値の設定
        self.element_def_const = 50/100

    #初期化
        self.attack_damage = is_input(0)
        self.dam_calc
        self.format_damage()

        self.level_dia_c = (1.1)
        self.attack_damage = is_input(self.attack_damage_li.text().strip())

        self.s_window_open.clicked.connect(self.open_second_window)
        self.t_window_open.clicked.connect(self.open_Third_window)


    #計算処理
        self.calc_dam_butt.pressed.connect(self.calc)

        self.stat_butt.pressed.connect(self.stat_calc)

        self.combatstat_butt.pressed.connect(self.combatstat_calc)

    #timer
        start_time = time.perf_counter()
        self.format_damage()
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        #print(f"処理にかかった時間: {elapsed_time:.8f} 秒")


    def open_second_window(self):
        self.second_window = GUI_calc_swindow.SecondWindow(parent_window=self)
        self.second_window.show()

    def open_Third_window(self):        
        if(self.select_job == "Ren"):
            self.Third_window = Ren_calc_twindow.SecondWindow(parent_window=self)
        else:
            self.Third_window = HEXA_calc_twindow.SecondWindow(parent_window=self)
        self.Third_window.show()



    #%適用
    def per_main_st(self):
        ba = is_input(self.main_st_ba_li.text().strip())
        per = is_input(self.main_st_per_li.text().strip())
        n_per = is_input(self.main_st_n_per_li.text().strip())


        self.main_st_li.setText(str(n_per + round((per/100+1) * ba)))

    def per_sub_st(self):
        ba = is_input(self.sub_st_ba_li.text().strip())
        per = is_input(self.sub_st_per_li.text().strip())
        n_per = is_input(self.sub_st_n_per_li.text().strip())


        self.sub_st_li.setText(str(n_per + round((per/100+1) * ba)))

    def per_a_ma(self):
        ba = is_input(self.a_ma_ba_li.text().strip())
        per = is_input(self.a_ma_per_li.text().strip())
        n_per = is_input(self.a_ma_n_per_li.text().strip())


        self.a_ma_li.setText(str(n_per + round((per/100+1) * ba)))

    #オプションメソッド
    def level_dia(self):
        #レベル処理
        level_vari = self.level_sp.value()
        if(level_vari == 0):
            level_dia = 1.1
        elif(level_vari>=1 and level_vari<=4):
            level_dia = 1.1
            level_dia += (level_vari)*0.02
        elif(level_vari == 5):
            level_dia = 1.2
        elif(level_vari == -1):
            level_dia = 1.053
        elif(level_vari == -2):
            level_dia = 1.007
        elif(level_vari == -3):
            level_dia = 0.962
        elif(level_vari == -4):
            level_dia = 0.918
        elif(level_vari<=-5):
            level_dia = 0.875
            level_dia -= (level_vari-5)*2.5
        else:
            level_dia = 1.1
        self.level_li.setText(str(level_dia))
        self.level_dia_c = level_dia

    def arca_dia(self):
        arca  = self.arca_sp.value()
        if(arca<=10):
            mons_ageru_higai = 0.1
        elif(arca<=29):
            mons_ageru_higai = 0.3
        elif(arca<=49):
            mons_ageru_higai = 0.6
        elif(arca<=69):
            mons_ageru_higai = 0.7
        elif(arca<=99):
            mons_ageru_higai = 0.8
        elif(arca<=109):
            mons_ageru_higai = 1
        elif(arca<=129):
            mons_ageru_higai = 1.1
        elif(arca<=149):
            mons_ageru_higai = 1.3
        elif(arca>=150):
            mons_ageru_higai = 1.5
        else:
            mons_ageru_higai = 1.0
        self.higai_li = mons_ageru_higai

    def aut_dia(self):
        orce = self.aut_sp.value()
        if(orce<=-91):
            mons_ukeru_dam = 0.05
        elif(orce>=50):
            mons_ukeru_dam = 1.25
        elif(orce>=0):
            orce = math.floor(orce*0.1)
            mons_ukeru_dam = 1+(orce*0.1*0.5)
        elif(orce>=-90):
            orce = math.floor(orce*0.1)
            mons_ukeru_dam = 1+(orce*0.1)
        else:
            mons_ukeru_dam = 1.0
        self.ukerudam_li = mons_ukeru_dam

    def combo_set(self):
        self.select_job = self.combobox.currentText()
        self.wepon_coe_li.setText(str(self.job_wepon_coe[self.select_job]))
        self.profic_li.setText(str(self.job_profic[self.select_job]))

        if (self.select_job == "Zero"):
            self.al_ra.setEnabled(True)
            self.be_ra.setEnabled(True)
            if (self.al_ra.isChecked()):
                self.wepon_coe_li.setText("1.34")
            if (self.be_ra.isChecked()):
                self.wepon_coe_li.setText("1.49")
        else:
            self.al_ra.setEnabled(False)
            self.be_ra.setEnabled(False)


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

    def calc(self):
        self.setUpdatesEnabled(False)
        start_time = time.perf_counter()

        arorn_is  = self.arca_ra.isChecked()
        if(arorn_is == True):
            mons_ageru_higai  = self.higai_li
            mons_ukeru_dam = 1.0
        else:
            mons_ukeru_dam  = self.ukerudam_li
            mons_ageru_higai = 1.0
        #print(mons_ukeru_dam)
        #///////////////////
        self.dam_calc()
        #print(self.attack_damage)
        #print(self.level_dia_c)
        if(self.attack_damage<0):
            self.attack_damage = 0
        else:
            self.attack_damage = self.attack_damage * self.level_dia_c * mons_ageru_higai * mons_ukeru_dam
            self.attack_damage = self.attack_damage*self.numb_t
            self.attack_damage = round(self.attack_damage)
        #print(self.attack_damage)
        self.format_damage()
        print(self.damage_text)
        #self.print_check()
        #attack_damage = attack_damage * self.level_dia_c * mons_ageru_higai * mons_ukeru_dam
        #self.attack_damage_li.setText(self.damage_text)
        self.attack_damage_li.repaint()
        self.setUpdatesEnabled(True)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        #print(f"処理にかかった時間: {elapsed_time:.8f} 秒")

    def def_calc(self):
        self.def_a = is_input(self.def_a_li.text().strip())
        self.skill_de_att = is_input(self.skill_de_att_li.text().strip())
        self.def_a = 1- (1-self.def_a/100) * (1-self.skill_de_att/100)

    def dam_calc(self):
        mons_def = (1-self.mons_def*(1-self.def_a))
        #print(self.mons_def)
        self.attack_damage = (
        self.wepon_coe * (self.main_st*4 + self.sub_st) * (self.a_ma/100) *(1 + self.damage + self.boss_damage) * (1-(self.element_def_const-self.element_ig)) *
        (1.35 + self.crit_dam) * self.skill_dam * (mons_def) * (1 + self.fainal_dam) * self.profic )


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
        self.attack_damage_li.setText(self.damage_text)


    def print_check(self):
        print(self.wepon_coe)
        print(self.main_st)
        print(self.sub_st)
        print(self.a_ma)
        print(self.damage)
        print(self.boss_damage)
        #print(element_def)
        print(self.element_ig)
        print(self.crit_dam)
        print(self.skill_dam)
        print(self.mons_def)
        print(self.def_a)
        print(self.fainal_dam)
        print(self.profic)
        print(self.level_dia_c)
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


if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    app = QApplication(sys.argv)    # PySide6の実行
    window = MainWindow()           # ユーザがコーディングしたクラス

    app.setStyle("Fusion")  # 他のスタイルも試せます
    # ダークカラーパレットの設定
    pal = QPalette()
    pal.setColor(QPalette.ColorRole.Window, QColor("#121212"))
    pal.setColor(QPalette.ColorRole.WindowText, QColor("#FFFFFF"))
    pal.setColor(QPalette.ColorRole.Base, QColor("#1E1E1E"))
    pal.setColor(QPalette.ColorRole.Text, QColor("#FFFFFF"))
    pal.setColor(QPalette.ColorRole.Button, QColor("#2A2A2A"))
    pal.setColor(QPalette.ColorRole.ButtonText, QColor("#FFFFFF"))
    pal.setColor(QPalette.ColorRole.Highlight, QColor("#3D6DEB"))
    pal.setColor(QPalette.ColorRole.HighlightedText, QColor("#FFFFFF"))

    app.setPalette(pal)
#//////////////////
    window.show()                   # PySide6のウィンドウを表示
    sys.exit(app.exec())            # PySide6の終了
