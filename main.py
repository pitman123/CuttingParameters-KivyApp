# -*- coding: utf-8 -*-
"""
    The main application module, containing all main screens classes and main settings of app.

    Individual parts of the application and all of its applications and settings are in the following catalogs:
        "parametersPart" - contains all screens class of calculator and cutting parameters selection
        "knowledgePart" - contains all screens class of  knowledge of cutting parameters, milling, drilling
        "testPart" - contains all screens class of test of basic knowledge about cutting parameters
        "plotPart" - contains all screens class of  creating various charts to compare cutting parameters

    In the "pages" directory you can find all .kv files.

"""

import codecs
import re

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField

# import all parts app(knowledge, parameters, test, plot)
from parametersPart import parameters
from knowledgePart import content, knowledge
from testPart import test
from plotPart import plot


###############################################################
#   Main set
###############################################################
Window.size = (350, 550)  # set display screen size


class MyMDTextField(MDTextField):
    """Class for text field which only allow write floats and a single period."""
    pat = re.compile('[^0-9]')  # allow write floats (0-9)

    def insert_text(self, substring, from_undo=False):
        """Input text formatting function."""
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(MyMDTextField, self).insert_text(s, from_undo=from_undo)


class WindowManager(ScreenManager):
    """Class manage all screens of applications. """
    pass


################################################################
#  The first screen of the application
################################################################

class MainScreen(Screen):
    """The main application screen class containing the basic functions."""
    pass


class ParametersScreen(Screen):
    """The main screen containing various types of cutting."""
    pass


class KnowledgeScreen(Screen):
    """The main screen containing individual chapters related to cutting knowledgePart."""
    pass


class PlotScreen(Screen):
    """The main screen for choosing the type of graph comparing individual cutting parameters."""
    pass


class TestScreen(Screen):
    """The main screen containing all test about cutting knowledgePart."""
    pass


################################################################
#  Main app functions
################################################################

class MainApp(MDApp):
    """Main class include basic settings of app"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # set the main app title
        self.title = "App - Cutting Parameters"

        # open the main .kv file with screen manager
        with codecs.open("pages/main.kv", 'r', encoding='utf-8') as f:
            self.root = Builder.load_string(f.read())

        # set the main color style app
        self.theme_cls.theme_style = "Light"
        self.a = 0
        self.b = 0
        self.c = 0

    # Build application
    def build(self):
        return self.root

    # Change screens with property direction
    def change_screen(self, screen_name, direction):
        # Get the window manager from the kv file
        screen_manager = self.root.ids['window_manager']
        # Set the current screen
        screen_manager.current = screen_name
        # Set page change direction
        screen_manager.transition.direction = direction

    def on_start(self):
        # start all knowledgePart screens
        content.introduction(self)
        content.turning(self)
        content.drilling(self)
        content.milling(self)

    #  Switch tab
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        instance_tab.ids.label.text = tab_text

    # clear text from text input
    def clear_text(self, *args):
        for ar in args:
            ar.text = ''


if __name__ == "__main__":
    # Run application
    MainApp().run()
