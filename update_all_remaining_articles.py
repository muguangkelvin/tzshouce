import os
import re

jishu_articles = [
    {
        "filename": "jishu-article-1.md",
        "title": "IPLC 物理专线与 BGP 中继传输机制对比：原理与晚高峰稳定性分析",
        "summary": "深入剖析 IPLC 点对点物理专线与 BGP 公网中继的传输链路差异。解释为何 IPLC 能在敏感时期实现 0 丢包与超低延迟抖动，推荐灵动云专线服务。",
        "keywords": ["IPLC专线", "BGP中继", "传输原理", "晚高峰抖动", "灵动云"],
        "lead": "了解代理网络的底层物理传输架构是挑选高质量梯子的第一步。本文从内网过境专线、BGP 入口节点以及 GFW 阻断原理切入，系统对比 IPLC 与中继的区别。"
    },
    {
        "filename": "jishu-article-2.md",
        "title": "Shadowsocks, Trojan 与 Hysteria2 代理协议抗封锁能力横向测评",
        "summary": "对比 SS、Trojan、Hysteria2 及 TUIC v5 协议在恶劣网络环境下的 TLS 伪装特征与 UDP 拥堵控制算法。指导用户选择最高效协议搭配飞猫云使用。",
        "keywords": ["Trojan协议", "Hysteria2", "Shadowsocks", "协议对比", "飞猫云"],
        "lead": "不同的代理协议在流量加密与伪装特性上各有千秋。本文对比分析加密流量在被主动探测时的抵抗力，助你根据本地 ISP 运营商特征选择最佳代理协议。"
    },
    {
        "filename": "jishu-article-3.md",
        "title": "代理客户端分流规则 ACL4SSR 配置与自定义 Direct / Proxy 语法",
        "summary": "详解 Clash 和 Sing-box 中基于 Domain, IP-CIDR, GeoIP 的规则匹配机制。手把手教你编写自定义规则，实现学术网站与国内 APP 智能分流。",
        "keywords": ["ACL4SSR", "分流规则", "Clash规则", "Domain-KEYWORD", "微风网络"],
        "lead": "高效的分流规则不仅能加速访问，还能极大节省机场月度流量。本文拆解分流规则的优先级策略，教你通过正则表达式与 GeoIP 编写属于自己的专属分流文件。"
    },
    {
        "filename": "jishu-article-4.md",
        "title": "DNS 污染与 DNS 泄露机制剖析：如何配置 DoH 加密防护",
        "summary": "揭秘 GFW 域名污染与运营商 DNS 劫持的底层技术细节。提供 Cloudflare 与 DNSPod DoH 服务地址，确保访问海外网站时 IP 隐私不被泄漏。",
        "keywords": ["DNS污染", "DNS泄露", "DoH加密", "Cloudflare", "隐形人机场"],
        "lead": "DNS 污染是海外网页无法加载最常见的幕后黑手。本文演示如何通过在代理客户端中启用 DNS-over-HTTPS (DoH) 和 Fake-IP 模式，彻底杜绝 DNS 劫持。"
    },
    {
        "filename": "jishu-article-5.md",
        "title": "BGP 多线中继入口与智能负载均衡调度技术拆解",
        "summary": "分析优质机场如何通过电信、联通、移动三网 BGP 入口进行流量调度。讲解均衡负载与自动 Failover 切换机制，推荐暮光网络（优惠码 mm88）。",
        "keywords": ["BGP中继", "负载均衡", "三网优化", "Failover切换", "暮光网络"],
        "lead": "为什么选择 BGP 入口能让不同运营商的用户都获得极低延迟？本文揭秘 BGP 路由协议在跨国加速中的动态寻路优势，并分析机场如何做到故障自动无感切节点。"
    },
    {
        "filename": "jishu-article-6.md",
        "title": "TUN 模式与系统 HTTP 代理的物理层拦截机制差异",
        "summary": "深入探讨 Windows wintun 驱动与 macOS utun 设备如何接管系统所有 IP 数据包。解决 UWP、Docker、Steam 客户端无法走常规代理的难题。",
        "keywords": ["TUN模式", "wintun驱动", "HTTP代理", "UDP转发", "梯子云"],
        "lead": "系统代理只能拦截支持 HTTP/SOCKS5 的应用，而 TUN 模式从网络层驱动接管流量。本文对比两者的性能开销与应用场景，手把手演示高效开启 TUN 模式。"
    },
    {
        "filename": "jishu-article-7.md",
        "title": "原生 IP (Native IP) 与 广播 IP (Broadcast IP) 对流媒体与 AI 工具的影响",
        "summary": "讲解 IP 数据库（MaxMind / IPinfo）如何判定节点地理属性。解释原生 IP 为何能无视 Netflix 版权检测与 ChatGPT 403 封锁，推荐灵动云。",
        "keywords": ["原生IP", "广播IP", "Netflix解锁", "ChatGPT封锁", "灵动云"],
        "lead": "为什么同样的节点有的能看 Netflix 4K 有的却报错？核心在于 IP 是否为当地 ISP 颁发的原生纯净 IP。本文教你如何查询节点的纯净度与欺诈得分。"
    },
    {
        "filename": "jishu-article-8.md",
        "title": "长途内网 IEPL/IPLC 物理光缆架构与节点延迟极限计算",
        "summary": "基于光速在光纤中的传输物理极限（每千米约 5 微秒），计算沪日、深港、京韩物理专线的理论最低 Ping 值，帮助用户理性评测机场节点测速数据。",
        "keywords": ["IPLC物理光缆", "延迟极限", "深港专线", "沪日专线", "飞猫云"],
        "lead": "网络延迟受物理距离与光纤传导速率限制。本文通过光纤传输物理公式计算各常用线路的极限延迟，让你一眼看穿假伪专线与延迟造假虚标现象。"
    }
]

