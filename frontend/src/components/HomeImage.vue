<template>
  <div id="homeimage">
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
      <div class="upload-box">
        <el-upload class="upload-demo" drag action="">
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">
              <template>
                <span style="font-family: 楷体,serif;font-size: large;margin: 0 10px 0 10px;">将文件拖到此处，或<em>点击上传</em></span>
              </template>
            </div>
            <div slot="tip" class="el-upload__tip">
              <template>
                <span style="font-family: 楷体,serif;font-size: medium;margin: 0 10px 0 10px;">考虑网站负载暂时只能上传1张图片</span>
              </template>
            </div>
        </el-upload>
        <div class="button-box">
          <el-button type="primary" style="margin: 0 auto;" @click="submitUpload" plain>
            <template>
              <span style="font-family: 楷体,serif;font-size: large;margin: 0 10px 0 10px;">点击上传</span>
            </template>
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeImage",
  mounted() {
    this.$notify.info({
      title: "PicSmart",
      message: "在线图片格式转换,支持包括jpg,png,jp2,bmp,gif,webp,jpeg在内的80多种图片格式"
    })
  },
}
</script>

<style scoped>
#homeimage {
  max-width: 100%;
  min-width: 1550px;
  min-height: 1000px;
}

.breadcrumb {
  max-width: 100%;
  min-width: 1550px;
  max-height: 40px;
  min-height: 35px;
  margin-top: 1px;
}

.breadcrumb-content {
  width: 90%;
  max-height: 40px;
  min-height: 35px;
  margin: 0 auto;
}

.upload-content {
  max-width: 100%;
  min-width: 1550px;
  /*max-height: 550px;*/
  /*min-height: 500px;*/
  min-height: 1000px;
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
