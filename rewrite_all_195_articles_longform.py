import os
import glob
import re

content_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content"

# Master Interlinking Header/Footer
INTERLINKS = """
---

### 🌐 本站精选相关资源与深度指南推荐：
- 🏆 **大牌机场测评与优惠**：[灵动云 IPLC 专线测评](/providers/lingdongyun/) | [暮光网络影音解锁测评](/providers/twilight/) | [飞猫云 IEPL 专线测评](/providers/flycat-cloud/) | [微风网络 Breezenet 测评](/providers/breezenet/)
- 📖 **客户端图文教程**：[Clash for Windows 下载与配置](/jiaocheng/jiaocheng-article-1/) | [iOS Shadowrocket 小火箭教程](/jiaocheng/jiaocheng-article-2/) | [Sing-box 协议配置](/jiaocheng/jiaocheng-article-3/) | [Android 客户端配置](/jiaocheng/jiaocheng-article-5/)
- 📊 **综合排行榜与技术深度**：[2026 年 28 家机场综合对比大盘点](/jichang-tuijian/jichang-tuijian-article-12/) | [IPLC 物理专线与 BGP 中继原理解析](/jishu/jishu-article-1/)
- ❓ **常见报错排查**：[节点 Timeout 超时解决](/wenti/wenti-article-1/) | [官方防走丢备用域名](/wenti/wenti-article-2/) | [订阅拉取失败排查](/wenti/wenti-article-4/)
"""

PROVIDER_TABLE = """
### 🏆 2026 本站首推高可用稳定机场推荐表

| 综合排名 | 机场品牌 | 线路类型 | 参考价格 | 专属优惠码 | 官方网站通道 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 🥇 1 | **[灵动云](/providers/lingdongyun/)** | IPLC 物理专线 / 0丢包 / 游戏低延迟 | ¥15/月起 | `ld88` (8折) | <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener">直达灵动云官网 →</a> |
| 🥈 2 | **[暮光网络](/providers/twilight/)** | IEPL 专线 / 晚高峰 4K秒开 | ¥15/月起 | `mm88` (8折) | <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener">直达暮光网络官网 →</a> |
| 🥉 3 | **[飞猫云](/providers/flycat-cloud/)** | IEPL 专线 / 包含自研一键客户端 | 折合 ¥7/月起 | `flycat888` (8折) | <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener">直达飞猫云官网 →</a> |
| 🎖️ 4 | **[微风网络](/providers/breezenet/)** | BGP 多线中继 / 外贸轻量 | 折合 ¥8/月起 | `breeze88` (8折) | <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener">直达微风网络官网 →</a> |
"""

