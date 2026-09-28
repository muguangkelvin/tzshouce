import os

providers_28_complete = [
    ("🥇 1", "灵动云", "¥15/月起 (用码8折)", "香港、日本、新加坡、美国、台湾、韩国、欧洲等 30+ 节点", "IPLC物理专线 / 多节点智能分流 / 4K秒开 / 原生IP解封", "Win/Mac/iOS(小火箭)/Android/Linux/路由器全通用", "100GB-800GB/月 (含不限时包)", "ld88 (8折)", "/providers/lingdongyun/", "https://varnexa.lingdongaff.com/#/?code=JoIy7bO1"),
    ("🥈 2", "暮光网络", "¥20/月起 (用码8折)", "香港、日本、新加坡、美国、台湾、德国", "高质BGP中继 / 优质专线 / 晚高峰4K秒开 / 全流媒体解锁", "Win/Mac/iOS/Android/TVBox全通用", "120GB-1500GB/月 (含300G按量包)", "mm88 (8折)", "/providers/twilight/", "https://varnexa.twilightaff.com/#/?code=KvGly3jY"),
    ("🥉 3", "飞猫云", "折合 ¥7/月起 (用码8折)", "香港、日本、新加坡、美国、韩国", "IEPL专线 / 包含自研一键客户端 / 极速稳健", "Win/Mac/iOS/Android (含自研客户端)", "50GB-500GB/月 (含200G按量包)", "flycat888 (8折)", "/providers/flycat-cloud/", "https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH"),
    ("🎖️ 4", "微风网络 Breezenet", "¥12/月起 (用码8折)", "香港、日本、新加坡、美国", "中继+直连混合 / 高连通率 / 适合轻量外贸", "Win/Mac/iOS/Android全通用", "80GB-600GB/月 (轻量大流量年付)", "breeze88 (8折)", "/providers/breezenet/", "https://edp01.breezenetaff.com/#/?code=He4n3zxg"),
    ("5", "隐形人", "¥18/月起", "香港、日本、新加坡、美国、英国", "高隐匿传输 / 防封锁加密节点 / 数据安全屏障", "Win/Mac/iOS/Android全通用", "100GB-800GB/月", "yxr888", "/providers/yinxingren/", "https://varnexa.invisibleaff.com/#/?code=FlyoraeM"),
    ("6", "浪网 WaveNet", "¥25/月起", "香港、日本、新加坡、美国、加拿大", "千兆大带宽 / 4K/8K 影音秒开 / 高吞吐量", "Win/Mac/iOS/Android/Linux全通用", "200GB-1200GB/月", "wave888", "/providers/wavenet/", "https://varnexa.wavenetaff.com/#/?code=a9HF4LBZ"),
    ("7", "梯子云 LadderCloud", "¥15/月起", "香港、日本、新加坡、美国、台湾", "节点订阅转换支持 / 小白一键扫码 / 零门槛", "Win/Mac/iOS/Android全通用", "80GB-800GB/月", "ladder88", "/providers/laddercloud/", "https://varnexa.ladderaff.com/#/?code=bYVSMHMh"),
    ("8", "飞V", "¥16/月起", "香港、日本、新加坡、美国", "Hysteria2 极速协议 / 多端适配 / 秒级握手", "Win/Mac/iOS/Android全通用", "100GB-1000GB/月", "flyv888", "/providers/feiv/", "https://varnexa.flyvaff.com/#/?code=qaMgTyhY"),
    ("9", "全球云", "¥20/月起 (用码8折)", "香港、日本、新加坡、美国", "IPLC专线 / 原生IP / ChatGPT+Netflix全解封", "Win/Mac/iOS/Android全通用", "120GB-1500GB/月", "qq88 (8折)", "/providers/quanqiu-cloud/", "https://sswdh.gcvipaff.com/#/?code=Ys0xKqnU"),
    ("10", "星岛梦", "¥15/月起", "香港、日本、新加坡、美国", "优质中继 / 低延迟节点 / 全端订阅导入", "Win/Mac/iOS/Android全通用", "100GB-500GB/月", "xdm888", "/providers/xingdaomeng/", "https://kfccbb.xingdaomeng.com/#/?code=tLbhLnNf"),
    ("11", "光速云", "¥18/月起", "香港、日本、新加坡、美国", "极速BGP / 4K秒开 / 适配流畅追剧", "Win/Mac/iOS/Android全通用", "150GB-800GB/月", "gsy888", "/providers/guangshuyun/", "https://mdlky.gsyaff.com/#/?code=5snwJVcD"),
    ("12", "唯兔云 (V2云)", "¥16/月起", "香港、日本、新加坡、美国", "V2ray加密 / 稳定防封 / 传输稳健", "Win/Mac/iOS/Android全通用", "100GB-600GB/月", "v2yun88", "/providers/weituyun/", "https:/fast.v2yunvipaff.com/#/?code=xkiG3YWN"),
    ("13", "U1S1 (有一说一)", "¥12/月起", "香港、日本、新加坡、美国", "真实测速 / 资费透明 / 线路稳健", "Win/Mac/iOS/Android全通用", "100GB-500GB/月", "u1s1888", "/providers/u1s1/", "https://pkdj7.vipaff.cc/#/?code=nYbe5pKy"),
    ("14", "极连云", "¥15/月起", "香港、日本、新加坡、美国", "极速连通 / 自动化订阅 / 节点稳定", "Win/Mac/iOS/Android全通用", "120GB-600GB/月", "jly888", "/providers/jilianyun/", "https://kdjhao.jlyvipaff.com/#/?code=rO50GIZj"),
    ("15", "光年梯", "¥18/月起", "香港、日本、新加坡、美国", "全节点中继 / 高可用性 / 备用线路多", "Win/Mac/iOS/Android全通用", "100GB-500GB/月", "gnt888", "/providers/guangnianti/", "https://ggmq.gntaff.com/#/?code=34i9Naos"),
    ("16", "Sogo云", "¥15/月起", "香港、日本、韩国、台湾", "BGP多线 / 流媒体支持 / 亚太节点密集", "Win/Mac/iOS/Android全通用", "150GB-800GB/月", "sogo888", "/providers/sogoyun/", "https://wzjc.sogoyunaff.cc/#/?code=nWA62UuJ"),
    ("17", "宇宙云 YuZhou", "¥22/月起", "香港、日本、新加坡、美国", "负载均衡 / 低延迟 / 适合高并发下载", "Win/Mac/iOS/Android全通用", "200GB-1000GB/月", "yuzhou88", "/providers/yuzhoucloud/", "https://wzjc.yuzoucloud.cc/#/?code=hMqs74rd"),
    ("18", "二猫云 2mao", "折合 ¥9.9/月起", "香港、日本、新加坡", "低门槛中继 / 新手适用 / 快捷配置", "Win/Mac/iOS/Android全通用", "50GB-300GB/月", "2mao888", "/providers/ermaoyun/", "https://waaa.2maoyunaff.cc/#/?code=tbIH9UGF"),
    ("19", "一翻云 1fly", "¥15/月起", "香港、日本、新加坡、美国", "按月计费 / 一键导入 / 连通率高", "Win/Mac/iOS/Android全通用", "100GB-500GB/月", "1fly888", "/providers/yifanyun/", "https://wzjc.1flyunaff.cc/#/?code=vq9IugSn"),
    ("20", "边缘节点 EdgeNova", "¥18/月起", "香港、日本、新加坡、欧洲", "分布式节点 / 智能路由 / 响应迅捷", "Win/Mac/iOS/Android全通用", "150GB-800GB/月", "edge888", "/providers/edgenova/", "https://work.edgenovaaff.cc/#/?code=6Mi7km72"),
    ("21", "可信云", "¥20/月起", "香港、日本、新加坡、美国", "数据加密 / 稳定不掉线 / 跨境保障", "Win/Mac/iOS/Android全通用", "100GB-600GB/月", "kx888", "/providers/kexinyun/", "https://work.kosingaff.com/#/?code=BmIpbeEn"),
    ("22", "速界 SuJie", "¥16/月起", "香港、日本、新加坡、美国", "高速带宽 / 全平台兼容 / 低延迟传输", "Win/Mac/iOS/Android全通用", "150GB-800GB/月", "sujie88", "/providers/sujie/", "https://work.speedworldaff.cc/#/?code=YhcpJLbr"),
    ("23", "快狸 KuaiLi", "¥12/月起", "香港、日本、新加坡", "快速连通 / 稳定线路 / 简单导入", "Win/Mac/iOS/Android全通用", "80GB-400GB/月", "kuaili88", "/providers/kuaili/", "https://work.kuailicloud.cc/#/?code=7BsufMC0"),
    ("24", "无忧", "¥15/月起", "香港、日本、新加坡、美国", "多出口传输 / 稳定省心 / 避坑优选", "Win/Mac/iOS/Android全通用", "100GB-500GB/月", "worryfree88", "/providers/wuyou/", "https://wep01.worryfreeaff.com/#/?code=vak0gPse"),
    ("25", "灵猫", "¥14/月起", "香港、日本、新加坡", "灵敏接入 / 低延迟 / 兼容各大客户端", "Win/Mac/iOS/Android全通用", "100GB-500GB/月", "civet88", "/providers/lingmao/", "https://vip02.civetaff.com/#/?code=Z4KLo3Wz"),
    ("26", "闪跃 FlashLeap", "¥20/月起", "香港、日本、新加坡、美国", "IPLC闪速专线 / 专线传输 / 零过墙", "Win/Mac/iOS/Android全通用", "150GB-800GB/月", "flash888", "/providers/flashleap/", "https://vip02.flashleapaff.com/#/?code=wnLaKVaU"),
    ("27", "飞为 (Firefly)", "¥18/月起", "香港、日本、新加坡、美国", "流媒体解封 / 解锁4K追剧 / 稳定运行", "Win/Mac/iOS/Android全通用", "120GB-600GB/月", "firefly88", "/providers/firefly/", "https://vip02.fireflyaff.com/#/?code=1n1ZIJab"),
    ("28", "跨界", "¥22/月起", "香港、日本、新加坡、美国、欧洲", "跨境办公 / 稳定外贸 / 多出口IP", "Win/Mac/iOS/Android全通用", "150GB-800GB/月", "kuajie888", "/providers/kuajie/", "https://vip02.kuajieaff.com/#/?code=RQ4b2tfV")
]

