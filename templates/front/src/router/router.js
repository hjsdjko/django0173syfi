import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Forum from '../pages/forum/list'
import ForumAdd from '../pages/forum/add'
import ForumDetail from '../pages/forum/detail'
import MyForumList from '../pages/forum/myForumList'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import laorenList from '../pages/laoren/list'
import laorenDetail from '../pages/laoren/detail'
import laorenAdd from '../pages/laoren/add'
import fuwurenyuanList from '../pages/fuwurenyuan/list'
import fuwurenyuanDetail from '../pages/fuwurenyuan/detail'
import fuwurenyuanAdd from '../pages/fuwurenyuan/add'
import manxingbingList from '../pages/manxingbing/list'
import manxingbingDetail from '../pages/manxingbing/detail'
import manxingbingAdd from '../pages/manxingbing/add'
import shipuxinxiList from '../pages/shipuxinxi/list'
import shipuxinxiDetail from '../pages/shipuxinxi/detail'
import shipuxinxiAdd from '../pages/shipuxinxi/add'
import jiankangjianceList from '../pages/jiankangjiance/list'
import jiankangjianceDetail from '../pages/jiankangjiance/detail'
import jiankangjianceAdd from '../pages/jiankangjiance/add'
import jiankangbaogaoList from '../pages/jiankangbaogao/list'
import jiankangbaogaoDetail from '../pages/jiankangbaogao/detail'
import jiankangbaogaoAdd from '../pages/jiankangbaogao/add'
import fuwuleixingList from '../pages/fuwuleixing/list'
import fuwuleixingDetail from '../pages/fuwuleixing/detail'
import fuwuleixingAdd from '../pages/fuwuleixing/add'
import fuwudingdanList from '../pages/fuwudingdan/list'
import fuwudingdanDetail from '../pages/fuwudingdan/detail'
import fuwudingdanAdd from '../pages/fuwudingdan/add'
import jiedanfuwuList from '../pages/jiedanfuwu/list'
import jiedanfuwuDetail from '../pages/jiedanfuwu/detail'
import jiedanfuwuAdd from '../pages/jiedanfuwu/add'
import fuwupingjiaList from '../pages/fuwupingjia/list'
import fuwupingjiaDetail from '../pages/fuwupingjia/detail'
import fuwupingjiaAdd from '../pages/fuwupingjia/add'
import jinjiqiuzhuList from '../pages/jinjiqiuzhu/list'
import jinjiqiuzhuDetail from '../pages/jinjiqiuzhu/detail'
import jinjiqiuzhuAdd from '../pages/jinjiqiuzhu/add'
import jiuzhuxiangyingList from '../pages/jiuzhuxiangying/list'
import jiuzhuxiangyingDetail from '../pages/jiuzhuxiangying/detail'
import jiuzhuxiangyingAdd from '../pages/jiuzhuxiangying/add'
import xinxijiaoliuList from '../pages/xinxijiaoliu/list'
import xinxijiaoliuDetail from '../pages/xinxijiaoliu/detail'
import xinxijiaoliuAdd from '../pages/xinxijiaoliu/add'
import huifuxinxiList from '../pages/huifuxinxi/list'
import huifuxinxiDetail from '../pages/huifuxinxi/detail'
import huifuxinxiAdd from '../pages/huifuxinxi/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import systemintroList from '../pages/systemintro/list'
import systemintroDetail from '../pages/systemintro/detail'
import systemintroAdd from '../pages/systemintro/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'forum',
					component: Forum
				},
				{
					path: 'forumAdd',
					component: ForumAdd
				},
				{
					path: 'forumDetail',
					component: ForumDetail
				},
				{
					path: 'myForumList',
					component: MyForumList
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'laoren',
					component: laorenList
				},
				{
					path: 'laorenDetail',
					component: laorenDetail
				},
				{
					path: 'laorenAdd',
					component: laorenAdd
				},
				{
					path: 'fuwurenyuan',
					component: fuwurenyuanList
				},
				{
					path: 'fuwurenyuanDetail',
					component: fuwurenyuanDetail
				},
				{
					path: 'fuwurenyuanAdd',
					component: fuwurenyuanAdd
				},
				{
					path: 'manxingbing',
					component: manxingbingList
				},
				{
					path: 'manxingbingDetail',
					component: manxingbingDetail
				},
				{
					path: 'manxingbingAdd',
					component: manxingbingAdd
				},
				{
					path: 'shipuxinxi',
					component: shipuxinxiList
				},
				{
					path: 'shipuxinxiDetail',
					component: shipuxinxiDetail
				},
				{
					path: 'shipuxinxiAdd',
					component: shipuxinxiAdd
				},
				{
					path: 'jiankangjiance',
					component: jiankangjianceList
				},
				{
					path: 'jiankangjianceDetail',
					component: jiankangjianceDetail
				},
				{
					path: 'jiankangjianceAdd',
					component: jiankangjianceAdd
				},
				{
					path: 'jiankangbaogao',
					component: jiankangbaogaoList
				},
				{
					path: 'jiankangbaogaoDetail',
					component: jiankangbaogaoDetail
				},
				{
					path: 'jiankangbaogaoAdd',
					component: jiankangbaogaoAdd
				},
				{
					path: 'fuwuleixing',
					component: fuwuleixingList
				},
				{
					path: 'fuwuleixingDetail',
					component: fuwuleixingDetail
				},
				{
					path: 'fuwuleixingAdd',
					component: fuwuleixingAdd
				},
				{
					path: 'fuwudingdan',
					component: fuwudingdanList
				},
				{
					path: 'fuwudingdanDetail',
					component: fuwudingdanDetail
				},
				{
					path: 'fuwudingdanAdd',
					component: fuwudingdanAdd
				},
				{
					path: 'jiedanfuwu',
					component: jiedanfuwuList
				},
				{
					path: 'jiedanfuwuDetail',
					component: jiedanfuwuDetail
				},
				{
					path: 'jiedanfuwuAdd',
					component: jiedanfuwuAdd
				},
				{
					path: 'fuwupingjia',
					component: fuwupingjiaList
				},
				{
					path: 'fuwupingjiaDetail',
					component: fuwupingjiaDetail
				},
				{
					path: 'fuwupingjiaAdd',
					component: fuwupingjiaAdd
				},
				{
					path: 'jinjiqiuzhu',
					component: jinjiqiuzhuList
				},
				{
					path: 'jinjiqiuzhuDetail',
					component: jinjiqiuzhuDetail
				},
				{
					path: 'jinjiqiuzhuAdd',
					component: jinjiqiuzhuAdd
				},
				{
					path: 'jiuzhuxiangying',
					component: jiuzhuxiangyingList
				},
				{
					path: 'jiuzhuxiangyingDetail',
					component: jiuzhuxiangyingDetail
				},
				{
					path: 'jiuzhuxiangyingAdd',
					component: jiuzhuxiangyingAdd
				},
				{
					path: 'xinxijiaoliu',
					component: xinxijiaoliuList
				},
				{
					path: 'xinxijiaoliuDetail',
					component: xinxijiaoliuDetail
				},
				{
					path: 'xinxijiaoliuAdd',
					component: xinxijiaoliuAdd
				},
				{
					path: 'huifuxinxi',
					component: huifuxinxiList
				},
				{
					path: 'huifuxinxiDetail',
					component: huifuxinxiDetail
				},
				{
					path: 'huifuxinxiAdd',
					component: huifuxinxiAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'systemintro',
					component: systemintroList
				},
				{
					path: 'systemintroDetail',
					component: systemintroDetail
				},
				{
					path: 'systemintroAdd',
					component: systemintroAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
