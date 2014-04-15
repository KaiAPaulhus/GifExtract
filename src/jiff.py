import subprocess
import os


#Outdated file, kept for reference only.
def extractFrames():
    ffmpeg = "C:/Google_Drive/coding_projects/libraries/" \
             "ffmpeg-20140102/bin/ffmpeg.exe"

    video = "\"C:/Users/Kyras/Videos/Puella Magi Madoka Magica" \
            " The Movie Part 1 Hajimari no Monogatari.mp4\""
    start = "02:03:30"
    length = "02:05:50"

    ffargs = [
        ' -ss %s' % start,
        ' -i %s' % video,
        ' -t %s' % length,
        ' -qscale 0 ',
        ' -an ',
        ' -r 12 ',
        ' imgs/pmmm%03d.png'
    ]

    args = [ffmpeg, ffargs]
    output = subprocess.check_output(args)
    print(output)


def toGif(folder=None,resize=True,animate=True):
    magic = "C:/Google_Drive/coding_projects/libraries/" \
            "ImageMagick-6.8.8-1/convert"
    imgloc = "C:/Google_Drive/coding_projects/general_python_work/PyJiff/" \
             "togif/" + folder + "/*.png"
    smlimgloc = "C:/Google_Drive/coding_projects/general_python_work/" \
                "PyJiff/togif/small/*.png"

    smlpath = "C:/Google_Drive/coding_projects/general_python_work/" \
              "PyJiff/togif/small"
    if not os.path.exists(smlpath):
        os.makedirs(smlpath)

    resizeargs = [
        imgloc,
        ' -resize 444x250',
        ' togif/small/small_%03d.png'
    ]
    animateargs = [
        smlimgloc,
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


def addText():
    magic = "C:/Google_Drive/coding_projects/libraries/" \
            "ImageMagick-6.8.8-1/convert"
    imgloc = "C:/Google_Drive/coding_projects/general_python_work/" \
             "PyJiff/togif/text/test/img.png"
    outloc = "C:/Google_Drive/coding_projects/general_python_work/" \
             "PyJiff/togif/text/test/out.png"
    
    textargs = [
        imgloc,
        " -fill white",
        " -undercolor black",
        " -font \"Trebuchet MS\"",
        " -draw \"text 900,200\ 'I was stupid... so stupid.'\""
        " -gravity south ",
        outloc
        ]
    args = [magic, textargs]
    output = subprocess.check_output(args)
    print(output)
