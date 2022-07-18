from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.modalview import ModalView

KV = '''
Screen:
  canvas.before:
    Color:
      rgb: [.5,.5,.5]
    Rectangle:
      pos: self.pos
      size: self.size
  BaseBoxLayout:
    btn_popup: btn_popup
    orientation: "vertical"
    Label:
      text: "You are in the BaseBoxLayout"
      font_size: 30
    Button:
      id: btn_popup
      text: "Display Popup"
      on_press:
        self.parent.call_popup()

<CustomPopup>
  box_popup: box_popup
  label_title: label_title
  anchor_popup: anchor_popup

  BoxLayout:
    id: box_popup
    orientation: 'vertical'
    canvas.before:
      Color:
        rgb: [.5,.7,.5]
      RoundedRectangle:
        pos: self.pos
        size: self.size
        radius: [(5,5),(5,5),(5,5),(5,5)]
      Color:
        rgb: [.3,.3,.3]
      RoundedRectangle:
        pos: (self.x + (self.width * .03 * .5), self.y + root.anchor_popup.height)
        size: (self.width * .97, 3)
        radius: [(2,2),(2,2),(2,2),(2,2)]
    Label:
      id: label_title
      text: "You can do this!"
      size_hint: (1, .3)

    PopupAnchor
      id: anchor_popup
      size_hint: (1, .7)

<PopupAnchor>
  btn_popup: btn_popup
  Button:
    id: btn_popup
    text: 'dismiss'
    on_press:
      root.button_pressed()

'''


class BaseBoxLayout(BoxLayout):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)

  def call_popup(self):
    self.popup = CustomPopup()
    self.popup.open()


class CustomPopup(ModalView):
  anchor_popup = ObjectProperty(AnchorLayout())

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.size_hint = (.3,.3)

  ### This seemed necessary but apparently not ###
  # def on_touch_down(self, touch):
  #   return super().on_touch_down(touch)#This allows the children to recieve touch
  #   # return True# This is key to "digest the event and stop it propagate further"


class PopupAnchor(AnchorLayout):

  def button_pressed(self):
    print('self.parent.parent:', self.parent.parent)#CustomPopup
    print('self.parent.parent.parent:', self.parent.parent.parent)#Window
    self.parent.parent.dismiss()


class MainApp(MDApp):
  def build(self):
    return Builder.load_string(KV)

if __name__ == '__main__':
  MainApp().run()
