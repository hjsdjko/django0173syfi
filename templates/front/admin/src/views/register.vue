<template>
	<div>
		<div class="container" :style='{"minHeight":"100vh","alignItems":"center","background":"url(http://codegen.caihongy.cn/20231230/12221b7460e0479da01d207672562c64.png)","display":"flex","width":"100%","backgroundSize":"100% 100%","backgroundPosition":"center center","backgroundRepeat":"no-repeat","justifyContent":"center"}'>
			<el-form v-if="pageFlag=='register'" :style='{"padding":"20px","boxShadow":"0 1px 6px rgbargb(66, 185, 131)","margin":"0","borderRadius":"10px","background":"#fff","width":"600px","height":"auto"}' ref="rgsForm" class="rgs-form" :model="rgsForm" :rules="rules">
				<div v-if="true" :style='{"width":"100%","margin":"0 0 10px 0","lineHeight":"44px","fontSize":"20px","color":"rgb(66, 185, 131)","textAlign":"center"}' class="title">基于大数据技术的智慧居家养老服务平台注册</div>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('laorenzhanghao')?'required':''">老人账号：</div>
					<el-input  v-model="ruleForm.laorenzhanghao"  autocomplete="off" placeholder="老人账号"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('mima')?'required':''">密码：</div>
					<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
					<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('laorenxingming')?'required':''">老人姓名：</div>
					<el-input  v-model="ruleForm.laorenxingming"  autocomplete="off" placeholder="老人姓名"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
                    <el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
                        <el-option
                            v-for="(item,index) in laorenxingbieOptions"
                            v-bind:key="index"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('nianling')?'required':''">年龄：</div>
					<el-input  v-model.number="ruleForm.nianling"  autocomplete="off" placeholder="年龄"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('shoujihaoma')?'required':''">手机号码：</div>
					<el-input  v-model="ruleForm.shoujihaoma"  autocomplete="off" placeholder="手机号码"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('manxingbing')?'required':''">慢性病：</div>
                    <el-select @change="laorenmanxingbingChange" v-model="ruleForm.manxingbingArray" multiple placeholder="请选择慢性病" >
                        <el-option
                            v-for="(item,index) in laorenmanxingbingOptions"
                            v-bind:key="index"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='laoren'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
                    <file-upload
                        tip="点击上传头像"
                        action="file/upload"
                        :limit="3"
                        :multiple="true"
                        :fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
                        @change="laorentouxiangUploadChange"
                    ></file-upload>
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('renyuanbianhao')?'required':''">人员编号：</div>
					<el-input  v-model="ruleForm.renyuanbianhao"  autocomplete="off" placeholder="人员编号"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('mima')?'required':''">密码：</div>
					<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
					<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('renyuanxingming')?'required':''">人员姓名：</div>
					<el-input  v-model="ruleForm.renyuanxingming"  autocomplete="off" placeholder="人员姓名"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
                    <el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
                        <el-option
                            v-for="(item,index) in fuwurenyuanxingbieOptions"
                            v-bind:key="index"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('nianling')?'required':''">年龄：</div>
					<el-input  v-model.number="ruleForm.nianling"  autocomplete="off" placeholder="年龄"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('lianxidianhua')?'required':''">联系电话：</div>
					<el-input  v-model="ruleForm.lianxidianhua"  autocomplete="off" placeholder="联系电话"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('fuwuleixing')?'required':''">服务类型：</div>
                    <el-select v-model="ruleForm.fuwuleixing" placeholder="请选择服务类型" >
                        <el-option
                            v-for="(item,index) in fuwurenyuanfuwuleixingOptions"
                            v-bind:key="index"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('fuwufei')?'required':''">服务费：</div>
					<el-input  v-model.number="ruleForm.fuwufei"  autocomplete="off" placeholder="服务费"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('jifeibiaozhun')?'required':''">计费标准：</div>
					<el-input  v-model="ruleForm.jifeibiaozhun"  autocomplete="off" placeholder="计费标准"  type="text"  />
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('zhaopian')?'required':''">照片：</div>
                    <file-upload
                        tip="点击上传照片"
                        action="file/upload"
                        :limit="3"
                        :multiple="true"
                        :fileUrls="ruleForm.zhaopian?ruleForm.zhaopian:''"
                        @change="fuwurenyuanzhaopianUploadChange"
                    ></file-upload>
				</el-form-item>
				<el-form-item :style='{"width":"80%","padding":"0","margin":"0 auto 15px","height":"auto"}' class="list-item" v-if="tableName=='fuwurenyuan'">
					<div v-if="false" :style='{"width":"64px","lineHeight":"44px","fontSize":"14px","position":"relative","color":"rgba(64, 158, 255, 1)"}' class="lable" :class="changeRules('fuwujianjie')?'required':''">服务简介：</div>
					<editor
						style="min-width: 200px; max-width: 600px;"
						:style='{"width":"100%","boxShadow":"0 0 6px rgb(66, 185, 131)","height":"auto"}'
						v-model="ruleForm.fuwujianjie" 
						class="editor" 
						action="file/upload">
					</editor>
				</el-form-item>
				<button :style='{"border":"0","cursor":"pointer","padding":"0 10px","boxShadow":"0 0 6px rgb(66, 185, 131)","margin":"20px auto 5px","color":"#fff","display":"block","outline":"none","borderRadius":"8px","background":"rgb(66, 185, 131)","width":"80%","fontSize":"16px","height":"44px"}' type="button" class="r-btn" @click="login()">注册</button>
				<div :style='{"cursor":"pointer","padding":"0 10%","color":"rgba(159, 159, 159, 1)","display":"inline-block","lineHeight":"1","fontSize":"12px","textDecoration":"underline"}' class="r-login" @click="close()">已有账号，直接登录</div>
			</el-form>
			
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			ruleForm: {
			},
			forgetForm: {},
            pageFlag : '',
			tableName:"",
			rules: {},
            laorenxingbieOptions: [],
            laorenmanxingbingOptions: [],
            fuwurenyuanxingbieOptions: [],
            fuwurenyuanfuwuleixingOptions: [],
		};
	},
	mounted(){
		this.pageFlag = this.$route.query.pageFlag
		if(this.$route.query.pageFlag=='register'){
			
			let table = this.$storage.get("loginTable");
			this.tableName = table;
			if(this.tableName=='laoren'){
				this.ruleForm = {
					laorenzhanghao: '',
					mima: '',
					laorenxingming: '',
					xingbie: '',
					nianling: '',
					shoujihaoma: '',
					manxingbing: '',
					touxiang: '',
				}
			}
			if(this.tableName=='fuwurenyuan'){
				this.ruleForm = {
					renyuanbianhao: '',
					mima: '',
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
				this.rules.laorenzhanghao = [{ required: true, message: '请输入老人账号', trigger: 'blur' }]
			}
			if ('laoren' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('laoren' == this.tableName) {
				this.rules.laorenxingming = [{ required: true, message: '请输入老人姓名', trigger: 'blur' }]
			}
			if ('fuwurenyuan' == this.tableName) {
				this.rules.renyuanbianhao = [{ required: true, message: '请输入人员编号', trigger: 'blur' }]
			}
			if ('fuwurenyuan' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('fuwurenyuan' == this.tableName) {
				this.rules.renyuanxingming = [{ required: true, message: '请输入人员姓名', trigger: 'blur' }]
			}
			if ('fuwurenyuan' == this.tableName) {
				this.rules.fuwuleixing = [{ required: true, message: '请输入服务类型', trigger: 'blur' }]
			}
			this.laorenxingbieOptions = "男,女".split(',')
			this.$http({
				url: `option/manxingbing/manxingbing`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.laorenmanxingbingOptions = data.data;
				} else {
					this.$message.error(data.msg);
				}
			});
			this.fuwurenyuanxingbieOptions = "男,女".split(',')
			this.$http({
				url: `option/fuwuleixing/fuwuleixing`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.fuwurenyuanfuwuleixingOptions = data.data;
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	},
	created() {
	},
	destroyed() {
		  	},
	methods: {
		changeRules(name){
			if(this.rules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		close(){
			this.$router.push({ path: "/login" });
		},
        laorenmanxingbingChange(e) {
            this.ruleForm.manxingbing = e.join(',');
        },
        laorentouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },
        fuwurenyuanzhaopianUploadChange(fileUrls) {
            this.ruleForm.zhaopian = fileUrls;
        },

        // 多级联动参数


		// 注册
		login() {
			var url=this.tableName+"/register";
					if((!this.ruleForm.laorenzhanghao) && `laoren` == this.tableName){
						this.$message.error(`老人账号不能为空`);
						return
					}
					if((!this.ruleForm.mima) && `laoren` == this.tableName){
						this.$message.error(`密码不能为空`);
						return
					}
					if((this.ruleForm.mima!=this.ruleForm.mima2) && `laoren` == this.tableName){
						this.$message.error(`两次密码输入不一致`);
						return
					}
					if((!this.ruleForm.laorenxingming) && `laoren` == this.tableName){
						this.$message.error(`老人姓名不能为空`);
						return
					}
					if(`laoren` == this.tableName && this.ruleForm.nianling &&(!this.$validate.isIntNumer(this.ruleForm.nianling))){
						this.$message.error(`年龄应输入整数`);
						return
					}
					if(`laoren` == this.tableName && this.ruleForm.shoujihaoma &&(!this.$validate.isMobile(this.ruleForm.shoujihaoma))){
						this.$message.error(`手机号码应输入手机格式`);
						return
					}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
			  if(this.tableName=='fuwurenyuan'){
				  this.ruleForm.sfsh = '待审核'
			  }
					if((!this.ruleForm.renyuanbianhao) && `fuwurenyuan` == this.tableName){
						this.$message.error(`人员编号不能为空`);
						return
					}
					if((!this.ruleForm.mima) && `fuwurenyuan` == this.tableName){
						this.$message.error(`密码不能为空`);
						return
					}
					if((this.ruleForm.mima!=this.ruleForm.mima2) && `fuwurenyuan` == this.tableName){
						this.$message.error(`两次密码输入不一致`);
						return
					}
					if((!this.ruleForm.renyuanxingming) && `fuwurenyuan` == this.tableName){
						this.$message.error(`人员姓名不能为空`);
						return
					}
					if(`fuwurenyuan` == this.tableName && this.ruleForm.nianling &&(!this.$validate.isIntNumer(this.ruleForm.nianling))){
						this.$message.error(`年龄应输入整数`);
						return
					}
					if(`fuwurenyuan` == this.tableName && this.ruleForm.lianxidianhua &&(!this.$validate.isMobile(this.ruleForm.lianxidianhua))){
						this.$message.error(`联系电话应输入手机格式`);
						return
					}
					if((!this.ruleForm.fuwuleixing) && `fuwurenyuan` == this.tableName){
						this.$message.error(`服务类型不能为空`);
						return
					}
					if(`fuwurenyuan` == this.tableName && this.ruleForm.fuwufei &&(!this.$validate.isNumber(this.ruleForm.fuwufei))){
						this.$message.error(`服务费应输入数字`);
						return
					}
            if(this.ruleForm.zhaopian!=null) {
                this.ruleForm.zhaopian = this.ruleForm.zhaopian.replace(new RegExp(this.$base.url,"g"),"");
            }
			this.$http({
				url: url,
				method: "post",
				data:this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "注册成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.$router.replace({ path: "/login" });
						}
					});
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	}
};
</script>

<style lang="scss" scoped>
	.container {
	  position: relative;
	  background: url(http://codegen.caihongy.cn/20231230/12221b7460e0479da01d207672562c64.png);

		.el-date-editor.el-input {
		  width: 100%;
		}
		
		.rgs-form .el-input /deep/ .el-input__inner {
						border: 0;
						border-radius: 8px;
						padding: 0 10px;
						box-shadow: 0 0 6px rgb(66, 185, 131);
						outline: none;
						color: rgb(66, 185, 131);
						width: 100%;
						font-size: 14px;
						height: 44px;
					}
		
		.rgs-form .el-select /deep/ .el-input__inner {
						border: 0;
						border-radius: 8px;
						padding: 0 10px;
						box-shadow: 0 0 6px rgb(66, 185, 131);
						outline: none;
						color: rgb(66, 185, 131);
						width: 288px;
						font-size: 14px;
						height: 44px;
					}
		
		.rgs-form .el-date-editor /deep/ .el-input__inner {
						border: 0;
						border-radius: 8px;
						padding: 0 10px 0 30px;
						box-shadow: 0 0 6px rgb(66, 185, 131);
						outline: none;
						color: rgb(66, 185, 131);
						width: 288px;
						font-size: 14px;
						height: 44px;
					}
		
		.rgs-form .el-date-editor /deep/ .el-input__inner {
						border: 0;
						border-radius: 8px;
						padding: 0 10px 0 30px;
						box-shadow: 0 0 6px rgb(66, 185, 131);
						outline: none;
						color: rgb(66, 185, 131);
						width: 288px;
						font-size: 14px;
						height: 44px;
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
		  		  border: 1px dashed  rgb(66, 185, 131);
		  		  cursor: pointer;
		  		  border-radius: 8px;
		  		  color: rgb(66, 185, 131);
		  		  width: 160px;
		  		  font-size: 32px;
		  		  line-height: 160px;
		  		  text-align: center;
		  		  height: 160px;
		  		}
		
		.rgs-form /deep/ .el-upload-list .el-upload-list__item {
		  		  border: 1px dashed  rgb(66, 185, 131);
		  		  cursor: pointer;
		  		  border-radius: 8px;
		  		  color: rgb(66, 185, 131);
		  		  width: 160px;
		  		  font-size: 32px;
		  		  line-height: 160px;
		  		  text-align: center;
		  		  height: 160px;
		  		}
		
		.rgs-form /deep/ .el-upload .el-icon-plus {
		  		  border: 1px dashed  rgb(66, 185, 131);
		  		  cursor: pointer;
		  		  border-radius: 8px;
		  		  color: rgb(66, 185, 131);
		  		  width: 160px;
		  		  font-size: 32px;
		  		  line-height: 160px;
		  		  text-align: center;
		  		  height: 160px;
		  		}
	}
	.required {
		position: relative;
	}
	.required::after{
				color: red;
				left: -10px;
				position: absolute;
				content: "*";
			}
	.editor>.avatar-uploader {
		line-height: 0;
		height: 0;
	}
</style>
