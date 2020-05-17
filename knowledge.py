import codecs

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine


def read_text(file):
    """..."""
    with codecs.open(file, 'r', 'utf-8') as f:
        contents = f.read()
    return contents


class IntroductionContent(BoxLayout):
    contents = read_text('knowledge_text/itroduction.txt')
    text = StringProperty(contents)


class MaterialsContent(BoxLayout):
    contents = read_text('knowledge_text/mateobr.txt')
    text_01 = StringProperty(contents)

    contents = read_text('knowledge_text/kindof.txt')
    text_02 = StringProperty(contents)


class EdgeContent(BoxLayout):
    pass


class ToolsMaterialsContent(BoxLayout):
    pass


class UsageContent(BoxLayout):
    pass


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
                )
            )
        )





class IntroductionTurning(BoxLayout):
    contents = read_text('knowledge_text/itroduction.txt')
    text = StringProperty(contents)

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
                )
            )
        )
    pass











def drilling(self):
    dic = {'WSTĘP DO WIERCENIA': IntroductionContent, "PROCEDURY WYBORU": MaterialsContent, 'STOSOWANIE': EdgeContent,
           'JAKOŚĆ OTWORU': ToolsMaterialsContent,}

    for i in dic:
        self.root.ids.knowledge_drilling.ids.box.add_widget(
            MDExpansionPanel(
                icon="icons/education.png",
                content=dic[i](),
                panel_cls=MDExpansionPanelOneLine(
                    text=i,
                )
            )
        )
    pass