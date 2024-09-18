<template>
<div class="center-preview" :style='{"padding":"0 18%","margin":"20px auto 40px","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","position":"relative","justifyContent":"space-between"}'>
	<div class="title" :style='{"padding":"0","margin":"20px auto 20px","borderColor":"#ffc652","color":"#222","textAlign":"center","background":"none","borderWidth":"0px 0 0 ","width":"100%","fontSize":"26px","borderStyle":"solid","fontWeight":"600","height":"60px"}'>{{ title }}</div>
	
	<div class="info" :style='{"padding":"0px 0 0 20px","boxShadow":"0 0px 0px rgba(0, 0, 0, 0.3)","margin":"20px 0 0 0","borderColor":"#28890b20","alignItems":"center","display":"flex","justifyContent":"center","borderRadius":"0px","flexWrap":"wrap","background":"#fff","borderWidth":"0px","width":"100%","position":"relative","borderStyle":"solid","height":"auto","order":"1"}'>
		<div :style='{"padding":"0px 20px","borderColor":"#f9eacc","margin":"0 20px 0 0","color":"#fff","textAlign":"center","letterSpacing":"0px","top":"0","borderRadius":"0px","left":"0","borderWidth":"0px","background":"linear-gradient(to right,#f67536,#f64d36),#f64d36","width":"200px","lineHeight":"44px","fontSize":"16px","position":"absolute","borderStyle":"solid","fontWeight":"600","height":"auto"}'>个人信息</div>
		<div :style='{"padding":"20px 0","borderColor":"#f8524630","top":"46px","left":"0","borderWidth":"1px 1px","width":"200px","fontSize":0,"position":"absolute","borderStyle":"solid","height":"auto"}' v-if="userTableName=='laoren'">
			<el-image :style='{"boxShadow":"1px 2px 4px #ddd","margin":"0 auto","borderColor":"#fcfcfc","objectFit":"cover","borderRadius":"100%","borderWidth":"4px","display":"block","width":"100px","borderStyle":"solid","height":"100px"}' :src="sessionForm.touxiang?baseUrl + sessionForm.touxiang:require('@/assets/avator.png')" fit="cover"></el-image>
		</div>
		<div :style='{"padding":"20px 0","borderColor":"#f8524630","top":"46px","left":"0","borderWidth":"1px 1px","width":"200px","fontSize":0,"position":"absolute","borderStyle":"solid","height":"auto"}' v-if="userTableName=='fuwurenyuan'">
			<el-image :style='{"boxShadow":"1px 2px 4px #ddd","margin":"0 auto","borderColor":"#fcfcfc","objectFit":"cover","borderRadius":"100%","borderWidth":"4px","display":"block","width":"100px","borderStyle":"solid","height":"100px"}' :src="sessionForm.zhaopian?baseUrl + sessionForm.zhaopian:require('@/assets/avator.png')" fit="cover"></el-image>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='laoren'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"margin":"0 10px 0 0","fontSize":"14px","color":"#333","display":"inline-block"}'>老人账号</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.laorenzhanghao}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='laoren'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>老人姓名</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.laorenxingming}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='laoren'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>性别</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.xingbie}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='laoren'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>年龄</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.nianling}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='laoren'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>手机号码</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.shoujihaoma}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='laoren'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>慢性病</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.manxingbing}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='fuwurenyuan'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"margin":"0 10px 0 0","fontSize":"14px","color":"#333","display":"inline-block"}'>人员编号</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.renyuanbianhao}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='fuwurenyuan'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>人员姓名</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.renyuanxingming}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='fuwurenyuan'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>性别</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.xingbie}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='fuwurenyuan'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>年龄</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.nianling}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='fuwurenyuan'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>联系电话</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.lianxidianhua}}</div>
		</div>
		<div :style='{"padding":"0 20px","borderColor":"#f9eacc","margin":"0 2% 20px 0","borderWidth":"0px","background":"none","display":"flex","width":"32%","lineHeight":"40px","borderStyle":"solid","height":"auto"}' v-if="userTableName=='fuwurenyuan'">
			<span class="icon iconfont icon-shouye-zhihui" :style='{"padding":"0 5px","fontSize":"14px","color":"#333","display":"none"}'></span>
			<div :style='{"color":"#333","margin":"0 10px 0 0","fontSize":"14px"}'>服务类型</div>
			<div :style='{"color":"#999","textAlign":"left","fontSize":"14px"}'>{{sessionForm.fuwuleixing}}</div>
		</div>
		
	</div>
	
    <el-tabs tab-position="left" :style='{"width":"100%","margin":"20px 0 0","flexWrap":"wrap","background":"#fff","display":"flex","order":"1"}' @tab-click="handleClick">
      <el-tab-pane label="个人中心">
        <el-form class="center-preview-pv" ref="sessionForm" :model="sessionForm" :rules="rules" label-width="100px">
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='laoren'" label="老人账号" prop="laorenzhanghao">
            <el-input v-model="sessionForm.laorenzhanghao" placeholder="老人账号" readonly></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='laoren'" label="老人姓名" prop="laorenxingming">
            <el-input v-model="sessionForm.laorenxingming" placeholder="老人姓名" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='laoren'" label="性别" prop="xingbie">
            <el-select v-model="sessionForm.xingbie" placeholder="请选择性别" >
              <el-option v-for="(item, index) in dynamicProp.xingbie" :key="index" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='laoren'" label="年龄" prop="nianling">
            <el-input v-model="sessionForm.nianling" placeholder="年龄" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='laoren'" label="手机号码" prop="shoujihaoma">
            <el-input v-model="sessionForm.shoujihaoma" placeholder="手机号码" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='laoren'" label="慢性病" prop="manxingbing">
            <el-select v-model="sessionForm.manxingbingArray" placeholder="请选择慢性病" multiple @change="laorenmanxingbingMulChange" >
              <el-option v-for="(item, index) in dynamicProp.manxingbing" :key="index" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='laoren'" label="头像" prop="touxiang">
			<file-upload
			tip="点击上传头像"
			action="file/upload"
			:limit="1"
			:multiple="true"
			:fileUrls="sessionForm.touxiang?sessionForm.touxiang:''"
			@change="laorentouxiangHandleAvatarSuccess"
			></file-upload>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="人员编号" prop="renyuanbianhao">
            <el-input v-model="sessionForm.renyuanbianhao" placeholder="人员编号" readonly></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="人员姓名" prop="renyuanxingming">
            <el-input v-model="sessionForm.renyuanxingming" placeholder="人员姓名" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="性别" prop="xingbie">
            <el-select v-model="sessionForm.xingbie" placeholder="请选择性别" >
              <el-option v-for="(item, index) in dynamicProp.xingbie" :key="index" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="年龄" prop="nianling">
            <el-input v-model="sessionForm.nianling" placeholder="年龄" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="联系电话" prop="lianxidianhua">
            <el-input v-model="sessionForm.lianxidianhua" placeholder="联系电话" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="服务类型" prop="fuwuleixing">
            <el-select v-model="sessionForm.fuwuleixing" placeholder="请选择服务类型" >
              <el-option v-for="(item, index) in dynamicProp.fuwuleixing" :key="index" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="服务费" prop="fuwufei">
            <el-input v-model="sessionForm.fuwufei" placeholder="服务费" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="计费标准" prop="jifeibiaozhun">
            <el-input v-model="sessionForm.jifeibiaozhun" placeholder="计费标准" ></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="照片" prop="zhaopian">
			<file-upload
			tip="点击上传照片"
			action="file/upload"
			:limit="1"
			:multiple="true"
			:fileUrls="sessionForm.zhaopian?sessionForm.zhaopian:''"
			@change="fuwurenyuanzhaopianHandleAvatarSuccess"
			></file-upload>
          </el-form-item>
		  <el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' v-if="userTableName=='fuwurenyuan'" label="服务简介">
		    <editor
		        :style='{"minHeight":"250px","border":"0px solid #1abc9e30","outline":"none","color":"#333","borderRadius":"4px","width":"100%","lineHeight":"32px","fontSize":"14px"}'
		        v-model="sessionForm.fuwujianjie" 
		        class="editor" 
		        action="file/upload">
		    </editor>
		  </el-form-item>
          <el-form-item :style='{"padding":"0","margin":"0"}'>
            <el-button :style='{"border":"0px solid #eccc19","cursor":"pointer","padding":"0","margin":"0 20px 0 0","outline":"none","color":"#fff","borderRadius":"20px","background":"linear-gradient(to right,#f67536,#f64d36),#f64d36","width":"110px","lineHeight":"40px","fontSize":"14px","height":"40px"}' type="primary" @click="onSubmit('sessionForm')">更新信息</el-button>
            <el-button :style='{"border":"1px solid #ccc","cursor":"pointer","padding":"0","margin":"0","outline":"none","color":"#666","borderRadius":"20px","background":"none","width":"110px","lineHeight":"40px","fontSize":"14px","height":"40px"}' type="danger" @click="logout">退出登录</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
	  <el-tab-pane label="修改密码">
		<el-form class="center-preview-pv" ref="passwordForm" :model="passwordForm" :rules="passwordRules" label-width="100px">
			<el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' label="原密码" prop="password">
			  <el-input type="password" v-model="passwordForm.password" placeholder="原密码"></el-input>
			</el-form-item>
			<el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' label="新密码" prop="newpassword">
			  <el-input type="password" v-model="passwordForm.newpassword" placeholder="新密码"></el-input>
			</el-form-item>
			<el-form-item :style='{"width":"auto","padding":"0px","margin":"0 0 40px","background":"#fff","display":"inline-block"}' label="确认密码" prop="repassword">
			  <el-input type="password" v-model="passwordForm.repassword" placeholder="确认密码"></el-input>
			</el-form-item>
			<el-form-item :style='{"padding":"0","margin":"0"}'>
			  <el-button :style='{"border":"0px solid #eccc19","cursor":"pointer","padding":"0","margin":"0 20px 0 0","outline":"none","color":"#fff","borderRadius":"20px","background":"linear-gradient(to right,#f67536,#f64d36),#f64d36","width":"110px","lineHeight":"40px","fontSize":"14px","height":"40px"}' type="primary" @click="updatePassword">修改密码</el-button>
			</el-form-item>
		</el-form>
	  </el-tab-pane>
		<el-tab-pane v-for="(item,index) in menuList" :key="index" v-if="hasBack(item.menu)" :label="item.child[0].menu" :name="item.child[0].tableName"></el-tab-pane>
      <el-tab-pane label="我的发布"></el-tab-pane>
      <el-tab-pane label="我的收藏"></el-tab-pane>
    </el-tabs>

