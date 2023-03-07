from dreams import pornhub as ph

def test_embed():
    embed_data = ph.get_video_embed('https://pt.pornhub.com/view_video.php?viewkey=ph62d65cfe4d0f0')
    print(embed_data)
    
    
test_embed()