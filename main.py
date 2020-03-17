import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from random import randint
from kivy.core.window import Window
from kivy.utils import get_color_from_hex 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.weakproxy import WeakProxy
from kivy.animation import Animation
Window.size = (320,600)

kvfile = Builder.load_file('style.kv')


class Main(Screen):     
    
    def camera_screen(self):
        self.manager.get_screen('main').ids.btn_camera.color = get_color_from_hex('#2196F3')
        self.manager.get_screen('main').ids.btn_home.color = get_color_from_hex('#FFFFFF')
        self.manager.get_screen('main').ids.btn_user.color = get_color_from_hex('#FFFFFF')

        self.manager.get_screen('main').ids.master.clear_widgets()

        camera_layout = GridLayout()
        camera_layout.id = 'camera_layout'
        camera_layout.spacing=(0, 0.5)
        camera_layout.padding = 40,10,40,10
        camera_layout.cols=1
        camera_layout.row_default_height=self.height*0.25
        camera_layout.row_force_default=True

        lbl_camera = Label()
        lbl_camera.id = 'lbl_camera'
        lbl_camera.color = get_color_from_hex('#212121')
        lbl_camera.text = 'Camera Layout'

        self.manager.get_screen('main').ids[camera_layout.id] = \
            WeakProxy(camera_layout)

        self.manager.get_screen('main').ids[lbl_camera.id] = \
            WeakProxy(lbl_camera)

        self.manager.get_screen('main').ids.master.\
            add_widget(camera_layout)

        self.manager.get_screen('main').ids.camera_layout.\
            add_widget(lbl_camera)  

    def home_screen(self):
        self.manager.get_screen('main').ids.btn_camera.color = get_color_from_hex('#FFFFFF')
        self.manager.get_screen('main').ids.btn_home.color = get_color_from_hex('#2196F3')
        self.manager.get_screen('main').ids.btn_user.color = get_color_from_hex('#FFFFFF')

        self.manager.get_screen('main').ids.master.clear_widgets()

        home_layout = GridLayout()
        home_layout.id = 'home_layout'
        home_layout.spacing=(0, 0.5)
        home_layout.padding = 40,10,40,10
        home_layout.cols=1
        home_layout.row_default_height=self.height*0.25
        home_layout.row_force_default=True

        lbl_home = Label()
        lbl_home.id = 'lbl_home'
        lbl_home.color = get_color_from_hex('#212121')
        lbl_home.text = 'Home Layout'                    

        self.manager.get_screen('main').ids[home_layout.id] = \
            WeakProxy(home_layout)

        self.manager.get_screen('main').ids[lbl_home.id] = \
            WeakProxy(home_layout)

        self.manager.get_screen('main').ids.master.\
            add_widget(home_layout)

        self.manager.get_screen('main').ids.lbl_home.\
            add_widget(lbl_home)                        


    def user_screen(self):
        self.manager.get_screen('main').ids.btn_camera.color = get_color_from_hex('#FFFFFF')
        self.manager.get_screen('main').ids.btn_home.color = get_color_from_hex('#FFFFFF')
        self.manager.get_screen('main').ids.btn_user.color = get_color_from_hex('#2196F3')    

        self.manager.get_screen('main').ids.master.clear_widgets()

        user_layout = GridLayout()
        user_layout.id = 'user_layout'
        user_layout.spacing=(0, 0.5)
        user_layout.padding = 40,10,40,10
        user_layout.cols=1
        user_layout.row_default_height=self.height*0.25
        user_layout.row_force_default=True

        lbl_user = Label()
        lbl_user.id = 'lbl_home'
        lbl_user.color = get_color_from_hex('#212121')
        lbl_user.text = 'User Layout'

        self.manager.get_screen('main').ids[user_layout.id] = \
            WeakProxy(user_layout)

        self.manager.get_screen('main').ids[lbl_user.id] = \
            WeakProxy(lbl_user)

        self.manager.get_screen('main').ids.master.\
            add_widget(user_layout)

        self.manager.get_screen('main').ids.user_layout.\
            add_widget(lbl_user) 

    def menu_anim_open(self):
        anim_layout = Animation(x=250,duration=0.2)
        anim_layout.start(self.manager.get_screen('main').ids.header)
        anim_layout.start(self.manager.get_screen('main').ids.master)
        anim_layout.start(self.manager.get_screen('main').ids.grid_btn)

    def menu_anim_close(self):
        anim_layout = Animation(x=0,duration=0.2)
        anim_layout.start(self.manager.get_screen('main').ids.header)
        anim_layout.start(self.manager.get_screen('main').ids.master)
        anim_layout.start(self.manager.get_screen('main').ids.grid_btn)

sm = ScreenManager()
sm.add_widget(Main(name='main'))

class app(App):

    def build(self):
        return sm

app().run()        
