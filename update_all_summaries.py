import os
import re

# Comprehensive unique titles and summaries mapping per directory

jichang_tuijian_articles = [
    {
        "filename": "jichang-tuijian-article-1.md",
        "title": "2026 高性价比 IPLC 专线机场选购指南：告别晚高峰卡顿与频繁断连",
        "summary": "深度对比 2026 年主流 IPLC 物理专线与普通 BGP 中继线路在晚高峰时段的延迟与丢包表现。推荐首选灵动云与飞猫云，提供优惠码 ld88，助你实现 4K 视频秒开与低延迟游戏体验。",
        "keywords": ["IPLC专线机场", "高性价比梯子", "晚高峰4K", "灵动云", "科学上网指南"],
        "lead": "对于经常在晚高峰时段遇到视频缓冲或网页断连的用户来说，普通的公网直连中继已经很难满足高稳定性需求。本文从物理内网传输机制入手，全面解析 IPLC 专线优势，并精选灵动云与飞猫云作为全站首选通道。"
    },
    {
        "filename": "jichang-tuijian-article-2.md",
        "title": "海外学术科研与文献检索梯子推荐：Google Scholar 与 IEEE 极速访问",
        "summary": "专为高校师生与科研人员打造的跨境学术网络配置方案。重点解析直连镜像与学术域名规则分流，搭配暮光网络与灵动云，解决论文下载超时与镜像打不开的痛点。",
        "keywords": ["学术科研梯子", "Google Scholar加速", "IEEE文献下载", "暮光网络", "IPLC专线"],
        "lead": "学术文献检索与海外数据库访问对网络稳定性有极高的要求。本文针对 arXiv、Google Scholar、IEEE Xplore 等科研平台的特点，手把手教你配置规则分流，避免论文下载卡顿。"
    },
    {
        "filename": "jichang-tuijian-article-3.md",
        "title": "外贸出海与跨境电商多 IP 防封机场选购：亚马逊与 TikTok 稳定运营",
        "summary": "针对亚马逊店群、TikTok 运营及社媒营销的稳定代理方案。深入讲解原生静态 IP 隔离与防关联配置，推荐飞猫云与微风网络 Breezenet，保障跨境业务合规不封号。",
        "keywords": ["外贸出海机场", "跨境电商梯子", "多出口IP", "飞猫云", "防封策略"],
        "lead": "跨境电商与外贸运营最忌讳 IP 变动导致店铺被关联或账号风控。本文总结了亚马逊、Shopee、TikTok 账号防护技巧，并推荐具备稳定原生出口 IP 的专线服务商。"
    },
    {
        "filename": "jichang-tuijian-article-4.md",
        "title": "开发者跨境工具加速指南：GitHub 代码拉取与 Docker 镜像构建",
        "summary": "聚焦程序员与 DevOps 团队的工具链加速。实测在 Clash TUN 模式下构建 Docker 容器与 git clone 速度，推荐使用具备内网物理专线的灵动云与全球云。",
        "keywords": ["开发者梯子", "GitHub加速", "Docker镜像代理", "灵动云", "TUN模式"],
        "lead": "开发者在日常拉取 GitHub 仓库、构建 Docker 镜像或访问 AWS/GCP 终端时，网络延迟直接影响开发效率。本文详解全局 TUN 模式与代理规则构建，助你提升代码编译与部署速度。"
    },
    {
        "filename": "jichang-tuijian-article-5.md",
        "title": "4K 8K 极速影音播放机场推荐：Netflix / Disney+ / YouTube 全流媒体解锁",
        "summary": "横向测评 2026 年主流大流量影音机场。针对晚高峰 4K/8K 视频加载延迟与流媒体版权检测，推荐暮光网络（优惠码 mm88）与浪网 WaveNet，轻松解锁原生音画。",
        "keywords": ["4K秒开机场", "流媒体解锁梯子", "Netflix原生IP", "暮光网络", "大流量机场"],
        "lead": "想要在客厅大屏或电脑端畅享 Netflix、Disney+ 4K 乃至 8K 超高清画质，极速稳定的带宽是核心保障。本文横向测试多家机场的晚高峰吞吐率，为你推荐高品质大流量方案。"
    },
    {
        "filename": "jichang-tuijian-article-6.md",
        "title": "OpenAI ChatGPT 与 Claude AI 交互专属代理：避免 403 封禁与 IP 隔离",
        "summary": "解析 OpenAI 与 Anthropic 官方对代理节点的封锁机制。提供干净原生 IP 选择技巧与规则分流避坑指南，推荐灵动云与隐形人机场，保障 AI 工具流畅交互。",
        "keywords": ["ChatGPT代理", "Claude AI梯子", "原生IP机场", "灵动云", "AI工具加速"],
        "lead": "访问 OpenAI ChatGPT、Claude 或 Midjourney 等人工智能平台时，经常遇到 Access Denied 403 报错。本文详细拆解官方防刷机制，并提供高纯净度原生 IP 节点的选购与设置技巧。"
    },
    {
        "filename": "jichang-tuijian-article-7.md",
        "title": "学生党与新手小白预算型梯子推荐：折合 7 元/月高性价比方案",
        "summary": "针对低预算用户的实用避坑指南。对比按量计费与轻量月付套餐，推荐折合仅 7 元/月的飞猫云 IEPL 专线，支持自研一键客户端，无需复杂配置即可上手。",
        "keywords": ["便宜机场推荐", "学生党梯子", "性价比专线", "飞猫云", "新手选购"],
        "lead": "预算有限并不意味着必须使用高风险的免费软件。本文推荐多款年付折合仅几元/月的优质高性价比专线，如飞猫云 IEPL 方案，自带极简客户端，小白零门槛开箱即用。"
    },
    {
        "filename": "jichang-tuijian-article-8.md",
        "title": "iOS 苹果手机 Shadowrocket (小火箭) 最佳搭配节点与一键导入教程",
        "summary": "针对 iPhone 与 iPad 用户的专属节点匹配手册。涵盖免美区 ID 下载、订阅链接批量更新与节点连通测试，搭配微风网络 Breezenet，全天候稳定连通。",
        "keywords": ["小火箭节点", "Shadowrocket机场", "iOS科学上网", "微风网络", "订阅转换"],
        "lead": "iOS 系统用户最常使用的客户端无疑是 Shadowrocket（小火箭）。本文讲解如何正确导入机场订阅、测试节点延迟以及开启按需连接（On Demand），配合微风网络 Breezenet 实现全自动连通。"
    },
    {
        "filename": "jichang-tuijian-article-9.md",
        "title": "Windows 与 Mac 端 Clash Verge Rev 客户端高性能规则配置指南",
        "summary": "全面拆解 Windows 与 macOS 系统下新一代 Clash Verge Rev 客户端。手把手教你配置全局 TUN 模式与 ACL4SSR 分流规则，搭配梯子云 LadderCloud 快捷使用。",
        "keywords": ["Clash Verge教程", "电脑端梯子", "规则分流", "梯子云", "TUN模式"],
        "lead": "Clash for Windows 停更后，Clash Verge Rev 成为电脑端的全新标准。本文详细示范新版界面下的订阅导入、TUN 网卡模式开启与自定义分流规则设置。"
    },
    {
        "filename": "jichang-tuijian-article-10.md",
        "title": "全平台 Sing-box 客户端 Hysteria2 协议极速配置与测试",
        "summary": "深入探讨 Sing-box 新一代代理协议的高效配置。对比 Shadowsocks 与 Trojan 在恶劣网络下的抗丢包能力，推荐飞V 机场，实现秒级握手与极速无感切换。",
        "keywords": ["Sing-box教程", "Hysteria2协议", "低延迟梯子", "飞V", "协议对比"],
        "lead": "Sing-box 作为新一代通用代理核心，凭借对 Hysteria2 与 TUIC v5 协议的完美支持备受青睐。本文提供通用 JSON 配置模板与通用订阅转换工具，带来极致的低延迟握手体验。"
    },
    {
        "filename": "jichang-tuijian-article-11.md",
        "title": "如何识别超售跑路机场？2026 避坑防失联与长效续订策略",
        "summary": "揭秘“买断无限流量”与“超低价年付”背后的风险陷阱。教你识别机场跑路前兆、设置多备用节点与保护订阅 URL，推荐使用运营超 3 年的灵动云与暮光网络。",
        "keywords": ["避坑跑路机场", "机场防失联", "订阅备份", "灵动云", "安全选购"],
        "lead": "在选购科学上网机场时，安全性与长效稳定性比单纯的价格更加重要。本文拆解不良商家常见的超售跑路套路，教你通过备用订阅、月付试用及多服务商冗余配置确保网络永不失联。"
    },
    {
        "filename": "jichang-tuijian-article-12.md",
        "title": "2026 稳定好用梯子机场综合排行榜：28 家服务商多维度数据对比",
        "summary": "全站 28 家主流机场综合实测大盘点。汇总带宽、节点数量、解封能力与优惠码，方便用户快速定位适合自己的榜首灵动云、暮光网络、飞猫云及微风网络。",
        "keywords": ["28家机场对比", "梯子推荐排行榜", "IPLC专线", "优惠码汇总", "灵动云"],
        "lead": "面对市场上琳琅满目的网络加速服务商，如何挑选最符合自己用量与预算的服务？本指南基于数月实测数据，整理了 28 家主流机场的价格、线路类型、解封表现及专属优惠码全景对比表。"
    }
]

