# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(473, 436)
        self.actionDiscord_chat = QAction(MainWindow)
        self.actionDiscord_chat.setObjectName(u"actionDiscord_chat")
        self.actionDiscord_chat.setCheckable(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setGeometry(QRect(0, 0, 471, 431))
        self.main_widget.setLayoutDirection(Qt.LeftToRight)
        self.main_widget.setAutoFillBackground(True)
        self.pokemon_pushButton = QPushButton(self.main_widget)
        self.pokemon_pushButton.setObjectName(u"pokemon_pushButton")
        self.pokemon_pushButton.setGeometry(QRect(40, 50, 81, 81))
        self.fish_pushButton = QPushButton(self.main_widget)
        self.fish_pushButton.setObjectName(u"fish_pushButton")
        self.fish_pushButton.setGeometry(QRect(200, 50, 81, 81))
        self.pokemon_progressBar = QProgressBar(self.main_widget)
        self.pokemon_progressBar.setObjectName(u"pokemon_progressBar")
        self.pokemon_progressBar.setGeometry(QRect(30, 130, 101, 23))
        self.pokemon_progressBar.setValue(0)
        self.pokemon_progressBar.setAlignment(Qt.AlignCenter)
        self.fish_progressBar = QProgressBar(self.main_widget)
        self.fish_progressBar.setObjectName(u"fish_progressBar")
        self.fish_progressBar.setGeometry(QRect(190, 130, 101, 23))
        self.fish_progressBar.setValue(0)
        self.fish_progressBar.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.main_widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 400, 221, 25))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.discord_chat_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.discord_chat_pushButton.setObjectName(u"discord_chat_pushButton")
        self.discord_chat_pushButton.setEnabled(True)

        self.horizontalLayout.addWidget(self.discord_chat_pushButton)

        self.discord_chat_x_y = QLabel(self.horizontalLayoutWidget)
        self.discord_chat_x_y.setObjectName(u"discord_chat_x_y")
        self.discord_chat_x_y.setCursor(QCursor(Qt.ForbiddenCursor))
        self.discord_chat_x_y.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.discord_chat_x_y)

        self.battle_progressBar = QProgressBar(self.main_widget)
        self.battle_progressBar.setObjectName(u"battle_progressBar")
        self.battle_progressBar.setGeometry(QRect(340, 130, 101, 23))
        self.battle_progressBar.setValue(0)
        self.battle_progressBar.setAlignment(Qt.AlignCenter)
        self.battle_pushButton = QPushButton(self.main_widget)
        self.battle_pushButton.setObjectName(u"battle_pushButton")
        self.battle_pushButton.setGeometry(QRect(350, 50, 81, 81))
        self.pokeball_widget = QWidget(self.centralwidget)
        self.pokeball_widget.setObjectName(u"pokeball_widget")
        self.pokeball_widget.setGeometry(QRect(0, 0, 471, 431))
        self.pokeball_widget.setVisible(False)
        self.pokeball_pushButton = QPushButton(self.pokeball_widget)
        self.pokeball_pushButton.setObjectName(u"pokeball_pushButton")
        self.pokeball_pushButton.setGeometry(QRect(40, 50, 81, 81))
        self.greatball_pushButton = QPushButton(self.pokeball_widget)
        self.greatball_pushButton.setObjectName(u"greatball_pushButton")
        self.greatball_pushButton.setGeometry(QRect(200, 50, 81, 81))
        self.ultraball_pushButton = QPushButton(self.pokeball_widget)
        self.ultraball_pushButton.setObjectName(u"ultraball_pushButton")
        self.ultraball_pushButton.setGeometry(QRect(360, 50, 81, 81))
        self.premierball_pushButton = QPushButton(self.pokeball_widget)
        self.premierball_pushButton.setObjectName(u"premierball_pushButton")
        self.premierball_pushButton.setGeometry(QRect(120, 160, 81, 81))
        self.masterball_pushButton = QPushButton(self.pokeball_widget)
        self.masterball_pushButton.setObjectName(u"masterball_pushButton")
        self.masterball_pushButton.setGeometry(QRect(280, 160, 81, 81))
        self.cancel_pushButton = QPushButton(self.pokeball_widget)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setGeometry(QRect(440, 400, 31, 31))
        self.pokeball_fish_widget = QWidget(self.centralwidget)
        self.pokeball_fish_widget.setObjectName(u"pokeball_fish_widget")
        self.pokeball_fish_widget.setGeometry(QRect(0, 0, 471, 431))
        self.pokeball_fish_widget.setVisible(False)
        self.pokeball_fish_pushButton = QPushButton(self.pokeball_fish_widget)
        self.pokeball_fish_pushButton.setObjectName(u"pokeball_fish_pushButton")
        self.pokeball_fish_pushButton.setGeometry(QRect(40, 180, 81, 81))
        self.greatball_fish_pushButton = QPushButton(self.pokeball_fish_widget)
        self.greatball_fish_pushButton.setObjectName(u"greatball_fish_pushButton")
        self.greatball_fish_pushButton.setGeometry(QRect(200, 180, 81, 81))
        self.ultraball_fish_pushButton = QPushButton(self.pokeball_fish_widget)
        self.ultraball_fish_pushButton.setObjectName(u"ultraball_fish_pushButton")
        self.ultraball_fish_pushButton.setGeometry(QRect(360, 180, 81, 81))
        self.premierball_fish_pushButton = QPushButton(self.pokeball_fish_widget)
        self.premierball_fish_pushButton.setObjectName(u"premierball_fish_pushButton")
        self.premierball_fish_pushButton.setGeometry(QRect(40, 290, 81, 81))
        self.masterball_fish_pushButton = QPushButton(self.pokeball_fish_widget)
        self.masterball_fish_pushButton.setObjectName(u"masterball_fish_pushButton")
        self.masterball_fish_pushButton.setGeometry(QRect(360, 290, 81, 81))
        self.pull_fish_pushButton = QPushButton(self.pokeball_fish_widget)
        self.pull_fish_pushButton.setObjectName(u"pull_fish_pushButton")
        self.pull_fish_pushButton.setGeometry(QRect(40, 40, 401, 81))
        self.cancel_fish_pushButton = QPushButton(self.pokeball_fish_widget)
        self.cancel_fish_pushButton.setObjectName(u"cancel_fish_pushButton")
        self.cancel_fish_pushButton.setGeometry(QRect(440, 400, 31, 31))
        self.diveball_fish_pushButton = QPushButton(self.pokeball_fish_widget)
        self.diveball_fish_pushButton.setObjectName(u"diveball_fish_pushButton")
        self.diveball_fish_pushButton.setGeometry(QRect(200, 290, 81, 81))
        self.battle_widget = QWidget(self.centralwidget)
        self.battle_widget.setObjectName(u"battle_widget")
        self.battle_widget.setGeometry(QRect(0, 0, 471, 431))
        self.battle_widget.setVisible(False)
        self.verticalLayoutWidget = QWidget(self.battle_widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 131, 311))
        self.gym_verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.gym_verticalLayout.setObjectName(u"gym_verticalLayout")
        self.gym_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gym_kanto_pushButton = QPushButton(self.verticalLayoutWidget)
        self.gym_kanto_pushButton.setObjectName(u"gym_kanto_pushButton")

        self.gym_verticalLayout.addWidget(self.gym_kanto_pushButton)

        self.gym_johto_pushButton = QPushButton(self.verticalLayoutWidget)
        self.gym_johto_pushButton.setObjectName(u"gym_johto_pushButton")

        self.gym_verticalLayout.addWidget(self.gym_johto_pushButton)

        self.gym_hoenn_pushButton = QPushButton(self.verticalLayoutWidget)
        self.gym_hoenn_pushButton.setObjectName(u"gym_hoenn_pushButton")

        self.gym_verticalLayout.addWidget(self.gym_hoenn_pushButton)

        self.gym_sinnoh_pushButton = QPushButton(self.verticalLayoutWidget)
        self.gym_sinnoh_pushButton.setObjectName(u"gym_sinnoh_pushButton")

        self.gym_verticalLayout.addWidget(self.gym_sinnoh_pushButton)

        self.gym_unova_pushButton = QPushButton(self.verticalLayoutWidget)
        self.gym_unova_pushButton.setObjectName(u"gym_unova_pushButton")

        self.gym_verticalLayout.addWidget(self.gym_unova_pushButton)

        self.gym_kalos_pushButton = QPushButton(self.verticalLayoutWidget)
        self.gym_kalos_pushButton.setObjectName(u"gym_kalos_pushButton")

        self.gym_verticalLayout.addWidget(self.gym_kalos_pushButton)

        self.elite_four_label = QLabel(self.battle_widget)
        self.elite_four_label.setObjectName(u"elite_four_label")
        self.elite_four_label.setGeometry(QRect(210, 30, 47, 13))
        self.champions_label = QLabel(self.battle_widget)
        self.champions_label.setObjectName(u"champions_label")
        self.champions_label.setGeometry(QRect(370, 30, 47, 13))
        self.gym_label = QLabel(self.battle_widget)
        self.gym_label.setObjectName(u"gym_label")
        self.gym_label.setGeometry(QRect(60, 30, 47, 13))
        self.verticalLayoutWidget_4 = QWidget(self.battle_widget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(170, 40, 131, 311))
        self.elite_four_verticalLayout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.elite_four_verticalLayout.setObjectName(u"elite_four_verticalLayout")
        self.elite_four_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.elite_four_kanto_pushButton = QPushButton(self.verticalLayoutWidget_4)
        self.elite_four_kanto_pushButton.setObjectName(u"elite_four_kanto_pushButton")

        self.elite_four_verticalLayout.addWidget(self.elite_four_kanto_pushButton)

        self.elite_four_johto_pushButton = QPushButton(self.verticalLayoutWidget_4)
        self.elite_four_johto_pushButton.setObjectName(u"elite_four_johto_pushButton")

        self.elite_four_verticalLayout.addWidget(self.elite_four_johto_pushButton)

        self.elite_four_hoenn_pushButton = QPushButton(self.verticalLayoutWidget_4)
        self.elite_four_hoenn_pushButton.setObjectName(u"elite_four_hoenn_pushButton")

        self.elite_four_verticalLayout.addWidget(self.elite_four_hoenn_pushButton)

        self.elite_four_sinnoh_pushButton = QPushButton(self.verticalLayoutWidget_4)
        self.elite_four_sinnoh_pushButton.setObjectName(u"elite_four_sinnoh_pushButton")

        self.elite_four_verticalLayout.addWidget(self.elite_four_sinnoh_pushButton)

        self.elite_four_unova_pushButton = QPushButton(self.verticalLayoutWidget_4)
        self.elite_four_unova_pushButton.setObjectName(u"elite_four_unova_pushButton")

        self.elite_four_verticalLayout.addWidget(self.elite_four_unova_pushButton)

        self.elite_four_kalos_pushButton = QPushButton(self.verticalLayoutWidget_4)
        self.elite_four_kalos_pushButton.setObjectName(u"elite_four_kalos_pushButton")

        self.elite_four_verticalLayout.addWidget(self.elite_four_kalos_pushButton)

        self.verticalLayoutWidget_5 = QWidget(self.battle_widget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(330, 40, 131, 311))
        self.champions_verticalLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.champions_verticalLayout.setObjectName(u"champions_verticalLayout")
        self.champions_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.champions_kanto_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.champions_kanto_pushButton.setObjectName(u"champions_kanto_pushButton")

        self.champions_verticalLayout.addWidget(self.champions_kanto_pushButton)

        self.champions_johto_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.champions_johto_pushButton.setObjectName(u"champions_johto_pushButton")

        self.champions_verticalLayout.addWidget(self.champions_johto_pushButton)

        self.champions_hoenn_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.champions_hoenn_pushButton.setObjectName(u"champions_hoenn_pushButton")

        self.champions_verticalLayout.addWidget(self.champions_hoenn_pushButton)

        self.champions_sinnoh_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.champions_sinnoh_pushButton.setObjectName(u"champions_sinnoh_pushButton")

        self.champions_verticalLayout.addWidget(self.champions_sinnoh_pushButton)

        self.champions_unova_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.champions_unova_pushButton.setObjectName(u"champions_unova_pushButton")

        self.champions_verticalLayout.addWidget(self.champions_unova_pushButton)

        self.champions_kalos_pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.champions_kalos_pushButton.setObjectName(u"champions_kalos_pushButton")

        self.champions_verticalLayout.addWidget(self.champions_kalos_pushButton)

        self.horizontalLayoutWidget_2 = QWidget(self.battle_widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 360, 451, 41))
        self.npc_horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.npc_horizontalLayout.setObjectName(u"npc_horizontalLayout")
        self.npc_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.npc_xp_1_pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.npc_xp_1_pushButton.setObjectName(u"npc_xp_1_pushButton")

        self.npc_horizontalLayout.addWidget(self.npc_xp_1_pushButton)

        self.npc_xp_2_pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.npc_xp_2_pushButton.setObjectName(u"npc_xp_2_pushButton")

        self.npc_horizontalLayout.addWidget(self.npc_xp_2_pushButton)

        self.cancel_battle_pushButton = QPushButton(self.battle_widget)
        self.cancel_battle_pushButton.setObjectName(u"cancel_battle_pushButton")
        self.cancel_battle_pushButton.setGeometry(QRect(440, 400, 31, 31))
        self.battle_gym_widget = QWidget(self.centralwidget)
        self.battle_gym_widget.setObjectName(u"battle_gym_widget")
        self.battle_gym_widget.setGeometry(QRect(0, 0, 471, 431))
        self.battle_gym_widget.setVisible(False)
        self.cancel_battle_gym_pushButton = QPushButton(self.battle_gym_widget)
        self.cancel_battle_gym_pushButton.setObjectName(u"cancel_battle_gym_pushButton")
        self.cancel_battle_gym_pushButton.setGeometry(QRect(440, 400, 31, 31))
        self.gridLayoutWidget = QWidget(self.battle_gym_widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 70, 411, 357))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.arena2_pushButton = QPushButton(self.gridLayoutWidget)
        self.arena2_pushButton.setObjectName(u"arena2_pushButton")

        self.gridLayout.addWidget(self.arena2_pushButton, 0, 1, 1, 1)

        self.arena3_pushButton = QPushButton(self.gridLayoutWidget)
        self.arena3_pushButton.setObjectName(u"arena3_pushButton")

        self.gridLayout.addWidget(self.arena3_pushButton, 1, 0, 1, 1)

        self.arena4_pushButton = QPushButton(self.gridLayoutWidget)
        self.arena4_pushButton.setObjectName(u"arena4_pushButton")

        self.gridLayout.addWidget(self.arena4_pushButton, 1, 1, 1, 1)

        self.arena1_pushButton = QPushButton(self.gridLayoutWidget)
        self.arena1_pushButton.setObjectName(u"arena1_pushButton")

        self.gridLayout.addWidget(self.arena1_pushButton, 0, 0, 1, 1)

        self.arena6_pushButton = QPushButton(self.gridLayoutWidget)
        self.arena6_pushButton.setObjectName(u"arena6_pushButton")

        self.gridLayout.addWidget(self.arena6_pushButton, 2, 1, 1, 1)

        self.arena8_pushButton = QPushButton(self.gridLayoutWidget)
        self.arena8_pushButton.setObjectName(u"arena8_pushButton")

        self.gridLayout.addWidget(self.arena8_pushButton, 3, 1, 1, 1)

        self.arena7_pushButton = QPushButton(self.gridLayoutWidget)
        self.arena7_pushButton.setObjectName(u"arena7_pushButton")

        self.gridLayout.addWidget(self.arena7_pushButton, 3, 0, 1, 1)

        self.arena5_pushButton = QPushButton(self.gridLayoutWidget)
        self.arena5_pushButton.setObjectName(u"arena5_pushButton")

        self.gridLayout.addWidget(self.arena5_pushButton, 2, 0, 1, 1)

        self.verticalLayoutWidget_3 = QWidget(self.battle_gym_widget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(30, 50, 411, 21))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.region_name_gym_label = QLabel(self.verticalLayoutWidget_3)
        self.region_name_gym_label.setObjectName(u"region_name_gym_label")
        self.region_name_gym_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.region_name_gym_label)

        self.battle_elite_four_widget = QWidget(self.centralwidget)
        self.battle_elite_four_widget.setObjectName(u"battle_elite_four_widget")
        self.battle_elite_four_widget.setGeometry(QRect(0, 0, 471, 431))
        self.battle_elite_four_widget.setVisible(False)
        self.cancel_battle_elite_four_pushButton = QPushButton(self.battle_elite_four_widget)
        self.cancel_battle_elite_four_pushButton.setObjectName(u"cancel_battle_elite_four_pushButton")
        self.cancel_battle_elite_four_pushButton.setGeometry(QRect(440, 400, 31, 31))
        self.gridLayoutWidget_2 = QWidget(self.battle_elite_four_widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 70, 411, 357))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.elite2_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.elite2_pushButton.setObjectName(u"elite2_pushButton")

        self.gridLayout_2.addWidget(self.elite2_pushButton, 0, 1, 1, 1)

        self.elite4_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.elite4_pushButton.setObjectName(u"elite4_pushButton")

        self.gridLayout_2.addWidget(self.elite4_pushButton, 1, 1, 1, 1)

        self.elite3_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.elite3_pushButton.setObjectName(u"elite3_pushButton")

        self.gridLayout_2.addWidget(self.elite3_pushButton, 1, 0, 1, 1)

        self.elite1_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.elite1_pushButton.setObjectName(u"elite1_pushButton")

        self.gridLayout_2.addWidget(self.elite1_pushButton, 0, 0, 1, 1)

        self.verticalLayoutWidget_8 = QWidget(self.battle_elite_four_widget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(30, 50, 411, 21))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.region_name_elite_four_label = QLabel(self.verticalLayoutWidget_8)
        self.region_name_elite_four_label.setObjectName(u"region_name_elite_four_label")
        self.region_name_elite_four_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.region_name_elite_four_label)

        self.battle_pokemon_widget = QWidget(self.centralwidget)
        self.battle_pokemon_widget.setObjectName(u"battle_pokemon_widget")
        self.battle_pokemon_widget.setGeometry(QRect(0, 0, 471, 431))
        self.battle_pokemon_widget.setVisible(True)
        self.cancel_pokemon_pushButton = QPushButton(self.battle_pokemon_widget)
        self.cancel_pokemon_pushButton.setObjectName(u"cancel_pokemon_pushButton")
        self.cancel_pokemon_pushButton.setGeometry(QRect(440, 400, 31, 31))
        self.cancel_pokemon_pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayoutWidget_3 = QWidget(self.battle_pokemon_widget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(30, 20, 411, 321))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.attack2_pushButton = QPushButton(self.gridLayoutWidget_3)
        self.attack2_pushButton.setObjectName(u"attack2_pushButton")

        self.gridLayout_3.addWidget(self.attack2_pushButton, 0, 1, 1, 1)

        self.attack4_pushButton = QPushButton(self.gridLayoutWidget_3)
        self.attack4_pushButton.setObjectName(u"attack4_pushButton")

        self.gridLayout_3.addWidget(self.attack4_pushButton, 1, 1, 1, 1)

        self.attack3_pushButton = QPushButton(self.gridLayoutWidget_3)
        self.attack3_pushButton.setObjectName(u"attack3_pushButton")

        self.gridLayout_3.addWidget(self.attack3_pushButton, 1, 0, 1, 1)

        self.attack1_pushButton = QPushButton(self.gridLayoutWidget_3)
        self.attack1_pushButton.setObjectName(u"attack1_pushButton")

        self.gridLayout_3.addWidget(self.attack1_pushButton, 0, 0, 1, 1)

        self.horizontalLayoutWidget_4 = QWidget(self.battle_pokemon_widget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(30, 360, 411, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.swap1_pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.swap1_pushButton.setObjectName(u"swap1_pushButton")
        self.swap1_pushButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.swap1_pushButton)

        self.swap2_pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.swap2_pushButton.setObjectName(u"swap2_pushButton")

        self.horizontalLayout_2.addWidget(self.swap2_pushButton)

        self.swap3_pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.swap3_pushButton.setObjectName(u"swap3_pushButton")

        self.horizontalLayout_2.addWidget(self.swap3_pushButton)

        self.forfeit_pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.forfeit_pushButton.setObjectName(u"forfeit_pushButton")

        self.horizontalLayout_2.addWidget(self.forfeit_pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.battle_gym_widget.raise_()
        self.battle_widget.raise_()
        self.main_widget.raise_()
        self.pokeball_fish_widget.raise_()
        self.pokeball_widget.raise_()
        self.battle_elite_four_widget.raise_()
        self.battle_pokemon_widget.raise_()

        self.retranslateUi(MainWindow)
        self.pokemon_pushButton.released.connect(self.pokeball_widget.show)
        self.pokemon_pushButton.released.connect(self.main_widget.hide)
        self.fish_pushButton.released.connect(self.pokeball_fish_widget.show)
        self.fish_pushButton.released.connect(self.main_widget.hide)
        self.pokeball_pushButton.released.connect(self.main_widget.show)
        self.pokeball_pushButton.released.connect(self.pokeball_widget.hide)
        self.greatball_pushButton.released.connect(self.main_widget.show)
        self.greatball_pushButton.released.connect(self.pokeball_widget.hide)
        self.ultraball_pushButton.released.connect(self.main_widget.show)
        self.ultraball_pushButton.released.connect(self.pokeball_widget.hide)
        self.premierball_pushButton.released.connect(self.main_widget.show)
        self.premierball_pushButton.released.connect(self.pokeball_widget.hide)
        self.masterball_pushButton.released.connect(self.main_widget.show)
        self.masterball_pushButton.released.connect(self.pokeball_widget.hide)
        self.cancel_pushButton.released.connect(self.main_widget.show)
        self.cancel_pushButton.released.connect(self.pokeball_widget.hide)
        self.pokeball_fish_pushButton.released.connect(self.main_widget.show)
        self.pokeball_fish_pushButton.released.connect(self.pokeball_fish_widget.hide)
        self.greatball_fish_pushButton.released.connect(self.main_widget.show)
        self.greatball_fish_pushButton.released.connect(self.pokeball_fish_widget.hide)
        self.ultraball_fish_pushButton.released.connect(self.main_widget.show)
        self.ultraball_fish_pushButton.released.connect(self.pokeball_fish_widget.hide)
        self.premierball_fish_pushButton.released.connect(self.main_widget.show)
        self.premierball_fish_pushButton.released.connect(self.pokeball_fish_widget.hide)
        self.diveball_fish_pushButton.released.connect(self.main_widget.show)
        self.diveball_fish_pushButton.released.connect(self.pokeball_fish_widget.hide)
        self.masterball_fish_pushButton.released.connect(self.main_widget.show)
        self.masterball_fish_pushButton.released.connect(self.pokeball_fish_widget.hide)
        self.cancel_fish_pushButton.released.connect(self.main_widget.show)
        self.cancel_fish_pushButton.released.connect(self.pokeball_fish_widget.hide)
        self.discord_chat_pushButton.released.connect(MainWindow.showMinimized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDiscord_chat.setText(QCoreApplication.translate("MainWindow", u"Discord chat", None))
        self.pokemon_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pokemon", None))
        self.fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"Fish", None))
        self.discord_chat_pushButton.setText(QCoreApplication.translate("MainWindow", u"Discord Chat", None))
        self.discord_chat_x_y.setText(QCoreApplication.translate("MainWindow", u"X = | Y =", None))
        self.battle_pushButton.setText(QCoreApplication.translate("MainWindow", u"Battle", None))
        self.pokeball_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pokepall", None))
        self.greatball_pushButton.setText(QCoreApplication.translate("MainWindow", u"Greatball", None))
        self.ultraball_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ultraball", None))
        self.premierball_pushButton.setText(QCoreApplication.translate("MainWindow", u"Premierball", None))
        self.masterball_pushButton.setText(QCoreApplication.translate("MainWindow", u"Masterball", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pokeball_fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pokepall", None))
        self.greatball_fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"Greatball", None))
        self.ultraball_fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ultraball", None))
        self.premierball_fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"Premierball", None))
        self.masterball_fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"Masterball", None))
        self.pull_fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"PULL", None))
        self.cancel_fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.diveball_fish_pushButton.setText(QCoreApplication.translate("MainWindow", u"Diveball", None))
        self.gym_kanto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kanto", None))
        self.gym_johto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Johto", None))
        self.gym_hoenn_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hoenn", None))
        self.gym_sinnoh_pushButton.setText(QCoreApplication.translate("MainWindow", u"Sinnoh", None))
        self.gym_unova_pushButton.setText(QCoreApplication.translate("MainWindow", u"Unova", None))
        self.gym_kalos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kalos", None))
        self.elite_four_label.setText(QCoreApplication.translate("MainWindow", u"Elite Four", None))
        self.champions_label.setText(QCoreApplication.translate("MainWindow", u"Champions", None))
        self.gym_label.setText(QCoreApplication.translate("MainWindow", u"Gym", None))
        self.elite_four_kanto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kanto", None))
        self.elite_four_johto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Johto", None))
        self.elite_four_hoenn_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hoenn", None))
        self.elite_four_sinnoh_pushButton.setText(QCoreApplication.translate("MainWindow", u"Sinnoh", None))
        self.elite_four_unova_pushButton.setText(QCoreApplication.translate("MainWindow", u"Unova", None))
        self.elite_four_kalos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kalos", None))
        self.champions_kanto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kanto", None))
        self.champions_johto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Johto", None))
        self.champions_hoenn_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hoenn", None))
        self.champions_sinnoh_pushButton.setText(QCoreApplication.translate("MainWindow", u"Sinnoh", None))
        self.champions_unova_pushButton.setText(QCoreApplication.translate("MainWindow", u"Unova", None))
        self.champions_kalos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kalos", None))
        self.npc_xp_1_pushButton.setText(QCoreApplication.translate("MainWindow", u"NPC 675725560470831125", None))
        self.npc_xp_2_pushButton.setText(QCoreApplication.translate("MainWindow", u"NPC 508692505810698241", None))
        self.cancel_battle_pushButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.cancel_battle_gym_pushButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.arena2_pushButton.setText(QCoreApplication.translate("MainWindow", u"Arena 2", None))
        self.arena3_pushButton.setText(QCoreApplication.translate("MainWindow", u"Arena 3", None))
        self.arena4_pushButton.setText(QCoreApplication.translate("MainWindow", u"Arena 4", None))
        self.arena1_pushButton.setText(QCoreApplication.translate("MainWindow", u"Arena 1", None))
        self.arena6_pushButton.setText(QCoreApplication.translate("MainWindow", u"Arena 6", None))
        self.arena8_pushButton.setText(QCoreApplication.translate("MainWindow", u"Arena 8", None))
        self.arena7_pushButton.setText(QCoreApplication.translate("MainWindow", u"Arena 7", None))
        self.arena5_pushButton.setText(QCoreApplication.translate("MainWindow", u"Arena 5", None))
        self.region_name_gym_label.setText(QCoreApplication.translate("MainWindow", u"Nom de la r\u00e9gion", None))
        self.cancel_battle_elite_four_pushButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.elite2_pushButton.setText(QCoreApplication.translate("MainWindow", u" Elite #2", None))
        self.elite4_pushButton.setText(QCoreApplication.translate("MainWindow", u"Elite #4", None))
        self.elite3_pushButton.setText(QCoreApplication.translate("MainWindow", u"Elite #3", None))
        self.elite1_pushButton.setText(QCoreApplication.translate("MainWindow", u" Elite #1", None))
        self.region_name_elite_four_label.setText(QCoreApplication.translate("MainWindow", u"Nom de la r\u00e9gion", None))
        self.cancel_pokemon_pushButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.attack2_pushButton.setText(QCoreApplication.translate("MainWindow", u"Attack #2", None))
        self.attack4_pushButton.setText(QCoreApplication.translate("MainWindow", u"Attack #4", None))
        self.attack3_pushButton.setText(QCoreApplication.translate("MainWindow", u"Attack #3", None))
        self.attack1_pushButton.setText(QCoreApplication.translate("MainWindow", u"Attack #1", None))
        self.swap1_pushButton.setText(QCoreApplication.translate("MainWindow", u"Swap 1", None))
        self.swap2_pushButton.setText(QCoreApplication.translate("MainWindow", u"Swap 2", None))
        self.swap3_pushButton.setText(QCoreApplication.translate("MainWindow", u"Swap 3", None))
        self.forfeit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Forfeit", None))
    # retranslateUi

