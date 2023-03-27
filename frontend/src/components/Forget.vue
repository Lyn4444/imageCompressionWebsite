<template>
 <div id="forget">
<!--   <div class="breadcrumb">-->
<!--      <div class="breadcrumb-content">-->
<!--        <el-breadcrumb separator="/" style="max-height: 39px;min-height: 34px;">-->
<!--          <el-breadcrumb-item :to="{path: '/home'}">-->
<!--            <template>-->
<!--              <span style="font-family: 楷体,serif;font-size: x-large;">首页</span>-->
<!--            </template>-->
<!--          </el-breadcrumb-item>-->
<!--          <el-breadcrumb-item :to="{path: '/forget'}">-->
<!--            <template>-->
<!--              <span style="font-family: 楷体,serif;font-size: x-large;">忘记密码</span>-->
<!--            </template>-->
<!--          </el-breadcrumb-item>-->
<!--          <el-breadcrumb-item></el-breadcrumb-item>-->
<!--        </el-breadcrumb>-->
<!--      </div>-->
<!--    </div>-->
   <div class="forget_area">
      <div class="box_area">
        <div class="box">
          <el-card class="box_card" shadow="hover">
            <div class="box_content">
              <el-form ref="fg_form" :model="fg_form" label-width="90px" label-position="left">
                <el-form-item label="账号名">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">用户名</span>
                  </template>
                  <el-input v-model="fg_form.name" clearable></el-input>
                </el-form-item>
                <el-form-item label="邮箱">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">邮箱</span>
                  </template>
                  <el-input v-model="fg_form.email" clearable></el-input>
                </el-form-item>
                <el-form-item>
                  <template>
                    <el-input v-model="fg_form.num" clearable placeholder="验证码" style="width: 60%;margin-right: 12px;"/><el-button type="primary" plain >获取验证码</el-button>
                  </template>
                </el-form-item>
                <el-form-item label="密码">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">新密码</span>
                  </template>
                  <el-input v-model="fg_form.passwd" show-password clearable></el-input>
                </el-form-item>
                <el-form-item label="确认密码">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">确认密码</span>
                  </template>
                  <el-input v-model="fg_form.passwd1" show-password clearable></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="info" round style="margin-right: 1px;float: right;" @click="">
                    <template>
                      <span style="font-family: 楷体,serif;font-size: large;margin: 0 20px 0 20px;">验证</span>
                    </template>
                  </el-button>
                </el-form-item>
              </el-form>
            </div>
          </el-card>
        </div>
      </div>
    </div>
 </div>
</template>

<script>
export default {
  name: "Forget",
  data() {
    return {
      fg_form: {
        name: '',
        email: '',
        num: '',
        passwd: '',
        passwd1: ''
      }
    }
  }
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
.forget_area {
  display: flex;
  max-width: 100%;
  min-width: 1550px;
  padding: 1px;
  margin: 1px;
  max-height: 800px;
  min-height: 750px;
}
.box_area {
  width: 99%;
  max-height: 750px;
  min-height: 700px;
  padding: 1px;
  margin: 0 auto;
  display: flex;
}
.box {
  width: 700px;
  height: 550px;
  padding: 1px;
  margin: auto;
}
.box_content {
  width: 67%;
  padding: 1px;
  margin: 0 auto;
}
</style>
