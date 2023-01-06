<!-- <img  height='200px' width='460px' src='https://raw.githubusercontent.com/reinanbr/dreams/main/img/logo.png'>
<br> -->
<div align='center'>
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
if you want help it free project, [come on](https://github.com/reinanbr/dreams 'github dreams')

## getting videos data

### SpankBang
```py
import dreams.spankbang as sb

query = 'natasha nice'
page_limit = 2
```

getting data
```py

>>> sb_videos = sb.search_porn(query,page_limit)

finding 99 videos from 1 pages...
finding 198 videos from 2 pages...
```
```py
>>> print(f'data: {sb_videos}','\n')

data: {'url_base': 'https://spankbang.com', 'query': 'natasha+nice', 'url_search': 'https://spankbang.com/video/natasha+nice', 'ping': 3.6706933975219727, 'len_pages': 2, 'len_videos': 198, 'videos_per_pages': 99, 'videos': [{'title': 'natasha.nice.and.lumi.ray.cumming.in.for.a.wet.landing', 'time': '34 min', 'dur': 2040, 'stats': '\n11K\n91%\n6 days\n\xa0\n\n', 'page_number': 1, 'url': 'https://spankbang.com/7mwzt/video/natasha+nice+and+lumi+ray+cumming+in+for+a+wet+landing', 'url_font': 'https://spankbang.com/s/natasha+nice/1/?o=trending', 'thumbnail': 'https://tb-lb.sb-cd.com/t/12826505/1/2/w:800/t6-enh/natasha-nice-and-lumi-ray-cumm.jpg', 'preview': 'https://tbv.sb-cd.com/t/12826505/1/2/td.mp4'}, ....
```


### Pornone

```py
>>> import dreams.pornone as pn
>>> vds = pn.search_porn('pamela rios mother',page_limit=4)

finding 36 videos from 1 pages...[20:03:48 05/01/2023 (pornone)]:  is not page pornstar - https://pornone.com/search/?q=pamela+rios+mother&sort=relevance&filter=&page=2 

finding 72 videos from 2 pages...[20:03:49 05/01/2023 (pornone)]:  is not page pornstar - https://pornone.com/search/?q=pamela+rios+mother&sort=relevance&filter=&page=3 

finding 108 videos from 3 pages...[20:03:50 05/01/2023 (pornone)]:  is not page pornstar - https://pornone.com/search/?q=pamela+rios+mother&sort=relevance&filter=&page=4 

finding 144 videos from 4 pages...
```
```py
>>> vds

{'url_base': 'https://pornone.com', 'query': 'pamela+rios+mother', 'url_search': 'https://pornone.com/video/pamela+rios+mother', 'ping': 4.651678562164307, 'videos_per_pages': 36, 'len_pages': 4, 'len_videos': 144, 'videos': [{'title': 'Pamela Rios ', 'time': '19:37\n', 'dur': 1177, 'stats': '\n\n\n88,251\n\n\n\n41mo ago\n\n\n\n99%\n\n', 'page_number': 1, 'url': 'https://pornone.com/housewife/pamela-rios/276625807/', 'url_font': 'https://pornone.com/search/?q=pamela+rios+mother&sort=relevance&filter=&page=1', 'url_img': '/images/svg/hd.svg'}, {'title': 'Pamela Rios', 'time': '16:39\n', 'dur': 999, 'stats': '\n\n\n130,289\n\n\n\n21mo ago\n\n\n\n100%\n\n', 'page_number': 1, 'url': 'https://pornone.com/friend/pamela-rios/277501935/', 'url_font': 'https://pornone.com/search/?q=pamela+rios+mother&sort=relevance&filter=&page=1', 'thumbnail': 'https://th-eu4.pornone.com/t/7/276625807/b56.jpg'},  ...
```

if you seach just the name pornstar (saved on site pornone), he return the videos from page pornstar
```py
>>> vds = pn.search_porn('natasha nice',page_limit=4)

[20:38:58 05/01/2023 (pornone)]:  is page pornstar from Natasha Nice - https://pornone.com/natasha-nice-porn-videos-10468/1/ 

finding 36 videos from 1 pages...[20:38:59 05/01/2023 (pornone)]:  is page pornstar from Natasha Nice - https://pornone.com/natasha-nice-porn-videos-10468/2/ 

finding 72 videos from 2 pages...[20:39:00 05/01/2023 (pornone)]:  is page pornstar from Natasha Nice - https://pornone.com/natasha-nice-porn-videos-10468/3/ 

finding 108 videos from 3 pages...[20:39:02 05/01/2023 (pornone)]:  is page pornstar from Natasha Nice - https://pornone.com/natasha-nice-porn-videos-10468/4/ 

finding 144 videos from 4 pages...
```
```py
>>> vds

{'url_base': 'https://pornone.com', 'query': 'natasha+nice', 'url_search': 'https://pornone.com/video/natasha+nice', 'ping': 5.803735971450806, 'videos_per_pages': 36, 'len_pages': 4, 'len_videos': 144, 'videos': [{'title': 'Natasha Nice & Kenzie Love \u200b- Home For The Holidays', 'time': '40:13\n', 'dur': 2413, 'stats': '\n\n\n12\n\n\n\n2h ago\n\n\n\n\n\n', 'page_number': 1, 'url': 'https://pornone.com/love/natasha-nice-kenzie-love-home-for-the-holidays/278245379/?r=111', 'url_font': 'https://pornone.com/natasha-nice-porn-videos-10468/1/', 'thumbnail': 'https://th-eu4.pornone.com/t/79/278245379/b111.jpg'}, ...
```

### Ukevids

```py
>>> import dreams.ukevids as uk

>>> vds = uk.search_porn('natasha nice',page_limit=4)

finding 24 videos from 1 pages...
finding 48 videos from 2 pages...
finding 72 videos from 3 pages...
finding 96 videos from 4 pages...
```
```py
>>> vds

{'url_base': 'https://ukdevilz.com', 'query': 'natasha+nice', 'url_search': 'https://ukdevilz.com/video/natasha+nice', 'ping': 3.231513023376465, 'videos_per_pages': 24, 'len_pages': 4, 'len_videos': 96, 'videos': [{'title': 'Xandra sixx, darcie dolce, natasha nice (sorority initiation) sex porno', 'time': ' 31:58', 'dur': 1918, 'views': ' 122.88K', 'page_number': 1, 'url_font': 'https://ukdevilz.com/video/natasha+nice?p=1', 'url': 'https://ukdevilz.com/watch/-165193771_456239108', 'thumbnail': 'https://sun9-66.userapi.com/c845123/v845123080/699f2/42fyF8MAdjU.jpg'}, ....
```