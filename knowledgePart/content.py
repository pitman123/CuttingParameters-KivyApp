"""
    The content module, containing all content and main set of knowledge screens.
"""
import codecs

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.font_definitions import theme_font_styles


def read_text(file):
    """Method allow read and output with utf-8 encoding """
    with codecs.open(file, 'r', 'utf-8') as f:
        contents = f.read()
    return contents


class MachiningIntroductionScreen(Screen):
    """Class represents the screen with basic knowledgePart of cutting parameters."""
    pass


####################################################################
#  All classes representing the introduction to cutting parameters
####################################################################

class IntroductionContent(MDBoxLayout):
    contents = read_text('knowledgePart/knowledge_text/itroduction.txt')
    text = StringProperty(contents)


class MaterialsContent(BoxLayout):
    contents = read_text('knowledgePart/knowledge_text/mateobr.txt')
    text_01 = StringProperty(contents)

    contents = read_text('knowledgePart/knowledge_text/kindof.txt')
    text_02 = StringProperty(contents)


class EdgeContent(BoxLayout):
    pass


class ToolsMaterialsContent(BoxLayout):
    pass


class UsageContent(BoxLayout):
    pass


####################################################################
#  All classes representing the turning
####################################################################

class IntroductionTurning(BoxLayout):
    contents = read_text('knowledgePart/knowledge_text/itroduction.txt')
    text = StringProperty(contents)


####################################################################
#  All classes representing the milling
####################################################################

# Add!!!

####################################################################
#  All classes representing the drilling
####################################################################

# Add!!!


######################################################################
# All content from introduction to cutting parameters
######################################################################


def introduction(self):
    dic = {'WSTĘP': IntroductionContent, "MATERIAłY OBRABIANE": MaterialsContent, 'KRAWĘDŹ SKRAWAJĄCA': EdgeContent,
           'MATERIAŁY NARZĘDZIOWE': ToolsMaterialsContent, 'ZUŻYCIE I KONSERWACJA': UsageContent}

    for i in dic:
        self.root.ids.machining_introduction_screen.ids.box.add_widget(
            MDExpansionPanel(
                icon="icons/education.png",
                content=dic[i](),
                panel_cls=MDExpansionPanelOneLine(
                    text=i,
                    font_style=theme_font_styles[9]

                )
            )
        )


def turning(self):
    dic = {'WSTĘP DO TOCZENIA': IntroductionTurning, "PROCEDURY WYBORU": MaterialsContent, 'OZNACZENIA': EdgeContent,
           'WYBÓR PŁYTEK': ToolsMaterialsContent, 'WYBÓR OPRAWEK': UsageContent}

    for i in dic:
        self.root.ids.knowledge_turning.ids.box.add_widget(
            MDExpansionPanel(
                icon="icons/education.png",
                content=dic[i](),
                panel_cls=MDExpansionPanelOneLine(
                    text=i,
                    font_style=theme_font_styles[9]
                )
            )
        )


def milling(self):
    dic = {'WSTĘP DO FREZOWANIA': IntroductionContent, "PROCEDURY WYBORU": MaterialsContent, 'STOSOWANIE': EdgeContent,
           }

    for i in dic:
        self.root.ids.knowledge_milling.ids.box.add_widget(
            MDExpansionPanel(
                icon="icons/education.png",
                content=dic[i](),
                panel_cls=MDExpansionPanelOneLine(
                    text=i,
                    font_style=theme_font_styles[9]
                )
            )
        )


def drilling(self):
    dic = {'WSTĘP DO WIERCENIA': IntroductionContent, "PROCEDURY WYBORU": MaterialsContent, 'STOSOWANIE': EdgeContent,
           'JAKOŚĆ OTWORU': ToolsMaterialsContent, }

    for i in dic:
        self.root.ids.knowledge_drilling.ids.box.add_widget(
            MDExpansionPanel(
                icon="icons/education.png",
                content=dic[i](),

                panel_cls=MDExpansionPanelOneLine(
                    text=i,
                    font_style=theme_font_styles[9],

                )
            )
        )

######################################################################
# All content from turning
######################################################################

# Add!!!

######################################################################
# All content from milling
######################################################################

# Add!!

######################################################################
# All content from drilling
######################################################################

# Add!!