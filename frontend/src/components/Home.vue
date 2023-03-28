<template>
  <div id="home">
    <!--    <div class="breadcrumb">-->
    <!--      <div class="breadcrumb-content">-->
    <!--        <el-breadcrumb separator="/" style="max-height: 39px;min-height: 34px;">-->
    <!--          <el-breadcrumb-item :to="{path: '/home'}">-->
    <!--            <template>-->
    <!--              <span style="font-family: 楷体,serif;font-size: x-large;">首页</span>-->
    <!--            </template>-->
    <!--          </el-breadcrumb-item>-->
    <!--          <el-breadcrumb-item></el-breadcrumb-item>-->
    <!--        </el-breadcrumb>-->
    <!--      </div>-->
    <!--    </div>-->
    <div class="upload-content">
      <div class="upload-content">
        <div class="upload-box">
          <el-upload class="upload-demo" drag :action="action"
                     :on-success="handleUploadSuccess"
                     :before-upload="beforeUpload"
                     :on-preview="handlePreview"
                     :auto-upload="false"
                     :on-remove="handleRemove"
                     :file-list="fileList"
                     ref="upload" multiple v-loading.fullscreen.lock="fullscreenLoading">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          </el-upload>
          <div class="button-box">
            <el-button type="primary" style="margin: 0 auto;" @click="submitUpload">点击上传</el-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      action: "http://127.0.0.1:8000/api/file/upload/",
      fileList: [],
      filenamelist: [],
      fullscreenLoading: false
    }
  },
  methods: {
    submitUpload() {
      this.$refs.upload.submit();
    },
    handleUploadSuccess(response) {
      switch (response['code']) {
        case '500':
          this.$message.error(response['msg']);
          break;
        case '402':
          this.$message.error("未知错误，请联系网站管理员");
          break;
        case '503':
          this.$message.error('图片上传失败，请刷新后重新上传');
          break;
        default:
          this.$notify.success({
            title: "PicSmart",
            message: "图片上传成功，正在处理，请稍后......"
          })
          this.openFullScreen();
      }
    },
    beforeUpload(file, fileList) {
      console.log(file)
      const littleName = file.name.toLowerCase()
      const copyFile = new File([file], littleName)
      this.handlePddUploadFile(copyFile)
      return false
    },
    handleRemove(file, fileList) {
      console.log(file);
    },
    handlePreview(file, fileList) {
      console.log(file);
    },
    handlePddUploadFile(copyFile) {
      const formData = new FormData()
      formData.append('file', copyFile)
      let filename = copyFile.name;
      let type = filename.split(".")[1]
      let randomNum = Math.random().toFixed(10).slice(-10);
      let newfilename = randomNum + "." + type
      this.filenamelist.push(newfilename)
      formData.append('filename', newfilename)
      this.handlePddPostForm(formData)
    },
    async handlePddPostForm(formData) {
      try {
        const res = await this.$axios.post(this.action, formData, {
          headers: this.headers
        })
        this.handleUploadSuccess(res.data)
      } catch (error) {
        console.log(error)
        this.$message.error("未知错误，请联系网站管理员")
      }
    },
    openFullScreen() {
        this.fullscreenLoading = true;
        setTimeout(() => {
          this.fullscreenLoading = false;
        }, 10000);
      }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.breadcrumb {
  max-width: 100%;
  min-width: 1550px;
  max-height: 40px;
  min-height: 35px;
  background-color: #8cc5ff;
}

.breadcrumb-content {
  width: 90%;
  max-height: 40px;
  min-height: 35px;
  margin: 0 auto;
  background-color: #8cc5ff;
}

.upload-content {
  max-width: 100%;
  min-width: 1550px;
  max-height: 550px;
  min-height: 500px;
  background-color: #8cc5ff;
}

.upload-box {
  width: 360px;
  padding-top: 100px;
  margin: 0 auto;
}

.button-box {
  width: min-content;
  padding-top: 10px;
  margin: 0 auto;
}
</style>
