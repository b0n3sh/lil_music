#!venv/bin/python3
# We download the song
import sys, youtube_dl, os, requests
from shutil import copy
from gmusicapi import Musicmanager
from mp3_tagger import MP3File
from mutagen.id3 import ID3, APIC

print(sys.version)
folders = {1:
        {'suicidesheep': ['/media/b0nesh/Ayymacenamiento/musica/suicidesheep', '/media/b0nesh/Ayy lmao/Música/Buena/suicidesheep']}, 2: {'lil peep': ['/media/b0nesh/Ayymacenamiento/musica/lilpeep', '/media/b0nesh/Ayy lmao/Música/Buena/lil_peep']}, 3: {'bangers': ['/media/b0nesh/Ayymacenamiento/musica/bangers']},
}
menu = {
        1: "suicidesheep", 2:'lil peep', 3:'bangers',
}
lil = """
 ,dPYb,       ,dPYb,                                                         
 IP'`Yb       IP'`Yb                                                         
 I8  8I  gg   I8  8I                                           gg            
 I8  8'  ""   I8  8'                                           ""            
 I8 dP   gg   I8 dP   ,ggg,,ggg,,ggg,   gg      gg    ,g,      gg     ,gggg, 
 I8dP    88   I8dP   ,8" "8P" "8P" "8,  I8      8I   ,8'8,     88    dP"  "Yb
 I8P     88   I8P    I8   8I   8I   8I  I8,    ,8I  ,8'  Yb    88   i8'      
,d8b,_ _,88,_,d8b,_ ,dP   8I   8I   Yb,,d8b,  ,d8b,,8'_   8) _,88,_,d8,_    _
8P'"Y888P""Y88P'"Y888P'   8I   8I   `Y88P'"Y88P"`Y8P' "YY8P8P8P""Y8P""Y8888PP   v1.0
"""

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass
        #print(msg)
   
def my_hook(d):
    if d['status'] == 'finished':
        print('\nDone downloading, now converting...\n')

def insert_album_art(music_file, id_video):
    audio = ID3(music_file)

    with open('0.jpg', 'wb') as img:
        img.write(requests.get(f'https://img.youtube.com/vi/{id_video}/hqdefault.jpg').content)
    with open('0.jpg', 'rb') as albumart:
        audio['APIC'] = APIC(
                            encoding=3,
                            mime='image/jpeg',
                            type=3, desc=u'Cover',
                            data=albumart.read()
                            )
    audio.save()
    os.remove('0.jpg')
    


def download(mode, url, num):
        print(f"Downloading for {mode}")

        #Options
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'outtmpl': folders[num][mode][0] + '/%(title)s.%(ext)s'
        }

        #Download the video and extract all the metadata
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                video_title = info_dict.get('title', None)
                video_filename = '.'.join(ydl.prepare_filename(info_dict).split('.')[:-1]) + '.mp3'
        print(video_filename)

        #Edit mp3 tag.
        try:
                print(f"Editing artist tag to {mode.capitalize()}...")
                mp3 = MP3File(video_filename)
                mp3.artist = mode.title()
                mp3.save()
                insert_album_art(video_filename, info_dict['id'])
                print("Done!\n")
        except Exception as e:
                print("Error at editing mp3 tag.\n")
                print(e)

        #Backup
        if num != 3:
            try:
                    print(f"Making a backup of {video_title}...")
                    copy(video_filename, folders[num][mode][1])
                    print("Done!\n")
            except:
                    print("Error at doing backup.\n")

        #Upload to google
        if num != 3: 
            try:
                    print(f"Uploading {video_title} to Google Music\n")
                    print(f'With url {url}')
                    mm = Musicmanager()
                    mm.login(uploader_id='D0:50:99:83:B0:0C')
                    mm.upload(video_filename)
                    print("Done!\n")
            except Exception as e:
                print("Error at uploading the song to google:\n"+e)


def printing():
        print(f"\nChoose the number (enter 0 for exiting)\n{'='*18}")
        for x in menu:
                print(f'{x} for {menu[x]}')
        return int(input("\nEnter number: "))


if __name__ == '__main__':
        flag = True 
        print(lil)
        while flag:
                num = printing()
                if num == 0:
                        print("\nBye.")
                        flag = False
                elif num in menu:
                        flag2 = True
                        url = input("Enter the url to download: ")
                        while flag2:
                                while '&list' in url:
                                        url = input("That's a list!\n")
                                try:
                                        download(list(folders[num].keys())[0], url, num)
                                except Exception as e:
                                        print("Bad url!\n")
                                        print(e) #Debug

                                url = input("Enter next url to download (enter b to go back)\n")
                                if url == 'b':
                                        flag2 = False
                else:
                        pass
