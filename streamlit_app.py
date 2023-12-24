# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:01:51 2023

@author: zxf22
"""
# 使用 sqlite3 的 connect 函数可以创建数据库或者连接数据库，
# 如果这个数据库存在，就连接这个数据库，
# 如果这个库不存在，就创建数据库。
# conn = sqlite3.connect('.//db_data//db_data.db')  # 连接数据库
# # connect()方法，可以判断一个数据库文件是否存在，如果不存在就自动创建一个，如果存在的话，就打开那个数据库。
# cus = conn.cursor()  # 创建游标
# cus.execute('SELECT name, username FROM userstable')
# df = pd.DataFrame(cus)
# df 
# names = df[0]
# usernames = df[1]

import pickle
from pathlib import Path

import sqlite3
import pandas as pd
import numpy as np

import streamlit as st
from streamlit_multipage import MultiPage
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_multipage import MultiPage
# import streamlit.components.v1 as html
from streamlit.components.v1 import html
import streamlit_authenticator as stauth
import streamlit_nested_layout

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="页面展示", #页面标题
    page_icon="💖", #icon
    layout="wide", #页面布局
    initial_sidebar_state="auto" #侧边栏，'collapsed'，'expanded'
    )

# 去掉页头页脚
css = """
    <style>
    header {visibility:hidden;}
    footer {visibility:hidden;}
    </style>
