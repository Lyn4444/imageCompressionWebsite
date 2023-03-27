<template>
  <div id="login">
    <!--    <div class="breadcrumb">-->
    <!--      <div class="breadcrumb-content">-->
    <!--        <el-breadcrumb separator="/" style="max-height: 39px;min-height: 34px;">-->
    <!--          <el-breadcrumb-item :to="{path: '/home'}">-->
    <!--            <template>-->
    <!--              <span style="font-family: 楷体,serif;font-size: x-large;">首页</span>-->
    <!--            </template>-->
    <!--          </el-breadcrumb-item>-->
    <!--          <el-breadcrumb-item :to="{path: '/login'}">-->
    <!--            <template>-->
    <!--              <span style="font-family: 楷体,serif;font-size: x-large;">登录</span>-->
    <!--            </template>-->
    <!--          </el-breadcrumb-item>-->
    <!--          <el-breadcrumb-item></el-breadcrumb-item>-->
    <!--        </el-breadcrumb>-->
    <!--      </div>-->
    <!--    </div>-->
    <div class="login_area">
      <div class="box_area">
        <div class="box">
          <el-card class="box_card" shadow="hover">
            <div class="tittle">
              <p>登录</p>
            </div>
            <div class="box_content">
              <el-form ref="dl_form" :model="dl_form" label-width="80px" label-position="left" :rules="rules">
                <el-form-item label="账号名" prop="name">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">用户名</span>
                  </template>
                  <el-input v-model="dl_form.name"></el-input>
                </el-form-item>
                <el-form-item label="邮箱" prop="email">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">邮箱</span>
                  </template>
                  <el-input v-model="dl_form.email"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="passwd">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">密码</span>
                  </template>
                  <el-input v-model="dl_form.passwd" show-password></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" round style="margin-right: 40px;" @click="do_login">
                    <template>
                      <span style="font-family: 楷体,serif;font-size: large;margin: 0 10px 0 10px;">登录</span>
                    </template>
                  </el-button>
                  <el-button type="success" round @click="click_zc">
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
import {rules} from "vue-resource/.eslintrc";

const checkEmail = (rule, value, callback) => {
  const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((.[a-zA-Z0-9_-]{2,3}){1,2})$/
  if (!value) {
    return callback(new Error('邮箱不能为空'))
  }
  setTimeout(() => {
    if (mailReg.test(value)) {
      callback()
    } else {
      callback(new Error('请输入正确的邮箱格式'))
    }
  }, 100)
};
export default {
  name: "Login",
  data() {
    return {
      dl_form: {
        name: '',
        email: '',
        passwd: ''
      },
      rules: {
        name: [{
          required: true, message: "请输入账号名", trigger: 'blur'
        },
          {
            min: 3, message: "账号密码长度至少为3个字符", trigger: 'blur'
          }
        ],
        email: [{
          validator: checkEmail, trigger: 'blur'
        }],
        passwd: [{
          required: true, message: "请输入账号密码", trigger: 'blur'
        },
          {
            min: 3, message: "账号密码长度至少为3个字符", trigger: 'blur'
          }]
      }
    }
  },
  methods: {
    click_zc() {
      const this_url = this.$route.path
      if (this_url === '/login') {
        this.$router.push('/register')
      }
    },
    click_forget() {
      this.$router.push('/forget')
    },
    do_login() {
      let _data;
      this.$refs['dl_form'].validate((valid) => {
        if (valid) {
          this.$axios.get('/login', {
            params: this.dl_form
          }).then(res => {
            _data = res.data;
            console.log(_data);
            let code = _data['code'];
            switch (code) {
              case "500":
                this.$message.error(_data['msg']);
                break;
              case "501":
                this.$message.error("登录账号密码错误，请重新检查输入");
                break;
              case "502":
                this.$message.error(_data['msg']);
                break;
              case "400":
                this.$message.error("登录账号不存在，请检查登录信息");
                break;
              default:
                window.sessionStorage.setItem('avatar', _data['data']['avatar']);
                window.sessionStorage.setItem('id', _data['data']['id']);
                window.sessionStorage.setItem('email', _data['data']['email']);
                window.sessionStorage.setItem('name', _data['data']['name']);
                window.sessionStorage.setItem('time', _data['data']['time']);
                window.sessionStorage.setItem('isLogin', "1");
                this.$router.push("/home");
                location.reload()
                this.$notify.success({
                  title: "PicSmart",
                  message: "欢迎登录使用"
                });
            }
          })
        } else {
          this.$message.error("请检查登录信息")
        }
      })
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

.login_area {
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
  margin: 0 0 10px 0;
}

.tittle p {
  width: max-content;
  padding: 1px;
  margin: auto;
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
