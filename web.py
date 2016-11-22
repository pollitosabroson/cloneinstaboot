#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(sys.path[0],'src'))

from instabot import InstaBot
from check_status import check_status
from feed_scanner import feed_scanner
from unfollow_protocol import unfollow_protocol
from follow_protocol import follow_protocol
import time


def test():
    bot = InstaBot(
        login="pollitosabroson", password="lolalatrailera123.",
        like_per_day=1400,
        comments_per_day=100,
        tag_list=['follow4follow', 'f4f', 'primerolacomunidad', 'ilovepiques', 'exklusive_shot', 'shotawars', 'descobreixcatalunya', 'ig_catalonia', 'ig_europe', 'ig_barcelona', 'ig_clubaward', 'ig_worldclub', 'ig_photooftheday', 'vsco', 'vscocam', 'fotonline_es', 'igersmaresme', 'thebarcelonist', 'igersspain', 'unlimitedbarcelona', 'fotomovil_es', 'catalunyagrafias', 'ok_catalunya', 'canonespaña', 'AGameofTones', 'PortraitGames', 'artofvisuals', 'catalunyaexperience', 'MoodyGrams', 'street_focus_on', 'raconsde_catalunya',],
        tag_blacklist=['rain', 'thunderstorm'],
        user_blacklist={'cube.miami':'', 'josep_batet': '', 'avq_68': '', 'rcaneter': ''},
        max_like_for_one_tag=46,
        follow_per_day=1000,
        follow_time=4*60*60,
        unfollow_per_day=0,
        unfollow_break_min=15,
        unfollow_break_max=30,
        log_mod=0,
        proxy='',
        # Use unwanted username list to block users which have username contains one of this string
        ## Doesn't have to match entirely example: mozart will be blocked because it contains *art
        ### freefollowers will be blocked because it contains free
        unwanted_username_list=['second','stuff','art','project','love','life','food','blog','free','keren','indo',
                             'travel','art','shop','store','sex','toko','jual','online','murah','jam','kaos','case','baju','fashion',
                              'corp','tas','butik','grosir','karpet','sosis','salon','skin','care','cloth','tech','rental',
                              'kamera','beauty','express','kredit','collection','impor','preloved','follow','follower','gain',
                              '.id','_id','bags'])

    try:
        bot.new_auto_mod()
    except Exception:
        test()

test()