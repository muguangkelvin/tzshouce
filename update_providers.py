import os
import re

providers_data = [
    {
        "file": "lingdongyun.md",
        "name": "灵动云",
        "rank": "🥇 榜首推荐 (第 1 位)",
        "aff_url": "https://varnexa.lingdongaff.com/#/?code=JoIy7bO1",
        "coupon": "ld88",
        "coupon_desc": "ld88 (全场 8 折特惠)",
        "price": "官网为准 (使用优惠码 ld88 享 8 折特惠)",
        "users": "外贸出海 / 学术科研 / 4K追剧 / 跨境开发者",
        "devices": "Windows / macOS / iOS (小火箭) / Android / Linux / 路由器",
        "nodes": "IPLC 物理专线 / BGP 中继 / 多节点智能分流",
        "regions": "香港、日本、新加坡、美国、台湾、韩国、欧洲等 30+ 节点",
        "intro": "全站首推极速专线机场，专为高延迟敏感人群设计，晚高峰百兆带宽不拥堵。",
        "features": "4K秒开 / 零过墙低延迟 / 原生IP解封 ChatGPT & Netflix / 支持一键导入",
        "support": "提供 24 小时工单支持、Telegram 交流群协助及小白图文使用教程"
    },
    {
        "file": "twilight.md",
        "name": "暮光网络",
        "rank": "🥈 第 2 位",
        "aff_url": "https://varnexa.twilightaff.com/#/?code=KvGly3jY",
        "coupon": "mm88",
        "coupon_desc": "mm88 (全场 8 折优惠)",
        "price": "¥20/月 起 (使用优惠码 mm88 享 8 折)",
        "users": "大流量影音用户 / 4K 追剧党 / 跨境办公",
        "devices": "Windows / macOS / iOS / Android / TVBox",
        "nodes": "高质 BGP 中继 / 优质专线",
        "regions": "香港、日本、新加坡、美国、台湾、德国",
        "intro": "主打大流量与高清影音体验的高性价比服务商，晚高峰稳定输出。",
        "features": "120GB-1.5TB大流量 / 4K秒播 / 全流媒体解锁 / 稳定不掉线",
        "support": "极速售后答疑，提供 Telegram 交流群及多端一键配置链接"
    },
    {
        "file": "flycat-cloud.md",
        "name": "飞猫云",
        "rank": "🥉 第 3 位",
        "aff_url": "https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH",
        "coupon": "flycat888",
        "coupon_desc": "flycat888 (季付 8 折)",
        "price": "折合 ¥7/月 起 (使用优惠码 flycat888 季付 8 折)",
        "users": "新手小白 / 学生党 / 预算有限出海群体",
        "devices": "Windows / macOS / iOS / Android (包含自研一键客户端)",
        "nodes": "IEPL 专线 / 自动化负载均衡",
        "regions": "香港、日本、新加坡、美国、韩国",
        "intro": "低门槛超高性价比专线机场，内置小白自研客户端，秒速配置。",
        "features": "折合月付低至7元 / 自研极速客户端 / IEPL专线 / 零基础一键点亮",
        "support": "专人指导配置，提供客户端一键下载与在线帮助中心"
    },
    {
        "file": "breezenet.md",
        "name": "微风网络 Breezenet",
        "rank": "🎖️ 第 4 位",
        "aff_url": "https://edp01.breezenetaff.com/#/?code=He4n3zxg",
        "coupon": "breeze88",
        "coupon_desc": "breeze88 (全场 8 折)",
        "price": "结算页为准 (使用优惠码 breeze88 享 8 折)",
        "users": "轻量上网 / 邮件外贸 / 备用节点需求者",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "中继 + 直连混合优化",
        "regions": "香港、日本、新加坡、美国",
        "intro": "专注轻量与稳定性方案的服务商，适合低流量年付与日常使用。",
        "features": "轻量年付方案 / 高连通率 / 兼容所有主流代理工具",
        "support": "工单即时回复，在线配置教程指导"
    },
    {
        "file": "yinxingren.md",
        "name": "隐形人",
        "rank": "第 5 位",
        "aff_url": "https://varnexa.invisibleaff.com/#/?code=FlyoraeM",
        "coupon": "yxr888",
        "coupon_desc": "yxr888 (专属特惠)",
        "price": "官网结算页为准 (使用优惠码 yxr888 享特惠)",
        "users": "高隐私诉求 / 跨境电商 / 数据安全要求高人群",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "高隐匿传输协议 / 防封锁加密节点",
        "regions": "香港、日本、新加坡、美国、英国",
        "intro": "主打高隐匿安全传输的特色机场，具备极佳的抗封锁能力。",
        "features": "高隐匿协议 / 数据加密防护 / 节点高可用 / 跨境隐私屏障",
        "support": "Telegram 群组安全咨询与快速问题解答"
    },
    {
        "file": "wavenet.md",
        "name": "浪网 WaveNet",
        "rank": "第 6 位",
        "aff_url": "https://varnexa.wavenetaff.com/#/?code=a9HF4LBZ",
        "coupon": "wave888",
        "coupon_desc": "wave888 (专属优惠)",
        "price": "官网结算页为准 (使用优惠码 wave888 享优惠)",
        "users": "大吞吐量下载 / 视频博主 / 海外直播",
        "devices": "Windows / macOS / iOS / Android / Linux",
        "nodes": "大带宽 BGP 节点 / 专属速连通道",
        "regions": "香港、日本、新加坡、美国、加拿大",
        "intro": "主攻千兆大带宽传输的优质机场，满足超高清画质与高速下载。",
        "features": "千兆带宽 / 4K/8K视频流畅加载 / 节点平稳无卡顿",
        "support": "全天候后台工单解答与线路监控"
    },
    {
        "file": "laddercloud.md",
        "name": "梯子云 LadderCloud",
        "rank": "第 7 位",
        "aff_url": "https://varnexa.ladderaff.com/#/?code=bYVSMHMh",
        "coupon": "ladder88",
        "coupon_desc": "ladder88 (专属折扣)",
        "price": "官网结算页为准 (使用优惠码 ladder88 享折扣)",
        "users": "零基础新手 / 跨平台多设备用户",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "全协议兼容中继 / 快捷节点调度",
        "regions": "香港、日本、新加坡、美国、台湾",
        "intro": "小白友好型云端梯子服务，支持自动化订阅转换与一键扫码。",
        "features": "零门槛导入 / 全平台一键扫码 / 节点订阅转换支持",
        "support": "新手一对一指导说明与 FAQ 排错"
    },
    {
        "file": "feiv.md",
        "name": "飞V",
        "rank": "第 8 位",
        "aff_url": "https://varnexa.flyvaff.com/#/?code=qaMgTyhY",
        "coupon": "flyv888",
        "coupon_desc": "flyv888 (专享优惠)",
        "price": "官网结算页为准 (使用优惠码 flyv888 享特惠)",
        "users": "多端移动办公 / 短视频刷剧",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "多端适配中继 / 智能切换节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "轻量好用的多端代理服务，节点响应快，切换极其顺畅。",
        "features": "多端极速适配 / 极速切换 / 性价比高",
        "support": "工单系统与常用客户端常见问题解答"
    },
    {
        "file": "quanqiu-cloud.md",
        "name": "全球云",
        "rank": "精选推荐",
        "aff_url": "https://sswdh.gcvipaff.com/#/?code=Ys0xKqnU",
        "coupon": "qq88",
        "coupon_desc": "qq88 (8折优惠)",
        "price": "¥20/月起 (使用优惠码 qq88 享 8 折)",
        "users": "流媒体解封 / AI 工具访问 / 跨境流控",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "IPLC专线 / 原生IP",
        "regions": "香港、日本、新加坡、美国",
        "intro": "优质 IPLC 专线服务商，原生 IP 覆盖全面，AI 工具支持极佳。",
        "features": "IPLC专线 / 原生IP / ChatGPT+Netflix全解封",
        "support": "全天候客服在线服务"
    },
    {
        "file": "xingdaomeng.md",
        "name": "星岛梦",
        "rank": "精选推荐",
        "aff_url": "https://kfccbb.xingdaomeng.com/#/?code=tLbhLnNf",
        "coupon": "xdm888",
        "coupon_desc": "xdm888 (立减优惠)",
        "price": "官网结算页为准 (使用优惠码 xdm888 享优惠)",
        "users": "日常办公 / 网页浏览 / 学术检索",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "优质中继 / 低延迟节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "连通率高的稳定中继服务商，全端订阅导入简便。",
        "features": "低延迟节点 / 全端订阅导入 / 线路稳健",
        "support": "后台工单答疑与教程中心"
    },
    {
        "file": "guangshuyun.md",
        "name": "光速云",
        "rank": "精选推荐",
        "aff_url": "https://mdlky.gsyaff.com/#/?code=5snwJVcD",
        "coupon": "gsy888",
        "coupon_desc": "gsy888 (速享特惠)",
        "price": "官网结算页为准 (使用优惠码 gsy888 享优惠)",
        "users": "4K追剧 / 短视频播放 / 游戏加速",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "极速 BGP 节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "主打极速响应与 4K 秒开的大流量方案服务商。",
        "features": "极速响应 / 4K秒开 / 适配流畅追剧",
        "support": "即时客服指导"
    },
    {
        "file": "weituyun.md",
        "name": "唯兔云 (V2云)",
        "rank": "精选推荐",
        "aff_url": "https:/fast.v2yunvipaff.com/#/?code=xkiG3YWN",
        "coupon": "v2yun88",
        "coupon_desc": "v2yun88 (折扣优惠)",
        "price": "官网结算页为准 (使用优惠码 v2yun88 享折扣)",
        "users": "V2ray 协议偏好人群 / 跨境访问",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "V2ray 高隐匿协议节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "基于 V2ray 协议的抗封锁稳定代理服务商。",
        "features": "V2ray协议 / 稳定防封 / 传输稳健",
        "support": "工单处理与文档指南"
    },
    {
        "file": "u1s1.md",
        "name": "U1S1 (有一说一)",
        "rank": "精选推荐",
        "aff_url": "https://pkdj7.vipaff.cc/#/?code=nYbe5pKy",
        "coupon": "u1s1888",
        "coupon_desc": "u1s1888 (立减特惠)",
        "price": "官网结算页为准 (使用优惠码 u1s1888 享立减)",
        "users": "追求性价比用户 / 务实出海用户",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "透明资费中继节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "资费透明、无虚高宣传的真实测速高性价比服务商。",
        "features": "真实测速 / 透明资费 / 线路稳健",
        "support": "在线工单答疑"
    },
    {
        "file": "jilianyun.md",
        "name": "极连云",
        "rank": "精选推荐",
        "aff_url": "https://kdjhao.jlyvipaff.com/#/?code=rO50GIZj",
        "coupon": "jly888",
        "coupon_desc": "jly888 (专享特惠)",
        "price": "官网结算页为准 (使用优惠码 jly888 享特惠)",
        "users": "需要自动化更新订阅用户",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "自动化调度节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "极速连通与自动化订阅维护的可靠服务商。",
        "features": "极速连通 / 自动化订阅 / 节点稳定",
        "support": "社群支持与技术指导"
    },
    {
        "file": "guangnianti.md",
        "name": "光年梯",
        "rank": "精选推荐",
        "aff_url": "https://ggmq.gntaff.com/#/?code=34i9Naos",
        "coupon": "gnt888",
        "coupon_desc": "gnt888 (特惠码)",
        "price": "官网结算页为准 (使用优惠码 gnt888 享特惠)",
        "users": "多备用线路人群 / 跨境查阅",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "全节点高可用中继",
        "regions": "香港、日本、新加坡、美国",
        "intro": "备用节点充裕、全天候高可用的代理服务商。",
        "features": "全节点中继 / 高可用性 / 备用线路多",
        "support": "工单技术客服"
    },
    {
        "file": "sogoyun.md",
        "name": "Sogo云",
        "rank": "精选推荐",
        "aff_url": "https://wzjc.sogoyunaff.cc/#/?code=nWA62UuJ",
        "coupon": "sogo888",
        "coupon_desc": "sogo888 (8折优惠)",
        "price": "官网结算页为准 (使用优惠码 sogo888 享 8 折)",
        "users": "亚太节点偏好者 / 流媒体解锁人群",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "BGP 多线 / 亚太节点密集",
        "regions": "香港、日本、新加坡、韩国、台湾",
        "intro": "亚太地区节点密集、BGP 多线优化服务商。",
        "features": "BGP多线 / 流媒体支持 / 亚太节点密集",
        "support": "在线问题处理"
    },
    {
        "file": "yuzhoucloud.md",
        "name": "宇宙云 YuZhou",
        "rank": "精选推荐",
        "aff_url": "https://wzjc.yuzoucloud.cc/#/?code=hMqs74rd",
        "coupon": "yuzhou88",
        "coupon_desc": "yuzhou88 (折扣特惠)",
        "price": "官网结算页为准 (使用优惠码 yuzhou88 享折扣)",
        "users": "高并发下载 / 大流量传输",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "负载均衡多节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "适合高并发请求与大流量传输的负载均衡服务商。",
        "features": "多节点均衡 / 低延迟 / 适合高并发",
        "support": "工单快速答疑"
    },
    {
        "file": "ermaoyun.md",
        "name": "二猫云 2mao",
        "rank": "精选推荐",
        "aff_url": "https://waaa.2maoyunaff.cc/#/?code=tbIH9UGF",
        "coupon": "2mao888",
        "coupon_desc": "2mao888 (立减特惠)",
        "price": "官网结算页为准 (使用优惠码 2mao888 享立减)",
        "users": "学生党 / 新手试用",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "低价亲民中继",
        "regions": "香港、日本、新加坡",
        "intro": "资费亲民、新手上手快的低门槛云端服务商。",
        "features": "新手适用 / 快捷配置 / 资费亲民",
        "support": "图文指引与帮助文档"
    },
    {
        "file": "yifanyun.md",
        "name": "一翻云 1fly",
        "rank": "精选推荐",
        "aff_url": "https://wzjc.1flyunaff.cc/#/?code=vq9IugSn",
        "coupon": "1fly888",
        "coupon_desc": "1fly888 (8折优惠)",
        "price": "官网结算页为准 (使用优惠码 1fly888 享 8 折)",
        "users": "按月灵活用量人群",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "一键导入优化线路",
        "regions": "香港、日本、新加坡、美国",
        "intro": "按月计费灵活、连通率高的实用代理服务商。",
        "features": "一键导入 / 线路优化 / 连通率高",
        "support": "在线工单回复"
    },
    {
        "file": "edgenova.md",
        "name": "边缘节点 EdgeNova",
        "rank": "精选推荐",
        "aff_url": "https://work.edgenovaaff.cc/#/?code=6Mi7km72",
        "coupon": "edge888",
        "coupon_desc": "edge888 (专享优惠)",
        "price": "官网结算页为准 (使用优惠码 edge888 享优惠)",
        "users": "分布式边缘接入需求人群",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "分布式边缘节点 / 智能路由",
        "regions": "香港、日本、新加坡、美国、欧洲",
        "intro": "基于分布式边缘计费与智能路由调度的先进服务商。",
        "features": "分布式节点 / 智能路由 / 响应迅捷",
        "support": "工单与技术支持"
    },
    {
        "file": "kexinyun.md",
        "name": "可信云",
        "rank": "精选推荐",
        "aff_url": "https://work.kosingaff.com/#/?code=BmIpbeEn",
        "coupon": "kx888",
        "coupon_desc": "kx888 (安全特惠)",
        "price": "官网结算页为准 (使用优惠码 kx888 享特惠)",
        "users": "跨境业务 / 稳定办公保障者",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "加密安全传输节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "注重数据传输安全与高稳定不掉线的保障型服务商。",
        "features": "数据加密 / 稳定不掉线 / 跨境保障",
        "support": "24小时安全技术解答"
    },
    {
        "file": "sujie.md",
        "name": "速界 SuJie",
        "rank": "精选推荐",
        "aff_url": "https://work.speedworldaff.cc/#/?code=YhcpJLbr",
        "coupon": "sujie88",
        "coupon_desc": "sujie88 (优惠码)",
        "price": "官网结算页为准 (使用优惠码 sujie88 享优惠)",
        "users": "高速大带宽需求人群",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "全平台兼容高速节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "传输迅捷、低延迟的高速全平台兼容代理服务商。",
        "features": "高速带宽 / 全平台兼容 / 低延迟传输",
        "support": "后台即时解答"
    },
    {
        "file": "kuaili.md",
        "name": "快狸 KuaiLi",
        "rank": "精选推荐",
        "aff_url": "https://work.kuailicloud.cc/#/?code=7BsufMC0",
        "coupon": "kuaili88",
        "coupon_desc": "kuaili88 (折扣码)",
        "price": "官网结算页为准 (使用优惠码 kuaili88 享折扣)",
        "users": "灵活流量用户",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "快捷连通节点",
        "regions": "香港、日本、新加坡",
        "intro": "快速连通、稳定导入的快捷代理服务商。",
        "features": "快速连通 / 稳定线路 / 简单导入",
        "support": "图文指引"
    },
    {
        "file": "wuyou.md",
        "name": "无忧",
        "rank": "精选推荐",
        "aff_url": "https://wep01.worryfreeaff.com/#/?code=vak0gPse",
        "coupon": "worryfree88",
        "coupon_desc": "worryfree88 (立减优惠)",
        "price": "官网结算页为准 (使用优惠码 worryfree88 享立减)",
        "users": "省心追剧 / 避坑优选",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "多出口省心节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "稳定省心、多出口传输的避坑优选品牌。",
        "features": "稳定省心 / 多出口传输 / 避坑优选",
        "support": "售后工单支持"
    },
    {
        "file": "lingmao.md",
        "name": "灵猫",
        "rank": "精选推荐",
        "aff_url": "https://vip02.civetaff.com/#/?code=Z4KLo3Wz",
        "coupon": "civet88",
        "coupon_desc": "civet88 (8折特惠)",
        "price": "官网结算页为准 (使用优惠码 civet88 享 8 折)",
        "users": "基础/大流量用户",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "低延迟灵敏节点",
        "regions": "香港、日本、新加坡",
        "intro": "接入灵敏、低延迟的优质品牌。",
        "features": "灵敏接入 / 低延迟 / 兼容各大客户端",
        "support": "在线文档帮助"
    },
    {
        "file": "flashleap.md",
        "name": "闪跃 FlashLeap",
        "rank": "精选推荐",
        "aff_url": "https://vip02.flashleapaff.com/#/?code=wnLaKVaU",
        "coupon": "flash888",
        "coupon_desc": "flash888 (专享特惠)",
        "price": "官网结算页为准 (使用优惠码 flash888 享特惠)",
        "users": "极速传输 / 专线需求者",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "IPLC 闪速专线节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "闪速连接、IPLC 专线物理内网传输品牌。",
        "features": "闪速连接 / IPLC节点 / 专线传输",
        "support": "工单技术解答"
    },
    {
        "file": "firefly.md",
        "name": "飞为 (Firefly)",
        "rank": "精选推荐",
        "aff_url": "https://vip02.fireflyaff.com/#/?code=1n1ZIJab",
        "coupon": "firefly88",
        "coupon_desc": "firefly88 (特惠码)",
        "price": "官网结算页为准 (使用优惠码 firefly88 享特惠)",
        "users": "流媒体解封 / 4K追剧党",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "高清流媒体解封节点",
        "regions": "香港、日本、新加坡、美国",
        "intro": "流媒体解封出色、解锁 4K 追剧稳定运行。",
        "features": "流媒体解封 / 稳定运行 / 解锁4K追剧",
        "support": "在线工单支持"
    },
    {
        "file": "kuajie.md",
        "name": "跨界",
        "rank": "精选推荐",
        "aff_url": "https://vip02.kuajieaff.com/#/?code=RQ4b2tfV",
        "coupon": "kuajie888",
        "coupon_desc": "kuajie888 (专享优惠)",
        "price": "官网结算页为准 (使用优惠码 kuajie888 享优惠)",
        "users": "跨境办公 / 外贸电商业者",
        "devices": "Windows / macOS / iOS / Android",
        "nodes": "多出口跨境专属节点",
        "regions": "香港、日本、新加坡、美国、欧洲",
        "intro": "专为跨境外贸与多出口 IP 诉求打造的服务商。",
        "features": "跨境办公 / 稳定外贸 / 多出口IP",
        "support": "技术团队工单答疑"
    }
]

