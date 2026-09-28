import os
import glob
import re

content_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content"
wenti_files = glob.glob(os.path.join(content_dir, "wenti", "faq-*.md"))
print(f"Total faq files in wenti: {len(wenti_files)}")

# Map for wenti-article-6 to 10
wenti_extra_updates = {
    "wenti-article-6.md": {
        "title": "代理节点连通却无法上网？注册表与 DNS 修复步骤",
        "desc": "解决开启 Clash 或 V2Ray 后节点正常 Ping 通但浏览器打不开网页的常见问题。",
        "body": """# 代理节点连通却无法上网？注册表与 DNS 修复步骤

在日常使用代理软件时，有时会遇到节点在客户端内延迟显示正常（如 50ms），但打开浏览器却提示“无法连接网络”或“DNS_PROBE_FINISHED_NXDOMAIN”。

---

## 1. 原因一：系统代理注册表残留 (占 70%)

在非正常关机或强制结束 Clash 进程时，Windows 系统代理设置未被正确清除。

### 修复步骤：
1. 打开 Windows 设置 -> 【网络和 Internet】 -> 【代理】。
2. 确认【手动设置代理】中的【使用代理服务器】开关已关闭。
3. 或在 Clash 控制台重新勾选并取消勾选【System Proxy】开关。

---

## 2. 原因二：DNS 污染与 DNS 劫持

某些运营商 DNS 会强制拦截代理端口的 DNS 解析请求。推荐在客户端中启用 **DoH (DNS over HTTPS)** 加密解析，或使用 `1.1.1.1` 作为主 DNS。
"""
    },
    "wenti-article-7.md": {
        "title": "节点延迟过高与丢包率测试：IPLC 与 BGP 中继对比",
        "desc": "教你使用 Ping / Speedtest / MTR 工具检测机场节点的真实物理延迟与晚高峰丢包表现。",
        "body": """# 节点延迟过高与丢包率测试：IPLC 与 BGP 中继对比

许多新手看节点延迟时只注意软件里显示的毫秒数，实际上软件内测得的数值仅是本地到入口服务器的 HTTP 延迟，并不代表节点实际过境速度。

---

## 1. 真实物理延迟计算与原理

- **IPLC 物理专线**：深港/沪日内网光纤专线，物理延迟固定。例如深圳到香港通常在 3-8ms，极速稳定。
- **BGP 公网中继**：受国际出口骨干网波动影响，晚高峰时期容易产生 10% - 30% 的高丢包。

---

## 2. 如何使用 MTR 工具测试真实链路

使用 `mtr` (Linux/macOS) 或 `BestTrace` (Windows) 可以清晰追踪节点路由跳转，查看数据包是在国内入口还是海外出口丢包。选购机场时首推 **灵动云** 或 **暮光网络** 等高配专线服务商。
"""
    },
    "wenti-article-8.md": {
        "title": "多设备同时在线冲突与机场连接数限制规则说明",
        "desc": "讲解机场订阅中公共设备限制、IP 数量封禁机制及软路由分发配置技巧。",
        "body": """# 多设备同时在线冲突与机场连接数限制规则说明

在购买机场套餐时，通常会看到“限制 3 台设备”或“不限制设备数量”的说明。本文为你梳理设备连接数限制规则。

---

## 1. 机场是如何判定“设备在线数量”的？

机场后端节点根据同一时间连接至节点的 **公网 IP 数量** 或 **客户端并发连接数** 进行计算：

1. **同局域网下多设备（算 1 个 IP）**：家中手机、iPad 和电脑连接同一个路由器代理，在后端只占用 1 个连接位。
2. **异地不同网络（算多个 IP）**：你在家上网，朋友在公司使用同一个订阅，此时占用 2 个不同 IP 授权。

---

## 2. 软路由 (OpenWrt) 局域网分发

如果家中设备较多，推荐将订阅配置在软路由 (PassWall / OpenWrt) 上，整个局域网共享同一个代理连接，既不超标又省心。
"""
    },
    "wenti-article-9.md": {
        "title": "安卓/iOS 手机后台杀进程导致断网的保活设置",
        "desc": "详细教程：指导在小米 MIUI、华为 HarmonyOS、vivo/oppo 及 iOS 上配置代理应用后台白名单。",
        "body": """# 安卓/iOS 手机后台杀进程导致断网的保活设置

在智能手机锁屏或切换应用后，常常发现后台 Clash for Android 或 Shadowrocket 被系统彻底清杀，导致断网或频繁重连。

---

## 1. 安卓 (Android) 系统保活 4 大设置

1. **允许自启动**：在【应用权限】中将 Clash / v2rayNG 开启【自启动】与【关联启动】。
2. **省电策略设为无限制**：进入【电池与性能】 -> 【应用省电策略】，选为【无限制】。
3. **多任务卡片加锁**：在后台任务列表中，长按应用卡片并点击【小锁】图标。
4. **忽略电池优化**：允许应用在后台高能耗运行。

---

## 2. iOS (iPhone / iPad) 保活技巧

iOS 系统机制相对严格，开启 Shadowrocket 或 Quantumult X 后，尽量不要在后台彻底划掉 App，让系统 VPN 进程驻留即可。
"""
    },
    "wenti-article-10.md": {
        "title": "如何配置客户端自动更新订阅与智能策略分流",
        "desc": "教你在 Clash Verge / Stash / Surge 中设置 24 小时自动更新订阅及域名规则分流。",
        "body": """# 如何配置客户端自动更新订阅与智能策略分流

保持订阅更新是确保机场节点始终可用的关键。手写配置太麻烦？教你设置全自动更新与规则分流。

---

## 1. 设置客户端定时自动更新

在 **Clash Verge Rev** 中：
1. 点击左侧【订阅 / Profiles】菜单。
2. 右键目标订阅，选择【编辑 / Edit】。
3. 设置【更新间隔 / Update Interval】为 `1440` 分钟（即 24 小时）。
4. 勾选【静默更新】。

---

## 2. 智能策略分流配置 (Rule Mode)

务必确认代理模式选择为 `Rule 规则模式`：
- **Domestic / Direct**：国内微信、淘宝、百度流量直连，不耗机场流量。
- **Global / Proxy**：Google、YouTube、ChatGPT 走节点加速。
- **Reject**：自动拦截广告与追踪脚本。
"""
    }
}

for f_name, data in wenti_extra_updates.items():
    f_path = os.path.join(content_dir, "wenti", f_name)
    if os.path.exists(f_path):
        full_text = f"""---
title: "{data['title']}"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "{data['desc']}"
summary: "{data['desc']}"
keywords: ["科学上网", "排错指南", "Clash配置", "灵动云", "暮光网络"]
---

{data['body'].strip()}
"""
        with open(f_path, "w", encoding="utf-8") as f:
            f.write(full_text)

print("Updated wenti-article-6 to 10.")
