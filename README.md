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

<a href="https://www.buymeacoffee.com/ReinanBr" target="_blank"><img height='30px' widht='100px' src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 30px !important;width: 100px !important;" ></a>

<hr>

The initial idea from this lib, is create a API as lib for getting video's porn data from the best sites*, for working it in site's, bot's, app's, API's and other service's.
<br>
The SpankBang site was blocked request with cloudfare. <br>
In the present moment (Mar 06, 16:46 UTC-3, 2023), I added the following work's:

| site         | data video | preview | embed url video | sugest. embed url's video | videos per page's |
|--------------|:----------:|:-------:|:---------------:|:--------------------------:|:----------------:|
|pornone       |     ✅     |     x   |        ✅       |                            |         36       |
|~~spankbang~~ (blocked)    |     ✅     |    ✅   |        ✅       |              ✅            |         98       |
|noodlemagazine|     ✅     |     ✅     |       ✅            |        ✅                      |         24       |
|ukdelviz      |     ✅     |     x   |        ✅       |                            |         15       |
|tnaflix       |     ✅     |    ✅   |        ✅       |              ✅            |         60       |
|playvids      |            |         |                 |                            |                  |
|xvideos       |            |         |                 |                            |                  |
|pornhub       |            |         |                 |                            |                  |
|ma6tube       |            |         |                 |                            |                  |
|eponer        |            |         |                 |                            |                  |


And sites from <b>onlyfans</b> video's

| site         | data video | preview |
|--------------|:----------:|:-------:|
| nudes7       |     ✅     |     x   |
|viralpornhub  |     ✅     |    ✅   |


<img src='https://getdatausers.000webhostapp.com/index.php?file=views_dreams'>

<br>
Please, <a href="https://github.com/reinanbr/dreams" alt="github dreams">fork-me</a>.

<br>
<br>
<b><a href='https://github.com/reinanbr/dreams/blob/main/fixed.md' title='list of versions and you fix on'> version's fix</a></b>

<hr>

# Examples 

## getting videos data search

<!-- ### SpankBang
```py

>>> from dreams import spankbang as sb

>>> vds = sb.search_porn('lorena aquino')

>>> vds

SpankBang(
    sucess="True",
    query="lorena%20aquino",
    len_videos=195, 
    len_pages=2, 
    videos_per_pages=97, 
    ping=3.68935227394104, 
    url_base="https://spankbang.com", 
    url_search="https://spankbang.com/s/lorena%20aquino/1/?o=trending", 
    videos=[
        spankbang_video(
            site_name="SpankBang", 
            title="lorena aquino slave los monsta bbc", 
            time="358 min", 
            page_number=1, 
            url="https://spankbang.com/6971t/video/lorena+aquino+slave+los+monsta+bbc", 
            url_font="https://spankbang.com/s/lorena%20aquino/1/?o=trending", 
            thumbnail="https://tbi.sb-cd.com/t/10506737/1/0/w:800/t1-enh/lorena-aquino-slave-los-monsta.jpg",
            views="150K",
            views_int=150000,
            rating="99%",
            rating_int=99,
            date_upload="1 year",
            date_upload_seconds=1645519768.9531095,
            duration_seconds=21480,
            preview="https://tbv.sb-cd.com/t/10506737/1/0/td.mp4",
            indice=0), 
        ...
```

<hr>
 -->
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
<!-- 
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


``` -->


### noodlemagazine

```py
>>> from dreams import noodlemagazine as nd