def update_articles(dir_path, articles_meta):
    for meta in articles_meta:
        filepath = os.path.join(dir_path, meta["filename"])
        if not os.path.exists(filepath):
            continue
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            continue
        
        body_text = content[fm_match.end():]

        kw_str = ", ".join([f'"{k}"' for k in meta["keywords"]])
        new_fm = f"""---
title: "{meta['title']}"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "{meta['summary']}"
summary: "{meta['summary']}"
keywords: [{kw_str}]
---"""

        lines = body_text.strip().split("\n")
        new_body_lines = []
        heading_done = False
        lead_done = False

        for line in lines:
            if line.startswith("# ") and not heading_done:
                new_body_lines.append(f"# {meta['title']}")
                heading_done = True
            elif heading_done and not lead_done and line.strip() != "":
                new_body_lines.append(f"\n{meta['lead']}\n")
                lead_done = True
            else:
                new_body_lines.append(line)

        new_content = new_fm + "\n\n" + "\n".join(new_body_lines)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

update_articles(r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jishu", jishu_articles)

# Update wenti articles (wenti-article-1 to 10 and faq-001 to faq-100)
# Ensure each faq article has a unique title and summary based on its question!
wenti_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\wenti"
if os.path.exists(wenti_dir):
    for f_name in os.listdir(wenti_dir):
        if not f_name.endswith(".md") or f_name.startswith("_"):
            continue
        f_path = os.path.join(wenti_dir, f_name)
        with open(f_path, "r", encoding="utf-8") as f:
            text = f.read()
        
        fm_match = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            body = text[fm_match.end():]
            
            title_m = re.search(r'title:\s*"(.*?)"', fm)
            title_val = title_m.group(1) if title_m else "科学上网常见问题与排错解答"
            
            # Create a specific summary if missing or repetitive
            summary_val = f"针对【{title_val}】的专业解答指南。详细拆解节点排错步骤、系统配置优化与灵动云专线防封技巧，帮助新手快速搞定科学上网。"
            
            # Check if summary already in fm
            if "summary:" not in fm:
                new_fm = fm + f'\nsummary: "{summary_val}"'
            else:
                new_fm = re.sub(r'summary:\s*".*?"', f'summary: "{summary_val}"', fm)
            
            new_text = f"---\n{new_fm}\n---{body}"
            with open(f_path, "w", encoding="utf-8") as f:
                f.write(new_text)

print("Updated all remaining section articles successfully!")
