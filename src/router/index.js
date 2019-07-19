import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/pages/index'
import Trip from '@/pages/trip'
import Rob from '@/pages/rob'
import Mine from '@/pages/mine'
import Login from '@/pages/login'
import Reg from '@/pages/reg'

// “主页”子页面
import Search_alike from '@/pages/search_alike'//查询，市内
import Search_alien from '@/pages/search_alien'//查询，长途
import Feedback from '@/pages/feedback'//查询，长途

// “我的”子页面
import PerInfo from '@/pages/phone_mine/perInfo'
import Book from '@/pages/phone_mine/book'
import Bookman from '@/pages/phone_mine/bookman'
import Link from '@/pages/phone_mine/link'
import AddInfo from '@/pages/phone_mine/addInfo'
import BookInfo from '@/pages/phone_mine/bookInfo'

//测试
import Test from '@/pages/test';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/trip',
      name: 'trip',
      component: Trip
    },
    {
      path: '/rob',
      name: 'rob',
      component: Rob
    },
    {
      path: '/mine',
      name: 'mine',
      component: Mine
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/reg',
      name: 'reg',
      component: Reg
    },
    {//查询，市内
      path: '/search_alike',
      name: 'search_alike',
      component: Search_alike
    },
    {//查询，长途
      path: '/search_alien',
      name: 'search_alien',
      component: Search_alien
    },
    {//feedback
      path: '/feedback',
      name: 'feedback',
      component: Feedback
    },
    {//手机端“我的”子页面
      path: '/perInfo',
      name: 'perInfo',
      component: PerInfo
    },
    {//手机端“我的”子页面
      path: '/book',
      name: 'book',
      component: Book
    },
    {//手机端“我的”子页面
      path: '/bookman',
      name: 'bookman',
      component: Bookman
    },
    {//手机端“我的”子页面
      path: '/link',
      name: 'link',
      component: Link
    },
    {//手机端“我的”子页面
      path: '/addInfo',
      name: 'addInfo',
      component: AddInfo
    },
    {//手机端“我的”子页面
      path: '/bookInfo',
      name: 'bookInfo',
      component: BookInfo
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    }
  ]
})
