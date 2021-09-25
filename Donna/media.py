from ytmusicapi import YTMusic
import subprocess
import vlc
import pafy
ytmusic = YTMusic('headers_auth.json')
# playlistId = ytmusic.create_playlist("test", "test description")


def play(song_name):
    search_results = ytmusic.search(song_name)
    first_result = search_results[0]
    print(first_result)
    youtube_url = "https://www.youtube.com/watch?v=" + "{}".format(first_result['videoId'])

    video = pafy.new(youtube_url)
    best = video.getbest()
    playurl = best.url

    ins = vlc.Instance()
    player = ins.media_player_new()
    Media = ins.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

    good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
    while str(player.get_state()) in good_states:
        continue

    print('Stream is not working. Current state = {}'.format(player.get_state()))
    player.stop()



