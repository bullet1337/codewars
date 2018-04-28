# https://www.codewars.com/kata/551dc350bf4e526099000ae5
def song_decoder(song):
    return ' '.join(x for x in song.split('WUB') if x)