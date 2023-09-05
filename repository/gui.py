from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)
from typing import Union


class GUIRepository:
    
    @staticmethod
    def make_window(back_color: str = "#424645", title: str = ""):
        window = QWidget()
        window.setFixedSize(1024, 768)
        window.setWindowTitle(title)
        window.setStyleSheet(f"background-color: {back_color};")
        return window
    
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
            print(console, f"\'{str(callback)}\'")
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
            
        if isinstance(obj, list) and obj is not None:
            obj[0] = callback
        elif isinstance(obj, dict) and obj is not None:
            obj["callback"] = callback
        return callback
        
    @staticmethod
    def make_menu(window, cls):
        btns = cls.make_btns(window)
        labels = cls.make_labels(window)
        
        [btn.show() for btn in btns] if btns is not None else False
        [label.show() for label in labels] if labels is not None else False
        
        return {"btns": btns, "labels": labels}
    
    @staticmethod
    def input_value(label: Union[QLineEdit, QLabel] = None, obj: Union[list, any] = None):
        try:
            value = int(label.text())
            if isinstance(obj, list):
                obj[0] = value
                return obj[0]
            return value
        
        except:
            value = label.text()
            if isinstance(obj, list):
                obj[0] = value
                return obj[0]
            return value
    
    @staticmethod
    def clear_window(window: QWidget):
        for widget in window.children():
            widget.hide() if not isinstance(widget, QVBoxLayout) else None


class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLineEdit.mousePressEvent(self, event)
        