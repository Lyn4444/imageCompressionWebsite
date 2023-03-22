<template>
  <div id="register">
<!--    <div class="breadcrumb">-->
<!--      <div class="breadcrumb-content">-->
<!--        <el-breadcrumb separator="/" style="max-height: 39px;min-height: 34px;">-->
<!--          <el-breadcrumb-item :to="{path: '/home'}">-->
<!--            <template>-->
<!--              <span style="font-family: 楷体,serif;font-size: x-large;">首页</span>-->
<!--            </template>-->
<!--          </el-breadcrumb-item>-->
<!--          <el-breadcrumb-item :to="{path: '/register'}">-->
<!--            <template>-->
<!--              <span style="font-family: 楷体,serif;font-size: x-large;">注册</span>-->
<!--            </template>-->
<!--          </el-breadcrumb-item>-->
<!--          <el-breadcrumb-item></el-breadcrumb-item>-->
<!--        </el-breadcrumb>-->
<!--      </div>-->
<!--    </div>-->
    <div class="register_area">
      <div class="box_area">
        <div class="box">
          <el-card class="box_card" shadow="hover">
            <div class="tittle">
              <p>注册</p>
            </div>
            <div class="box_content">
              <el-form ref="dl_form" :model="zc_form" label-width="90px" label-position="left">
                <el-form-item label="账号名">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">用户名</span>
                  </template>
                  <el-input v-model="zc_form.name" clearable></el-input>
                </el-form-item>
                <el-form-item label="邮箱">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">邮箱</span>
                  </template>
                  <el-input v-model="zc_form.email" clearable></el-input>
                </el-form-item>
                <el-form-item>
                  <template>
                    <el-input v-model="zc_form.num" clearable placeholder="验证码" style="width: 60%;margin-right: 12px;"/><el-button type="primary" plain >获取验证码</el-button>
                  </template>
                </el-form-item>
                <el-form-item label="密码">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">密码</span>
                  </template>
                  <el-input v-model="zc_form.passwd" show-password clearable></el-input>
                </el-form-item>
                <el-form-item label="确认密码">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">确认密码</span>
                  </template>
                  <el-input v-model="zc_form.passwd1" show-password clearable></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" round style="margin-right: 40px;" @click="click_dl">
                    <template>
                      <span style="font-family: 楷体,serif;font-size: large;margin: 0 10px 0 10px;">登录</span>
                    </template>
                  </el-button>
                  <el-button type="success" round >
                    <template>
                      <span style="font-family: 楷体,serif;font-size: large;margin: 0 10px 0 10px;">注册</span>
                    </template>
                  </el-button>
                </el-form-item>
              </el-form>
            </div>
            <div class="remark">
              <el-link type="danger" style="float: right;" :underline="false" @click="click_forget">
                <span>忘记密码?</span>
              </el-link>
            </div>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      zc_form: {
        name: '',
        email: '',
        num: '',
        passwd: '',
        passwd1: ''
      }
    }
  },
  methods: {
    click_dl() {
      const this_url = this.$route.path
      if (this_url === '/register') {
        this.$router.push('/login')
      }
    },
    click_forget() {
      this.$router.push('/forget')
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
.register_area {
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
.tittle {
  display: flex;
  margin:  0 0 10px 0;
}
.tittle p {
  width: max-content;
  padding: 1px;
  margin:  auto;
  color: #409eff;
  font: xx-large bolder;
  font-family: 楷体, serif;
}
.box_content {
  width: 67%;
  padding: 1px;
  margin: 0 auto;
}
.remark {
  width: 99%;
  margin: 0 auto;
}
</style>
