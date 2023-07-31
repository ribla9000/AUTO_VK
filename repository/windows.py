from PyQt5.QtWidgets import (QApplication, QPushButton,
                             QLabel, QVBoxLayout,
                             QScrollArea, QGroupBox, QRadioButton,
                             QWidget, QFormLayout)
import sys
from typing import Optional
from endpoints.parser import (get_count_friends, scroll_page_down, login,
                              get_friends, choose_friend, get_profiles, check_login, run_browser, Chrome)
from .gui import GUIRepository, ClickableLineEdit


class GoogleProfilesWindow:
    
    @staticmethod
    def run_app():
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        window = GUIRepository.make_window()
        window.setGeometry(400, 150, 300, 0)
        
        make_prof = GoogleProfilesWindow.make_profiles_group
        profiles = []
        
        make_menu = GUIRepository.make_menu
        menu, r_btns = {}, []
        start_btn = QPushButton(window)
        start_btn.setText("GET PROFILES")
        start_btn.setStyleSheet(
            "background-color: #050505; color: #7f7f7f; font: 24px; border: 4px solid #180e33; border-radius: 9px")
        start_btn.move(400, 15)
        start_btn.clicked.connect(lambda x: (profiles.clear() if len(profiles) > 0 else ...,
                                             profiles.extend(get_profiles()),
                                             r_btns.clear() if len(r_btns) > 0 else ...,
                                             r_btns.extend(make_prof(window, profiles)),
                                             start_btn.hide(),
                                             menu.update(make_menu(window, GoogleProfilesWindow)),
                                             GoogleProfilesWindow.menu_actions(menu, r_btns, window)
                                             ))
        window.show()
        app.exec()
    
    @staticmethod
    def make_btns(window: QWidget):
        choose_btn = QPushButton(window)
        choose_btn.setText("choose profile")
        
        enter_btn = QPushButton(window)
        enter_btn.setText("enter the action")
        
        btns = [choose_btn, enter_btn]
        y_pos = 35
        for btn in btns:
            if btn == btns[1]:
                y_pos += 60
            btn.setFixedSize(200, 50)
            btn.setStyleSheet("background-color: #050505; color: #7f7f7f; font: 24px; border: 4px solid #180e33; border-radius: 9px")
            btn.move(400, y_pos)
        return btns
    
    @staticmethod
    def make_labels(window: QWidget):
        return
    
    @staticmethod
    def make_profiles_group(window, profiles: list):
        r_new_btn = QRadioButton(text="Make a new profile")
        r_new_btn.setStyleSheet("background-color: #303030;font: 20px ;color: #7f7f7f")
        r_btns = []
        r_btns.append(r_new_btn)
        
        prof_group = QGroupBox(title="GoogleProfilesWindow")
        prof_group.setStyleSheet("background-color: #212020;font: 20px ;color: #7f7f7f")
        
        form = QFormLayout()
        form.addWidget(r_new_btn)
        
        for i in profiles:
            r_btn = QRadioButton(text=f"{i}")
            r_btn.setStyleSheet("background-color: #303030;font: 20px ;color: #7f7f7f")
            r_btns.append(r_btn)
            form.addWidget(r_btn)
        
        prof_group.setLayout(form)
        
        scroll_area = QScrollArea()
        scroll_area.setFixedSize(290, 450)
        scroll_area.setWidget(prof_group)
        scroll_area.setWidgetResizable(True)
        
        lay = QVBoxLayout(window)
        lay.setContentsMargins(0, 0, 0, 450)
        lay.addWidget(scroll_area)
        
        return r_btns
    
    @staticmethod
    def menu_actions(menu: dict, r_btns: list, window: QWidget):
        on_click = GUIRepository.on_click
        profile = ["Profile 1"]
        menu["btns"][0].clicked.connect(lambda x: on_click(callback=GoogleProfilesWindow.get_radio(r_btns),
                                                           console=f"Chosen profile:",
                                                           callback_set=True,
                                                           obj=profile
                                                           ))
        menu["btns"][1].clicked.connect(lambda x: (GUIRepository.clear_window(window), VkLoginWindow.run_app(window, profile)))
    
    @staticmethod
    def get_radio(r_btns: list):
        for r_btn in r_btns:
            if r_btn.isChecked():
                return r_btn.text()


