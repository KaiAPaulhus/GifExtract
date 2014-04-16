from PyQt5 import QtCore
import subprocess
import os
import time
import re


class GifWorker(QtCore.QThread):

    progress = QtCore.pyqtSignal(QtCore.QObject, int, str, name="progressmade")

    def __init__(self, screen, args):
        QtCore.QThread.__init__(self)
        self.args = args
        self.screen = screen

    def run(self):
        args = self.args
        #TODO: Get location from config
        magick = "ImageMagick/convert.exe"
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
        animateargs = [
            ' -monitor ',
            imagedir + '*.png',
            ' -set delay 1x%i' % int(args['delay']),
            ' -loop %d' % int(args['loop']),
            ' -coalesce',
            ' -layers optimize',
            ' +set comment',
            ' imgs/out/%s.gif' % args['name']
        ]

        if args['resize']:
            args = [magick, resizeargs]
            output = subprocess.check_output(args)
            print(output)

        # args = [magick, animateargs]
        # output = subprocess.check_output(args)
        # self.progress.emit(self.screen, 100)

        percentstr = re.compile(
            r'(?P<action>\w+?)/.+?(?P<file_name>\[.+\]): '
            r'(?P<curr_file>\d+) of (?P<total_files>\d+),'
            r' (?P<percent>\d+)% complete')
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
