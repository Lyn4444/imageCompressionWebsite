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
              <el-form ref="zc_form" :model="zc_form" label-width="90px" label-position="left" :rules="rules">
                <el-form-item label="账号名" prop="name">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">用户名</span>
                  </template>
                  <el-input v-model="zc_form.name" clearable></el-input>
                </el-form-item>
                <el-form-item label="邮箱" prop="email">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">邮箱</span>
                  </template>
                  <el-input v-model="zc_form.email" clearable></el-input>
                </el-form-item>
                <el-form-item prop="num">
                  <template>
                    <el-input v-model="zc_form.num" clearable placeholder="验证码"
                              style="width: 60%;margin-right: 12px;"/>
                    <el-button type="primary" plain @click="get_num">获取验证码</el-button>
                  </template>
                </el-form-item>
                <el-form-item label="密码" prop="passwd">
                  <template #label>
                    <span style="font-family: 楷体,serif;font-size: large;">密码</span>
                  </template>
                  <el-input v-model="zc_form.passwd" show-password clearable></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="passwd1">
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
                  <el-button type="success" round @click="do_register">
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
  name: "Register",
  data() {
    const checkPasswd = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('请输入确认密码'))
      }

      setTimeout(() => {
        if (this.zc_form.passwd === value) {
          callback()
        } else if (value.length < 3) {
          callback(new Error('确认密码长度至少为3个字符'))
        } else {
          callback(new Error('两次输入的密码不相同，请重新输入确认'))
        }
      })
    }
    return {
      zc_form: {
        name: '',
        email: '',
        num: '',
        passwd: '',
        passwd1: ''
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
        num: [{
          required: true, message: "请输入验证码", trigger: 'blur'
        }],
        passwd: [{
          required: true, message: "请输入账号密码", trigger: 'blur'
        },
          {
            min: 3, message: "账号密码长度至少为3个字符", trigger: 'blur'
          }],
        passwd1: [{
          validator: checkPasswd, trigger: 'blur'
        }]
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
    },
    get_num() {
      if (this.zc_form.email) {
        this.$axios.get('/utils/get-email', {
          params: {
            "email": this.zc_form.email
          }
        }).then(res => {
          let e_code;
          e_code = res.data['code'];
          switch (e_code) {
            case "500":
              this.$message.error(res.data['msg']);
              break;
            case "501":
              this.$message.error(res.data['msg']);
              break;
            case "502":
              this.$message.error("验证码已发送，请勿重复请求");
              break;
            case "503":
              this.$message.error(res.data['msg']);
              break;
            case "402":
              this.$message.error("请输入正确的邮箱格式或者联系网站管理员");
              break;
            default:
              this.$message.success("验证码已发送，5分钟内有效");
          }
        })
      } else {
        this.$message.error("请输入正确的邮箱")
      }
    },
    do_register() {
      this.$refs['zc_form'].validate((valid) => {
        if (valid) {
          let tmp_data = new FormData();
          tmp_data.append('code', this.zc_form.num);
          tmp_data.append('email', this.zc_form.email);
          this.$axios.post('/utils/set-email/', tmp_data).then(res => {
            let t_code;
            t_code = res.data['code'];
            if (t_code === "500") {
              this.$message.error(res.data['msg'])
            } else if (t_code === "501") {
              this.$message.error(res.data['msg'])
            } else if (t_code === "503") {
              this.$message.error("输入的邮箱或者邮箱验证码为空")
            } else if (t_code === "400") {
              this.$message.error("验证码已失效，请重新获取邮箱验证码")
            } else if (t_code === "401") {
              this.$message.error("验证码错误，请重新确认后输入")
            } else if (t_code === "200") {
              let register_data = new FormData();
              register_data.append('email', this.zc_form.email);
              register_data.append('name', this.zc_form.name);
              register_data.append('passwd', this.zc_form.passwd);
              this.$axios.post('/register/', register_data).then(res => {
                let r_code;
                r_code = res.data['code'];
                switch (r_code) {
                  case "500":
                    this.$message.error(res.data['msg']);
                    break;
                  case "501":
                    this.$message.error(res.data['msg']);
                    break;
                  case "503":
                    this.$message.error("注册信息不能为空，请确认后重新输入");
                    break;
                  case "401":
                    this.$message.error("注册账号已存在");
                    break;
                  default:
                    this.$notify.info({
                      title: "PicSmart",
                      message: "注册成功，自动登录，欢迎使用"
                    });
                    this.$axios.get('/login', {
                      params: {
                        "name": this.zc_form.name,
                        "email": this.zc_form.email,
                        "passwd": this.zc_form.passwd
                      }
                    }).then(res => {
                      let _data;
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
                }
              })
            } else {
              this.$message.error("未知错误，请联系网站管理员")
            }
          })
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
