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