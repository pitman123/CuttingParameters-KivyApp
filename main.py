# -*- coding: utf-8 -*-
import re
import time
import codecs
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from kivymd.app import MDApp
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivymd import images_path
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.widget import Widget
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine
from kivymd.uix.list import IRightBodyTouch, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
# from kivya.kivymd.uix.button import MDFlatButton

from calculator import cuttingSpeed, spindleSpeed, metalRemovalRate, timeInCut

Window.size = (350, 550)


class WindowManager(ScreenManager):
    pass


#################################
# Home page
#################################

class MainScreen(Screen):
    """Main screen containg ..."""
    pass


class ParametersScreen(Screen):
    """Screen containing pages from moduls: """
    pass


class KnowledgeScreen(Screen):
    """..."""
    pass


class PlotScreen(Screen):
    """..."""
    pass


#################################
# All main screen from parameters
#################################

class TurningScreen(Screen):
    """"""
    pass


class MillingScreen(Screen):
    """"""
    pass


class DrillingScreen(Screen):
    """"""
    pass


class TappingScreen(Screen):
    """"""
    pass


class ReamingScreen(Screen):
    """"""
    pass


class TolerancesScreen(Screen):
    """"""
    pass


#################################
# All main screen from turning
#################################


class MyScreen(Screen):
    """...."""
    score = ObjectProperty(None)
    machined_diameter = ObjectProperty(None)
    spindle_speed = ObjectProperty(None)
    depth_of_cut = ObjectProperty(None)
    feed_per_revolution = ObjectProperty(None)
    cutting_speed = ObjectProperty(None)
    length_of_cut = ObjectProperty(None)
    start_diameter = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.submit, .3)  # add Clock


class CuttingSpeedScreen(MyScreen):
    """...."""

    def submit(self, *args):
        if self.machined_diameter.text and self.spindle_speed.text:
            md, ss = map(float, (self.machined_diameter.text, self.spindle_speed.text))
            self.score.text = f'{cuttingSpeed(md, ss):.2f}'  # calculate cutting speed


class SpindleSpeedScreen(MyScreen):
    """..."""

    def submit(self, *args):
        if self.machined_diameter.text and self.cutting_speed.text:
            md, cs = map(float, (self.machined_diameter.text, self.cutting_speed.text))
            self.score.text = f'{spindleSpeed(md, cs):.2f}'  # calculate spindle speed


class MetalRemovalRateScreen(MyScreen):
    """..."""

    def submit(self, *args):
        if self.depth_of_cut.text and self.feed_per_revolution.text and self.cutting_speed.text:
            doc, fpr, cs = map(float, (self.depth_of_cut.text, self.feed_per_revolution.text, self.cutting_speed.text))
            self.score.text = f'{metalRemovalRate(doc, fpr, cs):.2f}'  # calculate metal removal rate


class PowerRequirementScreen(MyScreen):
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

    def submit(self, *args):
        pass


class TimeInScreen(MyScreen):
    """..."""

    def submit(self, *args):
        if (self.start_diameter.text and self.cutting_speed.text and self.depth_of_cut.text
                and self.length_of_cut.text and self.machined_diameter and self.feed_per_revolution):
            sd, cs, soc, loc, md, fpr, = map(float, (self.start_diameter.text, self.cutting_speed.text,
                                                     self.depth_of_cut.text, self.length_of_cut.text,
                                                     self.machined_diameter, self.feed_per_revolution))
            self.score.text = f'{timeInCut(sd, cs, soc, loc, md, fpr):.2f}'


#################################
# All main screen from milling
#################################

class MillingCuttingSpeedScreen(MyScreen):
    pass


class MillingSpindleSpeedScreen(MyScreen):
    pass


class MillingTableFeedScreen(MyScreen):
    pass


class MillingRemovalRateScreen(MyScreen):
    pass


class MillingTimeInCutScreen(MyScreen):
    pass


class MillingTotalCycleTimeScreen(MyScreen):
    pass


class MillingPowerRequirement(MyScreen):
    pass


#################################
# All main screen from drilling
################################

class DrillingCuttingSpeedScreen(MyScreen):
    pass


class DrillingFeedForceScreen(MyScreen):
    pass


class DrillingFeedSpeedScreen(MyScreen):
    pass


class DrillingPowerRequirementScreen(MyScreen):
    pass


class DrillingTimeINCutScreen(MyScreen):
    pass


class DrillingTotalCycleTimeScreen(MyScreen):
    pass


#################################
# All main screen from tapping
################################

class TappingCuttingScreen(MyScreen):
    pass


class TappingPenetrationRateScreen(MyScreen):
    pass


class TappingSpindleSpeedScreen(MyScreen):
    pass


class TappingTimeInCutScreen(MyScreen):
    pass


class TappingTotalCycleTime(MyScreen):
    pass

#################################
# All main screen from reaming
################################

## Add !!!




#################################
# All main screen from knowledge
################################








# class KnowledgeScreen(Screen):
#     pass


class MachiningIntroductionScreen(Screen):
    with codecs.open("knowledge_text/itroduction.txt", 'r', 'utf-8') as f:
        contents = f.read()
    text = StringProperty(contents)


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class MyMDTextField(MDTextField):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(MyMDTextField, self).insert_text(s, from_undo=from_undo)


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
    contents = read_text('knowledge_text/itroduction.txt')
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
