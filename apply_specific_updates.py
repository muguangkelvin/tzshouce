import os
import glob
import re

content_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content"

# Map of specific titles and rich unique body content for service & wenti articles
service_updates = {
    "service-article-1.md": {
        "title": "优质机场挑选准则：IPLC 专线与流媒体解锁配置方案",
        "desc": "详细讲解挑选高质量梯子机场的核心维度，包括 IPLC 物理专线架构、全流媒体解锁能力及客服响应速度。",
        "body": """# 优质机场挑选准则：IPLC 专线与流媒体解锁配置方案

选购科学上网机场时，面对市场上琳琅满目的服务商，新手往往容易被“低价无限流量”的夸大宣传所蒙蔽。本文结合多年实测经验，拆解挑选优质机场的核心维度。

---

## 1. 为什么推荐优先选择 IPLC/IEPL 专线？

传统的 VPS 直连或 BGP 公网中继在敏感时期极易受到干扰与封锁，导致延迟骤增或高丢包率。而 **IPLC (International Private Leased Circuit)** 与 **IEPL** 属于点对点物理内网专线：

1. **不过 GFW 防火墙**：数据在内网过境，不受公网封锁与干扰影响。
2. **极低延迟与 0 丢包**：游戏平稳运行，音视频拖动无缓冲。
3. **晚高峰高度稳定**：即使在晚上 8:00 - 11:00 用网高峰期，带宽依然充足。

---

## 2. 首推优质专线机场清单

| 排名 | 机场品牌 | 线路架构 | 起步价格 | 专属优惠码 | 官方通道 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 🥇 1 | **灵动云** | IPLC 物理专线 | ¥15/月起 | `ld88` (8折) | <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener">官网直达 →</a> |
| 🥈 2 | **暮光网络** | IEPL 专线+BGP | ¥15/月起 | `mm88` (8折) | <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener">官网直达 →</a> |
| 🥉 3 | **飞猫云** | 极速 IEPL 专线 | 折合 ¥7/月起 | `flycat888` (8折) | <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener">官网直达 →</a> |
| 🎖️ 4 | **微风网络** | BGP 多线中继 | 折合 ¥8/月起 | `breeze88` (8折) | <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener">官网直达 →</a> |

---

## 3. 流媒体解锁与客户端一键导入配置

挑选机场时还需确认其节点是否原生支持 Netflix、Disney+、YouTube 4K 及 OpenAI ChatGPT 交互。选择支持“一键导入订阅”的服务商，可以大幅降低使用门槛。
"""
    },
    "service-article-2.md": {
        "title": "机场优惠码领取与全套餐最大折扣使用策略",
        "desc": "汇总全网主流梯子机场最新专属优惠码，教你如何在结算页无缝使用 8 折优惠码省钱。",
        "body": """# 机场优惠码领取与全套餐最大折扣使用策略

合理使用优惠码可以帮助你在购买机场套餐时节省 15% - 30% 的开支。本文整理了 2026 年最新大牌机场的官方专属折扣码及结算使用步骤。

---

## 1. 2026 年全网大牌机场专属优惠码汇总

> **提示**：优惠码在结算页面（Checkout）输入后点击“应用”即可自动扣减金额。

- **灵动云 (首选专线)**：专属 8 折优惠码 `ld88`，支持全套餐通用。
- **暮光网络 (影音大流量)**：专属 8 折优惠码 `mm88`，季付与年付更划算。
- **飞猫云 (性价比首选)**：专属 8 折优惠码 `flycat888`，折合每月低至 7 元。
- **微风网络 Breezenet**：专属 8 折优惠码 `breeze88`，轻量稳定年付特惠。
- **隐形人 (高隐匿代理)**：专属优惠码 `yxr888`，抗封锁高匿名保障。

---

## 2. 优惠码填写与折扣生效流程

1. 进入机场官方控制面板，选择需要的套餐（如月付、季付或年付）。
2. 在订单确认页面的【优惠码 / Promotion Code】输入框中填入上述对应代码。
3. 点击【验证 / Apply】按钮，确认订单总额已折减 20%。
4. 选择支付宝或微信支付完成付款，在【订阅管理】中复制订阅链接使用。
"""
    },
    "service-article-3.md": {
        "title": "灵动云官方直达：企业级物理专线与低延迟游戏配置",
        "desc": "深入评测灵动云 (优惠码 ld88) 的 IPLC 物理专线节点延迟、丢包率与企业级跨境加速表现。",
        "body": """# 灵动云官方直达：企业级物理专线与低延迟游戏配置

**灵动云** 凭借其全线配置的内网 IPLC 物理专线，在各大科技社区与跨境从业者中享有极高声誉。无论是对于要求低延迟的实时外服游戏，还是高吞吐量的 4K/8K 视频播放，灵动云都能提供卓越的表现。

---

## 1. 灵动云的核心优势

1. **纯正 IPLC 内网专线**：不经过公网 GFW，物理延迟极低，实测日韩节点 Ping 值低至 25ms。
2. **全流媒体与 AI 解锁**：解锁 Netflix 完整水库、Disney+、Hulu 及 OpenAI ChatGPT / Claude 3.5。
3. **SLA 99.99% 高可用**：多入口容灾调度，避免单节点故障导致的断连。

---

## 2. 灵动云套餐价格与优惠码

| 套餐名称 | 月流量 | 专线带宽 | 折后参考价 | 专属优惠码 |
| :---: | :---: | :---: | :---: | :---: |
| 基础轻量 | 100GB /月 | 300Mbps | **¥12.0 /月** (原¥15) | `ld88` |
| 标准进阶 | 300GB /月 | 500Mbps | **¥28.0 /月** (原¥35) | `ld88` |
| 尊享旗舰 | 800GB /月 | 1000Mbps | **¥68.0 /月** (原¥85) | `ld88` |

<div style="margin: 1.5rem 0; text-align: center;">
  <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" class="btn-mod-primary" style="padding: 0.8rem 2rem; font-size: 1rem;">👉 点击直达灵动云官方网站 (凭折扣码 ld88 享 8 折)</a>
</div>
"""
    },
    "service-article-4.md": {
        "title": "暮光网络大流量特惠：海量音画与全节点解锁选购",
        "desc": "评测暮光网络 (优惠码 mm88) 的大流量套餐、晚高峰 4K 播放能力与多设备同时在线支持。",
        "body": """# 暮光网络大流量特惠：海量音画与全节点解锁选购

对于喜欢追剧、观看 YouTube 4K/8K 视频或下载大文件的用户而言，流量上限往往是最关心的指标。**暮光网络 (Twilight Network)** 主打海量流量配额与极致影音解锁，是追剧党与流媒体爱好者的理想选择。

---

## 1. 暮光网络实测亮点

- **超大流量配额**：提供每月 500GB 至 1.5TB 的海量数据配额。
- **全流媒体 100% 解锁**：轻松解锁 YouTube 4K/8K、Netflix 独播剧集及 HBO Max。
- **设备无限制连接**：支持多台设备同时登录使用，适合家庭与小团队共享。

---

## 2. 暮光网络套餐一览

| 套餐类型 | 月流量 | 特点说明 | 优惠价 (使用 mm88) | 官方入口 |
| :---: | :---: | :---: | :---: | :---: |
| 追剧体验 | 300GB /月 | 常用节点解锁 | **¥12 /月** | <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener">官网直达 →</a> |
| 豪华影音 | 800GB /月 | 4K/8K秒开 | **¥28 /月** | <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener">官网直达 →</a> |
| 团队旗舰 | 2000GB /月 | 独享带宽 | **¥68 /月** | <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener">官网直达 →</a> |
"""
    },
    "service-article-5.md": {
        "title": "飞猫云 IEPL 专线全拆解：自研极速客户端开箱测速",
        "desc": "测评飞猫云 (优惠码 flycat888) 的自研 Windows/Mac 一键客户端与折合 7 元/月的高性价比方案。",
        "body": """# 飞猫云 IEPL 专线全拆解：自研极速客户端开箱测速

对于新手用户来说，配置 Clash 或 Shadowrocket 繁琐的订阅步骤常令人头疼。**飞猫云** 针对新手推出自研极速客户端，扫码登录一键开启代理，同时保持了 IEPL 专线的高质量传输。

---

## 1. 飞猫云特色与功能优势

1. **自研全平台客户端**：内置 Windows / macOS 原生客户端，无需手工转换或配置规则。
2. **极致高性价比**：年付折合每月仅需 7 元，非常适合学生党与预算有限的用户。
3. **IEPL 专线保证**：拒绝低质直连，全节点采用 IEPL 专线中继，确保晚高峰不卡顿。

---

## 2. 飞猫云官方选购通道

- **专属 8 折优惠码**：`flycat888`
- **官方注册链接**：<a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener">点击进入飞猫云官网注册页 →</a>
"""
    }
}

