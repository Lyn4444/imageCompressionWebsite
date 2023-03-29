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
              <span
                style="font-family: 楷体,serif;font-size: large;margin: 0 10px 0 10px;">将文件拖到此处，或<em>点击上传</em></span>
            </template>
          </div>
          <div slot="tip" class="el-upload__tip">
            <template>
              <span
                style="font-family: 楷体,serif;font-size: large;margin: 0 10px 0 10px;">考虑网站负载暂时只能上传1张图片</span>
            </template>
          </div>
          <div slot="tip" class="el-upload__tip">
            <template>
              <span
                style="font-family: 楷体,serif;font-size: large;margin: 0 10px 0 10px;">图片转换后格式：<strong>{{
                  this.filetype
                }}</strong></span>
            </template>
          </div>
        </el-upload>
        <div class="button-box">
          <el-button type="info" style="float: left;margin-right: 40px;" @click="drawer=true" plain>
            <template>
              <span style="font-family: 楷体,serif;font-size: large;margin: 0 10px 10px 10px;">选择格式</span>
            </template>
          </el-button>
          <el-button type="primary" style="float: right;margin-left: 40px;" @click="" plain>
            <template>
              <span style="font-family: 楷体,serif;font-size: large;margin: 0 10px 10px 10px;">点击上传</span>
            </template>
          </el-button>
        </div>
        <el-drawer title="选择图片转换后格式" :visible.sync="drawer" direction="rtl" size="33%">
          <div class="select-box">
            <div class="button-list">
              <el-button v-for="item in typeList" style="margin-left: 25px;" @click="selectType(item)">
                <template>
                  <span style="font-family: 楷体,serif;font-size: x-large;margin: 0 30px 30px 30px;">{{ item }}</span>
                </template>
              </el-button>
            </div>
            <br/>
            <br/>
            <div class="button-list">
              <el-button v-for="item in typeList1" style="margin-left: 25px;" @click="selectType(item)">
                <template>
                  <span style="font-family: 楷体,serif;font-size: x-large;margin: 0 30px 30px 30px;">{{ item }}</span>
                </template>
              </el-button>
            </div>
            <br/>
            <br/>
            <div class="button-list">
              <template>
                <span style="font-family: 楷体,serif;font-size: xx-large;margin: 0 30px 30px 30px;float: left;">上述格式不符合，自主输入格式: </span>
                <div style="width: 150px;float: right;">
                  <el-input v-model="filetype" clearable placeholder="目标格式"></el-input>
                </div>
              </template>
            </div>
          </div>
        </el-drawer>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeImage",
  data() {
    return {
      filetype: "",
      drawer: false,
      typeList: ['jpg', 'webp', 'jp2', 'bmp'],
      typeList1: ['gif', 'tiff', 'png', 'jpeg']
    }
  },
  mounted() {
    this.$notify.info({
      title: "PicSmart",
      message: "在线图片格式转换,支持包括jpg,png,jp2,bmp,gif,webp,jpeg在内的80多种图片格式"
    })
  },
  methods: {
    selectType(item) {
      this.filetype = item;
      console.log(this.filetype)
    }
  }
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
  width: max-content;
  padding-top: 10px;
  margin: 0 auto;
}

/deep/ .el-drawer__header {
  margin-left: 30%;
  font-weight: bold;
  font-family: 楷体, serif;
  font-size: xx-large;
}

/deep/ :focus {
  outline: 0;
}

.select-box {
  min-width: 500px;
  min-height: 500px;
  margin: auto 50px;
}

.button-list {
  width: max-content;
  height: min-content;
}
</style>