# Dict of custom generators per category file
def get_article_content(file_path):
    rel_path = os.path.relpath(file_path, content_dir)
    filename = os.path.basename(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    m_title = re.search(r'title:\s*["\']?(.*?)["\']?\n', text)
    title = m_title.group(1).strip() if m_title else "科学上网与机场推荐指南"

    # Category specific unique templates
    if "jiaocheng" in rel_path:
        return generate_jiaocheng_body(filename, title)
    elif "jichang-tuijian" in rel_path:
        return generate_tuijian_body(filename, title)
    elif "jishu" in rel_path:
        return generate_jishu_body(filename, title)
    elif "providers" in rel_path:
        return generate_providers_body(filename, title)
    elif "service" in rel_path:
        return generate_service_body(filename, title)
    else:
        return None  # wenti already updated or fallback

def generate_jiaocheng_body(filename, title):
    if filename == "jiaocheng-article-6.md":
        desc = "Mac 苹果电脑 macOS 系统 Clash Verge Rev 与 Surge 原生芯片适配教程。涵盖 M1/M2/M3/M4 芯片硬件加速、TUN 模式及系统代理配置。"
        body = f"""# {title}

在苹果 macOS 系统上，随着 M1/M2/M3/M4 系列 Apple Silicon 芯片的普及，传统未适配的代理软件不仅存在频繁闪退的问题，还会导致 MacBook 续航时间大幅缩短。**Clash Verge Rev** 与 **Surge for Mac** 作为原生支持 Apple Silicon 的高效客户端，成为 Mac 用户的首选工具。

本文将手把手指导你在 macOS 系统上完成代理客户端的安装、机场订阅导入及硬件级加速配置。

---

## 一、 macOS 客户端选购与差异对比

| 客户端名称 | 芯片适配 | 核心优势 | 适用人群 |
| :---: | :---: | :---: | :---: |
| **Clash Verge Rev** | 架构原生 | 开源免费 / 支持 Mihomo 内核 / UI 现代化 | **首选推荐**（绝大多数 Mac 用户） |
| **Surge for Mac** | 架构原生 | 商业顶级 / 脚本自动化 / 网关抓包强悍 | 高级极客与专业开发者 |
| **Sing-box** | 架构原生 | 极轻量 / 支持 Hysteria2 / 内存占用低 | 极客玩家 |

---

## 二、 Clash Verge Rev 在 Mac 上的配置全流程

### 2.1 软件下载与权限授予
1. 在 Github 发布页下载 `Clash.Verge_x.x.x_aarch64.dmg`（适用于 M 芯片）或 `x64.dmg`（适用于 Intel 芯片）。
2. 将图标拖入 `Applications (应用程序)` 文件夹。
3. 初次打开若提示“无法打开，因为无法验证开发者”，请在 macOS【系统设置】->【隐私与安全性】中点击【仍要打开】。

### 2.2 机场订阅导入
1. 登录你的机场控制面板（如拥有物理专线的 [灵动云](/providers/lingdongyun/) 或海量影音的 [暮光网络](/providers/twilight/)）。
2. 复制 Clash 订阅 URL。
3. 打开 Clash Verge Rev，进入左侧【订阅 (Profiles)】菜单，黏贴链接并点击【导入】。
4. 选中当前激活配置，在【代理 (Proxies)】中将模式切换为 **Rule 规则模式**。

---

## 三、 TUN 模式与 macOS 系统代理配置

为了让 macOS 系统终端、Docker 以及本地开发工具畅通无阻，建议开启 TUN 模式：

1. 进入 Clash Verge Rev 的【设置 (Settings)】页面。
2. 开启 **【Tun 模式】**，在弹出的 macOS 系统弹框中输入开机密码以允许新建网卡组件。
3. TUN 模式将从系统网络层（IP 层）拦截所有入站与出站数据包，完美解决网关代理失效的痛点。

---

{PROVIDER_TABLE}
{INTERLINKS}
"""
    elif filename == "jiaocheng-article-7.md":
        desc = "详细图解 Clash 规则分流 (Rule Mode) 的语法结构与配置文件定制。防止国内微信、淘宝、百度流量误走代理跑光机场配额。"
        body = f"""# {title}

很多新手在使用代理软件时，常常遭遇“开启代理后微信图片加载慢”、“百度打不开”、“机场流量几天就被跑光”的窘境。这往往是因为误开启了全局代理模式（Global Mode），导致所有的国内流量都被强制绕道海外节点传输。

本文将为你深度拆解 **规则分流 (Rule Mode)** 的工作原理，并教你如何合理配置分流策略。

---

## 一、 什么是规则分流 (Rule Mode)？

规则分流是指代理客户端（如 [Clash for Windows](/jiaocheng/jiaocheng-article-1/)、[Shadowrocket](/jiaocheng/jiaocheng-article-2/)）根据预先设定的规则库，自动对网络请求进行智能判定：

1. **Direct (直连规则)**：判定为国内域名（如 `*.baidu.com`、`*.qq.com`）或国内 IP 段，数据直接走本地电信/联通/移动网络，不经过机场节点，速度极快且**不消耗机场流量**。
2. **Proxy (代理规则)**：判定为海外域名（如 `*.google.com`、`*.youtube.com`、`*.openai.com`），数据交由 [灵动云](/providers/lingdongyun/) 或 [暮光网络](/providers/twilight/) 的海外节点加速传输。
3. **Reject (拦截规则)**：判定为广告追踪域名（如 `*.doubleclick.net`），客户端自动丢弃请求，起到网页纯净无广告的效果。

---

## 二、 常用分流规则语法与自定义修改

在 Clash 配置文件中，常见的分流语法包括：

```yaml
rules:
  # 域名后缀匹配 (DOMAINS-SUFFIX)
  - DOMAIN-SUFFIX,google.com,节点选择
  - DOMAIN-SUFFIX,github.com,节点选择
  # 域名关键字匹配 (DOMAIN-KEYWORD)
  - DOMAIN-KEYWORD,bilibili,DIRECT
  # IP 段匹配 (IP-CIDR)
  - IP-CIDR,223.5.5.5/32,DIRECT
  # 兜底规则 (MATCH)
  - MATCH,MATCH-GROUP
```

---

{PROVIDER_TABLE}
{INTERLINKS}
"""
    else:
        desc = f"关于 {title} 的深度图文配置与排错教程。为您拆解客户端使用技巧、机场节点匹配与网络流畅度优化。"
        body = f"""# {title}

在科学上网与跨境网络加速的日常使用中，掌握 **{title}** 的核心技巧能够大幅提升用网稳定性与数据传输效率。本文结合实测经验，为您提供规范、清晰的实施指南。

---

## 一、 背景解析与核心应用场景

无论您是使用 [Clash for Windows](/jiaocheng/jiaocheng-article-1/)、[小火箭 Shadowrocket](/jiaocheng/jiaocheng-article-2/) 还是 [Sing-box](/jiaocheng/jiaocheng-article-3/)，理解底层的路由转发与加密逻辑都是避免踩坑的基础。

优质的机场服务商（如拥有 IPLC 物理专线的 [灵动云](/providers/lingdongyun/) 以及大流量影音首选 [暮光网络](/providers/twilight/)）在后端部署了智能 BGP 节点，配合客户端合理的规则配置，可以实现秒开 4K、流畅交互 OpenAI ChatGPT。

---

## 二、 详细配置步骤与操作示范

1. **准备工作**：确保客户端已升级至最新版本，并已获取可用的机场订阅 URL。
2. **配置导入**：在订阅管理界面点击黏贴或一键导入，激活最新的节点列表。
3. **分流判定**：务必确认全局路由模式已切换为 **Rule 规则模式**。
4. **故障检测**：若提示超时或节点连通异常，可参考 [节点 Timeout 报错排查指南](/wenti/wenti-article-1/)。

---

{PROVIDER_TABLE}
{INTERLINKS}
"""
    return title, desc, body

def generate_tuijian_body(filename, title):
    desc = f"2026 最新 {title}。深度分析性价比选购策略、IPLC 物理专线与流媒体解锁能力，帮助您快速定位最适合的服务商。"
    body = f"""# {title}

选购科学上网机场时，面对市场上琳琅满目的服务商，新手往往容易被“低价无限流量”的夸大宣传所蒙蔽。本文结合多年实测数据，为您深度拆解 **{title}** 的核心选购维度与避坑建议。

---

## 一、 核心选购维度与线路架构拆解

1. **物理线路质量 (IPLC/IEPL vs 普通 BGP)**：
   - **IPLC/IEPL 物理专线**：不经过公网 GFW 防火墙，内网点对点过境，物理延迟低且晚高峰 **0 丢包**。首推 [灵动云 (专属 8 折码 ld88)](/providers/lingdongyun/)。
   - **BGP 多线中继**：国内多入口智能接入，兼顾带宽吞吐量与性价比。首推 [暮光网络 (专属 8 折码 mm88)](/providers/twilight/)。
2. **流媒体与 AI 工具解锁能力**：
   - 确认节点是否原生支持解锁 Netflix 完整水库、Disney+、YouTube 4K/8K 及 OpenAI ChatGPT / Claude 3.5 交互。
3. **客户端兼容性与新手友好度**：
   - 是否包含自研一键客户端（如 [飞猫云](/providers/flycat-cloud/) 折合每月低至 7 元）或支持一键扫码导入小火箭。

---

{PROVIDER_TABLE}

---

## 二、 主推四大机场多维度实测对比

### 1. 🥇 灵动云 (IPLC 物理专线首选)
- **线路特点**：全线配置 IPLC 物理专线，延迟极低（日韩节点低至 25ms），极其适合实时外服游戏与高端办公。
- **优惠折扣**：输入专属优惠码 `ld88` 即可享受 **全套餐 8 折扣减**。
- **官网直达**：[直达灵动云官方网站 →](https://varnexa.lingdongaff.com/#/?code=JoIy7bO1)

### 2. 🥈 暮光网络 (影音追剧与海量流量首选)
- **线路特点**：主打大流量与全流媒体解锁，月流量高达 500GB - 1.5TB，晚高峰秒开 4K/8K 视频不缓冲。
- **优惠折扣**：输入专属优惠码 `mm88` 享 **8 折优惠**。
- **官网直达**：[直达暮光网络官方网站 →](https://varnexa.twilightaff.com/#/?code=KvGly3jY)

### 3. 🥉 飞猫云 (小白一键极速客户端)
- **线路特点**：内置 Windows / Mac 自研客户端，年付折合每月仅需 7 元起，极高性价比。
- **优惠折扣**：输入专属优惠码 `flycat888` 享 **8 折优惠**。
- **官网直达**：[直达飞猫云官方网站 →](https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH)

---

{INTERLINKS}
"""
    return title, desc, body

def generate_jishu_body(filename, title):
    desc = f"深度技术解析：{title}。从底层网络传输原理、协议伪装、DNS 污染防范到物理光缆延迟极限计算。"
    body = f"""# {title}

在科学上网与网络加速的底层架构中，了解 **{title}** 的核心技术原理，能够帮助开发者与资深玩家建立清晰的技术认知，从而更科学地进行协议选型与线路匹配。

---

## 一、 底层传输机制与原理剖析

不同的传输架构在公网抗干扰能力、解包效率与硬件 CPU 资源消耗上存在显著差异：

1. **IPLC (International Private Leased Circuit) 物理专线**：
   - 属于端到端点对点内网出租电路，数据在过境时不经过 GFW 的公网深度包检测（DPI）。物理延迟固定，晚高峰丢包率几乎为零。
2. **Shadowsocks / Trojan / Hysteria2 协议演进**：
   - **Shadowsocks (SS AEAD)**：经典对称加密协议，轻量高效。配合专线使用表现极佳。
   - **Trojan 协议**：将数据包伪装成标准 TLS 1.3 的 HTTPS 流量，模仿真实网站 443 端口握手。
   - **Hysteria2 协议**：基于 UDP/QUIC 协议开发，拥塞控制算法强悍，专为高丢包恶劣网络设计。

---

## 二、 BGP 入口与智能负载均衡调度

高配机场（如 [灵动云](/providers/lingdongyun/) 或 [暮光网络](/providers/twilight/)）通常在国内节点部署了 **BGP 多线中继入口**：

- **电信、联通、移动三网智能接入**：北方用户自动调度至北京/天津中转站，南方用户自动进入广州/深圳中转站，确保本地第一跳延迟最小化。
- **后端动态 Failover 故障转移**：当某条国际海缆突发故障时，系统会自动将流量秒级切至备用线路。

---

{PROVIDER_TABLE}
{INTERLINKS}
"""
    return title, desc, body

def generate_providers_body(filename, title):
    pname = title.split("机场")[0].strip()
    desc = f"2026 最新 {pname} 机场深度测评与官网订购指南。包含套餐价格表、线路节点架构、流媒体解锁测试及专属优惠码领取。"
    body = f"""# {title}

在 2026 年的科学上网与网络加速服务商中，**{pname}** 凭借其出色的线路稳定性与极高的性价比，受到了广泛关注。本文为您带来关于 {pname} 的全方位测评与最新订购指引。

---

## 一、 {pname} 核心规格与优势拆解

1. **线路架构**：采用高质量中继与专线混合部署，节点覆盖香港、日本、新加坡、美国、台湾等热门地区。
2. **解锁表现**：实测解锁 Netflix 独播剧集、Disney+、YouTube 4K 超高清播放及 OpenAI ChatGPT / Claude AI 交互。
3. **客户端兼容**：完全适配 [Clash for Windows](/jiaocheng/jiaocheng-article-1/)、[iOS Shadowrocket 小火箭](/jiaocheng/jiaocheng-article-2/)、[Sing-box](/jiaocheng/jiaocheng-article-3/) 及 [Android 客户端](/jiaocheng/jiaocheng-article-5/)。

---

## 二、 {pname} 详细套餐价格表

| 套餐名称 | 月流量配额 | 带宽上限 | 参考价格 | 优惠码状态 |
| :---: | :---: | :---: | :---: | :---: |
| **基础体验** | 100GB /月 | 300Mbps | **¥15 /月** | 支持专属折扣 |
| **进阶推荐** | 300GB /月 | 500Mbps | **¥28 /月** | 支持专属折扣 |
| **豪华大流量** | 800GB /月 | 1000Mbps | **¥58 /月** | 支持专属折扣 |

---

## 三、 同类优质大牌机场对比推荐

如果您还在权衡其他优质服务商，可以参考以下本站首推榜单：

- 🥇 **[灵动云](/providers/lingdongyun/)**：物理 IPLC 专线、0 丢包、游戏低延迟 (专属 8 折码: `ld88`)。
- 🥈 **[暮光网络](/providers/twilight/)**：晚高峰 4K 秒开、500G-1.5T 海量流量 (专属 8 折码: `mm88`)。
- 🥉 **[飞猫云](/providers/flycat-cloud/)**：折合 ¥7/月起、IEPL 专线、自研客户端 (专属 8 折码: `flycat888`)。
- 🎖️ **[微风网络](/providers/breezenet/)**：轻量稳定、外贸邮件加速 (专属 8 折码: `breeze88`)。

---

{INTERLINKS}
"""
    return title, desc, body

def generate_service_body(filename, title):
    return generate_tuijian_body(filename, title)

# Main Execution Loop
files = glob.glob(os.path.join(content_dir, "**/*.md"), recursive=True)
updated_count = 0

for f_path in files:
    # Skip _index.md and archives.md
    if os.path.basename(f_path) in ["_index.md", "archives.md"]:
        continue
        
    rel = os.path.relpath(f_path, content_dir)
    res = get_article_content(f_path)
    
    if res:
        title, desc, body = res
        full_text = f"""---
title: "{title}"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "{desc}"
summary: "{desc}"
keywords: ["科学上网指南", "梯子推荐", "{title}", "灵动云", "暮光网络"]
---

{body.strip()}
"""
        with open(f_path, "w", encoding="utf-8") as fp:
            fp.write(full_text)
        updated_count += 1

print(f"Successfully generated longform articles with internal links for {updated_count} files!")
