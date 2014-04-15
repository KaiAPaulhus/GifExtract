import subprocess
import json
import os


class FFmpeg(object):
    
    def __init__(self, binfolder):
        self.ffmpeg = binfolder + "/ffmpeg.exe"
        self.probe = "ffmpeg/bin/ffprobe.exe"

    def getVideoInfo(self, file):
        subargs = [
            " -v quiet",
            " -print_format json",
            " -show_format",
            " -show_streams",
            " %s" % file,
        ]
        args = [self.probe, subargs]
        output = subprocess.check_output(args)
        output = output.decode(encoding='UTF-8')
        data = FileData(output)
        return data
            
    def extractFrames(self, job):
        if not os.path.exists('imgs/' + job['desc']):
            os.mkdir('imgs/' + job['desc'])
        subargs = [
            " -ss %s" % job["time_start"],
            " -i %s" % job["srcfile"],
            " -t %s" % job["duration"],
            " -qscale 0",
            " -an",
            " -r %s" % job["fps"],
            " imgs/%s/out%%03d.png" % job['desc'],
        ]

        args = [self.ffmpeg, subargs]
        output = subprocess.check_output(args)
        print(output)


class FileData(object):

    def __init__(self, jsontext):
        self.json = jsontext
        self.data = json.loads(jsontext)
        
        self.streams = self.data['streams']
    
    #Returns the FPS of the first video stream.
    def getFramesPerSecond(self):
        for x in range(0, len(self.data['streams'])):
            if self.data['streams'][x]['codec_type'] == "video":
                fps = self.data['streams'][x]['r_frame_rate']
                nums = fps.split('/')
                truefps = float(nums[0]) / float(nums[1])
                return truefps

    #Returns a list of subtitle files            
    def getSubtitleList(self):
        count = len(self.streams)
        subs = []
        for x in range(0, count):
            stream = self.streams[x]
            if stream['codec_type'] == "subtitle":
                index = stream['index']
                name = stream['tags']['handler_name']
                language = stream['tags']['language']
                codec = stream['codec_name']
                codeclong = stream['codec_long_name']
                
                subtitle = [index, name, language, codec, codeclong]
                subs.append(subtitle)
                
        return subs