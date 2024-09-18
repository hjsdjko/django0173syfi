<template>
	<div>

	<div class="container" :style='{"minHeight":"100vh","alignItems":"center","background":"url(http://codegen.caihongy.cn/20240111/52850f190df14e968d04c5b7fe9d35f2.jpg)","display":"flex","width":"100%","backgroundSize":"cover","backgroundPosition":"center center","backgroundRepeat":"no-repeat","justifyContent":"center"}'>
		<el-form class='rgs-form' v-if="pageFlag=='register'" :style='{"border":"1px solid #eee","padding":"30px 3% 30px","boxShadow":"0px 26px 26px -30px #999","margin":"0px auto","borderRadius":"20px","textAlign":"center","background":"rgba(255,255,255,.3)","width":"50vw","position":"relative","height":"auto"}' ref="registerForm" :model="registerForm" :rules="rules">
			<div v-if="false" :style='{"width":"100%","margin":"0 0 10px 0","lineHeight":"44px","fontSize":"20px","color":"rgba(64, 158, 255, 1)","textAlign":"center"}'>USER / REGISTER</div>
			<div v-if="true" :style='{"margin":"0px auto 10px","-webkit-text-stroke":"6px transparent","color":"#fff","textAlign":"center","background":"linear-gradient(178deg, rgba(0,0,0,1) 0%, rgba(163,86,80,0) 55%, rgba(0,0,0,1) 55%, rgba(186,86,79,0) 100%)","-webkitTextFillColor":"#ffffff","width":"100%","letterSpacing":"6px","lineHeight":"44px","fontSize":"26px","-webkitBackgroundClip":"text"}'>基于大数据技术的智慧居家养老服务平台注册</p></div>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="laorenzhanghao">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('laorenzhanghao')?'required':''">老人账号：</div>
				<el-input v-model="registerForm.laorenzhanghao"  placeholder="请输入老人账号" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="mima">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('mima')?'required':''">密码：</div>
				<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="mima2">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('mima')?'required':''">确认密码：</div>
				<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="laorenxingming">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('laorenxingming')?'required':''">老人姓名：</div>
				<el-input v-model="registerForm.laorenxingming"  placeholder="请输入老人姓名" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="xingbie">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('xingbie')?'required':''">性别：</div>
                <el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
                  <el-option
                      v-for="(item,index) in laorenxingbieOptions"
                      :key="index"
                      :label="item"
                      :value="item">
                  </el-option>
                </el-select>
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="nianling">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('nianling')?'required':''">年龄：</div>
				<el-input v-model.number="registerForm.nianling"  placeholder="请输入年龄" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="shoujihaoma">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('shoujihaoma')?'required':''">手机号码：</div>
				<el-input v-model="registerForm.shoujihaoma"  placeholder="请输入手机号码" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="manxingbing">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('manxingbing')?'required':''">慢性病：</div>
                <el-select v-model="registerForm.manxingbingArray" placeholder="请选择慢性病" @change="laorenmanxingbingMulChange" multiple >
                  <el-option
                      v-for="(item,index) in laorenmanxingbingOptions"
                      :key="index"
                      :label="item"
                      :value="item">
                  </el-option>
                </el-select>
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='laoren'" prop="touxiang">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('touxiang')?'required':''">头像：</div>
                <file-upload
					tip="点击上传头像"
					action="file/upload"
					:limit="1"
					:multiple="true"
					:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
					@change="laorentouxiangUploadChange"
				></file-upload>
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="renyuanbianhao">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('renyuanbianhao')?'required':''">人员编号：</div>
				<el-input v-model="registerForm.renyuanbianhao"  placeholder="请输入人员编号" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="mima">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('mima')?'required':''">密码：</div>
				<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="mima2">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('mima')?'required':''">确认密码：</div>
				<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="renyuanxingming">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('renyuanxingming')?'required':''">人员姓名：</div>
				<el-input v-model="registerForm.renyuanxingming"  placeholder="请输入人员姓名" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="xingbie">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('xingbie')?'required':''">性别：</div>
                <el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
                  <el-option
                      v-for="(item,index) in fuwurenyuanxingbieOptions"
                      :key="index"
                      :label="item"
                      :value="item">
                  </el-option>
                </el-select>
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="nianling">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('nianling')?'required':''">年龄：</div>
				<el-input v-model.number="registerForm.nianling"  placeholder="请输入年龄" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="lianxidianhua">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('lianxidianhua')?'required':''">联系电话：</div>
				<el-input v-model="registerForm.lianxidianhua"  placeholder="请输入联系电话" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="fuwuleixing">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('fuwuleixing')?'required':''">服务类型：</div>
                <el-select v-model="registerForm.fuwuleixing" placeholder="请选择服务类型" >
                  <el-option
                      v-for="(item,index) in fuwurenyuanfuwuleixingOptions"
                      :key="index"
                      :label="item"
                      :value="item">
                  </el-option>
                </el-select>
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="fuwufei">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('fuwufei')?'required':''">服务费：</div>
				<el-input v-model.number="registerForm.fuwufei"  placeholder="请输入服务费" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="jifeibiaozhun">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('jifeibiaozhun')?'required':''">计费标准：</div>
				<el-input v-model="registerForm.jifeibiaozhun"  placeholder="请输入计费标准" />
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="zhaopian">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('zhaopian')?'required':''">照片：</div>
                <file-upload
					tip="点击上传照片"
					action="file/upload"
					:limit="1"
					:multiple="true"
					:fileUrls="registerForm.zhaopian?registerForm.zhaopian:''"
					@change="fuwurenyuanzhaopianUploadChange"
				></file-upload>
			</el-form-item>
			<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","textAlign":"left","height":"auto"}' v-if="tableName=='fuwurenyuan'" prop="fuwujianjie">
				<div v-if="true" :style='{"padding":"0 10px","color":"#000","textAlign":"right","background":"none","display":"inline-block","width":"100px","lineHeight":"36px","fontSize":"14px"}' :class="changeRules('fuwujianjie')?'required':''">服务简介：</div>
			    <editor
			        :style='{"minHeight":"150px","border":"0px solid #1abc9e30","borderRadius":"0","color":"#666","background":"#fff","width":"auto","clear":"both","minWidth":"300px","height":"auto"}'
			        v-model="registerForm.fuwujianjie" 
			        class="editor" 
			        action="file/upload">
			    </editor>
			</el-form-item>
			<el-button :style='{"border":"0","cursor":"pointer","padding":"0 24px","margin":"20px 10px 20px 0","color":"#fff","borderRadius":"4px","background":"linear-gradient(to right,#f67536,#f64d36),#f64d36","display":"inline-block","width":"140px","letterSpacing":"4px","fontSize":"16px","height":"36px"}' type="primary" @click="submitForm('registerForm')">注册</el-button>
			<el-button :style='{"border":"0","cursor":"pointer","padding":"0 24px","margin":"0","color":"#666","borderRadius":"4px","textAlign":"center","background":"#fff","display":"inline-block","width":"140px","fontSize":"16px","height":"36px"}' @click="resetForm('registerForm')">重置</el-button>
			<router-link :style='{"cursor":"pointer","padding":"6px 8px","margin":"40px 0 0 0","color":"#666","textAlign":"right","display":"inline-block","textDecoration":"none","float":"right","borderRadius":"4px","background":"#fff","width":"auto","lineHeight":"20px","fontSize":"14px"}' to="/login">已有账户登录</router-link>
			<div class="idea1" :style='{"width":"100%","background":"red","display":"none","height":"40px"}'></div>
			<div class="idea2" :style='{"width":"100%","background":"blue","display":"none","height":"40px"}'></div>
		</el-form>
    </div>
  </div>
