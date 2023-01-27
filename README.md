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
In the present moment (jan 27 2, 16:40 UTC-3, 2023), I added the following work's:

| site         | data video | preview | embed url video | sugest. embed url's video | videos per page's |
|--------------|:----------:|:-------:|:---------------:|:--------------------------:|:----------------:|
|pornone       |         ✅ |     x   |        ✅       |                            |         36       |
|spankbang     |         ✅ |    ✅   |        ✅       |                ✅          |         98       |
|noodlemagazine|            |         |                 |                            |                  |
|ukdelviz      |  ✅        |     x   |        ✅       |                            |         15       |
|tnaflix       |     ✅     |    ✅   |        ✅        |             ✅            |         60       |
|playvids      |            |         |                 |                            |                  |
|xvideos       |            |         |                 |                            |                  |
|pornhub       |            |         |                 |                            |                  |
| ma6tube      |            |         |                 |                            |                  |
| eponer       |            |         |                 |                            |                  |


<br>
if you want help it free project, <a href="https://github.com/reinanbr/dreams" alt="github dreams">fork-me</a>.

## getting videos data search

### SpankBang

```py

>>> from dreams import spankbang as sb

>>> vds = sb.search_porn('lorena aquino')

>>> vds

SpankBang(
    query="lorena+aquino", 
    len_videos=196, 
    len_pages=2, 
    videos_per_pages=98, 
    ping=5.517827033996582, 
    url_base="https://spankbang.com", 
    url_search="https://spankbang.com/s/lorena+aquino/1/?o=trending", 
    videos=[
        spankbang_video(
            site_name="SpankBang", 
            title="lorena aquino slave los monsta bbc", 
            time="358 min", 
            page_number=1, 
            url="https://spankbang.com/6971t/video/lorena+aquino+slave+los+monsta+bbc", 
            url_font="https://spankbang.com/s/lorena+aquino/1/?o=trending", 
            thumbnail="https://tbi.sb-cd.com/t/10506737/1/0/w:800/t1-enh/lorena-aquino-slave-los-monsta.jpg",
            stats=" 150K 99% 1 year    ",
            duration=21480,
            preview="https://tbv.sb-cd.com/t/10506737/1/0/td.mp4",
            indice=1), 
        ...
```

<hr>
### pornone

```py
>>> from dreams import pornone as pn

>>> vds = pn.search_porn('lorena aquino')

>>> vds

pornone(
    query="lorena+aquino", 
    len_videos=72, 
    len_pages=2, 
    videos_per_pages=36, 
    ping=3.0705974102020264, 
    url_base="https://pornone.com", 
    url_search="https://pornone.com/search/?q=lorena+aquino&sort=relevance&filter=&page=1", 
    videos=[
        pornone_video(
            site_name="pornone", 
            title="Lorena Aquino Anal Total!", 
            time="25:17", 
            page_number=1, 
            url="https://pornone.com/brazilian/lorena-aquino-anal-total/276822039/", 
            url_font="https://pornone.com/search/?q=lorena+aquino&sort=relevance&filter=&page=1", 
            thumbnail="https://th-eu4.pornone.com/t/39/276822039/d48.jpg",
            stats="   12,780    38mo ago    100%  ",
            duration=1517,
            indice=0), 
        ...

```

<hr>

### ukdelviz

```py
>>> from dreams import ukdelviz as uk

>>> vds = uk.search_porn('lorena aquino')

>>> vds


ukdevilz(
    query="lorena+aquino", 
    len_videos=30, 
    len_pages=2, 
    videos_per_pages=15, 
    ping=2.1073954105377197, 
    url_base="https://ukdevilz.com", 
    url_search="https://ukdevilz.com/video/lorena+aquino?p=1", 
    videos=[
        ukdevilz_video(
            site_name="ukdevilz", 
            title="Lorena aquino white bubble butt sluts 2 ai enhanced video", 
            time=" 27:40", 
            page_number=1, 
            url="https://ukdevilz.com/watch/-209942790_456240637", 
            url_font="https://ukdevilz.com/video/lorena+aquino?p=1", 
            thumbnail="https://i.mycdn.me/getVideoPreview?id=2684034943497&idx=10&type=39&tkn=CzOYkDH_q-ldERSRuTGCyLKm85c&fn=vid_l&c_uniq_tag=ItwI2ATuwsYFuaz3EQKbLK2v4ueO-rHoABJMWYSudaM",
            stats=" 1.11K",
            duration=1660,
            indice=0), 
        ...
```

<hr>

### tnaflix

