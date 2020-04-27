from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

# class Computing:
#
#     def __init__(self, n, d):
#         self.n = n
#         self.d = d
#
#     def cutting_speed(self):
#
#         try:
#             if self.d.text and self.n.text:
#                 score = f'{(float(self.d.text) * float(self.n.text) * pi) / 1000:.2f}'
#                 self.n.text = score
#         except ValueError:
#             print('error')


# class MyCuttingSpeedScreen(Screen):
#     score = ObjectProperty(None)
#     machined_diameter = ObjectProperty(None)
#     spindle_speed = ObjectProperty(None)
#
#     def __init__(self, **kw):
#         super().__init__(**kw)
#         Clock.schedule_interval(self.submit, .5)
#
#     def submit(self, pi=3.14, *args):
#         self.score.text = '0'
#         try:
#             if self.root.machined_diameter.text and self.app.spindle_speed.text:
#                 score = f'{(float(self.app.machined_diameter.text) * float(self.app.spindle_speed.text) * pi) / 1000:.2f}'
#                 self.app.score.text = score
#         except ValueError:
#             print('error')