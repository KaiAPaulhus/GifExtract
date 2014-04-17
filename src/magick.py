from PyQt5 import QtCore
import subprocess
import os
import re


class GifWorker(QtCore.QThread):

    progress = QtCore.pyqtSignal(QtCore.QObject, int, str, name="progressmade")

    def __init__(self, screen, args):
        QtCore.QThread.__init__(self)
        self.args = args
        self.screen = screen

    def run(self):
        args = self.args
        magickdir = self.screen.config.getKey('gen_imagemagick')
        magick = magickdir + "/convert.exe"
        imagedir = "imgs/" + args['name'] + '/'
        outpath = "imgs/out"

        if not os.path.exists(outpath):
            os.makedirs(outpath)

        if not os.path.exists(imagedir + 'small/'):
            os.makedirs(imagedir + 'small/')
        smallout = imagedir + '/small/out%03d.png'
        resizeargs = [
            imagedir + '*.png',
            ' -resize %sx%s' % (args['width'], args['height']),
            ' -monitor ',
            smallout
        ]

        if args['resize']:
            animatein = imagedir + 'small/*.png'
        else:
            animatein = imagedir + '*.png'

        animateargs = [
            ' -monitor ',
            animatein,
            ' -set delay 1x%i' % int(args['delay']),
            ' -loop %d' % int(args['loop']),
            ' -coalesce',
            ' -layers optimize',
            ' +set comment',
            ' imgs/out/%s.gif' % args['name']
        ]
        percentstr = re.compile(
            r'(?P<action>\w+?)/.+?(?P<file_name>\[.+\]): '
            r'(?P<curr_file>\d+) of (?P<total_files>\d+),'
            r' (?P<percent>\d+)% complete')

        if args['resize']:
            args = [magick, resizeargs]
            process = subprocess.Popen(args,
                                       stderr=subprocess.PIPE,
                                       universal_newlines=True)

            while True:
                line = process.stderr.readline()
                if not line:
                    break
                result = percentstr.match(line)
                if result is not None:
                    action = str(result.group('action'))
                    percent = int(result.group('percent'))
                    self.progress.emit(self.screen, percent, action)

        args = [magick, animateargs]
        process = subprocess.Popen(args,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True)

        while True:
            line = process.stderr.readline()
            if not line:
                break
            result = percentstr.match(line)
            if result is not None:
                action = str(result.group('action'))
                percent = int(result.group('percent'))
                self.progress.emit(self.screen, percent, action)


class getImageSize(QtCore.QThread):

    update = QtCore.pyqtSignal(QtCore.QObject, str, str)

    def __init__(self, screen, folder):
        QtCore.QThread.__init__(self)
        self.folder = folder
        self.screen = screen

    def run(self):
        matchstr = re.compile(r'(?P<width>\d+)x(?P<height>\d+) ')
        magickdir = self.screen.config.getKey('gen_imagemagick')
        indentify = magickdir + "/identify.exe"
        loc = "imgs/%s/" % self.folder
        idargs = [
            ' %sout001.png' % loc
        ]
        args = [indentify, idargs]

        process = subprocess.Popen(args, stdout=subprocess.PIPE,
                                   universal_newlines=True)

        while True:
            line = process.stdout.readline()
            if not line:
                break
            result = matchstr.search(line)
            if result is not None:
                width = result.group('width')
                height = result.group('height')
                self.update.emit(self.screen, width, height)


class CommandFormatter(QtCore.QThread):

    progress = QtCore.pyqtSignal(QtCore.QObject, int, str, name="progressmade")

    def __init__(self, display=None, screen=None):
        QtCore.QThread.__init__(self)
        self.display = display
        self.listargs = []
        self.afm = None
        self.cmdorder = None
        self.screen = screen

    def run(self):
        if self.listargs is not []:
            self.testResults()

    def setDisplay(self, disp):
        self.display = disp

    def getCommandOrder(self):
        if self.afm is None:
            with open('data/autoformat_imagemagick.afm') as file:
                self.afm = file.readlines()

        if self.cmdorder is None:
            order = dict()

            for command in self.afm:
                if command[0] != "#":
                    cmd = command.split('\t')
                    order[cmd[0]] = cmd[1]
            self.cmdorder = order
        return self.cmdorder

    def updateString(self, valdict):
        cmdorder = self.getCommandOrder()
        arglist = [' -monitor ']
        for x in range(0, 99):
            for k, v in valdict.items():
                priority = cmdorder[k]
                if str(priority) == str(x):
                    formattedarg = self.formatArguement(k, v)
                    arglist.append(formattedarg)
        self.listargs = arglist

    def writeCommand(self, strin):
        self.display.setText(strin)

    def formatArguement(self, key, value):
        if self.afm is None:
            with open('data/autoformat_imagemagick.afm') as file:
                self.afm = file.readlines()

        for command in self.afm:
            if command[0] != "#":
                cmd = command.split('\t')
                if str(cmd[0]) == key:
                    return str(cmd[2]).replace('%s', str(value)).rstrip()

    def testResults(self):

        percentstr = re.compile(
            r'(?P<action>\w+?)/.+?(?P<file_name>\[.+\]): '
            r'(?P<curr_file>\d+) of (?P<total_files>\d+),'
            r' (?P<percent>\d+)% complete')

        magickdir = self.screen.config.getKey(
            'gen_imagemagick') + '/convert.exe'
        args = [magickdir, self.listargs]
        process = subprocess.Popen(args,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True)

        itercount = 0
        while True:
            line = process.stderr.readline()
            if not line:
                break

            itercount += 1
            if itercount == 5000:
                itercount = 0
                result = percentstr.match(line)
                if result is not None:
                    action = str(result.group('action'))
                    percent = int(result.group('percent'))
                    self.progress.emit(self.screen, percent, action)