>>> nd.get_video_embed('https://noodlemagazine.com/watch/-190558927_456239092')

    EmbedVideoNoodleMagazine(
        title="[sexmex] gali diva hot milf (newporn, latin, big tits, ass, blowjob, spanish, teen, milf, mother, sister, anal, porn)", 
        time="None", 
        url="https://nmcorp.video/player/-190558927_456239092?m=af3f0f69ad1abf20d97587c170515f2f", 
        thumbnail="https://p2-86.pvvstream.pro/preview/eAivkKcZHl8ke9AGgtxoNw/-190558927_456239092/sun9-17.userapi.com/z12glz2pKg1psV3kfe3pbNRRIAynap8g6OdHNA/jQxKqgm02N0.jpg", 
        views="None", 
        time_published="None",
        views_int=217289,
        duration_seconds=2554,
        likes=1500,
        upload_date="2020-01-11",
        person="Gali Diva",
        tags="anal, ass, big, big tits, blowjob, brazzers, diva, gali, hot, latin, milf, mother, newporn, sexmex, sister, spanish, teen, tits",
        len_videos_sugestions=24,
        videos_sugestions=[
        noodlemagazine_video(
            title="Sexmex gali diva", 
            time=" 27:09", 
            url="https://noodlemagazine.com/watch/-172454327_456260979", 
            url_font="https://noodlemagazine.com/watch/-190558927_456239092", 
            thumbnail="https://i.mycdn.me/getVideoPreview?id=1786320652880&idx=14&type=39&tkn=67jVd9PgvdjmOg4HIGXNxRaMVTs&fn=vid_t&c_uniq_tag=1WKQjJgtNSNWBmBli-cZkWrC-_FTxsPXUg5049thwok",
            site_name="NoodleMagazine",
            page_number=0,
            views=" 36.47K",
            duration_seconds=1629,
            indice=0), 
        ...

```

### tnaflix


```py

>>> from dreams import tnaflix as tn

>>> embed_data = tn.get_video_embed('https://www.tnaflix.com/big-boobs/MILG-LATINA-ESPERTA-Gali-Diva/video7957213')

>>> embed_data

 EmbedVideotnaflix(
        title=" MILG LATINA ESPERTA - Gali Diva", 
        time="None", 
        url="https://player.tnaflix.com/video/7957213", 
        thumbnail="https://img.tnastatic.com/a16:8q80w300/206/15/76/1576707/thumbs/5.jpg", 
        views="1,736", 
        time_published="None", 
        len_videos_sugestions=16, 
        videos_sugestions=[
        tnaflix_video(
            title="MILG LATINA ESPERTA - Gali Diva", 
            time="31:41", 
            url="https://tnaflix.com/big-boobs/MILG-LATINA-ESPERTA-Gali-Diva/video7957213", 
            url_font="https://www.tnaflix.com/big-boobs/MILG-LATINA-ESPERTA-Gali-Diva/video7957213&autoPlay=1", 
            thumbnail="https://img.tnastatic.com/a16:8q80w300/104/79/57/7957213/thumbs/10.jpg",
            site_name="tnaflix",
            page_number=0,
            views="4,108",
            rating="94%",
            date_upload="4.3 month's ago",
            duration=1901,
            duration_seconds=1901,
            preview="https://sh104.tnaflix.com/79/57/7957213/trailer.mp4?se=1678117333&ss=5c439028a3f8b6c4e1bc9fec65a4a079",
            indice=0), 
```

### onlyfans sites

#### virapornhub

```py

>>> from dreams.sites.only import viralpornhub as vp

>>> vp.search_porn('mia monroe')

```


```py

viralpornhub@only(
    sucess="True",
    query="mia%20monroe",
    len_videos=24, 
    len_pages=1, 
    videos_per_pages=24, 
    ping=2.7153677940368652, 
    url_base="https://viralpornhub.com", 
    url_search="https://viralpornhub.com/search/mia%20monroe", 
    videos=[
        viralpornhub@only_video(
            title="Mia Monroe Velma Porn Video", 
            time="9:22", 
            url="https://viralpornhub.com/videos/45100/mia-monroe-velma-porn-video/", 
            url_font="https://viralpornhub.com/search/mia%20monroe/", 
            thumbnail="https://viralpornhub.com/contents/videos_screenshots/45000/45100/336x189/3.jpg",
            site_name="viralpornhub@only",
            page_number=1,
            views="208",
            rating="100%",
            date_upload="22 hours ago",
            preview="https://viralpornhub.com/get_file/3/952f0963d1d49fcd8c2ea2e297d89f6afc1eec1005/45000/45100/45100_preview.mp4/",
            indice=0), 
        ...
```

#### Nudes7

```py

>>> from dreams.sites.only import nudes7

>>> nudes7.search_porn('mia monroe')
```

```py

nudes7@only(
    sucess="True",
    query="mia%20monroe",
    len_videos=18, 
    len_pages=None, 
    videos_per_pages=18, 
    ping=1.4019057750701904, 
    url_base="https://nudes7.com/", 
    url_search="https://nudes7.com/?s=mia%20monroe", 
    videos=[
        nudes7@only_video(
            title="Mia Monroe Nude Blowjob Sex Tape PPV Video Leaked", 
            time="None", 
            url="https://nudes7.com/mia-monroe-nude-blowjob-sex-tape-ppv-video-leaked-14347/", 
            url_font="https://nudes7.com/?s=mia%20monroe", 
            thumbnail="https://nudes7.com/wp-content/uploads/2023/03/Mia-Monroe-Nude-Blowjob-Sex-Tape-PPV-Video-Leaked.mp4.jpg",
            site_name="nudes7@only",
            page_number=1,
            indice=0), 
        ...
```