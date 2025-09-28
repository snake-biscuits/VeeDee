# TODOs

## UI
 * 2 viewports (IN & OUT)
 * 1 Window
 * Skeumorphic Controls
   - Touch / Mouse Controls
   - Controller Bindings
   - Keyboard Bindings


## Basic Operation
 1. **IN** playback
 2. User Edits
    -> edit log (w/ CRDT undo/redo)
 3. Render
    -> image processing (video -> image format) [`Pillow`]
    -> audio assembly (audio -> audio format) [`SDL_mixer`?]
    -> transcode (audio + video -> video format) [`ffmpeg`]

### File I/O Management
 * source files
   - video
   - audio
   - subtitles
   - overlays
     * image
     * animation
     * mask
 * temporary files
   - raw frames
   - raw audio


### Sub-projects
break off a chunk of the edit into it's own file
handy for managing large projects
heirarchy: take < shot < scene < project


## Bugs

`cassette.svg` isn't clipped to viewbox bounds
can't be used as a background image effectively

can you even center a background image?

working out a css animated tape insert / eject background is gonna suck


## Subtitles
 * Overlay
 * Editor
 * Save to File
   - `*.srt` SubRip
     `application/x-subrip`
   - `*.ass` Advanced Sub Station Alpha (libass)
   - `*.vtt` Web Video Text Tracks
     `text/vtt`
     HTML5 `<track>`
 * HardSubs
   - asset bakery
 * `yt-dlp` Live Chat
   - filter
   - emoji
   - danmaku
   - animation


## Python UI
> NOTE: `now_playing/ui` also uses `PySide6`

### Dependencies
 * ui
   - [`PySide6`](https://pypi.org/project/PySide6/)
 * viewport playback
   - [`python-mpv`](https://pypi.org/project/python-mpv/)
 * controller input
   - [`PySDL2`](https://pypi.org/project/PySDL2/)
 * transcode
   - [`python-ffmpeg`](https://pypi.org/project/python-ffmpeg/)
 * image processing
   - [`Pillow`](https://pypi.org/project/pillow/)

> NOTE: might be possible to handle UI entirely with SDL2
> -- just not sure how to capture it in a `SDL_Rect`
> -- will have to try and figure it out
> -- unless PySide6 can get controller input...

### **OUT** viewport
We can feed a player frames as a python stream
```python
#!/usr/bin/env python3
import mpv

player = mpv.MPV()
@player.python_stream('foo')
def reader():
    with open('test.webm', 'rb') as f:
        while True:
            yield f.read(1024*1024)

player.play('python://foo')
player.wait_for_playback()
```


## Testing
`bigbuckbunny.mp4`