```py
>>> from dreams import ukdelviz as uk

>>> vds = uk.search_porn('lorena aquino')

>>> vds

tnaflix(
    query="lorena+aquino", 
    len_videos=120, 
    len_pages=2, 
    videos_per_pages=60, 
    ping=5.709991693496704, 
    url_base="https://tnaflix.com", 
    url_search="https://www.tnaflix.com/search.php?tab=videos&what=lorena+aquino&category=&sb=relevance&su=anytime&sd=all&dir=desc&page=1", 
    videos=[
        tnaflix_video(
            site_name="tnaflix", 
            title="Lorena Aquino and Marcelinha Moraes Hot part4", 
            time="6:07", 
            page_number=1, 
            url="https://tnaflix.com/babe-videos/Lorena-Aquino-and-Marcelinha-Moraes-Hot-part4/video1430774", 
            url_font="https://www.tnaflix.com/search.php?tab=videos&what=lorena+aquino&category=&sb=relevance&su=anytime&sd=all&dir=desc&page=1", 
            thumbnail="https://img.tnastatic.com/a16:8q80w300/205/14/30/1430774/thumbs/5.jpg",
            views="6,132",
            rating="88%",
            date_upload="8.8 year's ago",
            duration=367,
            preview="https://sl205.tnaflix.com/14/30/1430774/trailer.mp4?secure=074fe97a886337701b912",
            indice=0),
        ...

```

<hr>

## get embed link info and video suggestions from link video

### spankbang

```py
>>> from dreams import spankbang as sb

>>> embed_data = sb.get_video_embed('https://spankbang.com/4b5uc/video/lorena+aquino')

>>> embed_data

    EmbedVideoSpankBang(
        title=Lorena aquino, 
        time=26:07, 
        url=https://vdownload-14.sb-cd.com/7/2/7239252-480p.mp4?secure=jzztPrBpX-BWs59AyiV_vw,1674891264&m=14&d=3&_tid=7239252, 
        thumbnail=https://tbi.sb-cd.com/t/7239252/7/2/w:300/t6-enh/lorena-aquino.jpg, 
        views=16,713 visualizações, 
        time_published=2 years, 
        len_videos_sugestions=48, 
        videos_sugestions=[
        spankbang_video(
            site_name="SpankBang", 
            title="Jenna Presley hot girl", 
            time="2 min", 
            page_number=None, 
            url="https://spankbang.com/dlju/video/jenna+presley+hot+girl", 
            url_font="https://spankbang.com/4b5uc/video/lorena+aquino", 
            thumbnail="https://tbi.sb-cd.com/t/634458/6/3/w:800/t6-enh/jenna-presley-hot-girl.jpg",
            stats=" 5.4K 93% 6 years   ",
            duration=120,
            indice=0),
        ...


```


### tnaflix


```py

>>> from dreams import tnaflix as tn

>>> embed_data = tn.get_video_embed('https://spankbang.com/4b5uc/video/lorena+aquino')

>>> embed_data

    EmbedVideotnaflix(
        title= Lorena Aquino big boobs brazilian blonde outdoors fuck, 
        time=None, 
        url=https://sl105.tnaflix.com/67/77/6777794/lorena-aquino-big-boobs-brazilian-blonde-outdoors-fuck-480p.mp4?burst=2148802&speed=120832&end=1674855442&secure=011e950f9245ed9851c2d, 
        thumbnail=https://img.tnastatic.com/a16:8q80w300/205/10/47/1047757/thumbs/5.jpg, 
        views=12,533, 
        time_published=None, 
        len_videos_sugestions=16, 
        videos_sugestions=[
        tnaflix_video(
            site_name="tnaflix", 
            title="Lorena Aquino big boobs brazilian blonde outdoors fuck", 
            time="25:09", 
            page_number=0, 
            url="https://tnaflix.com/anal-porn/Lorena-Aquino-big-boobs-brazilian-blonde-outdoors-fuck/video6777794", 
            url_font="https://www.tnaflix.com/anal-porn/Lorena-Aquino-big-boobs-brazilian-blonde-outdoors-fuck/video6777794&autoPlay=1", 
            thumbnail="https://img.tnastatic.com/a16:8q80w300/105/67/77/6777794/thumbs/10.jpg",
            views="1,225",
            rating="100%",
            date_upload="1.3 year's ago",
            duration=1509,
            preview="https://sh105.tnaflix.com/67/77/6777794/trailer.mp4?se=1674851584&ss=1ae4ea799d7834314ae41b4e4065ecb9",
            indice=0), 
```