"""
# header #MainMenu
st.markdown(css, unsafe_allow_html=True)






# --- USER AUTHENTICATION ---
names = ["zhouxf", "guest"]
usernames = ['zxf2287','guest']

# load hashed passwords
file_path = Path(__file__).parent /'pw_pkl/hashed_pw.pkl'
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=2)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password..."
                "游客访问 | 用户名：guest；密码：abc123")

if authentication_status:

    # 修改Streamlit右则背景颜色
    custon_style = """
        <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5
        {background-color: rgb(245 245 245 / 100%);  font-size: large;}
        <style>"""
    st.markdown(custon_style, unsafe_allow_html=True)

    
    # 欢迎与退出
    # authenticator.logout("Logout", "sidebar")
    st.sidebar.text(f"Welcome {name}") #title
    
    ## logout_a = authenticator.logout("Logout", "sidebar")

    # with st.sidebar:
    #     # # "https://static.streamlit.io/examples/cat.jpg"
    #     # st.sidebar.image("./image/cat.png",width=200)
    #     col1, col2 = st.columns([1, 1])
    #     with col1:
    #         st.sidebar.text(f"Welcome {name}")
    #     with col2:
    #         authenticator.logout("Logout", "sidebar")


    # 左侧导航栏
    with st.sidebar:
        choose = option_menu("数据中台", ["运营数据", "用户画像", "行为分析", "波次策略", "智慧物流解决方案", "项目介绍"],
                            icons=['bi bi-activity', 'bi bi-person', 'bar-chart', 'bi bi-graph-up', 'bi bi-globe', 'bi bi-search', 'house'],
                            menu_icon="bi bi-soundwave", default_index=0) #broadcast
    authenticator.logout("Logout", "sidebar")

    if choose == '项目介绍':
        st.subheader('开发：周笑丰')
        st.subheader('邮箱：zxf2287@live.com')
        st.header('数据可视化看板，非真实数据:sunglasses:')

    if choose == '运营数据':
        ## @st.cache
        # f_name = "./data_charts/index.html"
        # text_a=""
        # with open(f_name, encoding='utf-8') as fp: #如果遇到decode错误，就加上合适的encoding
        #     text_a=fp.read()
        # components.html(text_a, height=5500)
        index_dc = open("./data_charts/index.html", encoding='utf-8')
        components.html(f"""{index_dc.read()}""", height=5500)
    if choose == '用户画像':
        user_num = open("./data_charts/用户画像.html", encoding='utf-8')
        components.html(f"""{user_num.read()}""", height=6300)


    if choose == '波次策略':
        # # 右侧导航栏
        # selecte = option_menu(None, ["波次时间截点", "波次规则", "订单结构占比"],
        #                         icons=['bi bi-clock-history', 'bi bi-window-stack', 'bi bi-file-earmark-bar-graph'],
        #                         menu_icon="cast", default_index=0, orientation="horizontal")
        # if selecte == '波次时间截点':
        #     f_time = open("./assets/波次时间与订单量.html", encoding='utf-8')
        #     components.html(f"""{f_time.read()}""", height=1250)
        
        # if selecte == '波次规则':
        #     my_placeholder_a = st.empty()
        #     my_placeholder_b = st.empty()
        #     st.markdown('##### &#160;&#160;')
        #     f = open("./assets/波次策略.html", encoding='utf-8')
        #     # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
        #     components.html(f"""{f.read()}""", height=600)
        
        # if selecte == '订单结构占比':
        #     # st.markdown('### 订单结构占比')
        #     f_jiegou_jjt = open("./assets/订单结构占比.html", encoding='utf-8')
        #     # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
        #     components.html(f"""{f_jiegou_jjt.read()}""", height=500)

        #     f_jiegou_xudong = open("./assets/page_simple_layoutAA10.html", encoding='utf-8')
        #     # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
        #     components.html(f"""{f_jiegou_xudong.read()}""", height=500)

        custon_style_right = """
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.stTabs.css-0.exp6ofz0 > div > div:nth-child(1) > div
            {background-color: rgb(255 255 255 / 100%); font-size: large;}
            <style>"""
        st.markdown(custon_style_right, unsafe_allow_html=True)


        tab1, tab2, tab3 = st.tabs(["波次时间截点", "波次规则", "订单结构占比"])
        with tab1:
            f_time = open("./data_charts/波次时间与订单量.html", encoding='utf-8')
            components.html(f"""{f_time.read()}""", height=1250)

        with tab2:
            f = open("./data_charts/波次策略.html", encoding='utf-8')
            # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
            components.html(f"""{f.read()}""", height=600)

        with tab3:
            f_jiegou_jjt = open("./data_charts/订单结构占比.html", encoding='utf-8')
            # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
            components.html(f"""{f_jiegou_jjt.read()}""", height=500)
        

        # f_jiegou_jjt = open("./assets/分页组件_tab_base.html", encoding='utf-8')
        #     # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
        # components.html(f"""{f_jiegou_jjt.read()}""", height=500)   

            # 修改Streamlit右则背景颜色
    if choose == '行为分析':

        custon_style_right_SKU = """
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.stTabs.css-0.exp6ofz0 > div > div:nth-child(1) > div
            {background-color: rgb(255 255 255 / 100%); font-size: large;}
            <style>"""

        SKU_num = open("./data_charts/用户行为分析.html", encoding='utf-8')
        components.html(f"""{SKU_num.read()}""", height=10000)

    
    if choose == "关联分析":
        custon_style_right_link = """
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.stTabs.css-0.exp6ofz0 > div > div:nth-child(1) > div
            {background-color: rgb(255 255 255 / 100%); font-size: large;}
            <style>"""
        st.markdown(custon_style_right_link, unsafe_allow_html=True)

        tab_SKU_link, tab_SKU_ciyun, tab_SKU_top5 = st.tabs(["SKU关联图谱", "SKU销量", "SKU销量Top5_产品组合"])
        with tab_SKU_link:
            SKU_link = open("./data_charts/SKU关联图谱.html", encoding='utf-8')
            components.html(f"""{SKU_link.read()}""", height=650)
        with tab_SKU_ciyun:
            SKU_ciyun = open("./data_charts/SKU销量词云.html", encoding='utf-8')
            components.html(f"""{SKU_ciyun.read()}""", height=650)
        with tab_SKU_top5:
            SKU_num_top5 = open("./data_charts/SKU销量Top5组合.html", encoding='utf-8')
            components.html(f"""{SKU_num_top5.read()}""", height=650)
    
    if choose == "审单进度": 
        custon_style_right_shengdan = """
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.stTabs.css-0.exp6ofz0 > div > div:nth-child(1) > div
            {background-color: rgb(255 255 255 / 100%); font-size: large;}
            <style>"""
        st.markdown(custon_style_right_shengdan, unsafe_allow_html=True)

        tab_order_xiaosou, tab_order_shengdan, tab_order_top10 = st.tabs(["销售部订单占比", "销售部审单进度", "店铺销量Top10"])
        with tab_order_xiaosou:
            f_order_xiaosou = open("./data_charts/销售部单量占比.html", encoding='utf-8')
            # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
            components.html(f"""{f_order_xiaosou.read()}""", height=500)
        with tab_order_shengdan:
            f_shengdan_a = open("./data_charts/审单进度.html", encoding='utf-8')
            # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
            components.html(f"""{f_shengdan_a.read()}""", height=500)
        with tab_order_top10:
            f_order_top10 = open("./data_charts/店铺销量Top10.html", encoding='utf-8')
            # st.markdown( f"""{f.read()}""", unsafe_allow_html=True)
            components.html(f"""{f_order_top10.read()}""", height=500)

    if choose == '智慧物流解决方案':
        user_num = open("./data_charts/解决方案.html", encoding='utf-8')
        components.html(f"""{user_num.read()}""", height=6300)

