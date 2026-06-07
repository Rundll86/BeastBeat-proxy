# Patreon Proxy

> Readme written by GPT-4o

## 概述

`patreon-proxy` 是一个针对 Windows 环境的本地 HTTPS 代理/服务，模拟 Patreon OAuth2 登录流程并返回伪造的认证数据。该项目主要用于绕过 Patreon 登录验证，以便让 **依赖Patreon登录验证的** 游戏/应用在不进行真实 Patreon 授权的情况下获取“已登录”状态。

## 主要功能

- 修改 Windows `hosts` 文件，将 `www.patreon.com` 重定向到本机
- 安装本地自签名证书到当前用户的受信任根证书存储
- 启动 Flask HTTPS 服务器，监听来自 `www.patreon.com` 的 OAuth2 请求
- 返回固定的伪造 `access_token`、`refresh_token` 以及当前用户信息

## 目录结构

- `index.py`：程序入口，依次初始化 hosts、证书和服务器
- `engine/hosts.py`：修改 `C:/Windows/System32/drivers/etc/hosts`，添加指向本机的 `www.patreon.com` 记录
- `engine/certificate.py`：使用 Windows `certutil` 将 `cert.pem` 安装到当前用户的 `ROOT` 证书存储区
- `engine/server.py`：使用 Flask 启动 HTTPS 服务，并处理 Patreon OAuth2 相关接口
- `engine/config.py`：配置代理端口和目标域名
- `engine/constants.py`：返回模拟 OAuth2 数据与用户信息
- `engine/dir.py`：辅助函数，用于定位程序基础目录中的证书文件
- `cert.pem` / `key.pem`：本地 HTTPS 证书与私钥，用于 Flask 服务器的 SSL

## 工作原理

1. `index.py` 运行时调用：
   - `hosts.setup()`：清理并添加 `www.patreon.com` 到本地 hosts，指向 `127.0.0.1`
   - `certificate.setup()`：通过 `certutil` 将项目目录中的 `cert.pem` 安装到当前用户的受信任根证书
   - `server.start()`：启动 HTTPS Flask 服务，监听 `0.0.0.0:443`

2. 当 **依赖Patreon登录验证的** 客户端访问 `https://www.patreon.com/oauth2/authorize` 时，服务器会：
   - 模拟授权回调，向客户端指定的 `redirect_uri` 返回一个固定 `code`

3. 当客户端请求 `https://www.patreon.com/api/oauth2/token` 时，服务器返回固定的访问令牌响应。

4. 当客户端请求 `https://www.patreon.com/api/oauth2/api/current_user` 时，服务器返回固定的用户数据对象。

## 关键接口

- `GET /oauth2/authorize`
  - 直接调用 `redirect_uri` 并返回一个固定授权码
- `POST /api/oauth2/token`
  - 返回固定的 token JSON：`access_token`、`refresh_token`、`token_type`、`expires_in`
- `GET /api/oauth2/api/current_user`
  - 返回伪造的当前用户信息，包含 Patreon 用户、赞助者、奖励、活动等数据

## 依赖

- Python 3.x
- Flask
- requests
- pyinstaller（仅用于打包）

安装依赖：

```bash
pip install -r requirements.txt
```

## 运行方式

以管理员身份运行 Python 脚本，确保能够写入 `hosts` 文件并执行 `certutil`：

```bash
python index.py
```

## 注意事项

- 该项目会直接修改 Windows hosts 文件，请谨慎使用。
- 需要本地管理员权限/当前用户权限以写入 `C:/Windows/System32/drivers/etc/hosts`。
- 该程序会在 `443` 端口上启动 HTTPS 服务，请确保没有其他服务占用该端口。
- `certutil` 命令仅适用于 Windows 系统。

## 使用场景

适用于需要绕过 Patreon OAuth2 验证、并在本地模拟 Patreon 登录状态的场景。通常与 **依赖Patreon登录验证的** 游戏/应用配合使用，通过伪造 Patreon 授权数据实现自动登录。

## 免责声明

该项目会伪造 OAuth2 和用户信息，仅用于测试或特定兼容性场景。请勿用于未经授权的访问或绕过合法认证流程。
