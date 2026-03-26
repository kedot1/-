GUI_calc mainwidow 	1つ目のwindow
GUI_calc_swindws 	TOOL
HEXA_calc_twindow	２つ目のwindow(HEXA)
GUI_calc_HEXA		モジュールの部分
Ren_calc_twindow	レン職業個別の部分(HEXA部分のプロトタイプ的なもの)

mainwindowを実行するとアプリを実行できる。

実行には、pythonとpyside6が必要だ。


stack
-Python
-Pyside6
-VScode

機能
-武器係数,熟練度反映
-ダメージ計算
-レベル、シンボルなどの補正
-HEXA スキル
-最終ダメージ比での比較
-防御率無視,最終ダメージ計算TOOL
-デーモンアヴェンジャー.ZENON　メインステータス計算
GUI_Desktop_App

tech
-スキルデータの辞書管理
-クラス、メソッドに分割しての再利用
-各マスタリー、enhance(強化コア)を分離することによる、機能拡張性（スキル追記）

