import objc
from AppKit import NSApplication
from AppKit import NSKeyUp
from AppKit import NSSystemDefined
from PyObjCTools import AppHelper


class HotKeyApp(NSApplication):
    repeated = False

    @objc.python_method
    def setMusicMenu(self,menu):
        self.menu = menu

    def sendEvent_(self, event):
        if event.type() is NSSystemDefined and event.subtype() == 8:
            data = event.data1()
            key_code = (data & 0xFFFF0000) >> 16
            key_flags = data & 0x0000FFFF
            key_state = (key_flags & 0xFF00) >> 8
            key_repeat = key_flags & 0x1
        
        if key_state is NSKeyUp:
            if self.repeated:
                self.repeated = False
        elif key_code in (20, 18):
            self.menu.previous_song()
        elif key_code == 16:
            self.menu.pause()
        elif key_code in (19, 17):
            self.menu.next_song()