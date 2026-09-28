import os
import re

top4_html = """
<div class="plans-table-card">
  <h3 class="plans-card-title">⚡ 本站精选四大主推服务商对比矩阵</h3>
  <div class="table-wrapper">
    <table class="plans-detail-table">
      <thead>
        <tr>
          <th style="width: 75px; text-align: center;">排名</th>
          <th style="min-width: 140px;">机场品牌</th>
          <th style="min-width: 120px;">参考价格</th>
          <th style="min-width: 220px;">线路类型与解锁特点</th>
          <th style="min-width: 130px;">专属优惠码</th>
          <th style="width: 120px; text-align: center;">官方注册</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="text-align: center;"><strong>🥇 1</strong></td>
          <td><a href="/providers/lingdongyun/"><strong>灵动云</strong></a></td>
          <td>官网为准 (用码8折)</td>
          <td>多节点智能分流 / IPLC专线 / 4K秒开 / 原生IP解封</td>
          <td><code class="coupon-highlight">ld88 (8折)</code></td>
          <td style="text-align: center;"><a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" class="btn-aff-cta">官网注册 →</a></td>
        </tr>
        <tr>
          <td style="text-align: center;"><strong>🥈 2</strong></td>
          <td><a href="/providers/twilight/"><strong>暮光网络</strong></a></td>
          <td>¥20/月起 (用码8折)</td>
          <td>晚高峰4K秒开 / 大流量影音 / 稳定低延迟 / 全解锁</td>
          <td><code class="coupon-highlight">mm88 (8折)</code></td>
          <td style="text-align: center;"><a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener" class="btn-aff-cta">官网注册 →</a></td>
        </tr>
        <tr>
          <td style="text-align: center;"><strong>🥉 3</strong></td>
          <td><a href="/providers/flycat-cloud/"><strong>飞猫云</strong></a></td>
          <td>折合¥7/月起 (用码8折)</td>
          <td>IEPL专线 / 包含自研一键客户端 / 极速稳健</td>
          <td><code class="coupon-highlight">flycat888 (8折)</code></td>
          <td style="text-align: center;"><a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener" class="btn-aff-cta">官网注册 →</a></td>
        </tr>
        <tr>
          <td style="text-align: center;"><strong>🎖️ 4</strong></td>
          <td><a href="/providers/breezenet/"><strong>微风网络 Breezenet</strong></a></td>
          <td>结算页为准 (用码8折)</td>
          <td>中继+直连 / 兼容主流客户端 / 小白年付适用</td>
          <td><code class="coupon-highlight">breeze88 (8折)</code></td>
          <td style="text-align: center;"><a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener" class="btn-aff-cta">官网注册 →</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

jichang_dir = r"c:\Users\USER\Desktop\博客\tzshouce.cyou\content\jichang-tuijian"

for f_name in os.listdir(jichang_dir):
    if not f_name.endswith(".md"):
        continue
    f_path = os.path.join(jichang_dir, f_name)
    with open(f_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace plain markdown table in jichang-tuijian articles with styled HTML card table
    if "| 排名 | 机场品牌 | 参考价格 |" in content or "| 排名 | 机场品牌 |" in content:
        # Replace the markdown table block
        content = re.sub(
            r"\| 排名 \| 机场品牌 \|.*?\n(?:\|.*?\n)+",
            top4_html + "\n",
            content,
            flags=re.MULTILINE
        )
        with open(f_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Upgraded all article tables to rich, beautifully styled HTML card tables!")