jiaocheng_articles = [
    {
        "filename": "jiaocheng-article-1.md",
        "title": "Clash for Windows 零基础下载、安装与订阅导入图文步骤",
        "summary": "手把手教你在电脑端下载官方 Clash 客户端，复制机场订阅链接完成连通，开启规则代理模式。包含灵动云与飞猫云订阅快捷导入演示。",
        "keywords": ["Clash for Windows", "Clash下载", "订阅导入", "客户端教程", "灵动云"],
        "lead": "Clash for Windows 是桌面端最受欢迎的图形化代理客户端之一。本文针对零基础新手，提供一步一图的下载安装、订阅配置与规则切换使用流程。"
    },
    {
        "filename": "jiaocheng-article-2.md",
        "title": "Shadowrocket (小火箭) iPhone / iPad 扫码与一键导入节点指南",
        "summary": "针对 iOS 苹果手机用户，提供免美区 ID 选购、机场后台一键添加订阅及节点测试图文解说。轻松匹配暮光网络与微风网络专线节点。",
        "keywords": ["Shadowrocket", "小火箭教程", "iOS代理", "美区ID", "暮光网络"],
        "lead": "iPhone 和 iPad 用户使用 Shadowrocket（小火箭）可以获得最流畅的代理体验。本文从获取美区 Apple ID 开始，完整演示扫码配置与自动分流设置。"
    },
    {
        "filename": "jiaocheng-article-3.md",
        "title": "Sing-box 新一代代理协议配置与通用订阅转换教程",
        "summary": "解析 Sing-box 客户端在 Hysteria2 及 Shadowsocks 协议下的高效配置方法与转换工具使用。搭配飞猫云与飞V 机场打造低延迟体验。",
        "keywords": ["Sing-box", "Hysteria2", "订阅转换", "跨平台代理", "飞猫云"],
        "lead": "Sing-box 支持最新的 Hysteria2 和 TUIC 协议，抗封锁性能优异。本文指导你如何将传统 Clash 订阅一键转换并导入 Sing-box 客户端。"
    },
    {
        "filename": "jiaocheng-article-4.md",
        "title": "节点连接超时报错 Timeout 怎么解决？网络自动同步与排错清单",
        "summary": "汇总 90% 新手最常遇到的节点超时、证书错误、DNS 污染等核心问题的快速修复对策。帮助你迅速恢复灵动云或暮光网络的连通。",
        "keywords": ["节点超时", "Timeout报错", "排错清单", "时间同步", "灵动云"],
        "lead": "遇到节点提示 Timeout 或无法连通时不要慌张。90% 的连通故障均由系统时间偏差、订阅过期或客户端规则残留导致。本文提供一分钟快速排错清单。"
    },
    {
        "filename": "jiaocheng-article-5.md",
        "title": "Android 安卓端 Clash for Android 与 v2rayNG 下载与配置指南",
        "summary": "针对各大品牌安卓手机，讲解 Clash for Android 和 v2rayNG 的下载安装、后台保活设置与订阅更新。完美适配微风网络与梯子云。",
        "keywords": ["安卓梯子", "Clash for Android", "v2rayNG", "后台保活", "微风网络"],
        "lead": "安卓手机在开启代理时常受到系统杀后台的困扰。本文演示如何正确安装开源客户端，并针对华为、小米、OPPO/VIVO 系统完成后台保活与节点调度。"
    },
    {
        "filename": "jiaocheng-article-6.md",
        "title": "Mac 苹果电脑 Clash Verge Rev 与 Surge 原生芯片配置步骤",
        "summary": "适配 Apple Silicon M1/M2/M3/M4 芯片的 Mac 原生代理教程。演示系统代理与 TUN 模式开启，实现流畅访问 GitHub 与学术网。",
        "keywords": ["Mac梯子", "Clash Verge Mac", "Surge", "Apple Silicon", "灵动云"],
        "lead": "在 macOS 系统上，使用原生适配 ARM 架构的代理客户端能大幅降低功耗。本文手把手带你配置 Clash Verge Rev，并开启全局 TUN 模式。"
    },
    {
        "filename": "jiaocheng-article-7.md",
        "title": "如何正确配置规则分流 (Rule Mode)？避免国内流量走代理跑流量",
        "summary": "深入讲解 Direct 直连、Proxy 代理与 Reject 拦截规则。教你导入第三方 ACL4SSR 规则包，确保国内百度、微信不耗费机场流量。",
        "keywords": ["规则分流", "Rule模式", "ACL4SSR", "省流量配置", "飞猫云"],
        "lead": "开启代理后访问国内网站速度变慢或流量飞速消耗？这是因为没有正确配置规则分流。本文教你正确开启 Rule 模式，实现内外网智能路由。"
    },
    {
        "filename": "jiaocheng-article-8.md",
        "title": "TUN 模式与全局代理的区别：解决 UWP 应用与游戏无法接轨代理的痛点",
        "summary": "解析操作系统底层 TUN 虚拟网卡接管原理。解决 Windows 商店应用、微软 Teams 及 Steam 客户端不走 HTTP 代理的问题。",
        "keywords": ["TUN模式", "虚拟网卡", "全局代理", "游戏加速", "暮光网络"],
        "lead": "很多应用（如 Windows Store、Spotify 客户端、命令行终端）默认不读取系统 HTTP 代理。本文详解 TUN 模式原理与一键开启步骤，让全局流量无死角覆盖。"
    },
    {
        "filename": "jiaocheng-article-9.md",
        "title": "Quantumult X (圈x) 策略组自定义与分流规则进阶指引",
        "summary": "针对 iOS 进阶玩家的 Quantmult X 配置教程。讲解 Rewrite 脚本重定向、自动节点延迟测速策略组构建与多机场订阅合并。",
        "keywords": ["Quantumult X", "圈x教程", "策略组", "脚本重定向", "灵动云"],
        "lead": "Quantumult X 凭借强大的策略组与脚本重写功能成为 iOS 端的终极神器。本文教你构建自动优选策略组，在多个机场节点间实现无感自适应切换。"
    },
    {
        "filename": "jiaocheng-article-10.md",
        "title": "全平台 8 大主推机场后台一键订阅导入功能对比与快捷操作",
        "summary": "汇总灵动云、暮光网络、飞猫云等 8 大自营机场后台的一键导入快捷入口。手机扫描二维码即可几秒内完成全站节点同步。",
        "keywords": ["一键订阅", "机场后台", "扫码导入", "8大主推", "灵动云"],
        "lead": "手动复制粘贴订阅链接容易出错？现代优质机场后台均提供“一键导入 Clash/小火箭”功能。本文整理了 8 大主推机场的快捷导入按键位置与使用小技巧。"
    },
    {
        "filename": "jiaocheng-article-11.md",
        "title": "软路由 OpenWrt 与 PassWall / SSR-Plus 全家网络加速部署",
        "summary": "教你在软路由或 HomeLab 中部署 PassWall 插件，实现全家电视、游戏机、智能家居免客户端自动翻墙。支持 IPLC 专线负载均衡。",
        "keywords": ["OpenWrt", "PassWall", "软路由梯子", "全家加速", "飞猫云"],
        "lead": "在路由器端部署代理插件可以免去每台设备单独安装软件的麻烦。本文详细示范 OpenWrt 环境下 PassWall 插件的安装、节点导入与智能 DNS 分流配置。"
    },
    {
        "filename": "jiaocheng-article-12.md",
        "title": "小白如何在线完成机场节点订阅转换？在线 Subconverter 避坑安全指南",
        "summary": "讲解订阅转换工具的原理解析与安全风险防范。教你使用自建或可信第三方 API 转换 Sing-box 与 Clash 订阅，防止订阅链接泄露。",
        "keywords": ["订阅转换", "Subconverter", "转换安全", "防泄露", "微风网络"],
        "lead": "使用格式不兼容的客户端时，通常需要借助订阅转换服务。本文讲解 Subconverter 的运行机制，并提供安全转换规则，防止个人订阅被恶劣转换站窃取。"
    },
    {
        "filename": "jiaocheng-article-13.md",
        "title": "解决 DNS 污染与 DNS 泄露：配置 DoH / DoT 安全防追踪模式",
        "summary": "解析域名污染机制与 DNS 泄露隐患。指导用户在 Clash 和 小火箭 中配置 223.5.5.5 及 Cloudflare 安全 DoH 节点，提升上网隐匿度。",
        "keywords": ["DNS污染", "DNS泄露", "DoH配置", "隐私防护", "隐形人机场"],
        "lead": "域名污染是导致网站打不开或跳转防拦截页面的主因。本文深入剖析 DNS 污染原理，并手把手教你启用 DNS-over-HTTPS (DoH) 加密查询，杜绝运营商 DNS 劫持。"
    },
    {
        "filename": "jiaocheng-article-14.md",
        "title": "代理软件开机自启与后台无感连通优化技巧",
        "summary": "分享 Windows / macOS / Mobile 端的静默自启与网络状态监测配置。结合灵动云 IPLC 专线，实现开机即用、断网自动重连的流畅体验。",
        "keywords": ["开机自启", "静默运行", "无感连通", "自动重连", "灵动云"],
        "lead": "如何让科学上网像原生网络一样顺畅无感？本文汇总了各平台客户端的系统开机静默启动、后台自动守护以及网络环境切换时的自动重连配置方法。"
    },
    {
        "filename": "jiaocheng-article-15.md",
        "title": "新手科学上网常见错误术语科普：什么是倍率、重置日与直连节点",
        "summary": "扫盲机场后台常见的“1x/5x倍率”、“结算日”、“节点协议”、“BGP中继”。帮助新手合理规划月度流量，避免误用高倍率节点跑光流量。",
        "keywords": ["机场术语", "节点倍率", "流量重置", "BGP中继", "新手科普"],
        "lead": "刚接触机场的小白常常被“倍率”、“重置日”、“IPLC”等专业名词搞懵。本文用最通俗易懂的语言，为你一次性梳理机场使用中最常涉及的 10 大核心概念。"
    }
]

