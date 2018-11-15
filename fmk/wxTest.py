import pyautogui
import wx


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
        self.Bind(wx.EVT_MOUSE_EVENTS, self.on_mouse)
        target = FloatFileDropTarget(self)
        self.SetDropTarget(target)
        self.Show()

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

    def OnDropFiles(self, x, y, file_names):
        print(str(file_names))
        return True


if __name__ == '__main__':
    app = EricApp()
