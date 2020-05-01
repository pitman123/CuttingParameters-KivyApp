# -*- coding: utf-8 -*-
import re
import time
from math import pi
import codecs
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from kivy.garden.matplotlib import FigureCanvasKivyAgg

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu

from kivymd.uix.button import MDRaisedButton

from kivyappp.kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.widget import Widget

from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine

from kivy.uix.boxlayout import BoxLayout
from kivymd import images_path
from kivymd.uix.list import IRightBodyTouch, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.dialog import MDDialog

Window.size = (350, 550)


class MainScreen(Screen):
    pass


class ParametersScreen(Screen):
    pass


class TurningScreen(Screen):
    pass


class TimeInScreen(Screen):
    pass


class PowerRequirementScreen(Screen):
    # def __init__(self, **kw):
    #     super().__init__(**kw)
    #     menu_items = [90, 80, 70]
    #     self.menu = MDDropdownMenu(
    #         caller=self.ids.field,
    #         items=menu_items,
    #         position='bottom',
    #         callback=self.set_item,
    #         width_mult=4,
    #     )


    def set_item(self, instance):
        def set_item(interval):
            self.ids.field.text = instance.text


class MetalRemovalRateScreen(Screen):
    pass


class KnowledgeScreen(Screen):
    pass


class MachiningIntroductionScreen(Screen):
    with codecs.open("knowledge_text/itroduction.html", 'r', 'utf-8') as f:
        contents = f.read()
    text = StringProperty(contents)


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class CuttingSpeedScreen(Screen):
    score = ObjectProperty(None)
    machined_diameter = ObjectProperty(None)
    spindle_speed = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.submit, .5)

    def submit(self, *args):
        self.score.text = '0'
        try:
            if self.machined_diameter.text and self.spindle_speed.text:
                score = f'{(float(self.machined_diameter.text) * float(self.spindle_speed.text) * pi) / 1000:.2f}'
                self.score.text = score
        except ValueError:
            print('error')


class SpindleSpeedScreen(Screen):
    score = ObjectProperty(None)
    machined_diameter = ObjectProperty(None)
    cutting_speed = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.submit, .5)

    def submit(self, *args):
        self.score.text = '0'
        try:
            if self.machined_diameter.text and self.cutting_speed.text:
                score = f'{(float(self.cutting_speed.text) * 1000 / (float(self.machined_diameter.text) * pi)):.2f}'
                self.score.text = score
        except ValueError:
            print('error')


class MyMDTextField(MDTextField):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(MyMDTextField, self).insert_text(s, from_undo=from_undo)


class WindowManager(ScreenManager):
    pass


class TestScreen(Screen):
    pass


class Test01Screen(Screen):
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
        dialog = MDDialog(
            text=f'Your score: {result}/5',
            size_hint=[.8, .8],
            auto_dismiss=True,

            buttons=[
                MDRaisedButton(text='OK'),
            ],
        )
        dialog.open()


class Test02Screen(Screen):
    pass


class Test03Screen(Screen):
    pass


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MyCheckbox(IRightBodyTouch, MDCheckbox):
    pass


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    """Custom list item."""

    icon = StringProperty("android")


def read_text(file):
    with codecs.open(file, 'r', 'utf-8') as f:
        contents = f.read()
    return contents


class Content(BoxLayout):
    contents = read_text('knowledge_text/itroduction.html')
    text = StringProperty(contents)


class Content_2(BoxLayout):
    contents = read_text('knowledge_text/mateobr.txt')
    text_01 = StringProperty(contents)

    contents = read_text('knowledge_text/kindof.txt')
    text_02 = StringProperty(contents)


class Content_3(BoxLayout):
    pass


class Content_4(BoxLayout):
    pass


class Content_5(BoxLayout):
    pass


