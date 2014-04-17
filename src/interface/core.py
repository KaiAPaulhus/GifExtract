#The primary interface class, contains file dialog functions.

from interface.controls import FileDialog


def openDialog(screen, startdir, typefilter, dest, dirmode=False):
        browser = FileDialog.FileDialog(screen, dest, dirmode, screen)
        browser.setDirectory(startdir)
        browser.setNameFilter(typefilter)
        browser.show()