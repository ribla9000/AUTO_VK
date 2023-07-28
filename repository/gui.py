from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QLineEdit
import sys
from typing import Union, Optional
from endpoints.parser import (run_browser, get_count_friends, scroll_page_down,
                              get_friends, choose_friend, Chrome)


class GUIRepository:
    
    @staticmethod
    def run_app():
        browser, friends_value, friends_box, friend_id = [0], [0], {}, [0]
        
        app = QApplication(sys.argv)
        window = GUIRepository.make_window()
        start_btn, start_label = GUIRepository.make_started(window)
        on_click = GUIRepository.on_click
        menu = GUIRepository.make_menu(window)
        #start browser
        start_btn.clicked.connect(lambda x: on_click(console=f"Started Browser",
                                                btn=start_btn,
                                                label=start_label,
                                                label_text="Started Browser",
                                                btn_event="delete",
                                                obj=browser,
                                                callback=run_browser()))
        #get count of friends
        menu["btns"][0].clicked.connect(lambda x: on_click(console=f"Get Count of friends",
                                                           callback=get_count_friends(browser[0]),
                                                           label_text="Count of friends: ",
                                                           obj=friends_value,
                                                           callback_set=True,
                                                           label=menu["labels"][0]))
       #scroll down
        menu["btns"][1].clicked.connect(lambda x: on_click(console="Scrolling down",
                                                           label=menu["labels"][1],
                                                           label_text="Scrolled",
                                                           callback=scroll_page_down(browser[0], int(friends_value[0]))
                                                           ))
        
        menu["btns"][2].clicked.connect(lambda x: on_click(console="get friends",
                                                           label=menu["labels"][2],
                                                           label_text="Get Friends Box",
                                                           callback=get_friends(browser[0], int(friends_value[0])),
                                                           obj=friends_box,
                                                           ))
        
        menu["btns"][3].clicked.connect(lambda x: on_click(console="Your Choice is: ",
                                                           callback=GUIRepository.input_id(label=menu["labels"][3], obj=friend_id),
                                                           label=menu["labels"][3],
                                                           label_text="Your choice is: ",
                                                           callback_set=True,
                                                           ))
        menu["btns"][4].clicked.connect(lambda x: on_click(console=f"Your friend's name is: ",
                                                           callback=choose_friend(browser[0], friends_box['callback'], friend_id[0]),
                                                           callback_set=True,
                                                           label=menu["labels"][4],
                                                           label_text="Your Friend's name is: "
                                                           )
                                        )
        
        
        window.show()
        app.exec()
        return
        
    @staticmethod
    def make_window():
        window = QWidget()
        window.setFixedSize(1024, 768)
        window.setWindowTitle("VKAutoAuth")
        window.setStyleSheet("background-color: #424645;")
        return window
    
    @staticmethod
    def make_started(window):
        start_btn = QPushButton(window)
        start_label = QLabel(window)
        start_label.move(0, 90)
        start_label.setText("")
        start_label.setFixedSize(240, 40)
        start_label.setStyleSheet("background-color: #BBC9CD; color: red; font-size: 16px")
        start_btn.setText("START")
        start_btn.setStyleSheet("background-color: #09343F; "
                                "height: 80px; "
                                "width: 60px; "
                                "margin-left: 512px; "
                                "margin-top: 90px"
                                )
        return start_btn, start_label
    
    @staticmethod
    def test():
        return "BLOB"
    
    @staticmethod
    def on_click(callback: Union[None, callable] = None,
                 console: Union[None, str] = None,
                 callback_set: bool = False,
                 btn_event: Union[None, str] = "stay",
                 label_event: Union[None, str] = "stay",
                 label: Union[QLabel, None] = None,
                 label_text: Union[None, str] = None,
                 btn: Union[None, QPushButton] = None,
                 obj: Union[list, dict] = None,
                 ):
        
        if console is not None and callback_set is True:
            print(console, callback)
        elif console is not None and callback_set is False:
            print(console)
        elif console is None:
            pass
        
        if isinstance(label, QLineEdit) and label_text is not None:
            label.setText(label_text + label.text())
        
        if callback_set is True and label_text is not None:
            label.setText(label_text + str(callback))
        if label_text is not None and callback_set is False:
            label.setText(label_text)
            
        if btn_event == "stay" or btn_event is None:
            pass
        if btn_event == "delete":
            btn.hide()
            
        if label_event == "stay" or label_event is None:
            pass
        if label_event == "delete":
            label.hide()
            
        if isinstance(obj, list):
            obj[0] = callback
        elif isinstance(obj, dict):
            obj["callback"] = callback
        return
        
    @staticmethod
    def choose_friend(id: int = 10):
        pass
    
    @staticmethod
    def make_menu(window):
        btns = GUIRepository.make_btns(window)
        labels = GUIRepository.make_labels(window)
        return {"btns": btns, "labels": labels}
    
    @staticmethod
    def make_btns(window):
        btn_get_count_friends = QPushButton(window)
        btn_get_count_friends.move(512, 200)
        btn_get_count_friends.setStyleSheet("background-color: #09343F; "
                                            "height: 80px; "
                                            "width: 200px; ")
        btn_get_count_friends.setText("get count")
        
        btn_scroll_page_down = QPushButton(window)
        btn_scroll_page_down.move(512, 280)
        btn_scroll_page_down.setStyleSheet("background-color: #09343F; "
                                            "height: 80px; "
                                            "width: 200px; ")
        btn_scroll_page_down.setText("page down")
        
        btn_get_friends = QPushButton(window)
        btn_get_friends.move(512, 340)
        btn_get_friends.setStyleSheet("background-color: #09343F; "
                                      "height: 80px; "
                                      "width: 200px; ")
        btn_get_friends.setText("get friends")
        
        btn_choose_friend_id = QPushButton(window)
        btn_choose_friend_id.move(512, 400)
        btn_choose_friend_id.setStyleSheet("background-color: #09343F; "
                                        "height: 80px; "
                                        "width: 200px; ")
        btn_choose_friend_id.setText("choose friend id")

        btn_choose_friend = QPushButton(window)
        btn_choose_friend.move(512, 490)
        btn_choose_friend.setStyleSheet("background-color: #09343F; "
                                           "height: 80px; "
                                           "width: 200px; ")
        btn_choose_friend.setText("goto friend")
        
        return [btn_get_count_friends, btn_scroll_page_down, btn_get_friends, btn_choose_friend_id, btn_choose_friend]
        
    @staticmethod
    def make_labels(window):
        lbl_get_count_friends = QLabel(window)
        lbl_get_count_friends.move(0, 200)
        lbl_get_count_friends.setFixedSize(240, 40)
        lbl_get_count_friends.setStyleSheet("background-color: #BBC9CD; color: red; font-size: 16px")
        lbl_get_count_friends.setText("Count: ")
        
        lbl_scroll_page_down = QLabel(window)
        lbl_scroll_page_down.move(0, 280)
        lbl_scroll_page_down.setFixedSize(240, 40)
        lbl_scroll_page_down.setStyleSheet("background-color: #BBC9CD; color: red; font-size: 16px")
        lbl_scroll_page_down.setText("Scroll: ")
        
        lbl_get_friends = QLabel(window)
        lbl_get_friends.move(0, 340)
        lbl_get_friends.setFixedSize(240, 40)
        lbl_get_friends.setStyleSheet("background-color: #BBC9CD; color: red; font-size: 16px")
        lbl_get_friends.setText("Friends: ")
     
        lbl_choose_friend_id = QLineEdit(window)
        lbl_choose_friend_id.setText("Choose id")
        lbl_choose_friend_id.move(0, 400)
        lbl_choose_friend_id.setFixedSize(240, 40)
        lbl_choose_friend_id.setStyleSheet("background-color: #BBC9CD; color: red; font-size: 16px")

        lbl_choose_friend = QLabel(window)
        lbl_choose_friend.setText("Choose id")
        lbl_choose_friend.move(0, 490)
        lbl_choose_friend.setFixedSize(240, 40)
        lbl_choose_friend.setStyleSheet("background-color: #BBC9CD; color: red; font-size: 16px")

        return [lbl_get_count_friends, lbl_scroll_page_down, lbl_get_friends, lbl_choose_friend_id, lbl_choose_friend]
    
    @staticmethod
    def input_id(label: Union[QLineEdit, QLabel] = None, obj: Union[list, None] = None):
        
        try:
            value = int(label.text())
            obj[0] = value
            return obj[0]
        
        except:
            value = label.text()
            obj[0] = value
            return obj[0]
  