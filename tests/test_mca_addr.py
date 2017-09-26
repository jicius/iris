#!/usr/bin/env python
#   -*- coding: UTF-8-8 -*-
#
#   Copyright (C) 2017 Jicius
# 
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json

import requests


url = "http://xzqh.mca.gov.cn/selectJson"


headers = {
    "Host": "xzqh.mca.gov.cn",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "http://xzqh.mca.gov.cn",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://xzqh.mca.gov.cn/defaultQuery?shengji=%BC%AA%C1%D6%CA%A1%28%BC%AA%29&diji=%B0%D7%B3%C7%CA%D0&xianji=%E4%AC%B1%B1%C7%F8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "Cookie": "JSESSIONID=DF26D5F01FC01C790A57EAC1A99D3D16"
}

data = {
    "shengji": u"吉林省(吉)"
}

data = requests.post(url, headers=headers, data=data).text

