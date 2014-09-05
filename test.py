import wx
import sys
import threading
import calculation
import serial

class flyData(threading.Thread):
	"""docstring for flyData"""
	def __init__(self, arg):
		threading.Thread.__init__(self)
		self.arg = arg
'''
	def run(self):
		pass
	def stop(self):
		pass
		'''


class Frame(wx.Frame):

	def __init__(self,parent,id,title,pos,size):
		print "Frame __init__"
		wx.Frame.__init__(self,parent,id,title,pos,size)
		panel = wx.Panel(self)
		button = wx.Button(panel,label="Close",pos=(10,10))
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)

	def OnCloseWindow(self,event):
		print "Destroy"
		self.Destroy()

class App(wx.App):

	def __init__(self,redirect=True,filename=None):
		print "App __init__"
		wx.App.__init__(self,redirect,filename)
		

	def OnInit(self):
		print "OnInit"
		self.frame = Frame(parent=None,id=-1,title='My Demo',pos=(10,10),size=(600,400))
		self.frame.Show()
		self.SetTopWindow(self.frame)
		print>>sys.stderr,"A pretend error message"
		return True

	def OnExit(self):
		print "OnExit"
		
if __name__=='__main__':
	#app = App(redirect=True)
	print "before MainLoop"
	#app.MainLoop()
	print "after MainLoop"
	t = calculation.CalDistance(39.9327010000,116.3976510000,39.1420810000,117.1818350000)#39.9327010000,116.3976510000   39.1420810000,117.1818350000
	print t