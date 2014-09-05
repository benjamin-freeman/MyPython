import wx
import sys
import math
import threading

EARTH_RADIUS = 6377.830
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

def rad(temp):
	return temp*math.pi/180.0

def CalDistance(lat1,lng1,lat2,lng2):
	radLat1 = rad(lat1)
	radLat2 = rad(lat2)
	a = radLat1 - radLat2
	b = rad(lng1) - rad(lng2)
	s = 2*math.asin(math.sqrt(math.pow(a/2,2)+math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin(b/2),2)))
	s = s*EARTH_RADIUS*1000
	return s
		
if __name__=='__main__':
	#app = App(redirect=True)
	print "before MainLoop"
	#app.MainLoop()
	print "after MainLoop"
	t = CalDistance(39.9327010000,116.3976510000,39.1420810000,117.1818350000)#39.9327010000,116.3976510000   39.1420810000,117.1818350000
	print t