<h1 align="center">
  青年大学习
  <br>
  Author: chiupam
</h1>

# 简介
适用于 `昆医大` 的青年大学习自动学习, 不需要每周手动学习.
# 目录
- [简介](#简介)
- [目录](#目录)
- [功能](#功能)
- [使用方式](#使用方式)
  - [Surge（推荐）](#Surge推荐)
    - [1.打开Surge订阅模块](#1打开Surge订阅模块)
    - [2.获取cookie](#2获取cookie)
  - [腾讯云函数（推荐）](#腾讯云函数推荐)
    - [1.Fork本项目](#1fork本项目)
    - [2.准备需要的参数](#2准备需要的参数)
    - [3.将参数填到Secrets](#3将参数填到secrets)
    - [4.部署](#4部署)
  - [docker](#docker)
    - [1.创建好所需文件](#1创建好所需文件)
    - [2.编辑cookie](#2编辑cookie)
    - [3.部署容器](#3部署容器)
  - [使用Actions（被禁用）](#使用Actions被禁用)
    - [解释及声明](#解释及声明)
- [通知推送方式](#通知推送方式)
- [同步上游代码](#同步上游代码)
  - [使用GtiHubActions](#使用GtiHubActions)
    - [1.申请token](#1申请token)
    - [2.将参数填到Secrets](#2将参数填到Secrets)
  - [使用pull应用](#使用pull应用)
- [申明](#申明)
- [参考项目](#参考项目)
# 功能
- [x] 每天 `15` 点进行最新一期 `青年大学习` 的学习
- [x] 每天签到获取积分
# 使用方式
## Surge（推荐）
### 1.打开Surge订阅模块
```text
https://raw.githubusercontent.com/chiupam/QNDXX/master/surge/qndxx.sgmodule
```
### 2.获取cookie
```text
打开微信 => 点击通讯录 => 点击公众号 => 搜索云南共青团 => 
点击右下角大学习 => 点击注册团员登录学习 => 点击我的 => 点击签到 => 
【成功】写入 cookie 成功！🎉
```
> 请留意！请留意！请留意！
>> 此脚本只有在`cookie`失效时才会发送运行通知！
## 腾讯云函数（推荐）
### 1.Fork本项目
项目地址：[chiupam/QNDXX](https://github.com/chiupam/QNDXX)
### 2.准备需要的参数
- 为了确保权限足够, 获取以下这两个参数时不要使用子账户! 而且, 腾讯云账户需要 [实名认证](https://console.cloud.tencent.com/developer/auth) !
- 开通云函数 `SCF` 的腾讯云账号，在 [访问秘钥页面](https://console.cloud.tencent.com/cam/capi) 获取账号的 `SecretID`，`SecretKey`
- 依次登录 [SCF 云函数控制台](https://console.cloud.tencent.com/scf) 和 [SLS 控制台](https://console.cloud.tencent.com/sls) 开通相关服务，确保您已开通服务并创建相应 [服务角色](https://console.cloud.tencent.com/cam/role) **SCF_QcsRole、SLS_QcsRole**
- 开启抓包软件, 在`微信` 中打开 `云南共青团` 公共号的大学习页面, 把 `header` 中的 `Cookie` 值保存下来.
> 正确的cookie值应具备以下格式
>> `ASP.NET_SessionId=xxx; DianCMSUser=UserId=xxx&UserName=xxx&PassWord=xxx&NickName=xxx&Session=xxx; DianCMS_qndxx_71=1; DianCMS_qndxx_70=1; DianCMS_qndxx_69=1`
### 3.将参数填到Secrets
`Name`和`Value`格式如下：

| Name | Value |
|:---:|:---:|
|TENCENT_SECRET_ID | 腾讯云用户 SecretID|
|TENCENT_SECRET_KEY | 腾讯云账户 SecretKey|
|COOKIE | cookie.txt 中内容|
### 4.部署
- 首次 `fork` 可能要去 `Actions` 里面同意使用 `Actions` 条款.
- 添加完上面 `3` 个 `Secrets` 后, 进入 `Actions` --> `Serverless`, 点击右边的 `Run workflow` 即可部署至腾讯云函数
## docker
### 1.创建好所需文件
```shell
cd /root
mkdir qndxx
cd qndxx/
touch cookie.json
```
### 2.编辑cookie
编辑规则参考本仓库中的 [cookie.json](https://github.com/chiupam/QNDXX/blob/master/cookie.json) 即可
### 3.部署容器
```shell
docker run -dit \
  --name qndxx \
  --restart always \
  -v /root/qndxx:/data \
  chiupam/qndxx:latest
```
## 使用Actions（不推荐）
### 解释及声明
使用 GitHub Actions 执行此类任务属于 **滥用谷歌资源** , 因此 **不主动开发** 这种使用方法!
# 同步上游代码
## 使用GtiHubActions
### 1.申请token
- 点击右侧这个链接, [生成新的token](https://github.com/settings/tokens/new)
- 为 `token` 设置名字, 把 `workflow` 勾选上，点击最下方 `Generate token` 即可生成 `token`.
### 2.将参数填到Secrets
`Name` 和` Value` 格式如下：

| Name | Value |
|:---:|:---:|
| PAT | 刚刚申请的 `token` 的值 |

## 使用pull应用
### 安装pull应用
安装 [pull](https://github.com/apps/pull) 应用, 实现自动同步上游代码.
# 申明
1. 此脚本仅用于学习研究, 不保证其合法性, 准确性, 有效性, 请根据情况自行判断, 本人对此不承担任何保证责任.
2. 您必须在下载后 **24** 小时内将所有内容从您的计算机或手机或任何存储设备中完全删除, 若违反规定引起任何事件本人对此均不负责.
3. 请勿将此脚本用于任何商业或非法目的, 若违反规定请自行对此负责.
4. 此脚本涉及应用与本人无关, 本人对因此引起的任何隐私泄漏或其他后果不承担任何责任.
5. 本人对任何脚本引发的问题概不负责, 包括但不限于由脚本错误引起的任何损失和损害.
6. 如果任何单位或个人认为此脚本可能涉嫌侵犯其权利, 应及时通知并提供身份证明，所有权证明, 我将在收到认证文件确认后删除此脚本.
7. 所有直接或间接使用, 查看此脚本的人均应该仔细阅读此声明.
8. 本人保留随时更改或补充此声明的权利, 一旦您使用或复制了此脚本, 即视为您已接受此免责声明.

