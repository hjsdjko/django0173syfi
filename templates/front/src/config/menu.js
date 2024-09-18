const menu = {
    list() {
        return [{"backMenu":[{"child":[{"allButtons":["新增","查看","修改","删除","老人统计","老人慢性病","首页总数"],"appFrontIcon":"cuIcon-cardboard","buttons":["新增","查看","修改","删除"],"menu":"老人","menuJump":"列表","tableName":"laoren"}],"menu":"老人管理"},{"child":[{"allButtons":["新增","查看","修改","删除","审核","下单","交流"],"appFrontIcon":"cuIcon-rank","buttons":["新增","查看","修改","删除","审核"],"menu":"服务人员","menuJump":"列表","tableName":"fuwurenyuan"}],"menu":"服务人员管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-addressbook","buttons":["新增","查看","修改","删除"],"menu":"慢性病","menuJump":"列表","tableName":"manxingbing"}],"menu":"慢性病管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-cardboard","buttons":["新增","查看","修改","删除"],"menu":"食谱信息","menuJump":"列表","tableName":"shipuxinxi"}],"menu":"食谱信息管理"},{"child":[{"allButtons":["新增","查看","修改","删除","健康数据","首页总数","健康报告"],"appFrontIcon":"cuIcon-form","buttons":["查看","修改","删除","健康报告"],"menu":"健康监测","menuJump":"列表","tableName":"jiankangjiance"}],"menu":"健康监测管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-similar","buttons":["查看","修改","删除"],"menu":"健康报告","menuJump":"列表","tableName":"jiankangbaogao"}],"menu":"健康报告管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-qrcode","buttons":["新增","查看","修改","删除"],"menu":"服务类型","menuJump":"列表","tableName":"fuwuleixing"}],"menu":"服务类型管理"},{"child":[{"allButtons":["新增","查看","修改","删除","审核","老人服务需求","首页总数","服务"],"appFrontIcon":"cuIcon-full","buttons":["查看","修改","删除"],"menu":"服务订单","menuJump":"列表","tableName":"fuwudingdan"}],"menu":"服务订单管理"},{"child":[{"allButtons":["新增","查看","修改","删除","支付","评价"],"appFrontIcon":"cuIcon-present","buttons":["查看","修改","删除"],"menu":"接单服务","menuJump":"列表","tableName":"jiedanfuwu"}],"menu":"接单服务管理"},{"child":[{"allButtons":["新增","查看","修改","删除","审核"],"appFrontIcon":"cuIcon-camera","buttons":["查看","修改","删除"],"menu":"服务评价","menuJump":"列表","tableName":"fuwupingjia"}],"menu":"服务评价管理"},{"child":[{"allButtons":["新增","查看","修改","删除","救助"],"appFrontIcon":"cuIcon-skin","buttons":["查看","修改","删除"],"menu":"紧急求助","menuJump":"列表","tableName":"jinjiqiuzhu"}],"menu":"紧急求助管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-flashlightopen","buttons":["查看","修改","删除"],"menu":"救助响应","menuJump":"列表","tableName":"jiuzhuxiangying"}],"menu":"救助响应管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-group","buttons":["查看","修改","删除"],"menu":"社区互动","tableName":"forum"}],"menu":"社区互动"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-taxi","buttons":["查看","修改"],"menu":"轮播图管理","tableName":"config"},{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"健康资讯","tableName":"news"},{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"健康资讯分类","tableName":"newstype"},{"allButtons":["查看","修改"],"appFrontIcon":"cuIcon-clothes","buttons":["查看","修改"],"menu":"系统简介","tableName":"systemintro"}],"menu":"系统管理"}],"frontMenu":[{"child":[{"allButtons":["新增","查看","修改","删除","审核","下单","交流"],"appFrontIcon":"cuIcon-discover","buttons":["查看","下单"],"menu":"服务人员列表","menuJump":"列表","tableName":"fuwurenyuan"}],"menu":"服务人员模块"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-discover","buttons":["查看"],"menu":"食谱信息列表","menuJump":"列表","tableName":"shipuxinxi"}],"menu":"食谱信息模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"allButtons":["新增","查看","修改","删除","健康数据","首页总数","健康报告"],"appFrontIcon":"cuIcon-form","buttons":["新增","查看","修改","删除"],"menu":"健康监测","menuJump":"列表","tableName":"jiankangjiance"}],"menu":"健康监测管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-similar","buttons":["查看"],"menu":"健康报告","menuJump":"列表","tableName":"jiankangbaogao"}],"menu":"健康报告管理"},{"child":[{"allButtons":["新增","查看","修改","删除","审核","老人服务需求","首页总数","服务"],"appFrontIcon":"cuIcon-full","buttons":["查看"],"menu":"服务订单","menuJump":"列表","tableName":"fuwudingdan"}],"menu":"服务订单管理"},{"child":[{"allButtons":["新增","查看","修改","删除","支付","评价"],"appFrontIcon":"cuIcon-present","buttons":["查看","支付","评价"],"menu":"接单服务","menuJump":"列表","tableName":"jiedanfuwu"}],"menu":"接单服务管理"},{"child":[{"allButtons":["新增","查看","修改","删除","审核"],"appFrontIcon":"cuIcon-camera","buttons":["查看","修改","删除"],"menu":"服务评价","menuJump":"列表","tableName":"fuwupingjia"}],"menu":"服务评价管理"},{"child":[{"allButtons":["新增","查看","修改","删除","救助"],"appFrontIcon":"cuIcon-skin","buttons":["新增","查看","修改","删除"],"menu":"紧急求助","menuJump":"列表","tableName":"jinjiqiuzhu"}],"menu":"紧急求助管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-flashlightopen","buttons":["查看"],"menu":"救助响应","menuJump":"列表","tableName":"jiuzhuxiangying"}],"menu":"救助响应管理"}],"frontMenu":[{"child":[{"allButtons":["新增","查看","修改","删除","审核","下单","交流"],"appFrontIcon":"cuIcon-discover","buttons":["查看","下单"],"menu":"服务人员列表","menuJump":"列表","tableName":"fuwurenyuan"}],"menu":"服务人员模块"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-discover","buttons":["查看"],"menu":"食谱信息列表","menuJump":"列表","tableName":"shipuxinxi"}],"menu":"食谱信息模块"}],"hasBackLogin":"否","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"老人","tableName":"laoren"},{"backMenu":[{"child":[{"allButtons":["新增","查看","修改","删除","审核","下单","交流"],"appFrontIcon":"cuIcon-rank","buttons":["查看","交流"],"menu":"服务人员","menuJump":"列表","tableName":"fuwurenyuan"}],"menu":"服务人员管理"},{"child":[{"allButtons":["新增","查看","修改","删除","审核","老人服务需求","首页总数","服务"],"appFrontIcon":"cuIcon-full","buttons":["查看","审核","服务"],"menu":"服务订单","menuJump":"列表","tableName":"fuwudingdan"}],"menu":"服务订单管理"},{"child":[{"allButtons":["新增","查看","修改","删除","支付","评价"],"appFrontIcon":"cuIcon-present","buttons":["查看"],"menu":"接单服务","menuJump":"列表","tableName":"jiedanfuwu"}],"menu":"接单服务管理"},{"child":[{"allButtons":["新增","查看","修改","删除","审核"],"appFrontIcon":"cuIcon-camera","buttons":["查看","审核"],"menu":"服务评价","menuJump":"列表","tableName":"fuwupingjia"}],"menu":"服务评价管理"},{"child":[{"allButtons":["新增","查看","修改","删除","救助"],"appFrontIcon":"cuIcon-skin","buttons":["查看","救助"],"menu":"紧急求助","menuJump":"列表","tableName":"jinjiqiuzhu"}],"menu":"紧急求助管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-flashlightopen","buttons":["查看","修改"],"menu":"救助响应","menuJump":"列表","tableName":"jiuzhuxiangying"}],"menu":"救助响应管理"},{"child":[{"allButtons":["新增","查看","修改","删除","回复"],"appFrontIcon":"cuIcon-cardboard","buttons":["查看","回复"],"menu":"信息交流","menuJump":"列表","tableName":"xinxijiaoliu"}],"menu":"信息交流管理"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-newshot","buttons":["查看"],"menu":"回复信息","menuJump":"列表","tableName":"huifuxinxi"}],"menu":"回复信息管理"}],"frontMenu":[{"child":[{"allButtons":["新增","查看","修改","删除","审核","下单","交流"],"appFrontIcon":"cuIcon-discover","buttons":["查看","下单"],"menu":"服务人员列表","menuJump":"列表","tableName":"fuwurenyuan"}],"menu":"服务人员模块"},{"child":[{"allButtons":["新增","查看","修改","删除"],"appFrontIcon":"cuIcon-discover","buttons":["查看"],"menu":"食谱信息列表","menuJump":"列表","tableName":"shipuxinxi"}],"menu":"食谱信息模块"}],"hasBackLogin":"是","hasBackRegister":"是","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"服务人员","tableName":"fuwurenyuan"}]
    }
}
export default menu;