#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Replace removed bundled font them with symlinks
    shelltools.sym("/usr/share/fonts/dejavu/DejaVuSans.ttf", "%s/usr/share/stellarium/data/DejaVuSans.ttf" % get.installDIR())
    shelltools.sym("/usr/share/fonts/dejavu/DejaVuSansMono.ttf", "%s/usr/share/stellarium/data/DeJaVuSansMono.ttf" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "doc/images/stellarium-logo.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
