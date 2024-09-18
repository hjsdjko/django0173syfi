#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class laoren(BaseModel):
    __doc__ = u'''laoren'''
    __tablename__ = 'laoren'

    __loginUser__='laorenzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='laorenzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    laorenzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='老人账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    laorenxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='老人姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    manxingbing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='慢性病' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    laorenzhanghao=VARCHAR
    mima=VARCHAR
    laorenxingming=VARCHAR
    xingbie=VARCHAR
    nianling=Integer
    shoujihaoma=VARCHAR
    manxingbing=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'laoren'
        verbose_name = verbose_name_plural = '老人'
class fuwurenyuan(BaseModel):
    __doc__ = u'''fuwurenyuan'''
    __tablename__ = 'fuwurenyuan'

    __loginUser__='renyuanbianhao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='renyuanbianhao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    renyuanbianhao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='人员编号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    renyuanxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='人员姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    fuwuleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='服务类型' )
    fuwufei=models.FloatField   (  null=True, unique=False, verbose_name='服务费' )
    jifeibiaozhun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='计费标准' )
    zhaopian=models.TextField   (  null=True, unique=False, verbose_name='照片' )
    fuwujianjie=models.TextField   (  null=True, unique=False, verbose_name='服务简介' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    renyuanbianhao=VARCHAR
    mima=VARCHAR
    renyuanxingming=VARCHAR
    xingbie=VARCHAR
    nianling=Integer
    lianxidianhua=VARCHAR
    fuwuleixing=VARCHAR
    fuwufei=Float
    jifeibiaozhun=VARCHAR
    zhaopian=Text
    fuwujianjie=Text
    sfsh=VARCHAR
    shhf=Text
    clicktime=DateTime
    clicknum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'fuwurenyuan'
        verbose_name = verbose_name_plural = '服务人员'
class manxingbing(BaseModel):
    __doc__ = u'''manxingbing'''
    __tablename__ = 'manxingbing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    manxingbing=models.CharField ( max_length=255,null=False,unique=True, verbose_name='慢性病' )
    '''
    manxingbing=VARCHAR
    '''
    class Meta:
        db_table = 'manxingbing'
        verbose_name = verbose_name_plural = '慢性病'
class shipuxinxi(BaseModel):
    __doc__ = u'''shipuxinxi'''
    __tablename__ = 'shipuxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shipumingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='食谱名称' )
    shipufengmian=models.TextField   (  null=True, unique=False, verbose_name='食谱封面' )
    manxingbing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='慢性病' )
    shipugongxiao=models.TextField   (  null=True, unique=False, verbose_name='食谱功效' )
    yingyangchengfen=models.TextField   (  null=True, unique=False, verbose_name='营养成分' )
    shipuxiangqing=models.TextField   (  null=True, unique=False, verbose_name='食谱详情' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    shipumingcheng=VARCHAR
    shipufengmian=Text
    manxingbing=VARCHAR
    shipugongxiao=Text
    yingyangchengfen=Text
    shipuxiangqing=Text
    clicktime=DateTime
    clicknum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'shipuxinxi'
        verbose_name = verbose_name_plural = '食谱信息'
class jiankangjiance(BaseModel):
    __doc__ = u'''jiankangjiance'''
    __tablename__ = 'jiankangjiance'



    __authTables__={'laorenzhanghao':'laoren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    laorenzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人账号' )
    laorenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人姓名' )
    xinlv=models.FloatField   ( null=False, unique=False, verbose_name='心率(次/分钟)' )
    xueya=models.FloatField   ( null=False, unique=False, verbose_name='舒张压(mmHg)' )
    xuetang=models.FloatField   ( null=False, unique=False, verbose_name='空腹血糖(mmol/L)' )
    xueyang=models.FloatField   ( null=False, unique=False, verbose_name='血氧(%)' )
    jianceshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='监测时间' )
    '''
    laorenzhanghao=VARCHAR
    laorenxingming=VARCHAR
    xinlv=Float
    xueya=Float
    xuetang=Float
    xueyang=Float
    jianceshijian=DateTime
    '''
    class Meta:
        db_table = 'jiankangjiance'
        verbose_name = verbose_name_plural = '健康监测'
