
import sublime, sublime_plugin
import os

class CopyPathToClipboard(sublime_plugin.TextCommand):
  def run(self, edit):
    line_number, column = self.view.rowcol(self.view.sel()[0].begin())
    line_number += 1
    content = self.view.file_name() + ":" + str(line_number)
    prefix = "/Users/joshua_lee/Development/airbnb/"
    if prefix in content: content = content[len(prefix):]
    sublime.set_clipboard(content)
