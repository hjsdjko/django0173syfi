<template>
<div :style='{"width":"100%","padding":"30px 18% 40px","margin":"0px auto","position":"relative","background":"#fff"}'>
    <el-form
	  :style='{"border":"1px solid #eee","padding":"30px 0","alignItems":"flex-start","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","position":"relative"}'
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      :rules="rules"
      label-width="120px"
    >
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="报告单号" prop="baogaodanhao">
              <el-input v-model="ruleForm.baogaodanhao" placeholder="报告单号" disabled></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="老人账号" prop="laorenzhanghao">
            <el-input v-model="ruleForm.laorenzhanghao" 
                placeholder="老人账号" clearable :disabled=" false  ||ro.laorenzhanghao"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="老人姓名" prop="laorenxingming">
            <el-input v-model="ruleForm.laorenxingming" 
                placeholder="老人姓名" clearable :disabled=" false  ||ro.laorenxingming"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="报告图片" v-if="type!='cross' || (type=='cross' && !ro.baogaotupian)" prop="baogaotupian">
            <file-upload
            tip="点击上传报告图片"
            action="file/upload"
            :limit="3"
            :multiple="true"
            :fileUrls="ruleForm.baogaotupian?ruleForm.baogaotupian:''"
            @change="baogaotupianUploadChange"
            ></file-upload>
          </el-form-item>
            <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' class="upload" v-else label="报告图片" prop="baogaotupian">
                <img v-if="ruleForm.baogaotupian.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.baogaotupian.split(',')[0]" width="100" height="100">
                <img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.baogaotupian.split(',')" :src="baseUrl+item" width="100" height="100">
            </el-form-item>
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}'  label="健康状态" prop="jiankangzhuangtai">
            <el-select v-model="ruleForm.jiankangzhuangtai" placeholder="请选择健康状态" :disabled=" false  ||ro.jiankangzhuangtai" >
              <el-option
                  v-for="(item,index) in jiankangzhuangtaiOptions"
                  :key="index"
                  :label="item"
                  :value="item">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="健康报告" prop="jiankangbaogao">
            <file-upload
            tip="点击上传健康报告"
            action="file/upload"
            :limit="1"
			:type="3"
            :multiple="true"
            :fileUrls="ruleForm.jiankangbaogao?ruleForm.jiankangbaogao:''"
            @change="jiankangbaogaoUploadChange"
            ></file-upload>
          </el-form-item>  
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="报告时间" prop="baogaoshijian">
              <el-date-picker
				  :disabled=" false  ||ro.baogaoshijian"
                  value-format="yyyy-MM-dd HH:mm:ss"
                  v-model="ruleForm.baogaoshijian" 
                  type="datetime"
                  placeholder="报告时间">
              </el-date-picker>
          </el-form-item>
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="健康趋势" prop="jiankangqushi">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="健康趋势"
              v-model="ruleForm.jiankangqushi">
            </el-input>
          </el-form-item>
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="健康警报" prop="jiankangjingbao">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="健康警报"
              v-model="ruleForm.jiankangjingbao">
            </el-input>
          </el-form-item>
          <el-form-item :style='{"width":"48%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="健康建议" prop="jiankangjianyi">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="健康建议"
              v-model="ruleForm.jiankangjianyi">
            </el-input>
          </el-form-item>

      <el-form-item :style='{"width":"100%","padding":"0","margin":"0","textAlign":"center"}'>
        <el-button :style='{"border":"0px solid #eccc19","cursor":"pointer","padding":"0","margin":"0 20px 0 0","color":"#fff","borderRadius":"20px","background":"linear-gradient(to right,#f67536,#f64d36),#f64d36","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}'  type="primary" @click="onSubmit">提交</el-button>
        <el-button :style='{"border":"1px solid #ccc","cursor":"pointer","padding":"0","margin":"0","outline":"none","color":"#666","borderRadius":"20px","background":"none","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}' @click="back()">返回</el-button>
      </el-form-item>
    </el-form>
</div>
</template>