class jiankangbaogao(BaseModel):
    __doc__ = u'''jiankangbaogao'''
    __tablename__ = 'jiankangbaogao'



    __authTables__={'laorenzhanghao':'laoren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    baogaodanhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='报告单号' )
    laorenzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人账号' )
    laorenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人姓名' )
    baogaotupian=models.TextField   (  null=True, unique=False, verbose_name='报告图片' )
    jiankangzhuangtai=models.CharField ( max_length=255,null=False, unique=False, verbose_name='健康状态' )
    jiankangbaogao=models.TextField   ( null=False, unique=False, verbose_name='健康报告' )
    jiankangqushi=models.TextField   ( null=False, unique=False, verbose_name='健康趋势' )
    jiankangjingbao=models.TextField   (  null=True, unique=False, verbose_name='健康警报' )
    jiankangjianyi=models.TextField   (  null=True, unique=False, verbose_name='健康建议' )
    baogaoshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='报告时间' )
    '''
    baogaodanhao=VARCHAR
    laorenzhanghao=VARCHAR
    laorenxingming=VARCHAR
    baogaotupian=Text
    jiankangzhuangtai=VARCHAR
    jiankangbaogao=Text
    jiankangqushi=Text
    jiankangjingbao=Text
    jiankangjianyi=Text
    baogaoshijian=DateTime
    '''
    class Meta:
        db_table = 'jiankangbaogao'
        verbose_name = verbose_name_plural = '健康报告'
class fuwuleixing(BaseModel):
    __doc__ = u'''fuwuleixing'''
    __tablename__ = 'fuwuleixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    fuwuleixing=models.CharField ( max_length=255,null=False,unique=True, verbose_name='服务类型' )
    '''
    fuwuleixing=VARCHAR
    '''
    class Meta:
        db_table = 'fuwuleixing'
        verbose_name = verbose_name_plural = '服务类型'
class fuwudingdan(BaseModel):
    __doc__ = u'''fuwudingdan'''
    __tablename__ = 'fuwudingdan'



    __authTables__={'renyuanbianhao':'fuwurenyuan','laorenzhanghao':'laoren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='订单编号' )
    renyuanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员编号' )
    renyuanxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    fuwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务类型' )
    zhaopian=models.TextField   (  null=True, unique=False, verbose_name='照片' )
    fuwufei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务费' )
    jifeibiaozhun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='计费标准' )
    laorenzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人账号' )
    laorenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    dizhi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
    fuwuxuqiu=models.TextField   ( null=False, unique=False, verbose_name='服务需求' )
    xiadanshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='下单时间' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    dingdanbianhao=VARCHAR
    renyuanbianhao=VARCHAR
    renyuanxingming=VARCHAR
    lianxidianhua=VARCHAR
    fuwuleixing=VARCHAR
    zhaopian=Text
    fuwufei=VARCHAR
    jifeibiaozhun=VARCHAR
    laorenzhanghao=VARCHAR
    laorenxingming=VARCHAR
    shoujihaoma=VARCHAR
    dizhi=VARCHAR
    fuwuxuqiu=Text
    xiadanshijian=DateTime
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'fuwudingdan'
        verbose_name = verbose_name_plural = '服务订单'
