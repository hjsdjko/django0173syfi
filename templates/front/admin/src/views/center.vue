<template>
  <div :style='{"padding":"30px","background":" url(http://codegen.caihongy.cn/20231205/b1037a84990a40d38531410083b9d519.jpg) repeat fixed center center / cover"}'>
    <el-form
	  :style='{"padding":"30px","boxShadow":"0 1px 6px rgba(64, 158, 255, .3)","borderRadius":"6px","background":"#fff"}'
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      label-width="80px"
    >  
     <el-row>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='laoren'"  label="老人账号" prop="laorenzhanghao">
          <el-input v-model="ruleForm.laorenzhanghao" readonly              placeholder="老人账号" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='laoren'"  label="老人姓名" prop="laorenxingming">
          <el-input v-model="ruleForm.laorenxingming"               placeholder="老人姓名" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}' v-if="flag=='laoren'"  label="性别" prop="xingbie">
          <el-select v-model="ruleForm.xingbie"  placeholder="请选择性别">
            <el-option
                v-for="(item,index) in laorenxingbieOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='laoren'"  label="年龄" prop="nianling">
          <el-input v-model="ruleForm.nianling"               placeholder="年龄" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='laoren'"  label="手机号码" prop="shoujihaoma">
          <el-input v-model="ruleForm.shoujihaoma"               placeholder="手机号码" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='laoren'"  label="慢性病" prop="manxingbing">
          <el-input v-model="ruleForm.manxingbing"               placeholder="慢性病" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}' v-if="flag=='laoren'" label="头像" prop="touxiang">
          <file-upload
          tip="点击上传头像"
          action="file/upload"
          :limit="3"
          :multiple="true"
          :fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
          @change="laorentouxiangUploadChange"
          ></file-upload>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='fuwurenyuan'"  label="人员编号" prop="renyuanbianhao">
          <el-input v-model="ruleForm.renyuanbianhao" readonly              placeholder="人员编号" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='fuwurenyuan'"  label="人员姓名" prop="renyuanxingming">
          <el-input v-model="ruleForm.renyuanxingming"               placeholder="人员姓名" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}' v-if="flag=='fuwurenyuan'"  label="性别" prop="xingbie">
          <el-select v-model="ruleForm.xingbie"  placeholder="请选择性别">
            <el-option
                v-for="(item,index) in fuwurenyuanxingbieOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='fuwurenyuan'"  label="年龄" prop="nianling">
          <el-input v-model="ruleForm.nianling"               placeholder="年龄" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='fuwurenyuan'"  label="联系电话" prop="lianxidianhua">
          <el-input v-model="ruleForm.lianxidianhua"               placeholder="联系电话" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}' v-if="flag=='fuwurenyuan'"  label="服务类型" prop="fuwuleixing">
          <el-select v-model="ruleForm.fuwuleixing"  placeholder="请选择服务类型">
            <el-option
                v-for="(item,index) in fuwurenyuanfuwuleixingOptions"
                v-bind:key="index"
                :label="item"
                :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='fuwurenyuan'"  label="服务费" prop="fuwufei">
          <el-input v-model="ruleForm.fuwufei"               placeholder="服务费" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}'   v-if="flag=='fuwurenyuan'"  label="计费标准" prop="jifeibiaozhun">
          <el-input v-model="ruleForm.jifeibiaozhun"               placeholder="计费标准" clearable></el-input>
        </el-form-item>
        <el-form-item :style='{"margin":"0 0 20px 0"}' v-if="flag=='fuwurenyuan'" label="照片" prop="zhaopian">
          <file-upload
          tip="点击上传照片"
          action="file/upload"
          :limit="3"
          :multiple="true"
          :fileUrls="ruleForm.zhaopian?ruleForm.zhaopian:''"
          @change="fuwurenyuanzhaopianUploadChange"
          ></file-upload>
        </el-form-item>
		<el-form-item :style='{"margin":"0 0 20px 0"}' v-if="flag=='fuwurenyuan'" label="服务简介" prop="fuwujianjie">
		  <editor
		  	style="min-width: 200px; max-width: 600px;"
			 :style='{"width":"600px","boxShadow":"0 0 6px rgb(142, 195, 107)","height":"auto"}'
		  	v-model="ruleForm.fuwujianjie" 
		  	class="editor" 
		  	action="file/upload">
		  </editor>
		</el-form-item>
		<el-form-item :style='{"margin":"0 0 20px 0"}' v-if="flag=='users'" label="用户名" prop="username">
			<el-input v-model="ruleForm.username" placeholder="用户名"></el-input>
		</el-form-item>
		<el-form-item :style='{"margin":"0 0 20px 0"}' v-if="flag=='users'" label="头像" prop="image">
		  <file-upload
		  tip="点击上传头像"
		  action="file/upload"
		  :limit="1"
		  :multiple="false"
		  :fileUrls="ruleForm.image?ruleForm.image:''"
		  @change="usersimageUploadChange"
		  ></file-upload>
		</el-form-item>
		<el-form-item :style='{"padding":"0","margin":"0"}'>
			<el-button class="btn3" :style='{"border":"0","cursor":"pointer","padding":"0 24px","margin":"4px","outline":"none","color":"#fff","borderRadius":"4px","background":"rgb(142, 195, 107)","width":"auto","fontSize":"14px","height":"40px"}' type="primary" @click="onUpdateHandler">
				<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","height":"40px"}'></span>
				提交
			</el-button>
		</el-form-item>
      </el-row>
    </el-form>
  </div>
