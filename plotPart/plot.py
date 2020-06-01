"""
    The plot module, containing all screens and main set of plot part's app.
"""

import time
import matplotlib.pyplot as plt

from kivy.garden.matplotlib import FigureCanvasKivyAgg


# plot
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

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