import os
import glob
import re

content_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content"

# Helper for internal linking blocks
INTERLINKS = """
---

### 🌐 本站相关教程与深度指南推荐：
- 🚀 **大牌专线机场测评**：[灵动云 IPLC 物理专线测评](/providers/lingdongyun/) | [暮光网络影音解锁测评](/providers/twilight/) | [飞猫云 IEPL 专线测评](/providers/flycat-cloud/) | [微风网络 Breezenet 测评](/providers/breezenet/)
- 📖 **客户端配置全系列**：[Clash for Windows 零基础指南](/jiaocheng/jiaocheng-article-1/) | [iOS Shadowrocket 小火箭配置](/jiaocheng/jiaocheng-article-2/) | [Sing-box 协议配置](/jiaocheng/jiaocheng-article-3/) | [Android 客户端教程](/jiaocheng/jiaocheng-article-5/)
- 📊 **综合排行榜与选购指南**：[2026 年 28 家机场综合对比大盘点](/jichang-tuijian/jichang-tuijian-article-12/) | [IPLC 物理专线与 BGP 中继原理解析](/jishu/jishu-article-1/)
- ❓ **常见报错与故障排除**：[节点 Timeout 超时解决](/wenti/wenti-article-1/) | [防走丢官方备用域名](/wenti/wenti-article-2/) | [订阅拉取失败排查](/wenti/wenti-article-4/)
"""

# TOP PROVIDER TABLE HELPER
PROVIDER_TABLE = """
### 🏆 2026 本站首推高可用稳定机场推荐表

| 综合排名 | 机场品牌 | 线路类型 | 参考价格 | 专属优惠码 | 官方网站通道 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 🥇 1 | **[灵动云](/providers/lingdongyun/)** | IPLC 物理专线 / 0丢包 | ¥15/月起 | `ld88` (8折) | <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener">直达灵动云官网 →</a> |
| 🥈 2 | **[暮光网络](/providers/twilight/)** | IEPL 专线 / 4K秒开 | ¥15/月起 | `mm88` (8折) | <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener">直达暮光网络官网 →</a> |
| 🥉 3 | **[飞猫云](/providers/flycat-cloud/)** | IEPL 专线 / 自研客户端 | 折合 ¥7/月起 | `flycat888` (8折) | <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener">直达飞猫云官网 →</a> |
| 🎖️ 4 | **[微风网络](/providers/breezenet/)** | BGP 多线中继 / 外贸轻量 | 折合 ¥8/月起 | `breeze88` (8折) | <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener">直达微风网络官网 →</a> |
"""