<script>
  export default {
    data() {
	  let self = this
      return {
        id: '',
        baseUrl: '',
        ro:{
				baogaodanhao : false,
				laorenzhanghao : false,
				laorenxingming : false,
				baogaotupian : false,
				jiankangzhuangtai : false,
				jiankangbaogao : false,
				jiankangqushi : false,
				jiankangjingbao : false,
				jiankangjianyi : false,
				baogaoshijian : false,
        },
        type: '',
        userTableName: localStorage.getItem('UserTableName'),
        ruleForm: {
          baogaodanhao: this.getUUID(),
          laorenzhanghao: '',
          laorenxingming: '',
          baogaotupian: '',
          jiankangzhuangtai: '',
          jiankangbaogao: '',
          jiankangqushi: '',
          jiankangjingbao: '',
          jiankangjianyi: '',
          baogaoshijian: '',
        },
        jiankangzhuangtaiOptions: [],


        rules: {
          baogaodanhao: [
          ],
          laorenzhanghao: [
          ],
          laorenxingming: [
          ],
          baogaotupian: [
          ],
          jiankangzhuangtai: [
            { required: true, message: '健康状态不能为空', trigger: 'blur' },
          ],
          jiankangbaogao: [
            { required: true, message: '健康报告不能为空', trigger: 'blur' },
          ],
          jiankangqushi: [
            { required: true, message: '健康趋势不能为空', trigger: 'blur' },
          ],
          jiankangjingbao: [
          ],
          jiankangjianyi: [
          ],
          baogaoshijian: [
          ],
        },
		centerType: false,
      };
    },
    computed: {



    },
    components: {
    },
    created() {
		if(this.$route.query.centerType){
			this.centerType = true
		}
	  //this.bg();
      let type = this.$route.query.type ? this.$route.query.type : '';
      this.init(type);
      this.baseUrl = this.$config.baseUrl;
      this.ruleForm.baogaoshijian = this.getCurDateTime()
    },
    methods: {
      getMakeZero(s) {
          return s < 10 ? '0' + s : s;
      },
      // 下载
      download(file){
        window.open(`${file}`)
      },
      // 初始化
      init(type) {
        this.type = type;
        if(type=='cross'){
          var obj = JSON.parse(localStorage.getItem('crossObj'));
          for (var o in obj){
            if(o=='baogaodanhao'){
              this.ruleForm.baogaodanhao = obj[o];
              this.ro.baogaodanhao = true;
              continue;
            }
            if(o=='laorenzhanghao'){
              this.ruleForm.laorenzhanghao = obj[o];
              this.ro.laorenzhanghao = true;
              continue;
            }
            if(o=='laorenxingming'){
              this.ruleForm.laorenxingming = obj[o];
              this.ro.laorenxingming = true;
              continue;
            }
            if(o=='baogaotupian'){
              this.ruleForm.baogaotupian = obj[o].split(",")[0];
              this.ro.baogaotupian = true;
              continue;
            }
            if(o=='jiankangzhuangtai'){
              this.ruleForm.jiankangzhuangtai = obj[o];
              this.ro.jiankangzhuangtai = true;
              continue;
            }
            if(o=='jiankangbaogao'){
              this.ruleForm.jiankangbaogao = obj[o];
              this.ro.jiankangbaogao = true;
              continue;
            }
            if(o=='jiankangqushi'){
              this.ruleForm.jiankangqushi = obj[o];
              this.ro.jiankangqushi = true;
              continue;
            }
            if(o=='jiankangjingbao'){
              this.ruleForm.jiankangjingbao = obj[o];
              this.ro.jiankangjingbao = true;
              continue;
            }
            if(o=='jiankangjianyi'){
              this.ruleForm.jiankangjianyi = obj[o];
              this.ro.jiankangjianyi = true;
              continue;
            }
            if(o=='baogaoshijian'){
              this.ruleForm.baogaoshijian = obj[o];
              this.ro.baogaoshijian = true;
              continue;
            }
          }
        }else if(type=='edit'){
			this.info()
		}
        // 获取用户信息
        this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            var json = res.data.data;
          }
        });
        this.jiankangzhuangtaiOptions = "健康,异常".split(',')

		if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
			localStorage.removeItem('raffleType')
			setTimeout(() => {
				this.onSubmit()
			}, 300)
		}
      },

    // 多级联动参数
      // 多级联动参数
      info() {
        this.$http.get(`jiankangbaogao/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.ruleForm = res.data.data;
          }
        });
      },
      // 提交
      onSubmit() {

			if(this.ruleForm.baogaodanhao){
				this.ruleForm.baogaodanhao = String(this.ruleForm.baogaodanhao)
			}
			//更新跨表属性
			var crossuserid;
			var crossrefid;
			var crossoptnum;
			this.$refs["ruleForm"].validate(valid => {
				if(valid) {
					if(this.type=='cross'){
						var statusColumnName = localStorage.getItem('statusColumnName');
						var statusColumnValue = localStorage.getItem('statusColumnValue');
						if(statusColumnName && statusColumnName!='') {
							var obj = JSON.parse(localStorage.getItem('crossObj'));
							if(!statusColumnName.startsWith("[")) {
								for (var o in obj){
									if(o==statusColumnName){
										obj[o] = statusColumnValue;
									}
								}
								var table = localStorage.getItem('crossTable');
								this.$http.post(table+'/update', obj).then(res => {});
							} else {
								crossuserid=Number(localStorage.getItem('frontUserid'));
								crossrefid=obj['id'];
								crossoptnum=localStorage.getItem('statusColumnName');
								crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
							}
						}
					}
					if(crossrefid && crossuserid) {
						this.ruleForm.crossuserid=crossuserid;
						this.ruleForm.crossrefid=crossrefid;
						var params = {
							page: 1,
							limit: 10,
							crossuserid:crossuserid,
							crossrefid:crossrefid,
						}
						this.$http.get('jiankangbaogao/list', {
							params: params
						}).then(res => {
							if(res.data.data.total>=crossoptnum) {
								this.$message({
									message: localStorage.getItem('tips'),
									type: 'error',
									duration: 1500,
								});
								return false;
							} else {
								// 跨表计算


								this.$http.post(`jiankangbaogao/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
									if (res.data.code == 0) {
										this.$message({
											message: '操作成功',
											type: 'success',
											duration: 1500,
											onClose: () => {
												this.$router.go(-1);
											}
										});
									} else {
										this.$message({
											message: res.data.msg,
											type: 'error',
											duration: 1500
										});
									}
								});
							}
						});
					} else {


						this.$http.post(`jiankangbaogao/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
							if (res.data.code == 0) {
								this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				}
			});
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		// 返回
		back() {
			this.$router.go(-1);
		},
      baogaotupianUploadChange(fileUrls) {
          this.ruleForm.baogaotupian = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");;
      },
      jiankangbaogaoUploadChange(fileUrls) {
          this.ruleForm.jiankangbaogao = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");;
      },
    }
  };
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  padding: 0 10px 0 0;
	  color: #666;
	  font-weight: 500;
	  width: 120px;
	  font-size: 14px;
	  line-height: 40px;
	  text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 120px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  border: 1px solid #ddd;
	  padding: 0 12px;
	  color: #666;
	  font-size: 14px;
	  border-color: #ddd;
	  border-radius: 0px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  background: none;
	  width: auto;
	  border-width: 1px;
	  border-style: solid;
	  min-width: 200px;
	  height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
	  border: 1px solid #ddd;
	  padding: 0 12px;
	  color: #666;
	  font-size: 14px;
	  border-color: #ddd;
	  border-radius: 0px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  background: none;
	  width: auto;
	  border-width: 1px;
	  border-style: solid;
	  min-width: 200px;
	  height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  border-radius: 0px;
	  padding: 0 10px;
	  color: #666;
	  background: none;
	  width: auto;
	  font-size: 14px;
	  border-color: #ddd;
	  border-width: 1px;
	  border-style: solid;
	  min-width: 250px;
	  height: 40px;
	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  border-radius: 0px;
	  padding: 0 10px 0 30px;
	  color: #666;
	  background: none;
	  width: auto;
	  font-size: 14px;
	  border-color: #ddd;
	  border-width: 1px;
	  border-style: solid;
	  min-width: 250px;
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
	
	.add-update-preview /deep/ .upload .upload-img {
	  cursor: pointer;
	  color: #999;
	  font-size: 24px;
	  border-color: #ddd;
	  line-height: 54px;
	  border-radius: 2px;
	  background: none;
	  width: auto;
	  border-width: 1px;
	  border-style: solid;
	  text-align: center;
	  min-width: 150px;
	  height: 54px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  cursor: pointer;
	  color: #999;
	  font-size: 24px;
	  border-color: #ddd;
	  line-height: 54px;
	  border-radius: 2px;
	  background: none;
	  width: auto;
	  border-width: 1px;
	  border-style: solid;
	  text-align: center;
	  min-width: 150px;
	  height: 54px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  cursor: pointer;
	  color: #999;
	  font-size: 24px;
	  border-color: #ddd;
	  line-height: 54px;
	  border-radius: 2px;
	  background: none;
	  width: auto;
	  border-width: 1px;
	  border-style: solid;
	  text-align: center;
	  min-width: 150px;
	  height: 54px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  border: 1px solid #ddd;
	  border-radius: 0px;
	  padding: 12px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  color: #666;
	  background: none;
	  width: 100%;
	  font-size: 14px;
	  height: 120px;
	}
</style>
