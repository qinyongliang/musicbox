import ctypes
def play():
    print("play from python")

def nextSong():
    print("next song from python")

def lastSong():
    print("last song from python")

if __name__ == "__main__":
    lib = ctypes.cdll.LoadLibrary("NEMbox/osx/HotKey.lib")
    playControll = ctypes.CFUNCTYPE(None)(play)
    nextControll = ctypes.CFUNCTYPE(None)(nextSong)
    lastControll = ctypes.CFUNCTYPE(None)(lastSong)
    lib.setContorllFunc(playControll,nextControll,lastControll)
    lib.setup()