def update_section_articles(dir_path, articles_meta):
    for meta in articles_meta:
        filepath = os.path.join(dir_path, meta["filename"])
        if not os.path.exists(filepath):
            continue
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse front matter
        fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            continue
        
        fm_text = fm_match.group(1)
        body_text = content[fm_match.end():]

        # Construct new front matter
        kw_str = ", ".join([f'"{k}"' for k in meta["keywords"]])
        new_fm = f"""---
title: "{meta['title']}"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "{meta['summary']}"
summary: "{meta['summary']}"
keywords: [{kw_str}]
---"""

        # Update body heading and first paragraph
        lines = body_text.strip().split("\n")
        new_body_lines = []
        heading_done = False
        lead_done = False

        for line in lines:
            if line.startswith("# ") and not heading_done:
                new_body_lines.append(f"# {meta['title']}")
                heading_done = True
            elif heading_done and not lead_done and line.strip() != "":
                # Replace lead paragraph
                new_body_lines.append(f"\n{meta['lead']}\n")
                lead_done = True
            else:
                new_body_lines.append(line)

        new_content = new_fm + "\n\n" + "\n".join(new_body_lines)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

dir_jichang = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jichang-tuijian"
dir_jiaocheng = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jiaocheng"

update_section_articles(dir_jichang, jichang_tuijian_articles)
update_section_articles(dir_jiaocheng, jiaocheng_articles)

print("Updated jichang-tuijian and jiaocheng articles with unique titles and summaries!")
