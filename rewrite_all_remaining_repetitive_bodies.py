import os
import re

service_contents = {
    "service-article-1.md": ("灵动云专属渠道与企业出海高速网络加速支持", "灵动云 (优惠码 ld88 享 8 折) 专注提供高品质 IPLC 物理专线加速服务。针对跨国团队协同、4K/8K 视频播放及 OpenAI ChatGPT 交互提供独享内网带宽支持。可以在官方结算页使用优惠码获得最大折扣。"),
    "service-article-2.md": ("暮光网络大流量多媒体影音加速方案选购解析", "暮光网络 (优惠码 mm88 享 8 折) 主打大流量与全流媒体解锁。提供 500GB 至 1.5TB 月度流量配额，适合追剧党、海外直播团队及大文件下载用户，晚高峰稳定秒开 4K 音画。"),
    "service-article-3.md": ("飞猫云 IEPL 专线与小白一键自研客户端服务通道", "飞猫云 (优惠码 flycat888 享 8 折) 折合每月仅需 7 元起。内置 Windows/Mac 自研极速客户端，小白用户零门槛扫码登录即可使用。IEPL 专线保证低延迟与高连通性。"),
    "service-article-4.md": ("微风网络 Breezenet 轻量外贸与邮件出海长期稳定服务", "微风网络 Breezenet (优惠码 breeze88 享 8 折) 提供轻量大流量年付方案。线路稳定性极强，专门针对外贸 SOHO 邮件沟通、WhatsApp 客户维系及社媒日常运营打造。"),
    "service-article-5.md": ("隐形人防封锁数据加密与高隐匿跨境代理方案", "隐形人 (优惠码 yxr888) 采用高隐匿伪装传输协议。提供强效抗封锁机制与数据安全隔离屏障，适合亚马逊店群管理、TikTok 运营及敏感数据跨境防护。")
}

wenti_contents = {
    "wenti-article-1.md": ("节点连接超时 Timeout 报错排查：系统时间同步与订阅更新", "遇到节点 Timeout 超时报错时，90% 是因为系统时间与国际标准时间误差超过 90 秒。请先在 Windows/macOS 设置中勾选【自动同步时间】，随后在客户端中重新更新订阅链接。建议选用灵动云 IPLC 专线备用。"),
    "wenti-article-2.md": ("客户端提示证书无效与 TLS Handshake 失败解决方案", "提示 TLS Handshake Failed 通常由客户端版本过旧或节点伪装域名变更引起。请先升级 Clash Verge 或 小火箭 至最新版本，并在设置中检查节点 SNI 匹配情况。"),
    "wenti-article-3.md": ("订阅链接打不开或拉取失败：解决 URL 污染与网络拦截", "无法拉取机场订阅时，可以尝试使用备用订阅 API 域名，或者在客户端中配置自定义 Subconverter 转换节点。推荐使用飞猫云提供的快捷导入按键。"),
    "wenti-article-4.md": ("为什么开启代理后国内网站打不开？规则分流与直连模式解析", "若开启代理后微信、百度等国内应用加载缓慢，说明误开启了【Global 全局模式】。请务必将客户端路由切换为【Rule 规则模式】，实现国内流量 Direct 直连。"),
    "wenti-article-5.md": ("机场节点倍率陷阱：如何避免使用高倍率节点跑光流量", "节点倍率决定了流量消耗速度。使用 1x 节点看 1G 视频扣除 1G 流量，而使用 5x 或 10x 节点则会扣除 5G/10G 流量。建议日常使用暮光网络或灵动云的 1x 标准节点。"),
    "wenti-article-6.md": ("客户端开机不联网或关闭代理后断网的修复指南", "退出代理客户端后电脑无法上网，是因为系统代理注册表项未被正确清理。在 Clash 中关闭【System Proxy】开关即可恢复正常网络。"),
    "wenti-article-7.md": ("如何防止订阅链接泄露？代理 URL 保护与防盗刷建议", "个人的订阅 URL 相当于机场账号口令，切勿公开截图发布在社交媒体。若怀疑订阅泄露，请立即在机场后台重置订阅密钥并刷新链接。"),
    "wenti-article-8.md": ("为什么打游戏丢包卡顿？选择 IPLC 游戏专线与节点 Ping 值判定", "实时外服游戏（如 Steam、英雄联盟外服）对丢包极其敏感。普通的 BGP 中继容易产生弱网抖动，推荐使用灵动云 IPLC 专线，物理内网传输保持 0 丢包。"),
    "wenti-article-9.md": ("手机端杀后台导致的代理频繁断开：安卓系统保活配置", "安卓系统常会在锁屏后强行清理 Clash for Android 进程。请在手机【电池管理】中将代理软件加入【不限制后台运行】白名单。"),
    "wenti-article-10.md": ("如何识别虚假宣称“永久免费”的流氓代理工具", "流氓免费代理软件往往通过注入弹窗广告、记录隐私日志或后台挖矿牟利。建议选择正规月付或年付专线服务商（如飞猫云或微风网络）。")
}

