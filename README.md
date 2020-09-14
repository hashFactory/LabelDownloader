# LabelDownloader

Project repo for LabelDownloader

Goal is to have a web service (maybe) where you give it a Discogs label ID and it gives back either a youtube or a spotify playlist with all the releases organized chronologically.

The main code will be in discogs.py but right now everything is in disc_int.py for prototyping.

TODO list (not comprehensive at all):
- First fetch sample list of releases and if the user OKs it, it will lookup on Spotify based on info
- It will then check that the release found on Spotify is from the same year
- If can't find on Spotify, then YouTube 2 mp3 it
- Send telegram link to completed zip download from my server
- Concat all strings from release together and use that to make hash and check for duplicates
- Sort by year and then by cat number

A project by Tristan C.
