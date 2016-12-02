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
        login=os.environ.get('username', None), password=os.environ.get(
            'password', None),
        like_per_day=1400,
        comments_per_day=300,
        tag_list=[
            'primerolacomunidad', 'neverstopexploring', 'passionpassport',
            'guardiantravelsnaps', 'guardiancities', 'cnntravel', 'bbctravel',
            'folkmagazine', 'livefolk', 'liveauthentic', 'visualoflife',
            'travelstoke', 'wanderlust', 'mkexplore', 'letsgosomewhere',
            'agameoftones', 'hallazgosemanal', 'artofvisuals' 'Zacatecas',
            'México', 'España', 'España', 'Espanya', 'cataluña', 'catalunya',
            'Terrassa', 'follow4follow', 'f4f', 'ilovepiques', 'MoodyPorts',
            'MP_kingy_kings', 'artofvisuals', 'aov', 'bevisuallyinspired',
            'zeiss', 'vscocam', 'justgoshoot', 'artofvisuals',
            'CreateExploreTakeover', 'visualsgang', 'igworldclub',
            'special_shots', 'artofvisuals', 'igphotoworld', 'shotaward',
            'ig_worldclub', 'instagoodmyphoto', 'createcommune'],
        tag_blacklist=[],
        user_blacklist={
            # 'cube.miami': '', 'josep_batet': '', 'avq_68': '', 'rcaneter': '',
            # 'sergitugas': '', 'focvl_point': ''
        },
        max_like_for_one_tag=30,
        follow_per_day=0,
        follow_time=4 * 60 * 60,
        unfollow_per_day=0,
        unfollow_break_min=15,
        unfollow_break_max=30,
        log_mod=0,
        proxy='',
        # Use unwanted username list to block users which have username contains one of this string
        # Doesn't have to match entirely example: mozart will be blocked because it contains *art
        # freefollowers will be blocked because it contains free
        unwanted_username_list=[
            'second', 'stuff', 'art', 'project', 'love', 'life', 'food',
            'blog', 'free', 'keren', 'indo', 'travel', 'art', 'shop', 'store',
            'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos', 'case',
            'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
            'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental',
            'kamera', 'beauty', 'express', 'kredit', 'collection', 'impor',
            'preloved', 'follow', 'follower', 'gain', '.id', '_id', 'bags'
        ]
    )

    try:
        bot.new_auto_mod()
    except Exception:
        test()

test()
