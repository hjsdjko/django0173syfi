import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Board from '@/views/board'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import news from '@/views/modules/news/list'
    import xinxijiaoliu from '@/views/modules/xinxijiaoliu/list'
    import manxingbing from '@/views/modules/manxingbing/list'
    import huifuxinxi from '@/views/modules/huifuxinxi/list'
    import fuwudingdan from '@/views/modules/fuwudingdan/list'
    import shipuxinxi from '@/views/modules/shipuxinxi/list'
    import jiankangjiance from '@/views/modules/jiankangjiance/list'
    import fuwupingjia from '@/views/modules/fuwupingjia/list'
    import fuwuleixing from '@/views/modules/fuwuleixing/list'
    import jinjiqiuzhu from '@/views/modules/jinjiqiuzhu/list'
    import jiankangbaogao from '@/views/modules/jiankangbaogao/list'
    import forum from '@/views/modules/forum/list'
    import systemintro from '@/views/modules/systemintro/list'
    import laoren from '@/views/modules/laoren/list'
    import fuwurenyuan from '@/views/modules/fuwurenyuan/list'
    import jiuzhuxiangying from '@/views/modules/jiuzhuxiangying/list'
    import jiedanfuwu from '@/views/modules/jiedanfuwu/list'
    import config from '@/views/modules/config/list'
    import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
    path: '/',
    name: '系统首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '系统首页',
      component: Home,
      meta: {icon:'', title:'center', affix: true}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/news',
        name: '健康资讯',
        component: news
      }
      ,{
	path: '/xinxijiaoliu',
        name: '信息交流',
        component: xinxijiaoliu
      }
      ,{
	path: '/manxingbing',
        name: '慢性病',
        component: manxingbing
      }
      ,{
	path: '/huifuxinxi',
        name: '回复信息',
        component: huifuxinxi
      }
      ,{
	path: '/fuwudingdan',
        name: '服务订单',
        component: fuwudingdan
      }
      ,{
	path: '/shipuxinxi',
        name: '食谱信息',
        component: shipuxinxi
      }
      ,{
	path: '/jiankangjiance',
        name: '健康监测',
        component: jiankangjiance
      }
      ,{
	path: '/fuwupingjia',
        name: '服务评价',
        component: fuwupingjia
      }
      ,{
	path: '/fuwuleixing',
        name: '服务类型',
        component: fuwuleixing
      }
      ,{
	path: '/jinjiqiuzhu',
        name: '紧急求助',
        component: jinjiqiuzhu
      }
      ,{
	path: '/jiankangbaogao',
        name: '健康报告',
        component: jiankangbaogao
      }
      ,{
	path: '/forum',
        name: '社区互动',
        component: forum
      }
      ,{
	path: '/systemintro',
        name: '系统简介',
        component: systemintro
      }
      ,{
	path: '/laoren',
        name: '老人',
        component: laoren
      }
      ,{
	path: '/fuwurenyuan',
        name: '服务人员',
        component: fuwurenyuan
      }
      ,{
	path: '/jiuzhuxiangying',
        name: '救助响应',
        component: jiuzhuxiangying
      }
      ,{
	path: '/jiedanfuwu',
        name: '接单服务',
        component: jiedanfuwu
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
      ,{
	path: '/newstype',
        name: '健康资讯分类',
        component: newstype
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/board',
    name: 'board',
    component: Board,
    meta: {icon:'', title:'board'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
export default router;
