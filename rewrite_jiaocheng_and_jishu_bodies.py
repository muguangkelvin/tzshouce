import os

jiaocheng_bodies = {
    "jiaocheng-article-1.md": """---
title: "Clash for Windows 零基础下载、安装与订阅导入图文步骤"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "手把手教你在电脑端下载官方 Clash 客户端，复制机场订阅链接完成连通，开启规则代理模式。包含灵动云与飞猫云订阅快捷导入演示。"
summary: "手把手教你在电脑端下载官方 Clash 客户端，复制机场订阅链接完成连通，开启规则代理模式。包含灵动云与飞猫云订阅快捷导入演示。"
keywords: ["Clash for Windows", "Clash下载", "订阅导入", "客户端教程", "灵动云"]
---

# Clash for Windows 零基础下载、安装与订阅导入图文步骤

Clash for Windows 是桌面端最受欢迎的图形化代理客户端之一。本文针对零基础新手，提供一步一图的下载安装、订阅配置与规则切换使用流程。

---

## 1. 下载官方安全客户端安装包

首先在 GitHub 官方 Repository 或可信第三方加速源下载 Clash for Windows 0.20.39 最新安装包。避免在百度搜索广告下载篡改版本。

---

## 2. 复制机场订阅链接并导入 Clash

1. 登录机场后台（如 **灵动云** 或 **飞猫云**）。
2. 在仪表盘页面点击 **【快捷导入】**，选择 `一键导入 Clash`；或者点击 **【复制 Clash 订阅链接】**。
3. 打开 Clash for Windows 客户端，点击左侧菜单栏的 **`Profiles` (配置)** 选项。
4. 在上方输入框粘贴复制的订阅 URL，点击右侧的 **`Download`** 按钮。下载成功后选中该配置文件。

---

## 3. 开启 System Proxy 系统代理与 Rule 分流模式

1. 点击左侧 **`Proxies` (代理)** 页面，选择顶部的 **`Rule` (规则模式)**。
2. 展开节点列表，点击选择延迟最低的专线节点（如 `灵动云 香港 IPLC`）。
3. 点击左侧 **`General` (基础设置)** 页面，将 **`System Proxy`** 开关调整为绿色开启状态。
4. 此时打开浏览器访问 Google 或 YouTube 即可顺畅连接。

---

## 4. 推荐搭配机场与专属优惠

- 🥇 **灵动云**：全节点 IPLC 专线，支持 Clash 一键同步导入（优惠码：`ld88` 享 8 折）。<a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener">前往灵动云官网 →</a>
- 🥉 **飞猫云**：折合 ¥7/月起，支持内置客户端与 Clash 格式通用转换（优惠码：`flycat888`）。<a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener">前往飞猫云官网 →</a>
""",

    "jiaocheng-article-2.md": """---
title: "Shadowrocket (小火箭) iPhone / iPad 扫码与一键导入节点指南"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "针对 iOS 苹果手机用户，提供免美区 ID 选购、机场后台一键添加订阅及节点测试图文解说。轻松匹配暮光网络与微风网络专线节点。"
summary: "针对 iOS 苹果手机用户，提供免美区 ID 选购、机场后台一键添加订阅及节点测试图文解说。轻松匹配暮光网络与微风网络专线节点。"
keywords: ["Shadowrocket", "小火箭教程", "iOS代理", "美区ID", "暮光网络"]
---

# Shadowrocket (小火箭) iPhone / iPad 扫码与一键导入节点指南

iPhone 和 iPad 用户使用 Shadowrocket（小火箭）可以获得最流畅的代理体验。本文从获取美区 Apple ID 开始，完整演示扫码配置与自动分流设置。

---

## 1. 准备工作：获取美区 Apple ID 与正版 Shadowrocket

由于 iOS 政策限制，小火箭未在国区 App Store 上架。
1. 在电脑端或手机 Safari 中登录发卡的免美区 ID。
2. 打开手机 App Store，点击右上角头像滑动到最下方退出原账号，登录美区 ID。
3. 搜索 **Shadowrocket**，确认图标为白色小火箭背景，点击下载。安装完成后立即退出共享 ID。

---

## 2. 小火箭三种快捷节点导入方式

- **方式 A (扫码导入)**：打开小火箭，点击右上角 `+` 号，类型选择 `Subscribe`，点击扫描框扫描机场后台二维码。
- **方式 B (一键唤醒)**：在 Safari 打开 **暮光网络** 后台，点击 `一键导入 Shadowrocket` 自动跳转完成。
- **方式 C (剪贴板复制)**：复制订阅链接后打开小火箭，软件会自动识别剪贴板并弹窗提示添加。

---

## 3. 路由设置与连通测试

1. 将主界面的 **`全局路由`** 切换为 **`配置` (Config)** 模式。
2. 点击连通性测试 (Ping Test)，挑选延迟在 100ms 左右的优质节点（如 **暮光网络 8折码: mm88**）。
3. 开启顶部连接开关，首次使用需在弹出的系统对话框中输入锁屏密码允许安装 VPN Profile。
""",

    "jiaocheng-article-3.md": """---
title: "Sing-box 新一代代理协议配置与通用订阅转换教程"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "解析 Sing-box 客户端在 Hysteria2 及 Shadowsocks 协议下的高效配置方法与转换工具使用。搭配飞猫云与飞V 机场打造低延迟体验。"
summary: "解析 Sing-box 客户端在 Hysteria2 及 Shadowsocks 协议下的高效配置方法与转换工具使用。搭配飞猫云与飞V 机场打造低延迟体验。"
keywords: ["Sing-box", "Hysteria2", "订阅转换", "跨平台代理", "飞猫云"]
---

# Sing-box 新一代代理协议配置与通用订阅转换教程

Sing-box 作为跨平台的新一代通用代理核心，凭借对 Hysteria2 与 TUIC 协议的超凡支持受到广泛关注。本文指导你完成 Sing-box 配置与转换。

---

## 1. Sing-box 客户端下载与核心架构

Sing-box 拥有全平台客户端（Windows / macOS / iOS / Android）。其配置采用标准 JSON 格式，具备资源占用极低、握手极快的优势。

---

## 2. 在线订阅转换生成 Sing-box 配置

若你的机场服务商（如 **飞猫云** 或 **飞V**）尚未提供原生 Sing-box 订阅，可借助在线 Subconverter 工具完成格式转换：

1. 复制机场提供的通用 SS 或 Clash 订阅链接。
2. 打开转换工具，选择客户端目标为 **`Sing-box`**。
3. 生成并复制专用的 `sing-box://` 订阅地址导入客户端。

---

## 3. 极速节点匹配与体验推荐

- 🥉 **飞猫云**：支持通用协议转换，年付折合仅 7 元/月，极速低延迟。（优惠码：`flycat888`）
- ✈️ **飞V**：针对 Hysteria2 协议有良好优化，多端秒连。（优惠码：`flyv888`）
"""
}

dir_jiaocheng = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jiaocheng"

for filename, full_md in jiaocheng_bodies.items():
    filepath = os.path.join(dir_jiaocheng, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_md.strip())

print("Updated jiaocheng articles with 100% unique markdown bodies!")
