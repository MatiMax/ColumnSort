#    Plugin: ColumnSort
#    Author: Matthias M. Schneider
#   Verison: 2.0
# Copyright: IDC (I Don't Care) - Published under the GPL
#   Purpose: Sort lines by detecting columns separated by a tab character.
#	         The user can then choose the column to be used as sort key from a quick panel.
#            The plugin uses two commands as the handler of the pick panel has no access to the edit token,
#            so a second command is called with parameters to sort and replace the text.
import sublime, sublime_plugin

AUTO_FIELD_SEPARATORS = "\t,;:|/#"

class ColumnSortCommand(sublime_plugin.TextCommand):
	"""
	Command: column_sort
	"""
	def run(self, edit, rows_cols, col_num, field_separator, skip_header, ascending):
		# Check if the first line of the selection should be skipped
		starting_row = 1 if skip_header is True else 0
		# Sort the array of arrays with columns using a lambda function (see the Python Sort How-to)
		rows_cols_head = rows_cols[0:starting_row]
		rows_cols_tail = rows_cols[starting_row:]
		rows_cols_tail.sort(key=lambda col:col[col_num], reverse=ascending)
		rows_cols = rows_cols_head + rows_cols_tail
		# Produce the text for replacement by using a generator and according join function calls. Mind the trailling new-line character.
		sorded = "\n".join([field_separator.join(row) for row in rows_cols]) + "\n"
		# Now replace the selected text
		self.view.replace(edit, self.view.sel()[0], sorded)


class ColumnPickCommand(sublime_plugin.TextCommand):
	"""
	Command: column_pick
	"""
	rows_cols = None
	field_separator = None
	skip_header = None
	ascending = None

	def run(self, edit):
		# Get the selected text and split it in lines using a Sublime function
		text_lines = self.view.substr(self.view.sel()[0]).splitlines()
		# Return early if there is no selection
		if text_lines is None or len(text_lines) == 0: return

		# Load the settings afresh for each run
		settings = sublime.load_settings("ColumnSort.sublime-settings")

		# Set up the instance variables
		self.field_separator = settings.get('columnsort_field_separator')
		self.skip_header = settings.get('columnsort_skip_header')
		self.ascending = {'ascending': False, 'descending': True}[settings.get('columnsort_sort_direction')]

		# Check the field separator setting and try to find one if the setting is "auto"
		if self.field_separator == "auto":
			self.field_separator = None
			for fs in AUTO_FIELD_SEPARATORS:
				if len(text_lines[0].split(fs)) > 1:
					self.field_separator = fs
					break

		# Return if no field separator could be detected, so sorting will not be promoted
		if self.field_separator is None: return
		
		# Use a generator with the split function to get an array of arrays containing lines with its columns
		self.rows_cols = [line.split(self.field_separator) for line in text_lines]
		# Show a quick panel containing the values of the columns of the first line
		self.view.window().show_quick_panel(self.rows_cols[0], self.column_selected)

	def column_selected(self, col_num):
		# If the user didn't abort the action actually run the column_sort command
		if col_num >= 0:
			self.view.run_command('column_sort', {
				'rows_cols':self.rows_cols,
				'col_num':col_num,
				'field_separator': self.field_separator,
				'skip_header': self.skip_header,
				'ascending': self.ascending
			})
