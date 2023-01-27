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

getting data
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
