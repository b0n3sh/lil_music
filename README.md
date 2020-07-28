```
 ,dPYb,       ,dPYb,                                                         
 IP'`Yb       IP'`Yb                                                         
 I8  8I  gg   I8  8I                                           gg            
 I8  8'  ""   I8  8'                                           ""            
 I8 dP   gg   I8 dP   ,ggg,,ggg,,ggg,   gg      gg    ,g,      gg     ,gggg, 
 I8dP    88   I8dP   ,8" "8P" "8P" "8,  I8      8I   ,8'8,     88    dP"  "Yb
 I8P     88   I8P    I8   8I   8I   8I  I8,    ,8I  ,8'  Yb    88   i8'      
,d8b,_ _,88,_,d8b,_ ,dP   8I   8I   Yb,,d8b,  ,d8b,,8'_   8) _,88,_,d8,_    _
8P'"Y888P""Y88P'"Y888P'   8I   8I   `Y88P'"Y88P"`Y8P' "YY8P8P8P""Y8P""Y8888PP	v1.0
```
---

Script I made for myself but made it available in case it helps somebody.

## What does it do?
I had the struggle of everytime I liked a youtube song, having to:
* Download it using `youtube-dl -x --audio-format mp3`
* Move it to the folder I wanted in addition to making a backup in my other HDD.
* Edit tags (especially the `artist` one, as that's the way I shuffle my music in Google Music.
* Upload it to Google Music having to open the browser and bla bla.

So I automated the whole process.

## Dependencies.
* Python3.7
* Python3.7 modules:
	* It comes with a `requeriments.txt` 
* It uses Google's Oauth token system for authentification.
## Usage.
First of all, you have to create a Google's Oauth token so you can log in without having to store plain text in your computer.

For that, just open a python terminal:
```
from gmusicapi import Musicmanager
mm = Musicmanager()
mm.perform_oauth()
```
Now we have our oauth and can log in using `mm.login()`

Next, customize your folders variable to choose where to store the main mp3 and the backup.

Finally, the menu variable, keep using numbers and the name of the artist you wanna upload to google music.

## Update
All of a sudden Google changed their way of verifying uploads, we have to add our MAC address in the`Musicmanager().login()` function, this way.
```
Musicmanager().login(uploader_id='00:00:00:00:00:00') 
```



