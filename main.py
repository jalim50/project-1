from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from random import random
Window.size=(400,600)
 

class MyApp(MDApp):
    def build(self):
        self.btn=MDRaisedButton(
            text='click here',
            pos_hint= {'center_x':0.5,'center_y':0.5},
            on_press=self.change_pos
        )
        self.screen=Screen()    
        self.screen.add_widget(self.btn)          
        return self.screen 
                     
    def change_pos(self,*args):
        x=random()
        y=random()
        self.btn.pos_hint={'center_x':x,'center_y':y}
        
    
          
    
    
    


MyApp().run()

        