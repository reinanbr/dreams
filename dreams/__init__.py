'''
it project is a idea for a easy way for getting video's porn data from the best site's content porn
from internet.
For it, please, help it.
# '''
# # import toml
# import dreams.spankbang as bg
# import dreams.ukevids as uk
# import dreams.pornone as pn
# import dreams.noodlemagazine as nd
# import dreams.playvids as pv
# #import dreams.xvideos as xv
# #import dreams.pornhub as ph


# spankbang = bg.search_porn

# config = toml.load('settings/config.toml')
# print(config['INFO'])
from dreams.sites.pornone import pornone
#from dreams.sites import spankbang
from dreams.sites.ukdevilz import ukdevilz

from dreams.sites import tnaflix

from dreams.sites import noodlemagazine

from dreams.sites import pornhub

all = [ukdevilz,pornhub,pornone,tnaflix,noodlemagazine]


__version__ = '0.3'
__author__ = 'ReinanBr <slimchatuba@gmail.com>'