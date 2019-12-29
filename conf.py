# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
# 该值将用于生成帖子的永久链接。可能的值是https://myblog.com/或https://me.com/blog/或/blog/。如果要将站点放在子目录下，此选项可能很有用。最后不要忘记/。
site_prefix = "/notebook/"
# Maverick将尝试在其中查找文章的目录。它可以在您计算机上的任何位置，因此可以随时将您的文章存储在Dropbox，iCloud Drive或其他任何地方，以使它们跨多个设备同步。
source_dir = "../src/"
# Maverick应该将所有生成的HTML文件放在何处。该位置可以在您计算机上的任何位置，只需确保您对其具有写权限。
build_dir = "../dist/"
# 每页显示的帖子数，将其更改为任意数量。
index_page_size = 15
# 存档列表，类别列表和标签列表中每页显示的帖子数。
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "PrimaryFantasty/notebook@gh-pages"
}
# 指定模板以呈现您的网站。目前Galileo可用。
template = "Galileo"
# 指定Maverick如何处理您的图像。有关更多详细信息，请参阅图像和静态资产。默认false
fetch_remote_imgs = False
# 通过文件夹结构而不是前者对内容进行分类。默认false
category_by_folder = False

# 站点设置

# 网站名称。
site_name = "忘情錄"
# 网站徽标。最好是方形图像。
site_logo = "${static_prefix}logo.png"

site_build_date = "2019-12-28T16:51+08:00"
author = "Fantasty"
email = "primaryfantasty@qq.com"
author_homepage = "https://github.com/PrimaryFantasty/notebook"
description = "不亂於心 不困於情"
# 关于您的网站的四个或五个关键字。
# key_words = ['Fantasty','blog','']
# 网站语言。默认"english"
language = 'zh-CN'
# 将Links在主页的部分中使用。
external_links = [
]
# 将用于在网站标题后面生成导航。
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

# 将用于在网站标题后面生成社交链接。
social_links = [
   
]

# 这里的内容将添加到<head>生成的HTML的标签中，您可以meta在此处放置一些标签，或者使用<link>和<script>导入自定义CSS和JavaScript文件。
head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

# 这里的内容将被添加到<footer>标签中。您可以在此处添加一些其他信息。
footer_addon = ''

# 这里的内容将被添加到<body>标签，外部JavaScript中，并可以放在这里。
body_addon = ''

# 您网站的背景图片。最好是浅色的。
# background_img = ""
