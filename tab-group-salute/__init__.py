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
gi.require_version('Gtk', '3.0')
gi.require_version('Gedit', '3.0')

from gi.repository import GObject, Gdk, Gtk, Gedit


class TabGroupSaluteAppActivatable(GObject.Object, Gedit.AppActivatable):

	__gtype_name__ = 'TabGroupSaluteAppActivatable'

	app = GObject.Property(type=Gedit.App)


	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		app = self.app

		binding_set = Gtk.binding_set_find('GeditView')
		Gtk.binding_entry_remove(
			binding_set,
			Gdk.KEY_asciitilde,
			Gdk.ModifierType.CONTROL_MASK
		)

		prev_accels = app.get_accels_for_action('win.previous-tab-group');
		next_accels = app.get_accels_for_action('win.next-tab-group');

		app.set_accels_for_action(
			'win.previous-tab-group',
			prev_accels + ['<Control>asciitilde']
		)
		app.set_accels_for_action(
			'win.next-tab-group',
			next_accels + ['<Control>grave']
		)

		self._prev_accels = prev_accels
		self._next_accels = next_accels

	def do_deactivate(self):
		app = self.app

		app.set_accels_for_action(
			'win.previous-tab-group',
			self._prev_accels
		)
		app.set_accels_for_action(
			'win.next-tab-group',
			self._next_accels
		)

		binding_set = Gtk.binding_set_find('GeditView')
		Gtk.binding_entry_add_signal_from_string(
			binding_set,
			'bind "<Control>asciitilde" { "change_case" (GTK_SOURCE_CHANGE_CASE_TOGGLE) }'
		)

		self._prev_accels = None
		self._next_accels = None
