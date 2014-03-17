

import wx
# from wx.lib.wordwrap import wordwrap
import time
from reduction import execute

class MyFrame(wx.Frame):
    
#-----------------------------------------------------------------------------------------------------------------
    def __init__(self, parent, id, title):
        # this will be self
        wx.Frame.__init__(self, parent, id, title)
        # add panel
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('pink')

         # create a status bar at the bottom----------
        #self.CreateStatusBar()
        #self.SetStatusText("Summarizer")
        self.sb = wx.StatusBar(self, wx.ID_ANY)
        # set the status bar with three fields
        self.sb.SetFieldsCount(3)
        # set an absolute status field width in pixels
        # (negative indicates a variable width field)
        self.sb.SetStatusWidths([-1, -1, -1])
        self.SetStatusBar(self.sb)
        # put some text into field 0 (most left field)
        self.sb.SetStatusText("some text in field 0", 0)
        self.sb.SetStatusText("some text in field 1", 1)

         # use a timer to drive a date/time string in field 3
        # here the most right field of the statusbar
        self.timer = wx.PyTimer(self.onUpdate)
        # update every 1000 milliseconds
        self.timer.Start(1000)
        self.onUpdate()


        #menu bar-----------
        menu = wx.Menu()
        # the optional & allows you to use alt/a
        # the last string argument shows in the status bar on mouse_over
        menu_about = menu.Append(wx.ID_ANY, "&About", "About message")
        menu.AppendSeparator()
        # the optional & allows you to use alt/x
        #menu_exit = menu.Append(wx.ID_ANY, "E&xit", "Quit the program")

        # create a menu bar at the top---
        menuBar = wx.MenuBar()
        # the & allows you to use alt/f
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

         # bind the menu events to an action/function/method
        self.Bind(wx.EVT_MENU, self.onMenuAbout)
        #.Bind(wx.EVT_MENU, self.onCloseWindow)

         # now add the needed widgets
        self.label1 = wx.StaticText(panel, -1, 'Enter the text:')
        self.entry1 = wx.TextCtrl(panel, -1, 'here')
        self.button1 = wx.Button(panel, -1, 'Summarize it! ')
        self.button1.SetBackgroundColour('yellow')
        self.button1.Bind(wx.EVT_BUTTON, self.onCmd)
        info = "Output will be displayed here"
        self.display = wx.TextCtrl(panel, -1, info, size=(250, 100), 
            style=wx.TE_MULTILINE)
         #Import reduction.py
         #reduction.execute
         
        # use gridbagsizer for layout of widgets
        # set optional vertical and horizontal gaps
        sizer = wx.GridBagSizer(vgap=5, hgap=10)
        sizer.Add(self.label1, pos=(0, 0))       # pos(row,column)
        sizer.Add(self.entry1, pos=(0, 1))  # row 0, column 1

        # span=(1, 2) --> allow to span over 2 columns 
        sizer.Add(self.button1, pos=(1, 0), span=(1, 2))
        sizer.Add(self.display, pos=(2, 0), span=(1, 2))
        
        # use boxsizer to add border around sizer
        border = wx.BoxSizer()
        border.Add(sizer, 0, wx.ALL, 20)
        panel.SetSizerAndFit(border)
        self.Fit()

    def onMenuAbout(self, event):
        dlg = wx.MessageDialog(self,
            "A text summarizer by the students of B.E Computers from Xavier Institute of Engineering\n"
            "It will help you to save time.",
            "About", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    #def onMenuExit(self, event):
        # via wx.EVT_CLOSE event
        #self.Close(True)

    def onCloseWindow(self, event):
        self.Close(True)


        

        
    def onUpdate(self):
        t = time.localtime(time.time())
        st = time.strftime("%d-%b-%Y   %I:%M:%S", t)
        # put date/time display string into field 2
        self.sb.SetStatusText(st, 2)

       
       
    def onCmd(self, event):
        """process data and show result"""
        # get the data from the input widget
        string1 = self.entry1.GetValue()
        # do the processing ...
        proc_data = string1   
        # show the result ...
        self.display.SetValue(execute(proc_data))
        

app = wx.App(redirect=False)
frame = MyFrame(None, -1, "Summarizer")
frame.Show()
app.MainLoop()