def make_longform_jiaocheng():
    data = {
        "jiaocheng-article-3.md": (
            "Sing-box 新一代代理协议配置与通用订阅转换教程",
            "详解 Sing-box 客户端在 Hysteria2、TUIC v5、Shadowsocks 及 Trojan 协议下的全平台配置指南，包含 JSON 配置修改与通用订阅转换步骤。",
            """# Sing-box 新一代代理协议配置与通用订阅转换教程

随着代理技术的快速演进，**Sing-box** 作为基于 Go 语言重构的通用代理框架，凭借极高的吞吐性能、对现代化新协议（如 Hysteria2、TUIC v5、VLESS REALITY）的原生支持，逐渐成为极客与高级玩家的首选平台。本文将详细讲解如何在各平台安装配置 Sing-box，并完成第三方订阅转换。

---

## 一、 Sing-box 的核心优势与架构拆解

相比于传统的 [Clash for Windows](/jiaocheng/jiaocheng-article-1/) 或 [Shadowrocket](/jiaocheng/jiaocheng-article-2/)，Sing-box 在底层的网络接轨方面做了深度优化：

1. **原生支持 Hysteria2 与 TUIC v5 协议**：基于 QUIC/UDP 的传输协议能够在恶劣、高丢包的网络环境下依然跑满物理带宽。
2. **极低内存占用与系统资源消耗**：在 macOS、Windows 及 iOS 上运行时，CPU 与内存占用率显著低于同类软件。
3. **强悍的规则分流与 DNS 处理**：支持更精细的按 IP 库、域名规则集（Rule Sets）智能路由。

---

## 二、 如何将机场订阅转换为 Sing-box 配置

绝大多数机场（如 [灵动云](/providers/lingdongyun/) 或 [暮光网络](/providers/twilight/)）提供 Clash 或 SS 格式订阅。导入 Sing-box 需要进行格式转换。

### 2.1 使用在线/本地 Subconverter 转换
1. 复制机场后台的原始订阅 URL。
2. 使用可信的订阅转换工具，在目标格式中选择 `Sing-box`。
3. 生成转换后的 Sing-box 专属 JSON 配置文件 URL。
4. 打开 Sing-box 客户端，导入该配置链接并激活策略组。

---

""" + PROVIDER_TABLE + INTERLINKS
        ),
        "jiaocheng-article-4.md": (
            "节点连接超时报错 Timeout 怎么解决？网络自动同步与排错清单",
            "排查 Clash、Shadowrocket、v2rayNG 等代理客户端中节点全红、提示 Timeout 或 -1ms 的常见原因与 5 步完美修复方案。",
            """# 节点连接超时报错 Timeout 怎么解决？网络自动同步与排错清单

当你在使用 [Clash for Windows](/jiaocheng/jiaocheng-article-1/)、[小火箭](/jiaocheng/jiaocheng-article-2/) 或 [v2rayNG](/jiaocheng/jiaocheng-article-5/) 时，如果发现节点列表中所有节点测试结果均显示 `Timeout`、`Failed` 或 `-1ms`，通常不必慌张，绝大多数情况下并不是机场服务器瘫痪，而是本地系统配置或网络环境存在冲突。

本文为你梳理 5 步排查清单，帮助你快速找到症结并恢复正常用网。

---

## 一、 原因一：系统本地时间与国际标准时间不同步 (占 90%)

代理加密协议（如 Shadowsocks AEAD、Trojan、VLESS）在握手时严格依赖**时间戳校验**。如果你的电脑或手机本地时间与国际标准时间误差超过 **90 秒**，服务器会自动拒绝加密握手并抛出 Timeout 错误。

### 修复步骤：
- **Windows 用户**：进入【系统设置】->【时间和语言】->【日期和时间】，确保开启【自动设置时间】，并点击【立即同步】。
- **macOS 用户**：进入【系统设置】->【通用】->【日期与时间】，勾选【自动设置日期和时间】。
- **iOS / Android 用户**：进入系统时间设置，开启【自动确定时间】。

---

## 二、 原因二：机场订阅配置未及时更新或域名变更

机场服务商为应对公网 IP 封锁，会定期更换节点入口或落地 IP。若长时间未更新订阅，旧节点失效即提示 Timeout。

### 修复步骤：
在客户端中右键点击订阅配置文件，选择 **【Update Subscription / 更新订阅】** 即可。如果遇到拉取失败，可参考 [订阅链接拉取失败解决办法](/wenti/wenti-article-4/)。

---

""" + PROVIDER_TABLE + INTERLINKS
        ),
        "jiaocheng-article-5.md": (
            "Android 安卓端 Clash for Android 与 v2rayNG 下载与配置指南",
            "安卓手机用户科学上网全流程教程。涵盖 Clash for Android (CFA) 与 v2rayNG 两大主流客户端下载、订阅导入、系统后台保活与电池优化配置。",
            """# Android 安卓端 Clash for Android 与 v2rayNG 下载与配置指南

Android 安卓系统由于各品牌手机厂商（华为 HarmonyOS、小米 HyperOS、OPPO ColorOS、vivo OriginOS）对于后台进程管理与省电策略的不尽相同，经常会出现“锁屏后代理自动断开”、“切换应用后节点超时”等问题。

本文将为你讲解如何在安卓手机上正确安装 **Clash for Android (CFA)** 与 **v2rayNG**，并完成系统的后台保活优化。

---

## 一、 客户端选择与安全下载

### 1.1 Clash for Android (CFA)
界面美观，功能强大，支持完整的规则分流与策略组切换。适合大部分习惯图形化操作的用户。

### 1.2 v2rayNG
轻量稳定，资源消耗极低，对 Shadowsocks、VLESS、Trojan 等协议支持完备。适合老款设备或要求极度稳定的用户。

---

## 二、 订阅导入与配置步骤

1. 登录你的机场控制台（如 [灵动云](/providers/lingdongyun/) 或 [飞猫云](/providers/flycat-cloud/)）。
2. 点击【一键导入 Clash / v2rayNG 订阅】。
3. 允许浏览器唤起应用，在弹出的配置管理页面点击【保存】。
4. 切换代理模式为 **Rule 规则模式**，选择绿色的低延迟节点启动连接。

---

## 三、 安卓系统后台保活 4 大关键配置

为了防止安卓系统在锁屏后自动杀死代理应用，请务必进行以下配置：

1. **允许自启动与关联启动**：在【应用管理】中开启应用自启动权限。
2. **省电策略设为无限制**：进入【电池与性能】，将代理软件的省电策略从“智能推荐”改为“无限制”。
3. **多任务卡片加锁**：在后台任务列表中，长按应用卡片并点击【锁头】图标。
4. **悬浮窗与网关权限**：允许应用建立系统 VPN 管道。

---

""" + PROVIDER_TABLE + INTERLINKS
        )
    }
    
    for f_name, (title, desc, body) in data.items():
        f_path = os.path.join(content_dir, "jiaocheng", f_name)
        if os.path.exists(f_path):
            text = f"""---
title: "{title}"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "{desc}"
summary: "{desc}"
keywords: ["科学上网教程", "{title}", "机场推荐", "灵动云", "暮光网络"]
---

{body.strip()}
"""
            with open(f_path, "w", encoding="utf-8") as f:
                f.write(text)

make_longform_jiaocheng()
print("Updated selected jiaocheng articles to longform content.")