class VkLoginWindow:
    
    @staticmethod
    def run_app(window: Optional[QApplication], profile: Optional[list]):
        on_click = GUIRepository.on_click
        menu = GUIRepository.make_menu(window, VkLoginWindow)
        menu["labels"][0].setText(f"Profile: {profile[0]}")
        
        menu["btns"][0].clicked.connect(lambda x: (browser:=run_browser(profile=profile[0]),
                                                   answer:=on_click(callback=check_login(browser),
                                                            label=menu["labels"][1],
                                                            console="is_auth?",
                                                            label_text="",
                                                            callback_set=True,
                                                            ),
                                                   VkLoginWindow.next_action(window, browser) if answer is True else VkLoginWindow.make_auth_space(window, browser),
                                                   ))
        
    @staticmethod
    def next_action(window, browser):
        GUIRepository.clear_window(window)
        VkFriendsWindow.run_app(window, browser)
        
    @staticmethod
    def make_btns(window):
        check_btn = QPushButton(window)
        check_btn.setText("Check")
        check_btn.move(630, 5)
        check_btn.setFixedSize(100, 50)
        check_btn.setStyleSheet("background-color: #050505; color: #7f7f7f; font: 24px; border: 4px solid #180e33; border-radius: 9px")
        
        btns = [check_btn]
        return btns
    
    @staticmethod
    def make_labels(window):
        lbl_profile = QLabel(window)
        lbl_check_login = QLabel(window)
        
        lbls = [lbl_profile, lbl_check_login]
        x_pos = 0
        for lbl in lbls:
            if lbl == lbls[1]:
                x_pos += 320
            lbl.move(x_pos, 5)
            lbl.setFixedSize(300, 50)
            lbl.setStyleSheet("background-color: #212020; color: #3770c4; font-size: 16px; font-weight: bold")
        
        return lbls
    
    @staticmethod
    def make_auth_space(window, browser):
        lbl_login = ClickableLineEdit(window)
        lbl_login.move(0, 100)
        lbl_login.setFixedSize(300, 50)
        lbl_login.setText("Input your login here")
        lbl_login.setStyleSheet("background-color: #212020; color: #34574f; font: 24px bold")
        lbl_login.show()
        
        lbl_password = ClickableLineEdit(window)
        lbl_password.move(0, 160)
        lbl_password.setFixedSize(300, 50)
        lbl_password.setText("Input your password here")
        lbl_password.setStyleSheet("background-color: #212020; color: #212020; font: 24px bold")
        lbl_password.show()
        
        lbl_login.clicked.connect(lambda: lbl_login.setText(""))
        lbl_password.clicked.connect(lambda: lbl_password.setText(""))
        
        btn_accept = QPushButton(window)
        btn_accept.move(320, 140)
        btn_accept.setFixedSize(150, 35)
        btn_accept.setText("Accept")
        btn_accept.setStyleSheet("background-color: #212020; color: #a12716; font: 23px bold")
        btn_accept.show()
        
        btn_accept.clicked.connect(lambda x: (_login:=GUIRepository.input_value(lbl_login),
                                              password:=GUIRepository.input_value(lbl_password),
                                              login(browser, str(_login), str(password)),
                                              GUIRepository.clear_window(window),
                                              VkFriendsWindow.run_app(window, browser)
                                              ))
        return

    
