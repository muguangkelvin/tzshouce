# SEO Profile Replacement Contract - tzshouce.cyou

本文档定义后续全站 SEO 关键词、Hero 标语、页脚说明、导航结构及文章集的批量替换规约。

## 1. 替换数据接口规范

替换操作只需更新 `docs/site-seo-profile.json` 中的字段，并重新执行构建脚本 `build_site.py`。

### 必填替换字段
- `siteTopic`
- `primaryKeywords`
- `secondaryKeywords`
- `longTailKeywords`
- `heroKeywords`
- `footerKeywords`
- `navigationItems`

## 2. 301 重定向与旧 URL 处理规则

若导航或文章 URL 发生变更：
1. 建立旧 URL 到最相近新 URL 的 mapping。
2. 保留合规与法律页面 (`/privacy/`, `/terms/`, `/disclaimer/`, `/about/`, `/contact/`)。
3. 扫描并确保无残留断链。
