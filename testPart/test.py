"""
    The "test.py" module, containing all screens and main set of test app part.
"""
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.button import MDRaisedButton, MDFlatButton


###################################################
# All main screen from test
###################################################
class ListItemWithCheckbox(OneLineAvatarIconListItem):
    """Custom list item."""

    icon = StringProperty("android")



class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''
    pass


class TestMDRaisedButton(MDRaisedButton):
    pass


class Test01Screen(Screen):
    dialog = None
    a = ObjectProperty(None)
    b = ObjectProperty(None)
    c = ObjectProperty(None)

    def on_checkbox_active(self):
        result = 0
        if self.a.active:
            result += 1
        # if self.b.active:
        #     print('odp c')
        # if self.c.active:
        #     print('odp c')

        self.show_MDDialog(result)

    def show_MDDialog(self, result):
        if not self.dialog:
            self.dialog = MDDialog(
                text=f'Your score: {result}/5',
                size_hint=[.8, .8],
                auto_dismiss=True,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                    ),
                    MDFlatButton(
                        text="OK",
                    ),
                ],
            )
        self.dialog.open()


class Test02Screen(Screen):
    pass


class Test03Screen(Screen):
    pass


class Test04Screen(Screen):
    pass