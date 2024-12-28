# -*- coding: utf-8 -*-
#
# __init__.py
# This file is part of Tab Group Salute, a plugin for gedit
#
# Copyright (C) 2018 Jeffery To <jeffery.to@gmail.com>
# https://github.com/jefferyto/gedit-tab-group-salute
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('GObject', '2.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Gedit', '3.0')
gi.require_version('Gtk', '3.0')

from gi.repository import GObject, Gdk, Gedit, Gtk
from .utils import connect_handlers, disconnect_handlers
from . import log

CONTROL_MASK = Gdk.ModifierType.CONTROL_MASK
CONTROL_SHIFT_MASK = Gdk.ModifierType.CONTROL_MASK | Gdk.ModifierType.SHIFT_MASK


class TabGroupSaluteWindowActivatable(GObject.Object, Gedit.WindowActivatable):

	__gtype_name__ = 'TabGroupSaluteWindowActivatable'

	window = GObject.Property(type=Gedit.Window)


	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		if log.query(log.INFO):
			Gedit.debug_plugin_message(log.format("%s", self.window))

		connect_handlers(
			self, self.window,
			['key-press-event'],
			'window'
		)

	def do_deactivate(self):
		if log.query(log.INFO):
			Gedit.debug_plugin_message(log.format("%s", self.window))

		disconnect_handlers(self, self.window)

	def do_update_state(self):
		pass


	def on_window_key_press_event(self, window, event):
		if log.query(log.INFO):
			Gedit.debug_plugin_message(log.format("%s, key=%s", window, Gdk.keyval_name(event.keyval)))

		# we assume the key above tab has the keycode 49
		# see https://gitlab.gnome.org/GNOME/metacity/blob/master/src/core/above-tab-keycode.c

		if event.hardware_keycode != 49:
			if log.query(log.DEBUG):
				Gedit.debug_plugin_message(log.format("keycode is %s, skipping", event.hardware_keycode))

			return False

		action_name = None
		state = event.state & Gtk.accelerator_get_default_mod_mask()

		if state == CONTROL_MASK:
			action_name = 'next-tab-group'
		elif state == CONTROL_SHIFT_MASK:
			action_name = 'previous-tab-group'

		if action_name is None:
			if log.query(log.DEBUG):
				Gedit.debug_plugin_message(log.format("neither ctrl nor ctrl+shift held, skipping"))

			return False

		if log.query(log.DEBUG):
			Gedit.debug_plugin_message(log.format("activating %s", action_name))

		window.lookup_action(action_name).activate()

		return True

