# 📦 Cloud Blog - 卡通活泼风格博客

这是一个可以在线发布文字帖子、浏览图片、评论互动的卡通活泼风格博客系统。  
支持 **Cloudinary 云存储**，可以安全存储和加载图片及文件。  

---

## ✨ 功能特色
- 📝 发布文字帖子
- 🖼️ 上传和浏览图片（支持大小限制）
- 💬 帖子评论区
- ☁️ Cloudinary 云存储支持
- 🎨 卡通活泼 UI 样式

---

## 🚀 一键部署到 Render

点击下方按钮，一键部署到 Render：

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/kornhauserhair495-stack/x)

---

## ⚙️ 部署后配置环境变量

在 Render 的 **Environment Variables** 中添加：

| 变量名 | 说明 |
|--------|------|
| `CLOUDINARY_CLOUD_NAME` | 你的 Cloudinary Cloud Name |
| `CLOUDINARY_API_KEY` | 你的 Cloudinary API Key |
| `CLOUDINARY_API_SECRET` | 你的 Cloudinary API Secret |

---

## 🌩️ Cloudinary 注册与配置步骤

1. **注册 Cloudinary**
   - 打开 [Cloudinary 官网](https://cloudinary.com/)
   - 点击 **Sign up for free** 注册账号
   - 注册完成后登录控制台（Dashboard）

2. **获取 API 信息**
   - 登录后进入 **Dashboard**
   - 在页面右上方找到 `Cloud name`（对应 `CLOUDINARY_CLOUD_NAME`）
   - 在 **API Environment variable** 区域找到：
     - `API Key`（对应 `CLOUDINARY_API_KEY`）
     - `API Secret`（对应 `CLOUDINARY_API_SECRET`）

3. **添加到 Render 环境变量**
   - 部署到 Render 后，在 Render 服务的 **Environment Variables** 中添加上述三个值
   - 保存后点击 **Deploy** 重新部署

4. **完成配置**
   - 部署完成后，访问你的 Render 项目地址即可在线使用

---

## 🖥️ 本地运行（可选）
如果你想在本地测试：

```bash
git clone https://github.com/kornhauserhair495-stack/x.git
cd x
pip install -r requirements.txt
python app.py