</div>
</template>

<script>
  import config from '@/config/config'
  import menu from '@/config/menu'
  import Vue from 'vue'
  export default {
    //数据集合
    data() {
      return {
        title: '个人中心',
        baseUrl: config.baseUrl,
        sessionForm: {},
		passwordForm: {},
		passwordRules: {
			password: [
				{
					required: true,
					message: "密码不能为空",
					trigger: "blur"
				}
			],
			newpassword: [
				{
					required: true,
					message: "新密码不能为空",
					trigger: "blur"
				}
			],
			repassword: [
				{
					required: true,
					message: "确认密码不能为空",
					trigger: "blur"
				}
			]
		},
        rules: {},
		menuList: [],
        disabled: false,
        uploadUrl: config.baseUrl + 'file/upload',
        imageUrl: '',
        headers: {Token: localStorage.getItem('frontToken')},
        userTableName: localStorage.getItem('UserTableName'),
        dynamicProp: {},
      }
    },
    created() {
		let menus = menu.list()
		for(let x in menus){
			if(menus[x].tableName == this.userTableName){
				this.menuList = menus[x].backMenu
			}
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.sessionForm, 'laorenzhanghao', null);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.sessionForm, 'mima', null);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.sessionForm, 'laorenxingming', null);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.sessionForm, 'xingbie', null);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.sessionForm, 'nianling', null);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.sessionForm, 'shoujihaoma', null);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.sessionForm, 'manxingbing', null);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.sessionForm, 'touxiang', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'renyuanbianhao', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'mima', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'renyuanxingming', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'xingbie', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'nianling', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'lianxidianhua', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'fuwuleixing', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'fuwufei', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'jifeibiaozhun', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'zhaopian', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'fuwujianjie', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'sfsh', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'shhf', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'clicktime', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'clicknum', null);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.sessionForm, 'storeupnum', null);
		}

		if ('laoren' == this.userTableName&&this.rules['laorenzhanghao']){
			this.rules['laorenzhanghao'].push({ required: true, message: '请输入老人账号', trigger: 'blur' })
		}else if('laoren' == this.userTableName&&!this.rules['laorenzhanghao']) {
			this.$set(this.rules, 'laorenzhanghao', [{ required: true, message: '请输入老人账号', trigger: 'blur' }]);
		}
		if ('laoren' == this.userTableName&&this.rules['mima']){
			this.rules['mima'].push({ required: true, message: '请输入密码', trigger: 'blur' })
		}else if('laoren' == this.userTableName&&!this.rules['mima']) {
			this.$set(this.rules, 'mima', [{ required: true, message: '请输入密码', trigger: 'blur' }]);
		}
		if ('laoren' == this.userTableName&&this.rules['laorenxingming']){
			this.rules['laorenxingming'].push({ required: true, message: '请输入老人姓名', trigger: 'blur' })
		}else if('laoren' == this.userTableName&&!this.rules['laorenxingming']) {
			this.$set(this.rules, 'laorenxingming', [{ required: true, message: '请输入老人姓名', trigger: 'blur' }]);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.rules, 'nianling', [{ required: false, validator: this.$validate.isIntNumer, trigger: 'blur' }]);
		}
		if ('laoren' == this.userTableName) {
			this.$set(this.rules, 'shoujihaoma', [{ required: false, validator: this.$validate.isMobile, trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName&&this.rules['renyuanbianhao']){
			this.rules['renyuanbianhao'].push({ required: true, message: '请输入人员编号', trigger: 'blur' })
		}else if('fuwurenyuan' == this.userTableName&&!this.rules['renyuanbianhao']) {
			this.$set(this.rules, 'renyuanbianhao', [{ required: true, message: '请输入人员编号', trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName&&this.rules['mima']){
			this.rules['mima'].push({ required: true, message: '请输入密码', trigger: 'blur' })
		}else if('fuwurenyuan' == this.userTableName&&!this.rules['mima']) {
			this.$set(this.rules, 'mima', [{ required: true, message: '请输入密码', trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName&&this.rules['renyuanxingming']){
			this.rules['renyuanxingming'].push({ required: true, message: '请输入人员姓名', trigger: 'blur' })
		}else if('fuwurenyuan' == this.userTableName&&!this.rules['renyuanxingming']) {
			this.$set(this.rules, 'renyuanxingming', [{ required: true, message: '请输入人员姓名', trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.rules, 'nianling', [{ required: false, validator: this.$validate.isIntNumer, trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.rules, 'lianxidianhua', [{ required: false, validator: this.$validate.isMobile, trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName&&this.rules['fuwuleixing']){
			this.rules['fuwuleixing'].push({ required: true, message: '请输入服务类型', trigger: 'blur' })
		}else if('fuwurenyuan' == this.userTableName&&!this.rules['fuwuleixing']) {
			this.$set(this.rules, 'fuwuleixing', [{ required: true, message: '请输入服务类型', trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.rules, 'fuwufei', [{ required: false, validator: this.$validate.isNumber, trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.rules, 'clicknum', [{ required: false, validator: this.$validate.isIntNumer, trigger: 'blur' }]);
		}
		if ('fuwurenyuan' == this.userTableName) {
			this.$set(this.rules, 'storeupnum', [{ required: false, validator: this.$validate.isIntNumer, trigger: 'blur' }]);
		}

      this.init();
      this.sessionForm = JSON.parse(localStorage.getItem('sessionForm'))
    },
    //方法集合
    methods: {
      init() {
        if ('laoren' == this.userTableName) {
          this.dynamicProp.xingbie = '男,女'.split(',');
        }
        if ('laoren' == this.userTableName) {
          this.$http.get('option/manxingbing/manxingbing', {emulateJSON: true}).then(res => {
            if (res.data.code == 0) {
              this.dynamicProp.manxingbing = res.data.data;
			  this.$forceUpdate()
            }
          });
        }
        if ('fuwurenyuan' == this.userTableName) {
          this.dynamicProp.xingbie = '男,女'.split(',');
        }
        if ('fuwurenyuan' == this.userTableName) {
          this.$http.get('option/fuwuleixing/fuwuleixing', {emulateJSON: true}).then(res => {
            if (res.data.code == 0) {
              this.dynamicProp.fuwuleixing = res.data.data;
			  this.$forceUpdate()
            }
          });
        }
      },
	  setSession(){
		  localStorage.setItem('sessionForm',JSON.stringify(this.sessionForm))
	  },
        laorenmanxingbingMulChange(e){
            this.sessionForm.manxingbing = this.sessionForm.manxingbingArray.join(',')
        },
      onSubmit(formName) {
		if(`laoren` == this.userTableName && this.sessionForm.touxiang!=null){
			this.sessionForm.touxiang = this.sessionForm.touxiang.replace(new RegExp(this.$config.baseUrl,"g"),"");
		}
		if(`fuwurenyuan` == this.userTableName && this.sessionForm.zhaopian!=null){
			this.sessionForm.zhaopian = this.sessionForm.zhaopian.replace(new RegExp(this.$config.baseUrl,"g"),"");
		}
        this.$refs[formName].validate((valid) => {
			if (valid) {
				this.$http.post(this.userTableName + '/update', this.sessionForm).then(res => {
					if (res.data.code == 0) {
						this.setSession()
						this.$message({
							message: '更新成功',
							type: 'success',
							duration: 1500
						});
					}
				});
			} else {
				return false;
			}
        });
      },
      laorentouxiangHandleAvatarSuccess(fileUrls) {
        this.sessionForm.touxiang = fileUrls;
      },
      fuwurenyuanzhaopianHandleAvatarSuccess(fileUrls) {
        this.sessionForm.zhaopian = fileUrls;
      },
      handleClick(tab, event) {
        switch(event.target.outerText) {
          case '个人中心':
            tab.$router.push('/index/center');
            break;
          case '修改密码':
            this.passwordForm = {
				password: '',
				newpassword: '',
				repassword: '',
			}
			this.$forceUpdate()
            break;
          case '我的发布':
            tab.$router.push('/index/myForumList');
            break;
          case '我的收藏':
            localStorage.setItem('storeupType', 1);
            tab.$router.push('/index/storeup');
            break;
		  default:
		  	tab.$router.push(`/index/${tab.name}?centerType=1`);
        }

        this.title = event.target.outerText;
      },
	  async updatePassword(){
			this.$refs["passwordForm"].validate(async valid => {
				if (valid) {
					var password = "";
					if (this.sessionForm.mima) {
						password = this.sessionForm.mima;
					} else if (this.sessionForm.password) {
						password = this.sessionForm.password;
					}
					var nowpassword = ''
					await this.$http.get('encrypt/md5?text=' + this.passwordForm.password,).then(res=>{
						if(res.data&&res.data.code==0){
							nowpassword = res.data.data
						}
					})
					if(nowpassword!=password){
						this.$message.error("原密码错误");
						return;
					}
					if (this.passwordForm.newpassword != this.passwordForm.repassword) {
						this.$message.error("两次密码输入不一致");
						return;
					}
					if (this.userTableName == 'laoren') {
					}
					this.sessionForm.password = this.passwordForm.newpassword;
					this.sessionForm.mima = this.passwordForm.newpassword;
					this.$http.post(`${this.userTableName}/update`,this.sessionForm).then(({data})=>{
						if (data && data.code === 0) {
							this.$message({
								message: "修改密码成功,下次登录系统生效",
								type: "success",
								duration: 1500,
								onClose: () => {
								}
							});
							this.setSession()
						} else {
							this.$message.error(data.msg);
						}
					});
				}
			})
	  },
      logout() {
        localStorage.clear();
        Vue.http.headers.common['Token'] = "";
        this.$router.push('/index/home');
        this.activeIndex = '0'
        localStorage.setItem('keyPath', this.activeIndex)
        this.$forceUpdate()
        this.$message({
            message: '登出成功',
            type: 'success',
            duration: 1500,
        });
      },
	  hasBack(name){
		  switch(name){
			case '我的收藏管理':
				return false
				break;
			default:
				return true
		  }
	  }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .center-preview {
  
    .el-tabs {
      & /deep/ .el-tabs__header {
		.el-tabs__nav{
			overflow: auto;
		}
		::-webkit-scrollbar {
		  -webkit-appearance: none;
		  width: 6px;
		  height: 6px;
		}
		::-webkit-scrollbar-track {
		  background: rgba(0, 0, 0, 0.1);
		  border-radius: 0;
		}
		::-webkit-scrollbar-thumb {
		  cursor: pointer;
		  border-radius: 5px;
		  background: rgba(0, 0, 0, 0.15);
		  transition: color 0.2s ease;
		}
		::-webkit-scrollbar-thumb:hover {
		  background: rgba(0, 0, 0, 0.3);
		}
        .el-tabs__nav-wrap {
          margin: 0;
  
          &::after {
            content: none;
          }
        }
  
        .el-tabs__active-bar {
          display: none !important;
        }
      }
  
      .center-preview-pv {
        .el-date-editor.el-input {
          width: auto;
        }
  
        .balance {
          .el-input {
            width: auto;
          }
        }
      }
    }
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__header {
	padding: 0px;
	margin: 10px 20px 0 0;
	display: flex;
	border-color: #f8524630;
	float: left;
	flex-wrap: wrap;
	background: none;
	width: 200px;
	border-width: 1px;
	position: relative;
	border-style: solid;
	text-align: center;
	height: auto;
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__header .el-tabs__item {
  	padding: 0 10px;
  	color: #666;
  	background: #fff;
  	font-weight: 500;
  	width: 200px;
  	font-size: 14px;
  	line-height: auto;
  	transition: 400ms;
  	text-align: center;
  	height: auto;
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__header .el-tabs__item:hover {
  	padding: 0 10px;
  	color: #fff;
  	background: linear-gradient(to right,#f67536,#f64d36),#f64d36;
  	font-weight: 600;
  	font-size: 16px;
  	line-height: auto;
  	text-align: center;
  	height: auto;
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__header .el-tabs__item.is-active {
  	padding: 0 10px;
  	color: #fff;
  	background: linear-gradient(to right,#f67536,#f64d36),#f64d36;
  	font-weight: 600;
  	width: 100%;
  	font-size: 16px;
  	line-height: auto;
  	text-align: center;
  	height: auto;
  }
  
  .center-preview .el-tabs /deep/ .el-tabs__content {
  	padding: 30px 20px 40px;
  	margin: 10px 0 0;
  	background: #fff;
  	flex: 1;
  	width: calc(100% - 220px);
  	border-color: #eee;
  	border-width: 1px;
  	float: right;
  	border-style: solid;
  }
  .center-preview .el-tabs /deep/ .el-tabs__content .el-tab-pane {
  	width: 100%;
  }
  
  .center-preview-pv .el-form-item /deep/ .el-form-item__label {
  	padding: 0 10px 0 0;
  	color: #666;
  	font-weight: 500;
  	width: 100px;
  	font-size: 14px;
  	line-height: 40px;
  	text-align: right;
  }
  
  .center-preview-pv .el-form-item .el-form-item__content {
    margin-left: 100px;
  }
  
  .center-preview-pv .el-input /deep/ .el-input__inner {
  	border-radius: 0px;
  	padding: 0 12px;
  	box-shadow: 0 0 0px rgba(64, 158, 255, .5);
  	outline: none;
  	color: #666;
  	width: auto;
  	font-size: 14px;
  	border-color: #eee;
  	border-width: 1px;
  	border-style: solid;
  	min-width: 150px;
  	height: 40px;
  }
  
  .center-preview-pv .el-select /deep/ .el-input__inner {
  	border-radius: 0px;
  	padding: 0 12px;
  	box-shadow: 0 0 0px rgba(64, 158, 255, .5);
  	outline: none;
  	color: #666;
  	width: auto;
  	font-size: 14px;
  	border-color: #eee;
  	border-width: 1px;
  	border-style: solid;
  	min-width: 150px;
  	height: 40px;
  }
  
  .center-preview-pv .el-date-editor /deep/ .el-input__inner {
  	border-radius: 0px;
  	padding: 0 10px 0 30px;
  	box-shadow: 0 0 0px rgba(64, 158, 255, .5);
  	outline: none;
  	color: #666;
  	width: 200px;
  	font-size: 14px;
  	border-color: #eee;
  	border-width: 1px;
  	border-style: solid;
  	height: 40px;
  }
  
  .center-preview-pv /deep/ .avatar-uploader-icon {
  	cursor: pointer;
  	border-radius: 2px;
  	color: #999;
  	width: 130px;
  	font-size: 24px;
  	border-color: #eee;
  	border-width: 1px;
  	line-height: 50px;
  	border-style: solid;
  	text-align: center;
  	height: 50px;
  }
  
  .center-preview-pv .el-form-item.balance /deep/ .el-input__inner {
  	border-radius: 0px;
  	padding: 0 12px;
  	color: #666;
  	display: inline-block;
  	width: 200px;
  	font-size: 14px;
  	border-color: #eee;
  	border-width: 1px;
  	border-style: solid;
  	height: 36px;
  }
</style>
