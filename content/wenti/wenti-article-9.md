---
title: "安卓/iOS 手机后台杀进程导致断网的保活设置"
date: 2026-09-28T10:00:00+08:00
draft: false
description: "详细教程：指导在小米 MIUI、华为 HarmonyOS、vivo/oppo 及 iOS 上配置代理应用后台白名单。"
summary: "详细教程：指导在小米 MIUI、华为 HarmonyOS、vivo/oppo 及 iOS 上配置代理应用后台白名单。"
keywords: ["科学上网", "排错指南", "Clash配置", "灵动云", "暮光网络"]
---

# 安卓/iOS 手机后台杀进程导致断网的保活设置

在智能手机锁屏或切换应用后，常常发现后台 Clash for Android 或 Shadowrocket 被系统彻底清杀，导致断网或频繁重连。

---

## 1. 安卓 (Android) 系统保活 4 大设置

1. **允许自启动**：在【应用权限】中将 Clash / v2rayNG 开启【自启动】与【关联启动】。
2. **省电策略设为无限制**：进入【电池与性能】 -> 【应用省电策略】，选为【无限制】。
3. **多任务卡片加锁**：在后台任务列表中，长按应用卡片并点击【小锁】图标。
4. **忽略电池优化**：允许应用在后台高能耗运行。

---

## 2. iOS (iPhone / iPad) 保活技巧

iOS 系统机制相对严格，开启 Shadowrocket 或 Quantumult X 后，尽量不要在后台彻底划掉 App，让系统 VPN 进程驻留即可。
