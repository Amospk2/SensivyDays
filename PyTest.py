from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, WipeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import json
class Dia(BoxLayout):
	def __init__(self,texto = '', titulo = '', **kwargs):
		super().__init__(**kwargs)
		self.ids.lab.text = titulo
		self.ids.lab2.text = texto
class Box(BoxLayout):
	titu = mensa = ''
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.titu = self.ids.titu.text
		self.mensa = self.ids.mensa.text
		
class Tela1(Screen):
	pass
		
class PyTest(App):
	Dias = Dya = {}
	with open('dias.json', 'r') as file:
		Dya = Dias = json.load(file)
	def add(self, *args):
		for D in self.Dya:
			self.root.ids.boxi.add_widget(Dia(self.Dya[D], D))
		self.Dya = {}
	theme_cls = ThemeManager()
	menu_items = [
	{'viewclass':'MDMenuItem',
          'text':'Help!'}, {'viewclass':'MDMenuItem', 'text': 'Sair'}]
	def acao(self, texto):
		if texto == 'Menu lateral':
			self.root.toggle_nav_drawer()
		if texto == 'Help!':
			self.root.ids.sm.current = 'Help'
		if texto == 'Sair':
			self.stop()
	def addday(self, titulo, mensagem, *args):
		self.Dias[titulo] = mensagem
		with open('dias.json', 'w') as dia:
			json.dump(self.Dias, dia)
		self.root.ids.boxi.add_widget(Dia(mensagem, titulo))
		self.pop.dismiss()
	pop = None
	def popup(self, *args):
		self.pop = Popup(title = '				Adicione seu dia:', content=Box(),size_hint=(None,None),size=(self.root.size), auto_dismiss=False)
		self.pop.open()
	def change(self, titu, mensa,*args):
		self.root.ids.sm.current = 'Tela02'
		self.root.ids.t2lab.text =str('          ' + titu)
		self.root.ids.t2lab2.text = str('     ' +mensa)
	def put(self, titu, *args):
		self.Dias.pop(titu)
		with open('dias.json', 'w') as dia:
			json.dump(self.Dias, dia)
	def curre(self, tela, *args):
		self.root.ids.sm.current = tela
		self.root.ids.sm.transition.direction = 'right'
			
PyTest().run()