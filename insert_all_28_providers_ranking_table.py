import os

providers_28_data = [
    ("🥇 1", "灵动云", "官网为准 (用码8折)", "多节点智能分流 / IPLC专线 / 4K秒开 / 原生IP解封", "ld88 (8折)", "/providers/lingdongyun/", "https://varnexa.lingdongaff.com/#/?code=JoIy7bO1"),
    ("🥈 2", "暮光网络", "¥20/月起 (用码8折)", "晚高峰4K秒开 / 大流量影音 / 稳定低延迟 / 全解锁", "mm88 (8折)", "/providers/twilight/", "https://varnexa.twilightaff.com/#/?code=KvGly3jY"),
    ("🥉 3", "飞猫云", "折合¥7/月起 (用码8折)", "IEPL专线 / 包含自研一键客户端 / 极速稳健", "flycat888 (8折)", "/providers/flycat-cloud/", "https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH"),
    ("🎖️ 4", "微风网络 Breezenet", "结算页为准 (用码8折)", "中继+直连 / 兼容主流客户端 / 小白年付适用", "breeze88 (8折)", "/providers/breezenet/", "https://edp01.breezenetaff.com/#/?code=He4n3zxg"),
    ("5", "隐形人", "官网结算页为准", "高隐匿传输 / 防封锁加密节点 / 节点稳定", "yxr888", "/providers/yinxingren/", "https://varnexa.invisibleaff.com/#/?code=FlyoraeM"),
    ("6", "浪网 WaveNet", "官网结算页为准", "千兆大带宽 / 4K/8K 影音加载快 / 稳定输出", "wave888", "/providers/wavenet/", "https://varnexa.wavenetaff.com/#/?code=a9HF4LBZ"),
    ("7", "梯子云 LadderCloud", "官网结算页为准", "节点订阅转换支持 / 小白一键扫码 / 零门槛", "ladder88", "/providers/laddercloud/", "https://varnexa.ladderaff.com/#/?code=bYVSMHMh"),
    ("8", "飞V", "官网结算页为准", "多端极速适配 / 性价比节点 / 支持极速切换", "flyv888", "/providers/feiv/", "https://varnexa.flyvaff.com/#/?code=qaMgTyhY"),
    ("9", "全球云", "¥20/月起 (用码8折)", "IPLC专线 / 原生IP / ChatGPT+Netflix全解封", "qq88 (8折)", "/providers/quanqiu-cloud/", "https://sswdh.gcvipaff.com/#/?code=Ys0xKqnU"),
    ("10", "星岛梦", "官网结算页为准", "优质中继 / 低延迟节点 / 全端订阅导入", "xdm888", "/providers/xingdaomeng/", "https://kfccbb.xingdaomeng.com/#/?code=tLbhLnNf"),
    ("11", "光速云", "官网结算页为准", "极速响应 / 4K秒开 / 适配流畅追剧", "gsy888", "/providers/guangshuyun/", "https://mdlky.gsyaff.com/#/?code=5snwJVcD"),
    ("12", "唯兔云 (V2云)", "官网结算页为准", "V2ray协议 / 稳定防封 / 传输稳健", "v2yun88", "/providers/weituyun/", "https:/fast.v2yunvipaff.com/#/?code=xkiG3YWN"),
    ("13", "U1S1 (有一说一)", "官网结算页为准", "真实测速 / 透明资费 / 线路稳健", "u1s1888", "/providers/u1s1/", "https://pkdj7.vipaff.cc/#/?code=nYbe5pKy"),
    ("14", "极连云", "官网结算页为准", "极速连通 / 自动化订阅 / 节点稳定", "jly888", "/providers/jilianyun/", "https://kdjhao.jlyvipaff.com/#/?code=rO50GIZj"),
    ("15", "光年梯", "官网结算页为准", "全节点中继 / 高可用性 / 备用线路多", "gnt888", "/providers/guangnianti/", "https://ggmq.gntaff.com/#/?code=34i9Naos"),
    ("16", "Sogo云", "官网结算页为准", "BGP多线 / 流媒体支持 / 亚太节点密集", "sogo888", "/providers/sogoyun/", "https://wzjc.sogoyunaff.cc/#/?code=nWA62UuJ"),
    ("17", "宇宙云 YuZhou", "官网结算页为准", "多节点均衡 / 低延迟 / 适合高并发", "yuzhou88", "/providers/yuzhoucloud/", "https://wzjc.yuzoucloud.cc/#/?code=hMqs74rd"),
    ("18", "二猫云 2mao", "官网结算页为准", "新手适用 / 快捷配置 / 资费亲民", "2mao888", "/providers/ermaoyun/", "https://waaa.2maoyunaff.cc/#/?code=tbIH9UGF"),
    ("19", "一翻云 1fly", "官网结算页为准", "一键导入 / 线路优化 / 连通率高", "1fly888", "/providers/yifanyun/", "https://wzjc.1flyunaff.cc/#/?code=vq9IugSn"),
    ("20", "边缘节点 EdgeNova", "官网结算页为准", "分布式节点 / 智能路由 / 响应迅捷", "edge888", "/providers/edgenova/", "https://work.edgenovaaff.cc/#/?code=6Mi7km72"),
    ("21", "可信云", "官网结算页为准", "数据加密 / 稳定不掉线 / 跨境保障", "kx888", "/providers/kexinyun/", "https://work.kosingaff.com/#/?code=BmIpbeEn"),
    ("22", "速界 SuJie", "官网结算页为准", "高速带宽 / 全平台兼容 / 低延迟传输", "sujie88", "/providers/sujie/", "https://work.speedworldaff.cc/#/?code=YhcpJLbr"),
    ("23", "快狸 KuaiLi", "官网结算页为准", "快速连通 / 稳定线路 / 简单导入", "kuaili88", "/providers/kuaili/", "https://work.kuailicloud.cc/#/?code=7BsufMC0"),
    ("24", "无忧", "官网结算页为准", "稳定省心 / 多出口传输 / 避坑优选", "worryfree88", "/providers/wuyou/", "https://wep01.worryfreeaff.com/#/?code=vak0gPse"),
    ("25", "灵猫", "官网结算页为准", "灵敏接入 / 低延迟 / 兼容各大客户端", "civet88", "/providers/lingmao/", "https://vip02.civetaff.com/#/?code=Z4KLo3Wz"),
    ("26", "闪跃 FlashLeap", "官网结算页为准", "闪速连接 / IPLC节点 / 专线传输", "flash888", "/providers/flashleap/", "https://vip02.flashleapaff.com/#/?code=wnLaKVaU"),
    ("27", "飞为 (Firefly)", "官网结算页为准", "流媒体解封 / 稳定运行 / 解锁4K追剧", "firefly88", "/providers/firefly/", "https://vip02.fireflyaff.com/#/?code=1n1ZIJab"),
    ("28", "跨界", "官网结算页为准", "跨境办公 / 稳定外贸 / 多出口IP", "kuajie888", "/providers/kuajie/", "https://vip02.kuajieaff.com/#/?code=RQ4b2tfV")
]