class jiedanfuwu(BaseModel):
    __doc__ = u'''jiedanfuwu'''
    __tablename__ = 'jiedanfuwu'



    __authTables__={'renyuanbianhao':'fuwurenyuan','laorenzhanghao':'laoren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='订单编号' )
    renyuanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员编号' )
    renyuanxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    fuwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务类型' )
    zhaopian=models.TextField   (  null=True, unique=False, verbose_name='照片' )
    laorenzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人账号' )
    laorenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    dizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    fuwufei=models.FloatField   (  null=True, unique=False, verbose_name='服务费' )
    jifeibiaozhun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='计费标准' )
    jifei=models.FloatField   ( null=False, unique=False, verbose_name='计费' )
    dingdanfeiyong=models.FloatField   (  null=True, unique=False, verbose_name='订单费用' )
    fuwuxiangqing=models.TextField   ( null=False, unique=False, verbose_name='服务详情' )
    fuwushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='服务时间' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    dingdanbianhao=VARCHAR
    renyuanbianhao=VARCHAR
    renyuanxingming=VARCHAR
    lianxidianhua=VARCHAR
    fuwuleixing=VARCHAR
    zhaopian=Text
    laorenzhanghao=VARCHAR
    laorenxingming=VARCHAR
    shoujihaoma=VARCHAR
    dizhi=VARCHAR
    fuwufei=Float
    jifeibiaozhun=VARCHAR
    jifei=Float
    dingdanfeiyong=Float
    fuwuxiangqing=Text
    fuwushijian=DateTime
    crossuserid=BigInteger
    crossrefid=BigInteger
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'jiedanfuwu'
        verbose_name = verbose_name_plural = '接单服务'