</template>
<script>
// 数字，邮件，手机，url，身份证校验
import { isNumber,isIntNumer,isEmail,isMobile,isPhone,isURL,checkIdCard } from "@/utils/validate";

export default {
  data() {
    return {
      ruleForm: {},
      flag: '',
      usersFlag: false,
      laorenxingbieOptions: [],
      fuwurenyuanxingbieOptions: [],
      fuwurenyuanfuwuleixingOptions: [],
    };
  },
  mounted() {
    var table = this.$storage.get("sessionTable");
    this.flag = table;
    this.$http({
      url: `${this.$storage.get("sessionTable")}/session`,
      method: "get"
    }).then(({ data }) => {
      if (data && data.code === 0) {
        this.ruleForm = data.data;
      } else {
        this.$message.error(data.msg);
      }
    });
    this.laorenxingbieOptions = "男,女".split(',')
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
  },
  methods: {
    laorentouxiangUploadChange(fileUrls) {
        this.ruleForm.touxiang = fileUrls;
    },
    fuwurenyuanzhaopianUploadChange(fileUrls) {
        this.ruleForm.zhaopian = fileUrls;
    },
	usersimageUploadChange(fileUrls) {
		this.ruleForm.image = fileUrls;
	},
    onUpdateHandler() {
      if((!this.ruleForm.laorenzhanghao)&& 'laoren'==this.flag){
        this.$message.error('老人账号不能为空');
        return
      }


      if((!this.ruleForm.mima)&& 'laoren'==this.flag){
        this.$message.error('密码不能为空');
        return
      }


      if((!this.ruleForm.laorenxingming)&& 'laoren'==this.flag){
        this.$message.error('老人姓名不能为空');
        return
      }






      if( 'laoren' ==this.flag && this.ruleForm.nianling&&(!isIntNumer(this.ruleForm.nianling))){
       this.$message.error(`年龄应输入整数`);
        return
      }


      if( 'laoren' ==this.flag && this.ruleForm.shoujihaoma&&(!isMobile(this.ruleForm.shoujihaoma))){
        this.$message.error(`手机号码应输入手机格式`);
        return
      }




        if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
        }
      if((!this.ruleForm.renyuanbianhao)&& 'fuwurenyuan'==this.flag){
        this.$message.error('人员编号不能为空');
        return
      }


      if((!this.ruleForm.mima)&& 'fuwurenyuan'==this.flag){
        this.$message.error('密码不能为空');
        return
      }


      if((!this.ruleForm.renyuanxingming)&& 'fuwurenyuan'==this.flag){
        this.$message.error('人员姓名不能为空');
        return
      }






      if( 'fuwurenyuan' ==this.flag && this.ruleForm.nianling&&(!isIntNumer(this.ruleForm.nianling))){
       this.$message.error(`年龄应输入整数`);
        return
      }


      if( 'fuwurenyuan' ==this.flag && this.ruleForm.lianxidianhua&&(!isMobile(this.ruleForm.lianxidianhua))){
        this.$message.error(`联系电话应输入手机格式`);
        return
      }
      if((!this.ruleForm.fuwuleixing)&& 'fuwurenyuan'==this.flag){
        this.$message.error('服务类型不能为空');
        return
      }




      if( 'fuwurenyuan' ==this.flag && this.ruleForm.fuwufei&&(!isNumber(this.ruleForm.fuwufei))){
        this.$message.error(`服务费应输入数字`);
        return
      }




        if(this.ruleForm.zhaopian!=null) {
                this.ruleForm.zhaopian = this.ruleForm.zhaopian.replace(new RegExp(this.$base.url,"g"),"");
        }










      if( 'fuwurenyuan' ==this.flag && this.ruleForm.clicknum&&(!isIntNumer(this.ruleForm.clicknum))){
       this.$message.error(`点击次数应输入整数`);
        return
      }


      if( 'fuwurenyuan' ==this.flag && this.ruleForm.storeupnum&&(!isIntNumer(this.ruleForm.storeupnum))){
       this.$message.error(`收藏数应输入整数`);
        return
      }
      if('users'==this.flag && this.ruleForm.username.trim().length<1) {
	this.$message.error(`用户名不能为空`);
        return	
      }
	  if(this.flag=='users'){
	  	this.ruleForm.image = this.ruleForm.image.replace(new RegExp(this.$base.url,"g"),"")
	  }
      this.$http({
        url: `${this.$storage.get("sessionTable")}/update`,
        method: "post",
        data: this.ruleForm
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.$message({
            message: "修改信息成功",
            type: "success",
            duration: 1500,
            onClose: () => {
				if(this.flag=='users'){
					this.$storage.set('headportrait',this.ruleForm.image)
				}
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
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  	  padding: 0 10px 0 0;
	  	  color: #666;
	  	  font-weight: 500;
	  	  width: 80px;
	  	  font-size: 14px;
	  	  line-height: 40px;
	  	  text-align: right;
	  	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 80px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  	  border: 0;
	  	  border-radius: 4px;
	  	  padding: 0 12px;
	  	  box-shadow: 0 0 6px rgb(142, 195, 107);
	  	  outline: none;
	  	  width: 400px;
	  	  font-size: 14px;
	  	  height: 40px;
	  	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  	  border: 0;
	  	  border-radius: 4px;
	  	  padding: 0 10px;
	  	  box-shadow: 0 0 6px rgb(142, 195, 107);
	  	  outline: none;
	  	  width: 200px;
	  	  font-size: 14px;
	  	  height: 40px;
	  	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  	  border: 0;
	  	  border-radius: 4px;
	  	  box-shadow: 0 0 6px rgb(142, 195, 107);
	  	  outline: none;
	  	  width: 200px;
	  	  font-size: 14px;
	  	  height: 40px;
	  	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  	  border: 1px dashed rgb(142, 195, 107);
	  	  cursor: pointer;
	  	  border-radius: 6px;
	  	  width: 200px;
	  	  font-size: 32px;
	  	  line-height: 200px;
	  	  text-align: center;
	  	  height: 200px;
	  	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  	  border: 1px dashed rgb(142, 195, 107);
	  	  cursor: pointer;
	  	  border-radius: 6px;
	  	  width: 200px;
	  	  font-size: 32px;
	  	  line-height: 200px;
	  	  text-align: center;
	  	  height: 200px;
	  	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  	  border: 0;
	  	  border-radius: 4px;
	  	  padding: 12px;
	  	  box-shadow: 0 0 6px rgb(142, 195, 107);
	  	  outline: none;
	  	  width: 400px;
	  	  font-size: 14px;
	  	  height: 120px;
	  	}
	
	.add-update-preview .btn3 {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 24px;
				margin: 4px;
				outline: none;
				color: #fff;
				background: rgb(142, 195, 107);
				width: auto;
				font-size: 14px;
				height: 40px;
			}
	
	.add-update-preview .btn3:hover {
				opacity: 0.8;
			}
	
	.editor>.avatar-uploader {
		line-height: 0;
		height: 0;
	}
</style>