class VkFriendsWindow:
    
    @staticmethod
    def run_app(window: Optional[QApplication], browser: Chrome):
        friends_value, friends_box, friend_id = [0], {}, [0]
        on_click = GUIRepository.on_click
        menu = GUIRepository.make_menu(window, VkFriendsWindow)
        # get count of friends
        menu["btns"][0].clicked.connect(lambda x: on_click(console=f"Get Count of friends",
                                                           callback=get_count_friends(browser),
                                                           obj=friends_value,
                                                           label_text="Count of friends: ",
                                                           callback_set=True,
                                                           label=menu["labels"][0]
                                                           ))
        # scroll down
        menu["btns"][1].clicked.connect(lambda x: on_click(console="Scrolling down",
                                                           label=menu["labels"][1],
                                                           label_text="Scrolled",
                                                           callback=scroll_page_down(browser, int(friends_value[0]))
                                                           ))
        # get friends
        menu["btns"][2].clicked.connect(lambda x: on_click(console="get friends",
                                                           label=menu["labels"][2],
                                                           label_text="Done",
                                                           callback=get_friends(browser, int(friends_value[0])),
                                                           obj=friends_box,
                                                           ))
        # get value from Qline
        menu["btns"][3].clicked.connect(lambda x: on_click(console="Your Choice is: ",
                                                           callback=GUIRepository.input_value(label=menu["labels"][3],
                                                                                              obj=friend_id
                                                                                              ),
                                                           label=menu["labels"][3],
                                                           label_text="Your choice is: ",
                                                           callback_set=True,
                                                           ))
        # Choose a friend
        menu["btns"][4].clicked.connect(lambda x: on_click(console=f"Your friend's name is: ",
                                                           callback=choose_friend(browser,
                                                                                  friends_box['callback'],
                                                                                  friend_id[0]),
                                                           callback_set=True,
                                                           label=menu["labels"][4],
                                                           label_text=""
                                                           ))
        return
    
    @staticmethod
    def make_btns(window):
        btn_get_count_friends = QPushButton(window)
        btn_get_count_friends.setText("get count")
        
        btn_scroll_page_down = QPushButton(window)
        btn_scroll_page_down.setText("page down")
        
        btn_get_friends = QPushButton(window)
        btn_get_friends.setText("get friends")
        
        btn_choose_friend_id = QPushButton(window)
        btn_choose_friend_id.setText("choose friend id")
        
        btn_choose_friend = QPushButton(window)
        btn_choose_friend.setText("goto friend")
        
        y_pos = 0
        btns = [btn_get_count_friends, btn_scroll_page_down, btn_get_friends, btn_choose_friend_id, btn_choose_friend]
        for btn in btns:
            if btn == btns[4]:
                y_pos += 70
            else:
                y_pos += 40
            btn.move(512, y_pos)
            btn.setStyleSheet("background-color: #09343F; height: 80px; width: 200px;")
        return btns
    
    @staticmethod
    def make_labels(window):
        lbl_get_count_friends = QLabel(window)
        lbl_get_count_friends.setText("Count: ")
        
        lbl_scroll_page_down = QLabel(window)
        lbl_scroll_page_down.setText("Scroll: ")
        
        lbl_get_friends = QLabel(window)
        lbl_get_friends.setText("Friends: ")
        
        lbl_choose_friend_id = ClickableLineEdit(window)
        lbl_choose_friend_id.clicked.connect(lambda: lbl_choose_friend_id.setText(""))
        lbl_choose_friend_id.setText("Choose id")
        
        lbl_choose_friend = QLabel(window)
        lbl_choose_friend.setText("")

        lbls = [lbl_get_count_friends, lbl_scroll_page_down, lbl_get_friends, lbl_choose_friend_id, lbl_choose_friend]
        y_pos = 0
        for lbl in lbls:
            if lbl == lbls[4]:
                y_pos += 70
            else:
                y_pos += 40
            lbl.move(0, y_pos)
            lbl.setFixedSize(240, 40)
            lbl.setStyleSheet("background-color: #212020; color: #3e1e96; font-size: 16px; font-weight: bold")
        
        return lbls

    
