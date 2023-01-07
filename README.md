 <div align='center'>

 <img  height='200px' width='460px' src='https://raw.githubusercontent.com/reinanbr/dreams/main/img/logo.jpeg'>

<h1>Dreams</h1>

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

The initial idea from this lib, is create a API as lib for getting video's porn data from the best sites*, for working it in site's, bot's, app's, API's and other service's.
<br>
On the present moment (jan 5 20:49, 2023), I added the follow work's:

| site         | data video | preview | embed url video | sugest. video's url's page |
|--------------|:----------:|:-------:|:---------------:|:--------------------------:|
|pornone       |         ✅ |     x   |        ✅       |                            |
|spankbang     |         ✅ |    ✅   |        ✅       |                            |
|noodlemagazine|            |         |                 |                            |
|ukevids       |  ✅        |     x   |        ✅       |                            |
|playvids      |            |         |                 |                            |
|xvideos       |            |         |                 |                            |
|pornhub       |            |         |                 |                            |

<br>
if you want help it free project, <a href="https://github.com/reinanbr/dreams" alt="github dreams">come on</a>.

## getting videos data

### SpankBang

getting data
```py

>>> import dreams.spankbang as sp

>>> vd = sp.search_porn('natasha nice',page_limit=2)
[20:07:52 07/01/2023 (SpankBang)]:  finding 98 videos from 1 pages... 
[20:07:53 07/01/2023 (SpankBang)]:  finding 193 videos from 2 pages... 


>>> vd
SpankBang(site_name='SpankBang',
url_base='https://spankbang.com', 
query='natasha+nice', 
url_search='https://spankbang.com/video/natasha+nice', 
ping=3.639028787612915, 
videos_per_pages=96, len_pages=2, 
len_videos=193, 
videos=[
    spankbang_video(title='natasha.nice.and.lumi.ray.cumming.in.for.a.wet.landing', 
    time='34 min', 
    dur=2040, 
    stats='\n13K\n91%\n9 days\n\xa0\n\n', 
    page_number=1, 
    url='https://spankbang.com/7mwzt/video/natasha+nice+and+lumi+ray+cumming+in+for+a+wet+landing', 
    url_font='https://spankbang.com/s/natasha+nice/1/?o=trending', 
    thumbnail='https://tb-lb.sb-cd.com/t/12826505/1/2/w:800/t6-enh/natasha-nice-and-lumi-ray-cumm.jpg', 
    preview='https://tbv.sb-cd.com/t/12826505/1/2/td.mp4'),
    ...
```


### Pornone

```py

>>> import dreams.pornone as pn

>>> vd = pn.search_porn('natasha nice mother',page_limit=2)
[19:55:22 07/01/2023 (pornone)]:  finding 36 videos from 1 pages... 
[19:55:23 07/01/2023 (pornone)]:  finding 72 videos from 2 pages... 


>>> vd
pornone(site_name='pornone',
url_base='https://pornone.com', 
query='natasha+nice+mother', 
url_search='https://pornone.com/video/natasha+nice+mother', 
ping=2.7822909355163574, 
videos_per_pages=36, 
len_pages=2, 
len_videos=72, 
videos=[
    pornone_video(title='Mother Natasha And Her Stepson', 
    time='31:16\n', 
    dur=1876, 
    stats='\n\n\n7,066\n\n\n\n4mo ago\n\n\n\n100%\n\n', 
    page_number=1, 
    url='https://pornone.com/cougar/mother-natasha-and-her-stepson/278036723/'
    url_font='https://pornone.com/search/?q=natasha+nice+mother&sort=relevance&filter=&page=1', 
    thumbnail='https://th-eu4.pornone.com/t/23/278036723/d73.jpg'),
    ...
```


if you seach just the name pornstar (saved on site pornone), he return the videos from page pornstar


```py

>>> vd = pn.search_porn('natasha nice',page_limit=2)
[20:01:30 07/01/2023 (pornone)]:  is page pornstar from Natasha Nice - https://pornone.com/natasha-nice-porn-videos-10468/1/ 
[20:01:30 07/01/2023 (pornone)]:  finding 36 videos from 1 pages... 
[20:01:31 07/01/2023 (pornone)]:  is page pornstar from Natasha Nice - https://pornone.com/natasha-nice-porn-videos-10468/2/ 
[20:01:31 07/01/2023 (pornone)]:  finding 72 videos from 2 pages... 

>>> vd
pornone(site_name='pornone', 
url_base='https://pornone.com', 
query='natasha+nice', 
url_search='https://pornone.com/video/natasha+nice',
ping=2.9700820446014404, 
videos_per_pages=36, 
len_pages=2, 
len_videos=72, 
videos=[
    pornone_video(title='Xxxmas Mixxx Up',
    time='29:41\n', 
    dur=1781, 
    stats='\n\n\n6,022\n\n\n\n19h ago\n\n\n\n100%\n\n', 
    page_number=1, 
    url='https://pornone.com/taboo/xxxmas-mixxx-up/278239965/', 
    url_font='https://pornone.com/natasha-nice-porn-videos-10468/1/', 
    thumbnail='https://th-eu4.pornone.com/t/65/278239965/d3.jpg'),
    ...
```

### Ukevids

```py

>>> import dreams.ukevids as uk

>>> vd = uk.search_porn('natasha nice',page_limit=2)
[16:24:24 07/01/2023 (ukevids)]:  finding 24 videos from 1 pages... 
[16:24:24 07/01/2023 (ukevids)]:  finding 48 videos from 2 pages... 


>>> vd
ukevids(site_name='ukevids',
url_base='https://ukdevilz.com', 
query='natasha+nice', 
url_search='https://ukdevilz.com/video/natasha+nice',
ping=1.9254982471466064,
videos_per_pages=24,
len_pages=2,
len_videos=48,
videos=[
    ukevids_video(title='Xandra sixx, darcie dolce, natasha nice (sorority initiation) sex porno',
    time=' 31:58',
    dur=1918,
    views=' 122.88K',
    page_number=1,
    url_font='https://ukdevilz.com/video/natasha+nice?p=1',
    url='https://ukdevilz.com/watch/-165193771_456239108',
    thumbnail='https://sun9-66.userapi.com/c845123/v845123080/699f2/42fyF8MAdjU.jpg',
    site='ukevids'), 
    ...
```
```