wenti_updates = {
    "wenti-article-1.md": {
        "title": "节点超时 Timeout 终极排查：系统时间同步与订阅更新",
        "desc": "详细讲解解决代理客户端中所有节点提示 Timeout 或 20000ms 报错的 4 步修复法。",
        "body": """# 节点超时 Timeout 终极排查：系统时间同步与订阅更新

在 Clash Verge、Shadowrocket 或 v2rayNG 中，若遇到所有节点测试显示 `Timeout` 或 `-1ms`，通常并不是机场服务器崩溃，而是本地配置问题。

---

## 1. 核心原因一：系统时间不同步 (占 90%)

代理加密协议（如 TLS、VLESS、Shadowsocks）高度依赖时间戳校验。若本地电脑或手机的时间与国际标准时间误差超过 90 秒，握手将被强制拒绝。

### 修复方法：
1. **Windows**：打开【设置】->【时间和语言】->【日期和时间】，开启【自动设置时间】，并点击【立即同步】。
2. **macOS**：打开【系统设置】->【通用】->【日期与时间】，勾选【自动设置日期和时间】。
3. **iOS / Android**：在系统时间设置中开启【自动确定时间】。

---

## 2. 核心原因二：机场域名变更或订阅未更新

机场节点 IP 会不定期调整，若长时间未更新订阅，旧节点失效即报 Timeout。在客户端中右键点击订阅并选择【更新订阅 / Update Subscription】即可恢复。
"""
    },
    "wenti-article-2.md": {
        "title": "科学上网防走丢与官方备用域名防失联全攻略",
        "desc": "教你如何保存机场官方 Telegram 频道、备用主页发布页及防走丢邮件更新入口。",
        "body": """# 科学上网防走丢与官方备用域名防失联全攻略

由于国内网络环境的特殊性，机场官方主页域名可能会被 DNS 污染或封禁。为了避免失联后找不到最新官网地址，建议提前做好防走丢准备。

---

## 1. 必做防失联三大步骤

1. **关注官方 Telegram 频道/群组**：绝大多数优质机场（如灵动云、暮光网络）会在 Telegram 频道第一时间发布最新的备用域名。
2. **保存官方 Release 导航页**：将机场的永久导航页加入浏览器书签。
3. **绑定真实邮箱**：在机场后台绑定可用邮箱，通过【忘记密码】或邮件推送获取最新入口。

---

## 2. 本站四大推荐机场官方最新直达通道

- 🥇 **灵动云**：<a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener">最新官网备用地址 →</a> (8折码 `ld88`)
- 🥈 **暮光网络**：<a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener">最新官网备用地址 →</a> (8折码 `mm88`)
- 🥉 **飞猫云**：<a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener">最新官网备用地址 →</a> (8折码 `flycat888`)
- 🎖️ **微风网络**：<a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener">最新官网备用地址 →</a> (8折码 `breeze88`)
"""
    },
    "wenti-article-3.md": {
        "title": "翻墙避坑指南：识别虚假免费代理与超售跑路风险",
        "desc": "深入剖析免费 VPN 软件注入弹窗广告与数据窃取陷阱，教你选择长效稳定的优质专线机场。",
        "body": """# 翻墙避坑指南：识别虚假免费代理与超售跑路风险

“天下没有免费的午餐”，免费梯子软件背后往往隐藏着高昂的安全代价与隐性陷阱。

---

## 1. 免费代理软件的三大风险

1. **隐私泄露与数据贩卖**：免费 VPN 经常记录用户的浏览历史、真实 IP 及账号明文，并将其出售给广告商。
2. **植入恶意木马与挖矿脚本**：部分流氓客户端在后台静默运行挖矿程序，占用 CPU 导致电脑卡顿。
3. **极度不稳与频繁失效**：几千人挤在同一条劣质 VPS 节点上，播放 360p 视频都频繁缓冲。

---

## 2. 如何识别高风险“跑路机场”？

- 价格低得离谱（如 9.9 元买永久无限流量）。
- 没有 Telegram 交流群或禁言不解答问题。
- 不支持月付，强制要求年付或两年付。

建议选择支持 **月付** 且线路明透明的服务商（如 **灵动云** 或 **暮光网络**）。
"""
    },
    "wenti-article-4.md": {
        "title": "订阅链接拉取失败与 URL 污染拦截解决办法",
        "desc": "解决 Clash 或小火箭导入订阅提示 Subscription Fetch Failed 的常见方案与在线 Subconverter 转换。",
        "body": """# 订阅链接拉取失败与 URL 污染拦截解决办法

在客户端中复制机场订阅链接并点击导入时，如果弹出 `Subscription Fetch Failed` 或 `Download Failed` 错误，请按以下步骤排除。

---

## 1. 常见原因与解决方法

1. **订阅链接被运营商 DNS 污染**：
   - 解决方法：开启手机 4G/5G 热点拉取，或者将本地 DNS 改为 `119.29.29.29` / `223.5.5.5` 后重试。
2. **使用了旧的订阅地址**：
   - 解决方法：登录机场后台，点击【重置订阅密钥】，重新复制最新生成的 URL。
3. **客户端缺少 TLS 证书支持**：
   - 解决方法：更新 Clash Verge 或 Shadowrocket 到最新版本。
"""
    },
    "wenti-article-5.md": {
        "title": "客户端证书失效 (TLS Handshake Failed) 修复指南",
        "desc": "分析 TLS 握手失败、证书过期及 SNI 校验不匹配的底层原理与实操修复教程。",
        "body": """# 客户端证书失效 (TLS Handshake Failed) 修复指南

当代理日志显示 `TLS Handshake Failed` 或 `Certificate Validate Error` 时，表示客户端与代理节点在建立安全加密通道时判定证书无效。

---

## 1. 产生问题的根源

- **节点伪装域名 SNI 变更**：机场后端更换了伪装域名，但客户端本地配置未及时同步。
- **系统根证书库过旧**：旧版 Windows 7 或 Android 7.0 缺乏最新的 ISRG Root X1 根证书。
- **本地安全软件拦截**：火绒、360 或 Windows Defender 开启了 HTTPS 流量审计。

---

## 2. 快速排查清单

1. 在客户端中开启 `Skip Cert Verify / 跳过证书检查`（仅作为应急方案）。
2. 在机场后台重新导入最新订阅。
3. 暂时关闭第三方杀毒软件的“Web 防护”功能。
"""
    }
}

# Run the update on content/service and content/wenti
def apply_updates():
    for f_name, data in service_updates.items():
        f_path = os.path.join(content_dir, "service", f_name)
        if os.path.exists(f_path):
            full_text = f"""---
title: "{data['title']}"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "{data['desc']}"
summary: "{data['desc']}"
keywords: ["科学上网", "梯子推荐", "机场测评", "灵动云", "暮光网络"]
---

{data['body'].strip()}
"""
            with open(f_path, "w", encoding="utf-8") as f:
                f.write(full_text)

    for f_name, data in wenti_updates.items():
        f_path = os.path.join(content_dir, "wenti", f_name)
        if os.path.exists(f_path):
            full_text = f"""---
title: "{data['title']}"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "{data['desc']}"
summary: "{data['desc']}"
keywords: ["科学上网排错", "机场常见问题", "Clash报错", "超时解决"]
---

{data['body'].strip()}
"""
            with open(f_path, "w", encoding="utf-8") as f:
                f.write(full_text)

apply_updates()
print("Updated service and wenti articles successfully.")
