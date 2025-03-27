from PyQt5 import QtCore, QtGui, QtWidgets

from tools import *


class Ui_Regulator(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_Regulator, self).__init__()
        self.setupUi(self)

    def setupUi(self, Regulator):
        Regulator.setObjectName("Regulator")
        Regulator.resize(819, 490)
        Regulator.setWindowTitle("ALR")

        # 提示框相关
        self.tip_box = QtWidgets.QGroupBox(Regulator)
        self.tip_box.setGeometry(QtCore.QRect(10, 10, 801, 51))
        self.tip_box.setAccessibleDescription("")
        self.tip_box.setStyleSheet("font: 12pt \"宋体\";")
        self.tip_box.setObjectName("groupBox_4")
        self.tip_box.setTitle("选择项")

        self.label_ship = QtWidgets.QLabel(self.tip_box)
        self.label_ship.setGeometry(QtCore.QRect(60, 20, 121, 21))
        self.label_ship.setAccessibleDescription("")
        self.label_ship.setStyleSheet("")
        self.label_ship.setText("选择舰船")
        self.label_ship.setObjectName("label")

        self.label_p1 = QtWidgets.QLabel(self.tip_box)
        self.label_p1.setGeometry(QtCore.QRect(200, 20, 111, 21))
        self.label_p1.setAccessibleDescription("")
        self.label_p1.setStyleSheet("")
        self.label_p1.setText("一号机")
        self.label_p1.setObjectName("label_2")

        self.label_p2 = QtWidgets.QLabel(self.tip_box)
        self.label_p2.setGeometry(QtCore.QRect(320, 20, 121, 21))
        self.label_p2.setAccessibleDescription("")
        self.label_p2.setStyleSheet("")
        self.label_p2.setText("二号机")
        self.label_p2.setObjectName("label_3")

        self.label_p3 = QtWidgets.QLabel(self.tip_box)
        self.label_p3.setGeometry(QtCore.QRect(450, 20, 121, 21))
        self.label_p3.setAccessibleDescription("")
        self.label_p3.setStyleSheet("")
        self.label_p3.setText("三号机")
        self.label_p3.setObjectName("label_4")

        self.label_d1 = QtWidgets.QLabel(self.tip_box)
        self.label_d1.setGeometry(QtCore.QRect(580, 20, 61, 21))
        self.label_d1.setAccessibleDescription("")
        self.label_d1.setStyleSheet("")
        self.label_d1.setText("设备一")
        self.label_d1.setObjectName("label_5")

        self.label_d2 = QtWidgets.QLabel(self.tip_box)
        self.label_d2.setGeometry(QtCore.QRect(650, 20, 61, 21))
        self.label_d2.setAccessibleDescription("")
        self.label_d2.setStyleSheet("")
        self.label_d2.setText("设备二")
        self.label_d2.setObjectName("label_6")

        self.label_f = QtWidgets.QLabel(self.tip_box)
        self.label_f.setGeometry(QtCore.QRect(720, 20, 61, 21))
        self.label_f.setAccessibleDescription("")
        self.label_f.setStyleSheet("")
        self.label_f.setText("好感度")
        self.label_f.setObjectName("label_7")

        # 上僚舰框相关
        self.ship1_box = QtWidgets.QGroupBox(Regulator)
        self.ship1_box.setGeometry(QtCore.QRect(10, 60, 801, 61))
        self.ship1_box.setStyleSheet("font: 12pt \"宋体\";")
        self.ship1_box.setTitle("上僚舰")
        self.ship1_box.setObjectName("ship1_box")
        self.ship1 = QtWidgets.QComboBox(self.ship1_box)
        self.ship1.setGeometry(QtCore.QRect(60, 20, 121, 31))
        self.ship1.setCurrentText("")
        self.ship1.setObjectName("ship1")
        self.ship1.addItems(
            ['天城CV', '白龙', '信浓', '约克城II', '弗里茨·鲁梅', '契卡洛夫',
             '纳希莫夫海军上将', '企业', '香格里拉', '萨拉托加·改'])
        self.ship1.currentIndexChanged.connect(self.load_role_weapon)

        self.p11 = QtWidgets.QComboBox(self.ship1_box)
        self.p11.setGeometry(QtCore.QRect(190, 20, 121, 31))
        self.p11.setCurrentText("")
        self.p11.setObjectName("p11")

        self.p12 = QtWidgets.QComboBox(self.ship1_box)
        self.p12.setGeometry(QtCore.QRect(320, 20, 121, 31))
        self.p12.setCurrentText("")
        self.p12.setObjectName("p12")

        self.p13 = QtWidgets.QComboBox(self.ship1_box)
        self.p13.setGeometry(QtCore.QRect(450, 20, 121, 31))
        self.p13.setCurrentText("")
        self.p13.setObjectName("p13")

        self.d11 = QtWidgets.QComboBox(self.ship1_box)
        self.d11.setGeometry(QtCore.QRect(580, 20, 61, 31))
        self.d11.setAccessibleDescription("")
        self.d11.setCurrentText("液压")
        self.d11.setObjectName("d11")
        self.d11.addItems(['液压', '信标', '整备'])

        self.d12 = QtWidgets.QComboBox(self.ship1_box)
        self.d12.setGeometry(QtCore.QRect(650, 20, 61, 31))
        self.d12.setCurrentText("")
        self.d12.setObjectName("d12")
        self.d12.addItems(['液压', '信标', '整备'])

        self.f1 = QtWidgets.QComboBox(self.ship1_box)
        self.f1.setGeometry(QtCore.QRect(720, 20, 71, 31))
        self.f1.setAccessibleDescription("")
        self.f1.setCurrentText("200婚")
        self.f1.setObjectName("f1")
        self.f1.addItems(['200婚', '199婚', '100爱'])

        # 旗舰框相关
        self.ship2_box = QtWidgets.QGroupBox(Regulator)
        self.ship2_box.setGeometry(QtCore.QRect(10, 120, 801, 61))
        self.ship2_box.setAccessibleDescription("")
        self.ship2_box.setStyleSheet("font: 12pt \"宋体\";")
        self.ship2_box.setTitle("旗舰")
        self.ship2_box.setObjectName("ship2_box")

        self.ship2 = QtWidgets.QComboBox(self.ship2_box)
        self.ship2.setGeometry(QtCore.QRect(60, 20, 121, 31))
        self.ship2.setCurrentText("")
        self.ship2.setObjectName("ship2")
        self.ship2.addItems(
            ['信浓', '约克城II', '天城CV', '弗里茨·鲁梅', '白龙', '契卡洛夫',
             '纳希莫夫海军上将', '企业', '香格里拉', '萨拉托加·改'])
        self.ship2.currentIndexChanged.connect(self.load_role_weapon)

        self.p21 = QtWidgets.QComboBox(self.ship2_box)
        self.p21.setGeometry(QtCore.QRect(190, 20, 121, 31))
        self.p21.setCurrentText("")
        self.p21.setObjectName("p21")

        self.p22 = QtWidgets.QComboBox(self.ship2_box)
        self.p22.setGeometry(QtCore.QRect(320, 20, 121, 31))
        self.p22.setCurrentText("")
        self.p22.setObjectName("p22")


        self.p23 = QtWidgets.QComboBox(self.ship2_box)
        self.p23.setGeometry(QtCore.QRect(450, 20, 121, 31))
        self.p23.setCurrentText("")
        self.p23.setObjectName("p23")

        self.d21 = QtWidgets.QComboBox(self.ship2_box)
        self.d21.setGeometry(QtCore.QRect(580, 20, 61, 31))
        self.d21.setCurrentText("")
        self.d21.setObjectName("d21")
        self.d21.addItems(['液压', '信标', '整备'])

        self.d22 = QtWidgets.QComboBox(self.ship2_box)
        self.d22.setGeometry(QtCore.QRect(650, 20, 61, 31))
        self.d22.setCurrentText("")
        self.d22.setObjectName("d22")
        self.d22.addItems(['液压', '信标', '整备'])

        self.f2 = QtWidgets.QComboBox(self.ship2_box)
        self.f2.setGeometry(QtCore.QRect(720, 20, 71, 31))
        self.f2.setCurrentText("")
        self.f2.setObjectName("f2")
        self.f2.addItems(['200婚', '199婚', '100爱'])

        # 下僚舰相关
        self.ship3_box = QtWidgets.QGroupBox(Regulator)
        self.ship3_box.setGeometry(QtCore.QRect(10, 180, 801, 61))
        self.ship3_box.setAccessibleDescription("")
        self.ship3_box.setStyleSheet("font: 12pt \"宋体\";")
        self.ship3_box.setTitle("下僚舰")
        self.ship3_box.setObjectName("ship3_box")

        self.ship3 = QtWidgets.QComboBox(self.ship3_box)
        self.ship3.setGeometry(QtCore.QRect(60, 20, 121, 31))
        self.ship3.setAccessibleDescription("")
        self.ship3.setCurrentText("怨仇")
        self.ship3.setObjectName("ship3")
        self.ship3.addItem("怨仇")
        self.ship3.currentIndexChanged.connect(self.load_role_weapon)

        self.p31 = QtWidgets.QComboBox(self.ship3_box)
        self.p31.setGeometry(QtCore.QRect(190, 20, 121, 31))
        self.p31.setCurrentText("")
        self.p31.setObjectName("p31")

        self.p32 = QtWidgets.QComboBox(self.ship3_box)
        self.p32.setGeometry(QtCore.QRect(320, 20, 121, 31))
        self.p32.setCurrentText("")
        self.p32.setObjectName("p32")

        self.p33 = QtWidgets.QComboBox(self.ship3_box)
        self.p33.setGeometry(QtCore.QRect(450, 20, 121, 31))
        self.p33.setCurrentText("")
        self.p33.setObjectName("p33")

        self.d31 = QtWidgets.QComboBox(self.ship3_box)
        self.d31.setGeometry(QtCore.QRect(580, 20, 61, 31))
        self.d31.setCurrentText("")
        self.d31.setObjectName("d31")
        self.d31.addItems(['液压', '信标', '整备'])

        self.d32 = QtWidgets.QComboBox(self.ship3_box)
        self.d32.setGeometry(QtCore.QRect(650, 20, 61, 31))
        self.d32.setCurrentText("")
        self.d32.setObjectName("d32")
        self.d32.addItems(['液压', '信标', '整备'])

        self.f3 = QtWidgets.QComboBox(self.ship3_box)
        self.f3.setGeometry(QtCore.QRect(720, 20, 71, 31))
        self.f3.setCurrentText("")
        self.f3.setObjectName("f3")
        self.f3.addItems(['200婚', '199婚', '100爱'])

        # 跨队buff框相关
        self.buff_box = QtWidgets.QGroupBox(Regulator)
        self.buff_box.setGeometry(QtCore.QRect(10, 240, 801, 61))
        self.buff_box.setAccessibleDescription("")
        self.buff_box.setStyleSheet("font: 12pt \"宋体\";")
        self.buff_box.setTitle("跨队BUFF")
        self.buff_box.setObjectName("buff_box")

        self.role_buff = QtWidgets.QCheckBox(self.buff_box)
        self.role_buff.setGeometry(QtCore.QRect(60, 20, 341, 31))
        self.role_buff.setAccessibleDescription("")
        self.role_buff.setText("10级 空域辅助（独立/卡萨布兰卡/百眼巨人）")
        self.role_buff.setObjectName("role_buff")

        self.is_world = QtWidgets.QCheckBox(self.buff_box)
        self.is_world.setGeometry(QtCore.QRect(430, 20, 131, 31))
        self.is_world.setAccessibleDescription("")
        self.is_world.setText("大世界")
        self.is_world.setObjectName("is_world")

        # 猫和科技框相关
        self.other_box = QtWidgets.QGroupBox(Regulator)
        self.other_box.setGeometry(QtCore.QRect(10, 300, 801, 61))
        self.other_box.setAccessibleDescription("")
        self.other_box.setStyleSheet("font: 12pt \"宋体\";")
        self.other_box.setTitle("其它")
        self.other_box.setObjectName("other_box")

        self.neko_buff = QtWidgets.QCheckBox(self.other_box)
        self.neko_buff.setGeometry(QtCore.QRect(60, 20, 151, 31))
        self.neko_buff.setAccessibleDescription("")
        self.neko_buff.setText("30级参谋位毗沙丸")
        self.neko_buff.setObjectName("neko_buff")

        self.label_neko_reload = QtWidgets.QLabel(self.other_box)
        self.label_neko_reload.setGeometry(QtCore.QRect(230, 20, 161, 31))
        self.label_neko_reload.setAccessibleDescription("")
        self.label_neko_reload.setStyleSheet("")
        self.label_neko_reload.setText("猫装填词条（总数值）")
        self.label_neko_reload.setObjectName("label_8")

        self.neko_reload = QtWidgets.QLineEdit(self.other_box)
        self.neko_reload.setGeometry(QtCore.QRect(400, 20, 121, 31))
        self.neko_reload.setAccessibleDescription("")
        self.neko_reload.setText("0")
        self.neko_reload.setObjectName("neko_reload")

        self.label_tech_reload = QtWidgets.QLabel(self.other_box)
        self.label_tech_reload.setGeometry(QtCore.QRect(550, 20, 91, 31))
        self.label_tech_reload.setAccessibleDescription("")
        self.label_tech_reload.setStyleSheet("")
        self.label_tech_reload.setText("装填科技点")
        self.label_tech_reload.setObjectName("label_9")

        self.tech_reload = QtWidgets.QLineEdit(self.other_box)
        self.tech_reload.setGeometry(QtCore.QRect(660, 20, 121, 31))
        self.tech_reload.setAccessibleDescription("")
        self.tech_reload.setText("0")
        self.tech_reload.setObjectName("tech_reload")

        self.start_btn = QtWidgets.QPushButton(Regulator)
        self.start_btn.setGeometry(QtCore.QRect(10, 430, 801, 51))
        self.start_btn.setAccessibleDescription("")
        self.start_btn.setStyleSheet("font: 12pt \"宋体\";")
        self.start_btn.setObjectName("start_btn")
        self.start_btn.setText("开始调速")

        self.result_text = QtWidgets.QTextBrowser(Regulator)
        self.result_text.setGeometry(QtCore.QRect(10, 370, 801, 51))
        self.result_text.setAccessibleDescription("")
        self.result_text.setStyleSheet("font: 12pt \"宋体\";")
        self.result_text.setObjectName("result_text")

        self.start_btn.clicked.connect(self.deal_start)
        self.load_role_weapon()

    def deal_start(self):
        ship1, ship2, ship3 = [], [], []
        ship1.append(self.ship1.currentText())
        ship1.append(self.p11.currentText())
        ship1.append(self.p12.currentText())
        ship1.append(self.p13.currentText())
        ship1.append(self.d11.currentText())
        ship1.append(self.d12.currentText())
        ship1.append(self.f1.currentText())

        ship2.append(self.ship2.currentText())
        ship2.append(self.p21.currentText())
        ship2.append(self.p22.currentText())
        ship2.append(self.p23.currentText())
        ship2.append(self.d21.currentText())
        ship2.append(self.d22.currentText())
        ship2.append(self.f2.currentText())

        ship3.append(self.ship3.currentText())
        ship3.append(self.p31.currentText())
        ship3.append(self.p32.currentText())
        ship3.append(self.p33.currentText())
        ship3.append(self.d31.currentText())
        ship3.append(self.d32.currentText())
        ship3.append(self.f3.currentText())

        role_buff = self.role_buff.isChecked()
        is_world = self.is_world.isChecked()

        neko_buff = self.neko_buff.isChecked()
        neko_reload = self.neko_reload.text()
        tech_reload = self.tech_reload.text()

        result = deal_compute([ship1, ship2, ship3], role_buff, is_world, neko_buff, neko_reload, tech_reload)
        self.result_text.clear()
        self.result_text.setText(result)
        print(result)

    def load_role_weapon(self):
        ship = self.sender()
        if ship == self.ship1:
            self.p11.clear()
            self.p12.clear()
            self.p13.clear()
            reload_data, weapon_count, weapon_type = load_role_data(self.ship1.currentText())
            p1 = load_plane_name(weapon_type[0])
            for key, value in p1.items():
                self.p11.addItem(key)

            p2 = load_plane_name(weapon_type[1])
            for key, value in p2.items():
                self.p12.addItem(key)

            p3 = load_plane_name(weapon_type[2])
            for key, value in p3.items():
                self.p13.addItem(key)
        elif ship == self.ship2:
            self.p21.clear()
            self.p22.clear()
            self.p23.clear()
            reload_data, weapon_count, weapon_type = load_role_data(self.ship2.currentText())
            p1 = load_plane_name(weapon_type[0])
            for key, value in p1.items():
                self.p21.addItem(key)

            p2 = load_plane_name(weapon_type[1])
            for key, value in p2.items():
                self.p22.addItem(key)

            p3 = load_plane_name(weapon_type[2])
            for key, value in p3.items():
                self.p23.addItem(key)
        elif ship == self.ship3:
            self.p31.clear()
            self.p32.clear()
            self.p33.clear()
            reload_data, weapon_count, weapon_type = load_role_data(self.ship3.currentText())
            p1 = load_plane_name(weapon_type[0])
            for key, value in p1.items():
                self.p31.addItem(key)

            p2 = load_plane_name(weapon_type[1])
            for key, value in p2.items():
                self.p32.addItem(key)

            p3 = load_plane_name(weapon_type[2])
            for key, value in p3.items():
                self.p33.addItem(key)
        elif ship == None:
            self.p11.clear()
            self.p12.clear()
            self.p13.clear()
            reload_data, weapon_count, weapon_type = load_role_data(self.ship1.currentText())
            p1 = load_plane_name(weapon_type[0])
            for key, value in p1.items():
                self.p11.addItem(key)

            p2 = load_plane_name(weapon_type[1])
            for key, value in p2.items():
                self.p12.addItem(key)

            p3 = load_plane_name(weapon_type[2])
            for key, value in p3.items():
                self.p13.addItem(key)

            self.p21.clear()
            self.p22.clear()
            self.p23.clear()
            reload_data, weapon_count, weapon_type = load_role_data(self.ship2.currentText())
            p1 = load_plane_name(weapon_type[0])
            for key, value in p1.items():
                self.p21.addItem(key)

            p2 = load_plane_name(weapon_type[1])
            for key, value in p2.items():
                self.p22.addItem(key)

            p3 = load_plane_name(weapon_type[2])
            for key, value in p3.items():
                self.p23.addItem(key)

            self.p31.clear()
            self.p32.clear()
            self.p33.clear()
            reload_data, weapon_count, weapon_type = load_role_data(self.ship3.currentText())
            p1 = load_plane_name(weapon_type[0])
            for key, value in p1.items():
                self.p31.addItem(key)

            p2 = load_plane_name(weapon_type[1])
            for key, value in p2.items():
                self.p32.addItem(key)

            p3 = load_plane_name(weapon_type[2])
            for key, value in p3.items():
                self.p33.addItem(key)
