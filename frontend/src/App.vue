<template>
  <div id="app">
    <div class="head">
      <el-row  :gutter="20">
        <el-col :span="6">
          <div class="logo" @click="toHome">
            <img src="../src/assets/logo.png" alt="" width="32" @click="toHome" style="cursor: pointer;"/>
            <span style="font-family: Constantia,math;font-size: xx-large;color: whitesmoke;cursor: pointer;" @click="toHome">PicSmart</span>
          </div>
        </el-col>
        <el-col :span="3"><div class="blank"></div></el-col>
        <el-col :span="6">
          <div class="menu" v-if="isDone">
            <div class="menu-content">
              <el-menu mode="horizontal" :default-active="activeIndex[0]" background-color="#8cc5ff" text-color="whitesmoke" active-text-color="black" ellipsis router>
              <el-menu-item index="/home">
                <template>
                  <span style="font-family: 楷体, serif, bolder;font-size: x-large;">
                    图片压缩
                  </span>
                </template>
              </el-menu-item>
              <el-menu-item index="/home-image">
                <template>
                  <span style="font-family: 楷体, serif, bolder;font-size: x-large;">
                    图片转换
                  </span>
                </template>
              </el-menu-item>
            </el-menu>
            </div>
          </div>
          <div class="menu" v-else></div>
        </el-col>
        <el-col :span="3"><div class="blank"></div></el-col>
        <el-col :span="6">
          <div class="manage">
            <div class="manage-content">
              <div v-if="!isLogin">
                <div class="login-box">
                  <el-button type="text" class="login-button" @click="toLogin">
                    <template>
                      <span style="font-family: 楷体, serif;font-size: x-large;color: #e1f3d8;">登录</span>
                    </template>
                  </el-button>
                   <el-divider direction="vertical"></el-divider>
                  <el-button type="text" @click="toRegister">
                    <template>
                      <span style="font-family: 楷体, serif;font-size: x-large;color: #e1f3d8;">注册</span>
                    </template>
                  </el-button>
                </div>
              </div>
              <div v-else>
                <div class="dropdown">
                  <el-dropdown>
                    <template>
                      <el-avatar :src="src" :size="60"></el-avatar>
                    </template>
                    <el-dropdown-menu>
                      <el-dropdown-item icon="el-icon-user" @click="toInfo">
                        <template>
                          <span style="font-family: 楷体, serif;font-size: medium"@click="toInfo">我的账号</span>
                        </template>
                      </el-dropdown-item>
                      <el-dropdown-item icon="el-icon-warning-outline" @click="toAbout">
                        <template>
                          <span style="font-family: 楷体, serif;font-size: medium" @click="toAbout">关于我们</span>
                        </template>
                      </el-dropdown-item>
                      <el-dropdown-item icon="el-icon-switch-button" @click="out_login">
                        <template>
                          <span style="font-family: 楷体, serif;font-size: medium" @click="out_login">退出登录</span>
                        </template>
                      </el-dropdown-item>
                    </el-dropdown-menu>
                  </el-dropdown>
                </div>
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      activeIndex: ['/home', '/home-image'],
      isLogin: false,
      isDone: true,
      src: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
    }
  },
  mounted() {
    console.log("mounted");
    if (window.sessionStorage.getItem("isLogin") === "1") {
      this.isLogin = true
    }
  },
  methods: {
    toHome() {
      this.$router.push("/home")
    },
    toLogin() {
      this.$router.push("/login")
    },
    toRegister() {
      this.$router.push("/register")
    },
    out_login() {
      window.sessionStorage.clear();
      location.reload()
    },
    toAbout() {
      this.$router.push("/about")
    },
    toInfo() {
      this.$router.push("/info")
    }
  }
}
</script>

<style>
html,body{
  width: 100%;
  height: 100%;
  margin: 0;
  overflow: hidden;
}
#app {
  width: 100%;
  padding: 0;
  margin: 0;
}
.head {
  max-width: 100%;
  min-width: 1550px;
  padding: 0;
  max-height: 80px;
  min-height: 70px;
  background-color: #8cc5ff;
}
.logo {
  height: 35px;
  width: 44%;
  padding: 1px;
  margin: 12px auto;
}
.blank {
  max-height: 75px;
  min-height: 65px;
  padding: 1px;
}
.menu {
  max-height: 80px;
  min-height: 70px;
  padding: 0;
  margin: 0;
}
.menu-content {
  max-height: 80px;
  min-height: 70px;
  padding: 0;
  margin: 0;
}
.el-menu--horizontal {
  max-height: 80px;
  min-height: 70px;
}
.el-menu--horizontal>.el-menu-item {
  max-height: 80px;
  min-height: 70px;
}
.el-menu.el-menu--horizontal {
  border-bottom: 0;
}
.manage {
  max-height: 80px;
  min-height: 70px;
}
.manage-content {
  max-height: 80px;
  min-height: 70px;
}
.login-box {
  max-height: 80px;
  min-height: 70px;
  float: right;
  margin-right: 50px;
}
.el-button--text {
  max-height: 80px;
  min-height: 70px;
}
.el-divider--vertical {
  width: 2px;
  height: 3em;
}
.dropdown {
  max-height: 80px;
  min-height: 70px;
  margin-right: 70px;
  float: right;
}
.el-dropdown {
  max-height: 80px;
  min-height: 70px;
  cursor: pointer;
}
.el-avatar--circle {
  margin-top: 5px;
  margin-left: 5px;
}
</style>
