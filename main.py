# coding=utf-8
import networkx as nx
import matplotlib.pylab as plt

# G = nx.DiGraph()


nSize = 1
fSize = 1.0
w = 0.05



G = nx.Graph()

# 山手線
G.add_cycle([u"品川", u"大崎", u"五反田", u"目黒", u"恵比寿", u"渋谷", u"原宿",
                  u"代々木", u"新宿", u"新大久保", u"高田馬場", u"目白", u"池袋", u"大塚", u"巣鴨", u"駒越", u"田端駅", u"西日暮里",
                  u"日暮里", u"鶯谷", u"上野", u"御徒町", u"秋葉原", u"神田", u"東京", u"有楽町", u"新橋", u"浜松町", u"田町", u"品川"])

# 目黒線
G.add_path([u"日吉",u"元住吉",u"武蔵小杉",u"新丸子",u"多摩川",u"田園調布",u"奥沢",u"大岡山",u"洗足",u"西小山",u"武蔵小山",u"不動前",u"目黒"])

# 池上線
G.add_path([u"蒲田", u"蓮沼", u"池上", u"千鳥町", u"久が原", u"御嶽山", u"雪が谷大塚", u"石川台", u"洗足池", u"長原", u"旗の台", u"荏原中延",
                    u"戸越銀座", u"大崎広小路", u"五反田"])

# 大井町線
G.add_path([u"二子玉川", u"上野毛", u"等々力", u"尾山台", u"九品仏", u"自由が丘", u"緑が丘", u"大岡山", u"北千束", u"旗の台", u"荏原町",
                    u"中延", u"戸越公園", u"下神明", u"大井町"])

# 多摩川線
G.add_path([u"多摩川",u"沼部",u"鵜の木",u"下丸子",u"武蔵新田",u"矢口渡",u"蒲田"])

# 日比谷線
G.add_path([u"二子玉川", u"上野毛", u"等々力", u"尾山台", u"九品仏", u"自由が丘", u"緑が丘", u"大岡山", u"北千束", u"旗の台", u"荏原町",
                   u"中延", u"戸越公園", u"下神明", u"大井町"])


nx.draw_networkx(G,pos=nx.spring_layout(G), node_size=nSize, font_size=fSize, width=w)


# print('all paths')


path = nx.shortest_path(G,source=u"新宿",target=u"上野毛")
print "長さは"
print len(path)
print path

# shortestPath = pathlist[0]
# for num in range(1,len(pathlist)):
#     if len(shortestPath)<len(pathlist[num]):
#         shortestPath = pathlist[num]
#     print "最小pathは"
#     print shortestPath


# plt.xticks([])
# plt.yticks([])
# plt.show()