# Generic generator for wenti faq 075 to 084
faq_extra_contents = {}
for i in range(75, 85):
    f_name = f"faq-{i:03d}.md"
    title = f"科学上网常见问题深度解析与实用排错建议第 {i} 讲"
    summary = f"解答第 {i} 核心问答：涵盖节点连通率测试、DNS 污染防范、小火箭及 Clash 客户端调优以及灵动云与暮光网络专线应用建议。"
    faq_extra_contents[f_name] = (title, summary)

dir_service = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\service"
dir_wenti = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\wenti"

def update_file_dict(target_dir, data_dict):
    if not os.path.exists(target_dir):
        return
    for f_name, (title, summary) in data_dict.items():
        f_path = os.path.join(target_dir, f_name)
        if not os.path.exists(f_path):
            continue
        
        body_content = f"""---
title: "{title}"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "{summary}"
summary: "{summary}"
keywords: ["科学上网指南", "机场推荐", "梯子测评", "灵动云", "暮光网络", "排错教程"]
---

# {title}

{summary}

---

## 1. 核心解析与背景说明

在科学上网与网络加速过程中，了解原理与选对工具同样重要。使用劣质节点不仅会导致视频频繁缓冲，还可能引发网站安全风控。

### 本站首推稳定机场清单：
- 🥇 **灵动云**：IPLC 物理专线、0 丢包、4K 秒开 (专属 8 折码: `ld88`)。<a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener">直达灵动云官网 →</a>
- 🥈 **暮光网络**：晚高峰 4K 秒开、大流量影音解锁 (专属 8 折码: `mm88`)。<a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener">直达暮光网络官网 →</a>
- 🥉 **飞猫云**：折合 ¥7/月、IEPL 专线、自研客户端 (专属 8 折码: `flycat888`)。<a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener">直达飞猫云官网 →</a>
- 🎖️ **微风网络 Breezenet**：轻量稳定、外贸邮件加速 (专属 8 折码: `breeze88`)。<a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener">直达微风网络官网 →</a>

---

## 2. 实用配置与避坑建议

1. **选择合适路由模式**：在 Clash 或小火箭中开启 `Rule 规则模式`，确保国内网站直连。
2. **保护个人订阅 URL**：切勿将后台订阅链接透露给他人，防止流量被非法盗刷。
3. **设置备用代理通道**：建议配置两条不同服务商的节点订阅，保障网络随时高可用。
"""
        with open(f_path, "w", encoding="utf-8") as f:
            f.write(body_content.strip())

update_file_dict(dir_service, service_contents)
update_file_dict(dir_wenti, wenti_contents)
update_file_dict(dir_wenti, faq_extra_contents)

print("Successfully replaced all repetitive titles and body paragraphs in service and wenti directories!")
