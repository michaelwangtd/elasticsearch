# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch

if __name__ == '__main__':
    """
        连接到“node-test”节点
        创建newsbase索引（数据库）
        单条插入10条数据
    """

    es = Elasticsearch('127.0.0.1:9200')


    ## 创建索引（数据库）
    es.indices.create(
        index = 'newsbase',
        ignore = 400,
        body = {
            'index':{
                'number_of_replicas':0
            }
        }
    )


    ## 创建示例数据
    es.index(
        index = 'newsbase',
        doc_type = 'text',
        id = 1,
        body = {'type':'体育',
                'title':'鲍勃库西奖归谁属？',
                'digest':'NCAA最强控卫是坎巴还是弗神新浪体育讯如今，本赛季的NCAA进入到了末段，各项奖项的评选结果也即将出炉，其中评选最佳控卫的鲍勃-库西奖就将在下周最终四强战时公布，鲍勃-库西奖是由奈史密斯篮球名人堂提供，旨在奖励年度最佳大学控卫。'
                }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 2,
        body={'type': '娱乐',
              'title': '宁浩《无人区》定妆照曝光',
              'digest': '黄渤被剃光头(组图)新浪娱乐讯 由中国电影集团公司投资，宁浩执导的电影《无人区》已经在外景地新疆入驻两个多月，由于是宁浩的转型之作，再加上拍摄地选在广袤神秘的西域边陲，让这部电影备受关注。'
              }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 3,
        body={'type': '家居',
              'title': '前所未有的淡定从容',
              'digest': '2009年陶瓷行业渐趋理性这两天，我对今年陶瓷行业的发展情况作了一次小小的梳理，以期总结即将过去的上半年，然后展望即将迎来的下半年。'
              }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 4,
        body={'type': '家居',
              'title': '前沿卫浴',
              'digest': 'Zucchetti&KOS北京中粮旗舰店开业最前沿的意式风格卫浴世界——Zucchetti & KOS北京中粮广场旗舰店坐落于北京东城区的中粮广场内, “Zucchetti & KOS”这个卫浴界最璀璨的组合将全球最前沿的卫浴世界完美呈现在世人眼前，引领意大利式生活方式以及卫浴经典风情。卫浴精品店——“意大利生活馆”，是迄今为止Zucchetti&KOS进驻中国市场的唯一一家旗舰店。'
              }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 5,
        body={'type': '家居',
              'title': '力拓间谍门渐明晰',
              'digest': '陶瓷行业无间道却活跃近年来，“间谍类”影视剧在银幕大热,“无间道”系列影片更是席卷中国票房。但对于普通百姓而言,间谍在我们的生活中似乎并不真实出现。间谍片也更多是怀旧、纪念甚至是娱乐的性质。'
              }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 6,
        body={'type': '教育',
              'title': '名家指点：2012美国加拿大留学申请全攻略',
              'digest': '美国(微博)和加拿大留学一直是中国学生留学的首选和关注热点，2011年即将结束，在过去的这近1年中美国和加拿大(微博)留学又有哪些变化呢？'
              }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 7,
        body={'type': '教育',
              'title': '探访美国五所顶尖私立中学',
              'digest': '读高中并不轻松(组图)一直以来，到美国(微博)读书被视为孩子的天堂，作业少，考试少，没有一考定终身的高考，很多父母送孩子到美国读中学是因为听说在国外读书很轻松，可实际上记者此次应学美留学的邀请赴美国考察当地的一些私立中学发现，美国中学虽然上课较宽松'
              }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 8,
        body={'type': '体育',
              'title': '草根MVP表态愿终老大苹果',
              'digest': '让他们知道我还没过时新浪体育讯北京时间4月3日消息，本赛季交易截止日之前最重磅的交易，莫过于“小甜瓜”卡梅罗-安东尼加盟纽约尼克斯了。而作为这笔交易中被附带上的球员，昌西-比卢普斯一度被视为是那个最可怜的人——早在几个赛季之前，这位草根总决赛MVP就不止一次的表示过，自己愿意终老“雪域高原”丹佛，因为这里是他的家乡。'
              }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 9,
        body={'type': '科技',
              'title': '享受完美纯音质 iPod nano5评测',
              'digest': '9月10号苹果新品发布大会召开之前，几乎所有的小道消息都宣称新款iPod touch将配备摄像头，令人意外的是，这颗摄像头安到了iPod nano 5身上，再加上新增了FM收音机、外放扬声器、内置麦克风、计步器功能，并且屏幕从2.0英寸升级到2.2英寸，nano 5无疑是本次苹果大会上众人关注的焦点产品。'
              }
    )
    es.index(
        index='newsbase',
        doc_type='text',
        id= 10,
        body={'type': '科技',
              'title': '全画幅无敌兔！佳能5D MarkII售25200',
              'digest': '作为一款全画幅单反相机，佳能5D Mark II拥有出色的成像质量，是专业摄影师的好选择。由于采用全尺寸感光元件，所以在镜头使用时亦不需要折算焦距，在广角摄影方面也具备先天的优势。'
              }
    )
