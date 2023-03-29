<template>
  <div id="Info">
    <div class="content">
      <div class="content-box">
        <div class="avatar-box">
          <div class="avatar">
            <el-avatar shape="square" :size="120" fit="fill" :src="src"></el-avatar>
          </div>
          <div class="information">
            <div class="name"><span
              style="font-family: 楷体,serif;font-size: large;font-weight: bold;">账号名：{{ name }}</span></div>
            <el-divider/>
            <div class="introduction"><span
              style="font-family: 楷体,serif;font-size: large;font-weight: bold;">简介：{{ introduction }}</span></div>
          </div>
        </div>
        <div class="operate-box">
          <div class="operate">
            <span style="font-family: 楷体,serif;font-size: large;">账号名：{{ name }}&emsp;</span>
            <el-button type="text" icon="el-icon-edit-outline"><span
              style="font-family: 楷体,serif;font-size: large;font-weight: bold;">编辑</span></el-button>
          </div>
          <div class="operate">
            <span style="font-family: 楷体,serif;font-size: large;">邮&ensp;箱：{{ email }}&emsp;</span>
            <el-button type="text" icon="el-icon-edit-outline"><span
              style="font-family: 楷体,serif;font-size: large;font-weight: bold;">编辑</span></el-button>
          </div>
          <div class="operate">
            <span style="font-family: 楷体,serif;font-size: large;">密&ensp;码：&emsp;</span>
            <el-button type="text" icon="el-icon-edit-outline"><span
              style="font-family: 楷体,serif;font-size: large;font-weight: bold;">编辑</span></el-button>
          </div>
          <div class="operate">
            <span style="font-family: 楷体,serif;font-size: large;">头&ensp;像：&emsp;</span>
            <el-button type="text" icon="el-icon-upload2"><span
              style="font-family: 楷体,serif;font-size: large;font-weight: bold;">上传</span></el-button>
          </div>
          <div class="operate">
            <span style="font-family: 楷体,serif;font-size: large;">简&ensp;介：{{ introduction }}&emsp;</span>
            <el-button type="text" icon="el-icon-edit-outline"><span
              style="font-family: 楷体,serif;font-size: large;font-weight: bold;">编辑</span></el-button>
          </div>
          <div class="operate">
            <span style="font-family: 楷体,serif;font-size: large;">注册时间：{{ time }}&emsp;</span>
            <el-button type="text" disabled><span
              style="font-family: 楷体,serif;font-size: large;font-weight: bold;"></span></el-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "info",
  data() {
    return {
      src: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
      name: window.sessionStorage.getItem("name"),
      introduction: "暂无简介",
      email: window.sessionStorage.getItem("email"),
      time: window.sessionStorage.getItem("time"),
    }
  }
}
</script>

<style scoped>
#home {
  max-width: 100%;
  min-width: 1550px;
  min-height: 1000px;
}

.content {
  max-width: 100%;
  min-width: 1550px;
  min-height: 1000px;
  /*background-color: #8cc5ff;*/
}

.content-box {
  max-width: 1000px;
  min-width: 700px;
  min-height: 700px;
}

.avatar-box {
  min-width: 520px;
  min-height: 200px;
  margin-left: 200px;
  padding-top: 150px;
}

.avatar {
  float: left;
  width: 140px;
}

.information {
  float: left;
  min-width: 400px;
  height: max-content;
  margin-top: 10px;
}

.operate-box {
  min-width: 520px;
  min-height: max-content;
  margin-left: 200px;
}
</style>
