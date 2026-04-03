from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, QGridLayout, QTabWidget,QLineEdit
from PySide6.QtGui import QDoubleValidator
from GUI_calc import is_input
import math

class SecondWindow(QWidget):
    def __init__(self, parent_window, parent=None):
        super().__init__()
        self.setWindowTitle("Tools")

        self.main_window_ref = parent_window
    # ウィンドウサイズを指定（px単位）
        windowWidth = 800  # ウィンドウの横幅
        windowHeight = 200  # ウィンドウの高さ
    # ウィンドウサイズの変更
        self.setFixedSize(650, 300)
    #tab
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)  # タブバーの位置を設定（North, South, East, West）

        # タブを追加
        self.d_tab = QWidget()
        self.z_tab = QWidget()
        self.def_tab = QWidget()
        self.fainal_tab = QWidget()
        self.arca_tab = QWidget()
        tabs.addTab(self.d_tab, "デーモンアヴェンジャー計算機")
        tabs.addTab(self.z_tab, "ゼノン計算機")
        tabs.addTab(self.def_tab, "防御率無視計算機")
        tabs.addTab(self.fainal_tab, "最終ダメージ計算機")
        tabs.addTab(self.arca_tab, "アーケイン計算機")

        #d_a_tab
        d_layout = QGridLayout(self)
        self.d_tab.setLayout(d_layout)
        space = QLabel("")

        self.d_tab_a = QLabel("素の最大HP")
        self.d_tab_b = QLabel("加算された最大HP")
        self.d_tab_main_st = QPushButton("メインステータス")

        self.d_hp_li = QLineEdit()
        hp_v = QDoubleValidator()
        hp_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        hp_v.setTop(10000000000)
        hp_v.setDecimals(0)
        self.d_hp_li.setValidator(hp_v)

        self.d_hp_add_li = QLineEdit()
        self.d_hp_add_li.setValidator(hp_v)

        self.d_st_li = QLineEdit()
        self.d_st_li.setReadOnly(True)

        #self.z_tab
        z_layout = QGridLayout(self)
        self.z_tab.setLayout(z_layout)

        self.z_tab_s = QLabel("STR")
        self.z_tab_d = QLabel("DEX")
        self.z_tab_l = QLabel("LUK")
        self.z_tab_main_st = QPushButton("メインステータス")

        self.z_s_li = QLineEdit()
        st_v = QDoubleValidator()
        st_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        st_v.setTop(100000)
        st_v.setDecimals(0)
        self.z_s_li.setValidator(st_v)

        self.z_d_li = QLineEdit()
        self.z_d_li.setValidator(st_v)

        self.z_l_li = QLineEdit()
        self.z_l_li.setValidator(st_v)

        self.z_st_li = QLineEdit()
        self.z_st_li.setReadOnly(True)

        #self.def_tab
        def_layout = QGridLayout(self)
        self.def_tab.setLayout(def_layout)

        self.def_a_1 = QLabel("防御率無視1")
        self.def_a_2 = QLabel("防御率無視2")
        self.def_a_3 = QLabel("防御率無視3")
        self.def_a_4 = QLabel("防御率無視4")
        self.def_a_5 = QLabel("防御率無視5")
        self.def_a_sum = QPushButton("防御率無視の合計")

        self.def1_li = QLineEdit()
        def_v = QDoubleValidator()
        def_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        def_v.setTop(100)
        def_v.setDecimals(2)
        self.def1_li.setValidator(def_v)

        self.def2_li = QLineEdit()
        self.def2_li.setValidator(def_v)

        self.def3_li = QLineEdit()
        self.def3_li.setValidator(def_v)

        self.def4_li = QLineEdit()
        self.def4_li.setValidator(def_v)

        self.def5_li = QLineEdit()
        self.def5_li.setValidator(def_v)

        self.def_sum_li = QLineEdit()
        self.def_sum_li.setReadOnly(True)

        #self.fainal_tab
        f_layout = QGridLayout(self)
        self.fainal_tab.setLayout(f_layout)

        self.fi_1 = QLabel("最終ダメージ1")
        self.fi_2 = QLabel("最終ダメージ2")
        self.fi_3 = QLabel("最終ダメージ3")
        self.fi_4 = QLabel("最終ダメージ4")
        self.fi_5 = QLabel("最終ダメージ5")
        self.fi_sum = QPushButton("最終ダメージの合計")

        self.f1_li = QLineEdit()
        f_v = QDoubleValidator()
        f_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        f_v.setTop(500)
        f_v.setDecimals(2)
        self.f1_li.setValidator(f_v)

        self.f2_li = QLineEdit()
        self.f2_li.setValidator(f_v)

        self.f3_li = QLineEdit()
        self.f3_li.setValidator(f_v)

        self.f4_li = QLineEdit()
        self.f4_li.setValidator(f_v)

        self.f5_li = QLineEdit()
        self.f5_li.setValidator(f_v)

        self.f_sum_li = QLineEdit()
        self.f_sum_li.setReadOnly(True)

        #self.arca_tab
        arca_layout = QGridLayout(self)
        self.arca_tab.setLayout(arca_layout)

        self.arca_c = QLabel("保有アーケイン")
        self.arca_b = QLabel("要求アーケイン")

        self.arca_c_li = QLineEdit()
        a_v = QDoubleValidator()
        a_v.setNotation(QDoubleValidator.Notation.StandardNotation)
        a_v.setTop(1500)
        a_v.setDecimals(0)
        self.arca_c_li.setValidator(a_v)

        self.arca_b_li = QLineEdit()
        self.arca_b_li.setValidator(a_v)

        self.arca_a_li = QLineEdit()
        self.arca_a_li.setReadOnly(True)

        self.arca_tab_arca = QPushButton("アーケイン:%")
        #d_layout
        d_layout.setContentsMargins(10, 50, 10, 50)
        d_layout.addWidget(self.d_tab_a, 1,0)
        d_layout.addWidget(self.d_tab_b, 2,0)
        d_layout.addWidget(space, 3,0)
        d_layout.addWidget(self.d_tab_main_st, 4,0)

        d_layout.addWidget(self.d_hp_li, 1,1)
        d_layout.addWidget(self.d_hp_add_li, 2,1)
        d_layout.addWidget(space, 3,1)
        d_layout.addWidget(self.d_st_li, 4,1)

        #z_layout
        z_layout.setContentsMargins(10, 30, 10, 30)

        z_layout.addWidget(self.z_tab_s, 0,0)
        z_layout.addWidget(self.z_tab_d, 1,0)
        z_layout.addWidget(self.z_tab_l, 2,0)
        z_layout.addWidget(self.z_tab_main_st, 3,0)

        z_layout.addWidget(self.z_s_li, 0,1)
        z_layout.addWidget(self.z_d_li, 1,1)
        z_layout.addWidget(self.z_l_li, 2,1)
        z_layout.addWidget(self.z_st_li, 3,1)

        #def_layout
        def_layout.setContentsMargins(10, 10, 10, 10)

        def_layout.addWidget(self.def_a_1, 0,0)
        def_layout.addWidget(self.def_a_2, 1,0)
        def_layout.addWidget(self.def_a_3, 2,0)
        def_layout.addWidget(self.def_a_4, 3,0)
        def_layout.addWidget(self.def_a_5, 4,0)
        def_layout.addWidget(self.def_a_sum, 5,0)

        def_layout.addWidget(self.def1_li, 0,1)
        def_layout.addWidget(self.def2_li, 1,1)
        def_layout.addWidget(self.def3_li, 2,1)
        def_layout.addWidget(self.def4_li, 3,1)
        def_layout.addWidget(self.def5_li, 4,1)
        def_layout.addWidget(self.def_sum_li, 5,1)

        #final_layout
        f_layout.setContentsMargins(10, 10, 10, 10)

        f_layout.addWidget(self.fi_1, 0,0)
        f_layout.addWidget(self.fi_2, 1,0)
        f_layout.addWidget(self.fi_3, 2,0)
        f_layout.addWidget(self.fi_4, 3,0)
        f_layout.addWidget(self.fi_5, 4,0)
        f_layout.addWidget(self.fi_sum, 5,0)

        f_layout.addWidget(self.f1_li, 0,1)
        f_layout.addWidget(self.f2_li, 1,1)
        f_layout.addWidget(self.f3_li, 2,1)
        f_layout.addWidget(self.f4_li, 3,1)
        f_layout.addWidget(self.f5_li, 4,1)
        f_layout.addWidget(self.f_sum_li, 5,1)

        #arca_layout
        arca_layout.setContentsMargins(10, 30, 10, 30)
        arca_layout.addWidget(self.arca_c, 0,0)
        arca_layout.addWidget(self.arca_b, 1,0)
        arca_layout.addWidget(self.arca_tab_arca, 2,0)

        arca_layout.addWidget(self.arca_c_li, 0,1)
        arca_layout.addWidget(self.arca_b_li, 1,1)
        arca_layout.addWidget(self.arca_a_li, 2,1)

    #tab_layout
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        self.setLayout(layout)
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
                border: 1px solid Blue; /* フォーカス時の枠線 */
            }
        """
        d_layout.setSpacing(5)

        self.d_tab_main_st.pressed.connect(self.st_calc)

        self.z_tab_main_st.pressed.connect(self.zst_calc)

        self.def_a_sum.pressed.connect(self.def_a_calc)

        self.fi_sum.pressed.connect(self.final_calc)

        self.arca_tab_arca.pressed.connect(self.arca_calc)

    def st_calc(self):
        maxHP = is_input(self.d_hp_li.text().strip())
        addHP = is_input(self.d_hp_add_li.text().strip())
        d_st = (maxHP + addHP*0.8)/7

        d_st = round(d_st)
        self.d_st_li.setText(str(d_st))

    def zst_calc(self):
        st_str = is_input(self.z_s_li.text().strip())
        #st_str = is_input(self.main_window_ref.main_st)
        st_dex = is_input(self.z_d_li.text().strip())
        st_luk = is_input(self.z_l_li.text().strip())
        z_st = st_str + st_dex + st_luk

        z_st = round(z_st)
        self.z_st_li.setText(str(z_st))

    def def_a_calc(self):

        def1 = is_input(self.def1_li.text().strip())
        def2 = is_input(self.def2_li.text().strip())
        def3 = is_input(self.def3_li.text().strip())
        def4 = is_input(self.def4_li.text().strip())
        def5 = is_input(self.def5_li.text().strip())

        out_def_att = 1-(1-(def1/100))*(1-(def2/100))*(1-(def3/100))*(1-(def4/100))*(1-(def5/100))
        out_def_att = round(out_def_att*100, 2)
        self.def_sum_li.setText(str(out_def_att))

    def final_calc(self):

        f1 = is_input(self.f1_li.text().strip())
        f2 = is_input(self.f2_li.text().strip())
        f3 = is_input(self.f3_li.text().strip())
        f4 = is_input(self.f4_li.text().strip())
        f5 = is_input(self.f5_li.text().strip())

        final_sum = (1 + f1/100)*(1 + f2/100)*(1 + f3/100)*(1 + f4/100)*(1 + f5/100) -1

        final_sum = round(final_sum*100, 2)
        self.f_sum_li.setText(str(final_sum))

    def arca_calc(self):

        self.arca_c = is_input(self.arca_c_li.text().strip())
        self.arca_b = is_input(self.arca_b_li.text().strip())
        if(self.arca_b==0):
            self.arca_b = 1

        arca_par = math.floor((self.arca_c/self.arca_b)*100)
        self.arca_a_li.setText(str(arca_par))