rows_html = ""
for rank, name, price, region, node, device, traffic, coupon, review_url, aff_url in providers_28_complete:
    rows_html += f"""
        <tr>
          <td style="text-align: center;"><strong>{rank}</strong></td>
          <td><a href="{review_url}"><strong>{name}</strong></a></td>
          <td><strong>{price}</strong></td>
          <td>{region}</td>
          <td>{node}</td>
          <td><span class="plan-badge">{device}</span></td>
          <td><strong>{traffic}</strong></td>
          <td><code class="coupon-highlight">{coupon}</code></td>
          <td style="text-align: center;"><a href="{review_url}" class="btn-review-link">详细测评</a></td>
          <td style="text-align: center;"><a href="{aff_url}" target="_blank" rel="sponsored nofollow noopener" class="btn-aff-cta">官网注册 →</a></td>
        </tr>"""

table_html = f"""
<div class="plans-table-card">
  <h3 class="plans-card-title">📊 2026 年 28 家机场节点与起步价格全量对比大盘点 (明确起步价)</h3>
  <div class="table-wrapper">
    <table class="plans-detail-table">
      <thead>
        <tr>
          <th style="width: 75px; text-align: center;">排名</th>
          <th style="min-width: 140px;">机场品牌</th>
          <th style="min-width: 120px;">最低起步价格</th>
          <th style="min-width: 150px;">服务地区</th>
          <th style="min-width: 220px;">节点线路与特点</th>
          <th style="min-width: 160px;">设备通用</th>
          <th style="min-width: 140px;">流量说明</th>
          <th style="min-width: 120px;">专属优惠码</th>
          <th style="width: 100px; text-align: center;">详细测评</th>
          <th style="width: 120px; text-align: center;">官方注册</th>
        </tr>
      </thead>
      <tbody>{rows_html}
      </tbody>
    </table>
  </div>
  <div class="plans-notice">
    💡 <strong>选购说明与优惠提示</strong>：以上 28 家机场均标注真实最低起步价格。下单结算时使用对应的优惠码即可享受专属折扣。
  </div>
</div>
"""

target_files = [
    r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jichang-tuijian\jichang-tuijian-article-12.md",
    r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jichang-tuijian\jichang-tuijian-article-1.md"
]

for target_file in target_files:
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()

        new_section_1 = f"## 1. 全站 28 家机场节点与起步价格全量对比大盘点 (包含全部 lowest 价格)\n\n" + table_html

        if "## 1. " in content:
            parts = content.split("## 1. ")
            header = parts[0]
            if "## 2. " in parts[1]:
                sec2_parts = parts[1].split("## 2. ")
                content = header + new_section_1 + "\n\n---\n\n## 2. " + sec2_parts[1]
            else:
                content = header + new_section_1

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

print("Updated ranking article with exact lowest starting prices for all 28 providers!")