# Generate rows HTML
rows_html = ""
for rank, name, price, feat, coupon, review_url, aff_url in providers_28_data:
    rows_html += f"""
        <tr>
          <td style="text-align: center;"><strong>{rank}</strong></td>
          <td><a href="{review_url}"><strong>{name}</strong></a></td>
          <td>{price}</td>
          <td>{feat}</td>
          <td><code class="coupon-highlight">{coupon}</code></td>
          <td style="text-align: center;"><a href="{review_url}" class="btn-review-link">查看测评</a></td>
          <td style="text-align: center;"><a href="{aff_url}" target="_blank" rel="sponsored nofollow noopener" class="btn-aff-cta">官网注册 →</a></td>
        </tr>"""

table_html = f"""
<div class="plans-table-card">
  <h3 class="plans-card-title">📊 2026 年 28 家机场节点与资费全量对比大盘点</h3>
  <div class="table-wrapper">
    <table class="plans-detail-table">
      <thead>
        <tr>
          <th style="width: 75px; text-align: center;">排名</th>
          <th style="min-width: 140px;">机场品牌</th>
          <th style="min-width: 120px;">全部套餐价格</th>
          <th style="min-width: 220px;">线路类型与解锁特点</th>
          <th style="min-width: 130px;">专属优惠码</th>
          <th style="width: 100px; text-align: center;">机场测评</th>
          <th style="width: 120px; text-align: center;">官方注册</th>
        </tr>
      </thead>
      <tbody>{rows_html}
      </tbody>
    </table>
  </div>
  <div class="plans-notice">
    💡 <strong>选购说明与优惠提示</strong>：以上 28 家机场均经过全站定期实测。下单结算时请使用对应的专属优惠码享受折扣。首推榜首 <strong style="color: #2563eb;">灵动云 (优惠码 ld88)</strong> 与 <strong style="color: #7c3aed;">暮光网络 (优惠码 mm88)</strong>。
  </div>
</div>
"""

# Targets to update
target_files = [
    r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jichang-tuijian\jichang-tuijian-article-12.md",
    r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jichang-tuijian\jichang-tuijian-article-1.md"
]

for target_file in target_files:
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Update Section 1
        new_section_1 = f"## 1. 全站 28 家机场节点与资费全量对比大盘点 (含测评与官方注册通道)\n\n" + table_html

        if "## 1. 本站精选四大主推服务商对比矩阵" in content:
            content = content.replace("## 1. 本站精选四大主推服务商对比矩阵\n\n| 排名 | 机场品牌 | 参考价格 | 线路类型 | 专属优惠码 | 官网注册通道 |\n| :---: | :--- | :--- | :--- | :---: | :---: |\n| **🥇 1** | **灵动云** | 官网为准 | 多节点智能分流 / IPLC专线 / 4K秒开 | `ld88` (8折) | <a href=\"https://varnexa.lingdongaff.com/#/?code=JoIy7bO1\" target=\"_blank\" rel=\"sponsored nofollow noopener\">官网直达 →</a> |\n| **🥈 2** | **暮光网络** | ¥20/月起 | 晚高峰4K秒开 / 大流量影音 | `mm88` (8折) | <a href=\"https://varnexa.twilightaff.com/#/?code=KvGly3jY\" target=\"_blank\" rel=\"sponsored nofollow noopener\">官网直达 →</a> |\n| **🥉 3** | **飞猫云** | 折合¥7/月 | IEPL专线 / 包含自研一键客户端 | `flycat888` (8折) | <a href=\"https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH\" target=\"_blank\" rel=\"sponsored nofollow noopener\">官网直达 →</a> |\n| **🎖️ 4** | **微风网络** | 结算页为准 | 中继+直连 / 兼容主流客户端 | `breeze88` (8折) | <a href=\"https://edp01.breezenetaff.com/#/?code=He4n3zxg\" target=\"_blank\" rel=\"sponsored nofollow noopener\">官网直达 →</a> |", new_section_1)
        elif "## 1. " in content:
            # Replace section 1 heading
            parts = content.split("## 1. ")
            header = parts[0]
            remainder = parts[1]
            # split at next section ## 2.
            sec2_split = remainder.split("## 2. ")
            content = header + new_section_1 + "\n\n---\n\n## 2. " + sec2_split[1]

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

print("Successfully inserted full 28-provider ranking & comparison table into ranking articles!")
