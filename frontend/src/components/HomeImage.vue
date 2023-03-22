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
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        </el-upload>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeImage"
}
</script>

<style scoped>
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
  max-height: 550px;
  min-height: 500px;
  background-color: #8cc5ff;
}
.upload-box {
  width: 400px;
  padding-top: 100px;
  margin: 0 auto;
}

</style>