# plot
fig, ax = plt.subplots(tight_layout=True)
plt.plot([0, 0], [0, 0])
ax.set_ylabel('[...]', fontsize=8)
ax.set_title('[...]', fontsize=10)
ax.set_xlabel('[...]', fontsize=8)
ax.tick_params(axis="x", labelsize=8)
ax.tick_params(axis="y", labelsize=8)
canvas = fig.canvas


class Grafico(Screen):
    vc_01 = ObjectProperty(None)
    vc_02 = ObjectProperty(None)
    ra_01 = ObjectProperty(None)
    ra_02 = ObjectProperty(None)
    check_vc = ObjectProperty(None)
    check_vf = ObjectProperty(None)

    def create_plot(self):
        global fig, ax
        try:
            if self.vc_01 and self.vc_02 and self.ra_01 and self.ra_02:
                vc1 = int(self.vc_01.text)
                vc2 = int(self.vc_02.text)
                ra1 = int(self.ra_01.text)
                ra2 = int(self.ra_02.text)

                if self.check_vc.active:
                    # plt.clf()

                    ax.set_ylabel('Ra', fontsize=8)
                    ax.set_title('Ra = f(Vc)', fontsize=10)
                    ax.set_xlabel('Vc [mm]', fontsize=8)
                    ax.tick_params(axis="x", labelsize=8)
                    ax.tick_params(axis="y", labelsize=8)

                    plt.plot([ra1, ra2], [vc1, vc2])

                    canvas = fig.canvas
                    canvas.draw()
                elif self.check_vf.active:
                    ax.set_ylabel('Ra', fontsize=8)
                    ax.set_title('Ra = f(Vf)', fontsize=10)
                    ax.set_xlabel('Vf [mm]', fontsize=8)
                    ax.tick_params(axis="x", labelsize=8)
                    ax.tick_params(axis="y", labelsize=8)

                    canvas = fig.canvas
                    canvas.draw()

        except:
            print('Error')


class MyFigure(FigureCanvasKivyAgg):

    def __init__(self, **kwargs):
        super(MyFigure, self).__init__(plt.gcf(), **kwargs)
        self.text = str(time.asctime())


# # with open("pages/main.kv", encoding='utf-8') as f:
# b = Builder.load_file("pages/main.kv")

class MainApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        self.title = "App - Cutting Parameters"
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        self.a = 0
        self.b = 0
        self.c = 0

    def build(self):
        with codecs.open("pages/main.kv", 'r', encoding='utf-8') as f:
            self.root = Builder.load_string(f.read())

    def change_screen(self, screen_name, direction):
        # Get the window manager from the kv file
        screen_manager = self.root.ids['window_manager']
        screen_manager.current = screen_name
        screen_manager.transition.direction = direction

    def on_start(self):
        dic_01 = {'Wstęp': Content, "Materiały obrabiane": Content_2, 'Krawędź Skrawająca': Content_3,
                  'Materiały narzedziowe': Content_4, 'Zużycie narzędzia i konserwacja': Content_5}
        for i in dic_01:
            self.root.ids.machining_introduction_screen.ids.box.add_widget(
                MDExpansionPanel(

                    icon="icons/pytajnik.png",
                    content=dic_01[i](),
                    panel_cls=MDExpansionPanelOneLine(
                        text=i

                    )
                )
            )

    #  Switch tab
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        instance_tab.ids.label.text = tab_text

    # clear text from text input
    def clear_text(self, *args):
        for ar in args:
            ar.text = ''

    # def show_MDDialog(self):
    #         if not self.dialog:
    #             self.dialog = MDDialog(
    #                 text="Discard draft?",
    #                 size_hint=[.8, .8],
    #                 auto_dismiss=True,
    #
    #                 buttons=[
    #                      MDRaisedButton(text='OK'),
    #                 ],
    #             )
    #         self.dialog.open()

    def my_callback(self, text_of_selection, popup_widget):
        print(text_of_selection)


if __name__ == "__main__":
    MainApp().run()
