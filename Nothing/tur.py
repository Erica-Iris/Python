#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self, title):
        super(MyFrame, self).__init__(None, title=title, size=(250, 250))
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_KEY_DOWN, self.on_key)
        self.Centre()
        self.Show()

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush(wx.LIGHT_GREY))
        dc.Clear()
        dc.DrawRoundedRectangle(30, 30, 100, 100, 2)
        dc.DrawLine(25, 150, 190, 150)
        dc.DrawText("hello world", 35, 160)

    def on_key(self, event):
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_UP:
            print("UP")
        elif key_code == wx.WXK_DOWN:
            print("down")
        elif key_code == wx.WXK_LEFT:
            print("left")
        elif key_code == wx.WXK_RIGHT:
            print("right")

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame('appStudy')
        frame.Show(True)
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
    