dir_path = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\providers"

for item in providers_data:
    filepath = os.path.join(dir_path, item["file"])
    if not os.path.exists(filepath):
        print(f"Skipping {item['file']} because it doesn't exist.")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Create the structured specification grid HTML string
    spec_html = f'''
<div class="provider-spec-card">
  <div class="spec-card-header">
    <span class="spec-rank">{item["rank"]}</span>
    <h3 class="spec-title">{item["name"]} 核心规格与配置矩阵</h3>
  </div>
  
  <div class="spec-grid">
    <div class="spec-item">
      <span class="spec-label">💰 套餐价格</span>
      <span class="spec-val"><strong>{item["price"]}</strong></span>
    </div>
    <div class="spec-item">
      <span class="spec-label">👥 使用用户</span>
      <span class="spec-val"><strong>{item["users"]}</strong></span>
    </div>
    <div class="spec-item">
      <span class="spec-label">💻 支持设备</span>
      <span class="spec-val"><strong>{item["devices"]}</strong></span>
    </div>
    <div class="spec-item">
      <span class="spec-label">⚡ 节点线路</span>
      <span class="spec-val"><strong>{item["nodes"]}</strong></span>
    </div>
    <div class="spec-item">
      <span class="spec-label">🌐 服务地区</span>
      <span class="spec-val"><strong>{item["regions"]}</strong></span>
    </div>
    <div class="spec-item">
      <span class="spec-label">🎟️ 专属优惠码</span>
      <span class="spec-val"><code class="coupon-highlight">{item["coupon_desc"]}</code></span>
    </div>
    <div class="spec-item full-width">
      <span class="spec-label">📝 品牌简介</span>
      <span class="spec-val">{item["intro"]}</span>
    </div>
    <div class="spec-item full-width">
      <span class="spec-label">✨ 核心特点</span>
      <span class="spec-val"><strong>{item["features"]}</strong></span>
    </div>
    <div class="spec-item full-width">
      <span class="spec-label">💬 专业咨询与支持</span>
      <span class="spec-val">{item["support"]}</span>
    </div>
  </div>

  <div class="spec-cta-row">
    <a href="{item["aff_url"]}" target="_blank" rel="sponsored nofollow noopener" class="btn-mod-primary">👉 前往 {item["name"]} 官网注册享受优惠通道 →</a>
  </div>
</div>
'''

    # Replace Section 1 or insert right after heading
    # Find existing "## 1. 简要概述与推荐度" or replace it cleanly
    if "## 1. 简要概述与推荐度" in content:
        parts = content.split("## 1. 简要概述与推荐度")
        header = parts[0]
        remainder = parts[1]
        
        # If there's a Section 2 ("---" or "## 2. 核心优势"), split it
        if "## 2. 核心优势" in remainder:
            sec2_parts = remainder.split("## 2. 核心优势")
            new_content = header + "## 1. 简要概述与规格矩阵\n\n" + spec_html + "\n\n---\n\n## 2. 核心优势" + sec2_parts[1]
        else:
            new_content = header + "## 1. 简要概述与规格矩阵\n\n" + spec_html + "\n\n" + remainder
    else:
        # Fallback: append after front matter
        fm_end = content.find("---", 4)
        if fm_end != -1:
            new_content = content[:fm_end+3] + "\n\n" + spec_html + "\n\n" + content[fm_end+3:]
        else:
            new_content = content + "\n\n" + spec_html

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Updated all 28 provider review articles successfully!")