</div>
</template>

<script>

export default {
    //数据集合
    data() {
		return {
            pageFlag : '',
			tableName: '',
			registerForm: {},
			forgetForm: {},
			rules: {},
			requiredRules: {},
            laorenxingbieOptions: [],
            laorenmanxingbingOptions: [],
            fuwurenyuanxingbieOptions: [],
            fuwurenyuanfuwuleixingOptions: [],
		}
    },
	mounted() {
		if(this.$route.query.pageFlag=='register'){
			this.tableName = this.$route.query.role;
			if(this.tableName=='laoren'){
				this.registerForm = {
					laorenzhanghao: '',
					mima: '',
					mima2: '',
					laorenxingming: '',
					xingbie: '',
					nianling: '',
					shoujihaoma: '',
					manxingbing: '',
					touxiang: '',
				}
			}
			if(this.tableName=='fuwurenyuan'){
				this.registerForm = {
					renyuanbianhao: '',
					mima: '',
					mima2: '',
					renyuanxingming: '',
					xingbie: '',
					nianling: '',
					lianxidianhua: '',
					fuwuleixing: '',
					fuwufei: '',
					jifeibiaozhun: '',
					zhaopian: '',
					fuwujianjie: '',
					sfsh: '',
					shhf: '',
					clicktime: '',
					clicknum: '',
					storeupnum: '',
				}
			}
			if ('laoren' == this.tableName) {
				this.requiredRules.laorenzhanghao = [{ required: true, message: '请输入老人账号', trigger: 'blur' }]
			}
			if ('laoren' == this.tableName) {
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('laoren' == this.tableName) {
				this.requiredRules.laorenxingming = [{ required: true, message: '请输入老人姓名', trigger: 'blur' }]
			}
			if ('fuwurenyuan' == this.tableName) {
				this.requiredRules.renyuanbianhao = [{ required: true, message: '请输入人员编号', trigger: 'blur' }]
			}
			if ('fuwurenyuan' == this.tableName) {
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('fuwurenyuan' == this.tableName) {
				this.requiredRules.renyuanxingming = [{ required: true, message: '请输入人员姓名', trigger: 'blur' }]
			}
			if ('fuwurenyuan' == this.tableName) {
				this.requiredRules.fuwuleixing = [{ required: true, message: '请输入服务类型', trigger: 'blur' }]
			}
		}
	},
    created() {
		this.pageFlag = this.$route.query.pageFlag;
		if(this.$route.query.pageFlag=='register'){
		  if ('laoren' == this.tableName) {
			this.rules.laorenzhanghao = [{ required: true, message: '请输入老人账号', trigger: 'blur' }];
		  }
		  if ('laoren' == this.tableName) {
			this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
		  }
		  if ('laoren' == this.tableName) {
			this.rules.laorenxingming = [{ required: true, message: '请输入老人姓名', trigger: 'blur' }];
		  }
			this.laorenxingbieOptions = "男,女".split(',');
		  if ('laoren' == this.tableName) {
			this.rules.nianling = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
		  }
		  if ('laoren' == this.tableName) {
			this.rules.shoujihaoma = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
		  }
			this.$http({
			  url: `option/manxingbing/manxingbing`,
			  method: "get",
			  params: {}
			}).then(({ data }) => {
			  if (data && data.code === 0) {
				  this.laorenmanxingbingOptions = data.data;
			  }
			});
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.renyuanbianhao = [{ required: true, message: '请输入人员编号', trigger: 'blur' }];
		  }
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
		  }
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.renyuanxingming = [{ required: true, message: '请输入人员姓名', trigger: 'blur' }];
		  }
			this.fuwurenyuanxingbieOptions = "男,女".split(',');
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.nianling = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
		  }
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.lianxidianhua = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
		  }
			this.$http({
			  url: `option/fuwuleixing/fuwuleixing`,
			  method: "get",
			  params: {}
			}).then(({ data }) => {
			  if (data && data.code === 0) {
				  this.fuwurenyuanfuwuleixingOptions = data.data;
			  }
			});
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.fuwuleixing = [{ required: true, message: '请输入服务类型', trigger: 'blur' }];
		  }
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.fuwufei = [{ required: true, validator: this.$validate.isNumber, trigger: 'blur' }];
		  }
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.clicknum = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
		  }
		  if ('fuwurenyuan' == this.tableName) {
			this.rules.storeupnum = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
		  }
		}
    },
    //方法集合
    methods: {
		changeRules(name){
			if(this.requiredRules[name]){
				return true
			}
			return false
		},
      // 获取uuid
      getUUID () {
        return new Date().getTime();
      },
        // 下二随
      laorentouxiangUploadChange(fileUrls) {
          this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
      },
      fuwurenyuanzhaopianUploadChange(fileUrls) {
          this.registerForm.zhaopian = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
      },

        // 多级联动参数
        laorenmanxingbingMulChange(e){
            this.registerForm.manxingbing = this.registerForm.manxingbingArray.join(',')
            this.$forceUpdate()
        },


      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            var url=this.tableName+"/register";
				if((!this.registerForm.laorenzhanghao) && `laoren` == this.tableName){
					this.$message.error(`老人账号不能为空`);
					return
				}
               if(`laoren` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
                this.$message.error(`两次密码输入不一致`);
                return
               }
				if((!this.registerForm.mima) && `laoren` == this.tableName){
					this.$message.error(`密码不能为空`);
					return
				}
				if((!this.registerForm.laorenxingming) && `laoren` == this.tableName){
					this.$message.error(`老人姓名不能为空`);
					return
				}
				if(`laoren` == this.tableName && this.registerForm.nianling &&(!this.$validate.isIntNumer2(this.registerForm.nianling))){
					this.$message.error(`年龄应输入整数`);
					return
				}
					if(`laoren` == this.tableName && this.registerForm.shoujihaoma &&(!this.$validate.isMobile2(this.registerForm.shoujihaoma))){
						this.$message.error(`手机号码应输入手机格式`);
						return
					}
			  if(this.tableName=='fuwurenyuan'){
				  this.registerForm.sfsh = '待审核'
			  }
				if((!this.registerForm.renyuanbianhao) && `fuwurenyuan` == this.tableName){
					this.$message.error(`人员编号不能为空`);
					return
				}
               if(`fuwurenyuan` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
                this.$message.error(`两次密码输入不一致`);
                return
               }
				if((!this.registerForm.mima) && `fuwurenyuan` == this.tableName){
					this.$message.error(`密码不能为空`);
					return
				}
				if((!this.registerForm.renyuanxingming) && `fuwurenyuan` == this.tableName){
					this.$message.error(`人员姓名不能为空`);
					return
				}
				if(`fuwurenyuan` == this.tableName && this.registerForm.nianling &&(!this.$validate.isIntNumer2(this.registerForm.nianling))){
					this.$message.error(`年龄应输入整数`);
					return
				}
					if(`fuwurenyuan` == this.tableName && this.registerForm.lianxidianhua &&(!this.$validate.isMobile2(this.registerForm.lianxidianhua))){
						this.$message.error(`联系电话应输入手机格式`);
						return
					}
				if((!this.registerForm.fuwuleixing) && `fuwurenyuan` == this.tableName){
					this.$message.error(`服务类型不能为空`);
					return
				}
				if(`fuwurenyuan` == this.tableName && this.registerForm.fuwufei &&(!this.$validate.isNumber2(this.registerForm.fuwufei))){
					this.$message.error(`服务费应输入数字`);
					return
				}
            this.$http.post(url, this.registerForm).then(res => {
              if (res.data.code === 0) {
                this.$message({
                  message: '注册成功',
                  type: 'success',
                  duration: 1500,
                  onClose: () => {
                    this.$router.push('/login');
                  }
                });
              } else {
                this.$message.error(res.data.msg);
              }
            });
          } else {
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
		position: relative;
		background: url(http://codegen.caihongy.cn/20240111/52850f190df14e968d04c5b7fe9d35f2.jpg);
		
		.el-input {
		  width: auto;
		}
		
		.el-date-editor.el-input {
			width: auto;
		}
		
		.el-form-item /deep/ .el-form-item__content {
						display: flex;
						flex-wrap: wrap;
					}
		
		.rgs-form .el-input /deep/ .el-input__inner {
						border-radius: 20px;
						padding: 0 10px;
						color: #666;
						background: #fff;
						width: 100%;
						font-size: 14px;
						border-color: #be9a1b;
						border-width: 0 0 0px;
						border-style: solid;
						min-width: 400px;
						height: 40px;
					}
		
		.rgs-form .el-select /deep/ .el-input__inner {
						border-radius: 20px;
						padding: 0 10px;
						color: #666;
						background: #fff;
						width: auto;
						font-size: 14px;
						border-color: #be9a1b;
						border-width: 0 0 0px;
						border-style: solid;
						min-width: 400px;
						height: 40px;
					}
		
		.rgs-form .el-date-editor /deep/ .el-input__inner {
						border-radius: 20px;
						padding: 0 10px 0 30px;
						color: #666;
						background: #fff;
						width: auto;
						font-size: 14px;
						border-color: #be9a1b;
						border-width: 0 0 0px;
						border-style: solid;
						min-width: 400px;
						height: 40px;
					}
		
		.rgs-form .el-date-editor /deep/ .el-input__inner {
						border-radius: 20px;
						padding: 0 10px 0 30px;
						color: #666;
						background: #fff;
						width: auto;
						font-size: 14px;
						border-color: #be9a1b;
						border-width: 0 0 0px;
						border-style: solid;
						min-width: 400px;
						height: 40px;
					}
		
		.rgs-form /deep/ .el-upload--picture-card {
			background: transparent;
			border: 0;
			border-radius: 0;
			width: auto;
			height: auto;
			line-height: initial;
			vertical-align: middle;
		}
		
		.rgs-form /deep/ .upload .upload-img {
		  		  cursor: pointer;
		  		  border-radius: 8px;
		  		  color: #999;
		  		  background: #fff;
		  		  width: 80px;
		  		  font-size: 24px;
		  		  border-color: #be9a1b60;
		  		  border-width: 0px;
		  		  line-height: 80px;
		  		  border-style: solid;
		  		  text-align: center;
		  		  height: 80px;
		  		}
		
		.rgs-form /deep/ .el-upload-list .el-upload-list__item {
		  		  cursor: pointer;
		  		  border-radius: 8px;
		  		  color: #999;
		  		  background: #fff;
		  		  width: 80px;
		  		  font-size: 24px;
		  		  border-color: #be9a1b60;
		  		  border-width: 0px;
		  		  line-height: 80px;
		  		  border-style: solid;
		  		  text-align: center;
		  		  height: 80px;
		  		}
		
		.rgs-form /deep/ .el-upload .el-icon-plus {
		  		  cursor: pointer;
		  		  border-radius: 8px;
		  		  color: #999;
		  		  background: #fff;
		  		  width: 80px;
		  		  font-size: 24px;
		  		  border-color: #be9a1b60;
		  		  border-width: 0px;
		  		  line-height: 80px;
		  		  border-style: solid;
		  		  text-align: center;
		  		  height: 80px;
		  		}
	}
	.required {
		position: relative;
	}
	.required::after{
				color: red;
				left: 88px;
				position: absolute;
				content: "*";
				order: 2;
			}
</style>
