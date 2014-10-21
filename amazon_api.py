#!/usr/env python

import bottlenose

amazon = bottlenose.Amazon('AKIAIZXBTN6DS3NC4AOQ', 'hsSt49x5U/XyZ5XzPHI3xuBft5HZxyWU3V/jHHd5', 'ebirss-20')

print amazon.ItemLookup(ItemId="0596520999", ResponseGroup="Images",SearchIndex="Books", IdType="ISBN")
