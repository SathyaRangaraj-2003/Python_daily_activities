playlist=["TrackA","TrackB","TrackC","TrackD"]
playlist.remove('TrackC')
playlist.insert(0,'TrackX')
popped_str=playlist.pop(-1)
playlist.insert(1,popped_str)
print(*playlist)