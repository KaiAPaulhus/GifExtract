import subprocess
import os


def toGif(folder=None, resize=True, animate=True):

    magic = "ImageMagick/animate.exe"
    imagedir = "imgs/" + folder
    outpath = "imgs/out"

    if not os.path.exists(outpath):
        os.makedirs(outpath)

    resizeargs = [
        imagedir,
        ' -resize 444x250',
        ' togif/small/small_%03d.png'
    ]
    animateargs = [
        outpath,
        ' -set delay 1x12',
        ' -loop 0',
        ' -coalesce',
        ' -layers optimize'
        ' +set comment'
        ' output.gif'
    ]
                        
    if resize:
        args = [magic, resizeargs]
        output = subprocess.check_output(args)
        print(output)
    if animate:
        args = [magic, animateargs]
        output = subprocess.check_output(args)
        print(output)
