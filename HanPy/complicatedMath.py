import threading
import wx
import solveEquation


def solveEquation(equation):
    solveEquation.solveEquation(equation)


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Solve your Math Equation', size=(400, 500))
        panel = wx.Panel(self)

        self.lblAmount = wx.StaticText(panel, pos=(
            5, 5), label='Single line equation:')
        self.txtAmount = wx.TextCtrl(panel, pos=(5, 25), size=(375, 20))

        my_btn = wx.Button(panel, pos=(122, 65), size=(
            150, 30), label='Solve equation')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        self.percentage = wx.StaticText(
            panel, size=(30, 20), pos=(187, 100), label='100%')

        self.solution = wx.TextCtrl(panel, pos=(5, 125), size=(375, 300), style=wx.TE_MULTILINE ^ wx.TE_READONLY) 
        self.solution.write('Solution: \n')
        self.solution.write('do it yourself moron')

        self.Show()

    def on_press(self, event):
        equation = self.txtAmount.GetValue()
        self.percentage.SetLabel('0%')
        self.percentage.Refresh()
        

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()