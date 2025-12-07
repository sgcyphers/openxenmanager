#!/usr/bin/env python3
# -----------------------------------------------------------------------
# OpenXenManager
#
#    Updated to use Python3 and PyGObject - 2025-12-07
#    Copyright (C) 2025  Steve Cyphers (c-three@c3cyphers.com)
#
#
# Copyright (C) 2014 Daniel Lintott <daniel@serverb.co.uk>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.
#
# -----------------------------------------------------------------------

#    Python3+ uses PyGObjact; GTK2 is obsolete
import gi

import sys
import os


# FIXME: rather pathetic fix for ubuntu to show menus -  GTK3 migration should
# fix this  - Removed 2025-12-05 SgC
#  os.environ['UBUNTU_MENUPROXY'] = '0'

sys.path.append('./src')

from OXM.window import oxcWindow

if __name__ == "__main__":
    # Main function
    wine = oxcWindow()
    gtk.main()
