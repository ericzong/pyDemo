import os
import shutil
import pyautogui
import wx
import configparser
import xml.etree.ElementTree as et


class EricApp(wx.App):

    def OnInit(self):
        FloatFrame()
        self.MainLoop()
        return True


class FloatFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title='Eric Tool', size=FloatFrame.get_size(),
                         pos=FloatFrame.get_position(),
                         style=wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR)
        self.config_file = 'app.ini'
        self.config = self.load_config()
        self.Bind(wx.EVT_MOUSE_EVENTS, self.on_mouse)
        target = FloatFileDropTarget(self)
        self.SetDropTarget(target)
        self.Show()

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config

    def on_mouse(self, event):
        if event.Dragging():
            mouse_position = pyautogui.position()
            self.SetPosition(wx.Point(mouse_position[0] - 25, mouse_position[1] - 25))

    @staticmethod
    def get_position():
        screen_dimension = wx.DisplaySize()
        return wx.Point(screen_dimension[0] - 300, 200)

    @staticmethod
    def get_size():
        return wx.Size(50, 50)


class FloatFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.finisher = FileFinisher(window)

    def OnDropFiles(self, x, y, file_names):
        self.finisher.do_process(file_names)
        return True


class FileFinisher(object):
    def __init__(self, window):
        super().__init__()
        self.config_file = 'app_file.xml'
        self.config = self.load_config()
        self.window = window

    def load_config(self):
        config = et.parse(self.config_file)
        return config

        return config

    def do_process(self, file_names):
        for file_name in file_names:
            self.move_file(file_name)

    def move_file(self, file_name):
        ext = os.path.splitext(file_name)[1]
        if ext:
            target = self.get_target(ext)
            print(target)
            if target:
                shutil.move(file_name, target)
                print(f'move {file_name} => {target}')

    def get_target(self, ext):
        file_node = self.config.find(f'./list/file[@ext="{ext}"]')
        return file_node.get('target')


if __name__ == '__main__':
    app = EricApp()
