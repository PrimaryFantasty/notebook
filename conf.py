# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/notebook/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "PrimaryFantasty/notebook@gh-pages"
}

# 站点设置
site_name = "          忘情錄           "
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-28T16:51+08:00"
author = "Fantasty"
email = "primaryfantasty@qq.com"
author_homepage = "https://github.com/PrimaryFantasty/notebook"
description = "不亂於心 不困於情 不畏將來 不念過往"
key_words = ['Fantasty']
language = 'zh-CN'
external_links = [
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
   
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
