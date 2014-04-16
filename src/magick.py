from PyQt5 import QtCore
import subprocess
import os


class GifWorker(QtCore.QThread):

    progress = QtCore.pyqtSignal(QtCore.QObject, int, name="progressmade")

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
        self.progress.emit(self.screen, 5)
        resizeargs = [
            imagedir + '*.png',
            ' -resize %sx%s' % (args['width'], args['height']),
            ' -monitor ',
            smallout
        ]
        animateargs = [
            imagedir + '*.png',
            ' -set delay 1x%i' % int(args['delay']),
            ' -loop %d' % int(args['loop']),
            ' -coalesce',
            ' -layers optimize',
            ' -monitor',
            ' +set comment',
            ' imgs/out/%s.gif' % args['name']
        ]

        if args['resize']:
            args = [magick, resizeargs]
            output = subprocess.check_output(args)
            print(output)
            self.progress.emit(self.screen, 50)
        args = [magick, animateargs]
        output = subprocess.check_output(args)
        self.progress.emit(self.screen, 100)