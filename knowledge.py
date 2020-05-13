import codecs

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine


def read_text(file):
    """"""
    with codecs.open(file, 'r', 'utf-8') as f:
        contents = f.read()
    return contents


class Introduction(BoxLayout):
    contents = read_text('knowledge_text/itroduction.txt')
    text = StringProperty(contents)


class Materials(BoxLayout):
    contents = read_text('knowledge_text/mateobr.txt')
    text_01 = StringProperty(contents)

    contents = read_text('knowledge_text/kindof.txt')
    text_02 = StringProperty(contents)


class Edge(BoxLayout):
    pass


class ToolsMaterials(BoxLayout):
    pass


class Usage(BoxLayout):
    pass


def introduction(self):
    dic = {'Wstęp': Introduction, "Materiały obrabiane": Materials, 'Krawędź Skrawająca': Edge,
              'Materiały narzedziowe': ToolsMaterials, 'Zużycie narzędzia i konserwacja': Usage}

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


def turning(self):
    dic = {'Wstęp': Introduction, "Materiały obrabiane": Materials, 'Krawędź Skrawająca': Edge,
           'Materiały narzedziowe': ToolsMaterials, 'Zużycie narzędzia i konserwacja': Usage}

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


def milling(self):
    pass


def drilling(self):
    pass