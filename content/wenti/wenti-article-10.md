---
title: "如何配置客户端自动更新订阅与智能策略分流"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "教你在 Clash Verge / Stash / Surge 中设置 24 小时自动更新订阅及域名规则分流。"
summary: "教你在 Clash Verge / Stash / Surge 中设置 24 小时自动更新订阅及域名规则分流。"
keywords: ["科学上网", "排错指南", "Clash配置", "灵动云", "暮光网络"]
---

# 如何配置客户端自动更新订阅与智能策略分流

保持订阅更新是确保机场节点始终可用的关键。手写配置太麻烦？教你设置全自动更新与规则分流。

---

## 1. 设置客户端定时自动更新

在 **Clash Verge Rev** 中：
1. 点击左侧【订阅 / Profiles】菜单。
2. 右键目标订阅，选择【编辑 / Edit】。
3. 设置【更新间隔 / Update Interval】为 `1440` 分钟（即 24 小时）。
4. 勾选【静默更新】。

---

## 2. 智能策略分流配置 (Rule Mode)

务必确认代理模式选择为 `Rule 规则模式`：
- **Domestic / Direct**：国内微信、淘宝、百度流量直连，不耗机场流量。
- **Global / Proxy**：Google、YouTube、ChatGPT 走节点加速。
- **Reject**：自动拦截广告与追踪脚本。
