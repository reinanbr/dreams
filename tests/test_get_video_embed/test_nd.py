from dreams import noodlemagazine as nd

def test_embed():
    embed_data = nd.get_video_embed('https://noodlemagazine.com/watch/-190558927_456239092')
    print(embed_data)
    
    
test_embed()