class fuwupingjia(BaseModel):
    __doc__ = u'''fuwupingjia'''
    __tablename__ = 'fuwupingjia'



    __authTables__={'renyuanbianhao':'fuwurenyuan','laorenzhanghao':'laoren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='回复'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='订单编号' )
    renyuanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员编号' )
    renyuanxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    fuwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务类型' )
    zhaopian=models.TextField   (  null=True, unique=False, verbose_name='照片' )
    laorenzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人账号' )
    laorenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    pingjianeirong=models.TextField   ( null=False, unique=False, verbose_name='评价内容' )
    pingjiashijian=models.DateTimeField  (  null=True, unique=False, verbose_name='评价时间' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    dingdanbianhao=VARCHAR
    renyuanbianhao=VARCHAR
    renyuanxingming=VARCHAR
    lianxidianhua=VARCHAR
    fuwuleixing=VARCHAR
    zhaopian=Text
    laorenzhanghao=VARCHAR
    laorenxingming=VARCHAR
    shoujihaoma=VARCHAR
    pingjianeirong=Text
    pingjiashijian=DateTime
    crossuserid=BigInteger
    crossrefid=BigInteger
    shhf=Text
    '''
    class Meta:
        db_table = 'fuwupingjia'
        verbose_name = verbose_name_plural = '服务评价'
class jinjiqiuzhu(BaseModel):
    __doc__ = u'''jinjiqiuzhu'''
    __tablename__ = 'jinjiqiuzhu'



    __authTables__={'laorenzhanghao':'laoren',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiuzhubianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='求助编号' )
    laorenzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人账号' )
    laorenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    dizhi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
    qiuzhuneirong=models.TextField   ( null=False, unique=False, verbose_name='求助内容' )
    qiuzhushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='求助时间' )
    qiuzhuzhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='求助状态' )
    '''
    qiuzhubianhao=VARCHAR
    laorenzhanghao=VARCHAR
    laorenxingming=VARCHAR
    shoujihaoma=VARCHAR
    dizhi=VARCHAR
    qiuzhuneirong=Text
    qiuzhushijian=DateTime
    qiuzhuzhuangtai=VARCHAR
    '''
    class Meta:
        db_table = 'jinjiqiuzhu'
        verbose_name = verbose_name_plural = '紧急求助'
class jiuzhuxiangying(BaseModel):
    __doc__ = u'''jiuzhuxiangying'''
    __tablename__ = 'jiuzhuxiangying'



    __authTables__={'laorenzhanghao':'laoren','renyuanbianhao':'fuwurenyuan',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiuzhubianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='求助编号' )
    laorenzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人账号' )
    laorenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='老人姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    dizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    renyuanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员编号' )
    renyuanxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    jiuzhuhuiying=models.CharField ( max_length=255, null=True, unique=False, verbose_name='救助回应' )
    xiangyingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='响应时间' )
    '''
    qiuzhubianhao=VARCHAR
    laorenzhanghao=VARCHAR
    laorenxingming=VARCHAR
    shoujihaoma=VARCHAR
    dizhi=VARCHAR
    renyuanbianhao=VARCHAR
    renyuanxingming=VARCHAR
    lianxidianhua=VARCHAR
    jiuzhuhuiying=VARCHAR
    xiangyingshijian=DateTime
    '''
    class Meta:
        db_table = 'jiuzhuxiangying'
        verbose_name = verbose_name_plural = '救助响应'
class xinxijiaoliu(BaseModel):
    __doc__ = u'''xinxijiaoliu'''
    __tablename__ = 'xinxijiaoliu'



    __authTables__={'renyuanbianhao':'fuwurenyuan','jiaoliuzhe':'fuwurenyuan',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiaoliubianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='交流编号' )
    renyuanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员编号' )
    renyuanxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员姓名' )
    jiaoliuzhe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='交流者' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    neirong=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    fasongshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='发送时间' )
    '''
    jiaoliubianhao=VARCHAR
    renyuanbianhao=VARCHAR
    renyuanxingming=VARCHAR
    jiaoliuzhe=VARCHAR
    xingming=VARCHAR
    neirong=Text
    fasongshijian=DateTime
    '''
    class Meta:
        db_table = 'xinxijiaoliu'
        verbose_name = verbose_name_plural = '信息交流'
class huifuxinxi(BaseModel):
    __doc__ = u'''huifuxinxi'''
    __tablename__ = 'huifuxinxi'



    __authTables__={'renyuanbianhao':'fuwurenyuan','jiaoliuzhe':'fuwurenyuan',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiaoliubianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='交流编号' )
    renyuanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员编号' )
    renyuanxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='人员姓名' )
    jiaoliuzhe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='交流者' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    huifuneirong=models.TextField   ( null=False, unique=False, verbose_name='回复内容' )
    huifushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='回复时间' )
    '''
    jiaoliubianhao=VARCHAR
    renyuanbianhao=VARCHAR
    renyuanxingming=VARCHAR
    jiaoliuzhe=VARCHAR
    xingming=VARCHAR
    huifuneirong=Text
    huifushijian=DateTime
    '''
    class Meta:
        db_table = 'huifuxinxi'
        verbose_name = verbose_name_plural = '回复信息'
class forum(BaseModel):
    __doc__ = u'''forum'''
    __tablename__ = 'forum'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255, null=True, unique=False, verbose_name='帖子标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='帖子内容' )
    parentid=models.BigIntegerField  (  null=True, unique=False, verbose_name='父节点id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    isdone=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='是否置顶' )
    toptime=models.DateTimeField  (  null=True, unique=False, verbose_name='置顶时间' )
    '''
    title=VARCHAR
    content=Text
    parentid=BigInteger
    userid=BigInteger
    username=VARCHAR
    avatarurl=Text
    isdone=VARCHAR
    istop=Integer
    toptime=DateTime
    '''
    class Meta:
        db_table = 'forum'
        verbose_name = verbose_name_plural = '社区互动'
class newstype(BaseModel):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    typename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类名称' )
    '''
    typename=VARCHAR
    '''
    class Meta:
        db_table = 'newstype'
        verbose_name = verbose_name_plural = '健康资讯分类'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    typename=VARCHAR
    name=VARCHAR
    headportrait=Text
    clicknum=Integer
    clicktime=DateTime
    thumbsupnum=Integer
    crazilynum=Integer
    storeupnum=Integer
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '健康资讯'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class systemintro(BaseModel):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'systemintro'
        verbose_name = verbose_name_plural = '系统简介'
