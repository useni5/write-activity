import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import os

class FakeWriteActivity:
    def __init__(self):
        self.text_buffer = Gtk.TextBuffer()
        self.text_buffer.set_text("Hello world!")

        GLib.timeout_add(120000, self.autosave)  # 2 minutes

    def autosave(self):
        start_iter = self.text_buffer.get_start_iter()
        end_iter = self.text_buffer.get_end_iter()
        text = self.text_buffer.get_text(start_iter, end_iter, True)

        autosave_path = os.path.expanduser("~/WriteActivity_Autosave.txt")

        with open(autosave_path, 'w') as file:
            file.write(text)

        print("✅ Autosaved text!")
        return True

if __name__ == '__main__':
    activity = FakeWriteActivity()
    Gtk.main()
