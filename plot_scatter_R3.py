# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 08:41:06 2018

@author: Ping-Chen Lin 
"""

import numpy as np
import plotly.offline as pyo
from plotly.graph_objs import Figure, Data
#設定網頁離線的畫圖介面
pyo.offline.init_notebook_mode()
#設定樣本數
N = 1000
#設定x, y資料與線上的格式
trace1 = {'type':'scatter',
        'x' : np.random.randn(N),
        'y' : np.random.randn(N)+5,
        'name':'scatter plot',
        'mode':'markers', 
        'marker' : {
                'size' : 14, 
                'color' : np.random.randn(N),
                #設定顏色刻度的色系
                'colorscale' : 'Jet',
                #顯示顏色刻度
                'showscale' : True,
                'line' : {
                        'width' : 1,
                        }
                }
        }
#設定x,y軸與title名稱
layout = {'title':'分佈圖',
         'xaxis':{'title':'x軸'},
         'yaxis':{'title':'y軸'}}
#設定trace資料到data屬性
data = Data([trace1])
#帶入Figure畫圖函數包含資料與版面配置
fig = Figure(data=data, layout=layout)
#畫圖
pyo.plot(fig)
