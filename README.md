 <div align='center'>

 <img  height='200px' width='460px' src='https://raw.githubusercontent.com/reinanbr/dreams/main/img/logo.jpeg'>

<h1>Dreams</h1>

<p> a beautiful lib, for getting educative video's 🍑 (video's porn)</p>
<a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/reinanbr/dreams?logo=codefactor">
</a><img alt="CircleCI" src="https://img.shields.io/circleci/build/github/reinanbr/dreams">
<img alt="Code Climate maintainability" src="https://img.shields.io/codeclimate/maintainability-percentage/reinanbr/dreams">

<br/>
<a href='https://pypi.org/project/dreams/'><img src='https://img.shields.io/pypi/v/dreams'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/dreams"></a>
<br/>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/dreams?color=orange">
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

| site         | data video | preview | embed url video | sugest. embed url's video | videos per page's |
|--------------|:----------:|:-------:|:---------------:|:--------------------------:|:----------------:|
|pornone       |         ✅ |     x   |        ✅       |                            |         36       |
|spankbang     |         ✅ |    ✅   |        ✅       |                ✅          |         98       |
|noodlemagazine|            |         |                 |                            |                  |
|ukdelviz      |  ✅        |     x   |        ✅       |                            |         15       |
|tnaflix       |     ✅     |    ✅   |                 |                            |         60       |
|playvids      |            |         |                 |                            |                  |
|xvideos       |            |         |                 |                            |                  |
|pornhub       |            |         |                 |                            |                  |
| ma6tube      |            |         |                 |                            |                  |
| eponer       |            |         |                 |                            |                  |


<br>
if you want help it free project, <a href="https://github.com/reinanbr/dreams" alt="github dreams">fork-me</a>.

## getting videos data

### SpankBang

getting data
```py

>>> from dreams import spankbang as sb

>>> vds = sb.search_porn('lorena aquino')

>>> vds

SpankBang(
    query=lorena+aquino,
    len_videos=196,
    len_pages=2,
    videos_per_pages=98,
    ping=3.533900737762451, 
    url_base=https://spankbang.com, 
    url_search=https://spankbang.com/s/lorena+aquino/1/?o=trending, 
    videos=[
        spankbang_video(
            site_name=SpankBang, 
            title=lorena aquino slave los monsta bbc, 
            time=358 min, 
            page_number=1, 
            url=https://spankbang.com/6971t/video/lorena+aquino+slave+los+monsta+bbc, 
            url_font=https://spankbang.com/s/lorena+aquino/1/?o=trending, 
            thumbnail=https://tbi.sb-cd.com/t/10506737/1/0/w:800/t1-enh/lorena-aquino-slave-los-monsta.jpg, stats= 150K 99% 1 year    , 
            duration=21480, preview=https://tbv.sb-cd.com/t/10506737/1/0/td.mp4, 
            indice=1),
        ...
```
getting only one video from it data
```py
>>> vd = vds.videos[20]

>>> vd
spankbang_video(
    title=Joyce Oliveira fudendo com sua Mãe,
    time=26 min,
    duration=1560,
    stats= 190K 98% 4 years,
    page_number=1,
    url=https://spankbang.com/2k3ez/video/joyce+oliveira+fudendo+com+sua+m+e,
    url_font=https://spankbang.com/s/joyce+oliveira/1/?o=trending,
    thumbnail=https://tb-lb.sb-cd.com/t/4296779/4/2/w:800/t5-enh/joyce-oliveira-fudendo-com-sua.jpg,
    preview=https://tbv.sb-cd.com/t/4296779/4/2/td.mp4)

>>> type(vd)
dreams.settings.VideoData

```

### Pornone

if you seach just the name pornstar (saved on site pornone), he return the videos from page pornstar


