<!-- <img  height='200px' width='460px' src='https://raw.githubusercontent.com/reinanbr/dreams/main/img/logo.png'>
<br> -->
<div align='center'>
<h2>Dreams</h2>
<hr>
<p> a beautiful lib, for getting educative video's 🍑 (video's porn)</p>
<a href='https://pypi.org/project/dreams/'><img src='https://img.shields.io/pypi/v/dreams'></a>
<a href='#'><img src='https://img.shields.io/pypi/wheel/dreams'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/dreams"></a>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/dreams?color=orange">

<a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/reinanbr/dreams?logo=codefactor">
</a>


<img src='https://img.shields.io/badge/system-linux%20%7C%20deb-brightgreen'>

<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/reinanbr/dreams">


<!-- redes sociais -->
<br/>
<a href='https://instagram.com/reysofts/'><img src='https://shields.io/badge/insta-reysofts-darkviolet?logo=instagram&style=flat'></a>
</div>

<br>

<hr>

## Instalation
```sh
pip3 install -U dreams
```

### getting videos data
#### only site (SpankBang)
```py
import dreams.spankbang as sb

query = 'natasha nice'
page_limit = 100



sb_videos = sb.search_porn(query,page_limit)


print(f'{len(sb_videos)} videos','\n')


print('first video from list:\n',sb_videos[0],'\n')

```
result:
```sh
[spankbang]
finding 743 videos from 8 pages...

743 videos

first video from list:
{'url': 'https://spankbang.com/7btrt/video/natasha+nice+stepmom+natasha+s+big+tit+cum+candy+treat', 
'url_img': 'https://tb-lb.sb-cd.com/t/12309113/1/2/w:800/t6-enh/natasha-nice-stepmom-natasha.jpg', 
'title': "Natasha Nice - Stepmom Natasha'S Big Tit Cum Candy Treat", 
'time': '43 min'} 

```

#### all site's data from lib

```py
 
import dreams.playvids as pv
import dreams.noodlemagazine as nm
import dreams.ukevids as uk
import dreams.spankbang as sb


query = 'natasha nice'
page_limit = 100


# spankbang
sb_videos = sb.search_porn(query,page_limit)
print(f'spankbang search: {len(sb_videos)} videos')
print(sb_videos[0],'\n')

#nodlemagazine
nm_videos = nm.search_porn(query,page_limit)
print(f'nodlemagazine search: {len(nm_videos)} videos')
print(nm_videos[0],'\n')

#ukevids
uk_videos = uk.search_porn(query,page_limit)
print(f'ukevids search: {len(uk_videos)} videos')
print(uk_videos[0],'\n')

#playvids
pv_videos = pv.search_porn(query,page_limit)
print(f'playvids search: {len(pv_videos)} videos')
print(pv_videos[0])

```
result
```sh
[spankbang]
finding 743 videos from 8 pages...

spankbang search: 743 videos
{'url': 'https://spankbang.com/7btrt/video/natasha+nice+stepmom+natasha+s+big+tit+cum+candy+treat', 
'url_img': 'https://tb-lb.sb-cd.com/t/12309113/1/2/w:800/t6-enh/natasha-nice-stepmom-natasha.jpg',
 'title': "Natasha Nice - Stepmom Natasha'S Big Tit Cum Candy Treat", 
 'time': '43 min'} 

[nodlemagazine]
finding 1836 videos from 77 pages...

nodlemagazine search: 1836 videos
{'url': 'https://noodlemagazine.com/watch/-185685320_456241307', 'url_img': 'https://sun9-69.userapi.com/IGcjNOFDr5ZdMzaBphzTVbY3yHFgjTKtHrNjow/D5lJjhTt3p4.jpg', 'title': "Step mom natasha's big tits cum candy treat natasha nice familyxxx 2022 new porn milf big ass sex hd taboo incest pov", 'time': ' 43:06'} 

[ukevids]
finding 1825 videos from 77 pages...

ukevids search: 1825 videos
{'url': 'https://ukdevilz.com/watch/-165193771_456239108', 'url_img': 'https://sun9-66.userapi.com/c845123/v845123080/699f2/42fyF8MAdjU.jpg', 'title': 'Xandra sixx, darcie dolce, natasha nice (sorority initiation) sex porno', 'time': ' 31:58'} 

[plavids]
finding 424 videos from 21 pages...

playvids search: 424 videos
{'title': 'FamilyTherapy - Natasha Nice - Brother & Sistet New Living Arrangement', 'duration': '49:20', 'imgUrl': 'https://cdn-img1.playvids.com/thumbs/262/2624984/1483_m.jpg', 'url': 'https://www.playvids.com/Rkpy16IW7EX/familytherapy-natasha-nice-brother-sistet-new-living-arrangement', 'dur': 2960}
```


