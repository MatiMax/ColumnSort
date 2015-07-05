#    Plugin: ColumnSort
#    Author: Matthias M. Schneider
#   Verison: 1.0
# Copyright: None - Published under the GPL
#   Purpose: Sort lines by detecting columns separated by a tab character.
#	         The user can then choose the column to be used as sort key from a quick panel.
#            The plugin uses two commands as the handler of the pick panel has no access to the edit token,
#            so a second command is called with parameters to sort and replace the text.
import sublime, sublime_plugin


class ColumnSortCommand(sublime_plugin.TextCommand):
	"""
	Command: column_sort
	"""
	def run(self, edit, rows_cols, col_num):
		# Sort the array of arrays with columns using a lambda function (see the Python Sort How-to)
		rows_cols.sort(key=lambda col:col[col_num])
		# Produce the text for replacement by using a generator and according join function calls. Mind the trailling new-line character.
		sorded = "\n".join(["\t".join(row) for row in rows_cols]) + "\n"
		# Now replace the selected text
		self.view.replace(edit, self.view.sel()[0], sorded)


class ColumnPickCommand(sublime_plugin.TextCommand):
	"""
	Command: column_pick
	"""

	rows_cols = None

	def run(self, edit):
		# Get the selected text and split it in lines using a Sublime function
		text_lines = self.view.substr(self.view.sel()[0]).splitlines()
		# Use a generator with the split function to get an array of arrays containing lines with its columns
		self.rows_cols = [line.split('\t') for line in text_lines]

		# Show a quick panel containing the values of the columns of the first line
		self.view.window().show_quick_panel(self.rows_cols[0], self.column_selected)

	def column_selected(self, col_num):
		# If the user didn't abort the action actually run the column_sort command
		if col_num >= 0:
			self.view.run_command('column_sort', {'rows_cols':self.rows_cols, 'col_num':col_num})