```py

>>> import dreams.pornone as pn

>>> vds = pn.search_porn('joyce oliveira',page_limit=2)
[23:06:45 09/01/2023 (pornone)]:  is page pornstar from Joyce Oliveira - https://pornone.com/joyce-oliveira-porn-videos-935/1/ 
[23:06:45 09/01/2023 (pornone)]:  finding 36 videos from 1 pages of 2 limit pages... 
[23:06:46 09/01/2023 (pornone)]:  is page pornstar from Joyce Oliveira - https://pornone.com/joyce-oliveira-porn-videos-935/2/ 
[23:06:46 09/01/2023 (pornone)]:  finding 72 videos from 2 pages of 2 limit pages... 

>>>> type(vds)
dreams.settings.DataVideos

>>> vds
pornone(query=joyce+oliveira, 
len_videos=72, 
len_pages=2, 
videos_per_pages=36, 
ping=2.7089011669158936, 
url_base=https://pornone.com, 
url_search=https://pornone.com/joyce-oliveira-porn-videos-935/1/), 
videos=[
    pornone_video(
        title=Big Bubble Butt Brazilian Orgy, 
        time=19:44, 
        duration=1184, 
        stats=   117    1wk ago      ,
        page_number=1, 
        url=https://pornone.com/swimsuit/big-bubble-butt-brazilian-orgy/278238363/?r=3, 
        url_font=https://pornone.com/joyce-oliveira-porn-videos-935/1/, 
        thumbnail=https://th-eu4.pornone.com/t/63/278238363/d3.jpg, 
        preview=None), 
    ...
```
getting only video from it data
```py

>>> vd = vds.videos[20]

>>> vd
pornone_video(
    title=Taboo Brazil #2, 
    time=03:04:23, 
    duration=184, 
    stats=   42,163    21mo ago    97%  , 
    page_number=1, 
    url=https://pornone.com/taboo/taboo-brazil/277503033/, 
    url_font=https://pornone.com/joyce-oliveira-porn-videos-935/1/, 
    thumbnail=https://th-eu4.pornone.com/t/33/277503033/d3.jpg, 
    preview=None)

>>> type(vd)
dreams.settings.VideoData
```

### Ukdelviz

```py
>>> import dreams.ukdelviz as uk

>>> vds = uk.search_porn('joyce oliveira',page_limit=2)
[22:49:35 09/01/2023 (ukdelviz)]:  finding 8 videos from 1 pages of 2 limit pages... 
[22:49:36 09/01/2023 (ukdelviz)]:  error Exception: invalid literal for int() with base 10: ' 2 days, 11' 
[22:49:36 09/01/2023 (ukdelviz)]:  finding 28 videos from 2 pages of 2 limit pages... 

>>> type(vds)
dreams.settings.DataVideos

>>> vds
ukdelviz(query=joyce+oliveira,
len_videos=28,
len_pages=2,
videos_per_pages=14,
ping=0.7920231819152832,
url_base=https://ukdevilz.com,
url_search=https://ukdevilz.com/video/joyce+oliveira?p=1),
videos=[
    ukevids_video(
        title=Joyce oliveira i am wearing no panties (big wet butts), 
        time= 35:26,
        duration=2126, 
        stats= 624, 
        page_number=1, 
        url=https://ukdevilz.com/watch/94112237_158975131, 
        url_font=https://ukdevilz.com/video/joyce+oliveira?p=1,
         thumbnail=https://sun9-87.userapi.com/c12491/u33879252/video/l_8374bd19.jpg,
         preview=None),
    ...
```

getting only video from it data:
```py
>>> vd = vds.videos[20]

>>> vd
ukevids_video(
    title=Sissy brainwashing,
    time= 11:41, 
    duration=701, 
    stats= 6.57K, 
    page_number=2, 
    url=https://ukdevilz.com/watch/-127636532_456241846, 
    url_font=https://ukdevilz.com/video/joyce+oliveira?p=2,
    thumbnail=https://sun9-68.userapi.com/impf/c846019/v846019732/77367/14I1GmrLsPs.jpg?size=800x450&quality=96&keep_aspect_ratio=1&background=000000&sign=73c5e51d7a6f52bcb9075f454f724bad&c_uniq_tag=Dp82kMhnAVqhJ0il5d-A8BiVUDlgo8H8n856ijOpFEM&type=video_thumb,
    preview=None)

>>> type(vd)
dreams.settings.VideoData


```
```