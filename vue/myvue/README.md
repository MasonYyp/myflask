# Secretary

### 1 功能介绍
主系统，主要展示系统模块，包括多个子系统。

### 2 常用命令
```
# 清除缓存
npm cache clean --force
# 启动服务
npm run serve
# 编译发布
npm run build
```

### 3 必备的基础安装包
```

使用vue2，尽量先不用vue3

js-base64
cnpm install  --save js-base64@3.6.0

axios
cnpm install axios@0.24.0 --save

qs
cnpm install qs@6.10.1 --save

vue-router
cnpm install vue-router@3.5.2 --save

vuex
cnpm install vuex@3.6.2 --save

echart
cnpm install echarts@4.8.0 --save

echarts-wordcloud
cnpm install echarts-wordcloud@1.1.3 --save

element-ui
cnpm install element-ui@2.15.6 --save

svg.js(version:3)
cnpm install @svgdotjs/svg.js@3.1.1 --save

quill（富文本编辑器）
cnpm install vue-quill-editor@3.0.6 --save
// 实现拖拽图片
cnpm install quill@1.3.7 --save
cnpm install quill-image-resize-module@3.0.0 --save
cnpm install quill-image-drop-module@1.0.3 --save

jsmind(思维导图)
cnpm install jsmind@0.4.6 --save

jsplumb(绘制流程图)
cnpm install jsplumb@2.15.6 --save

vuedraggable(组件拖拽)
cnpm install vuedraggable@2.24.3 --save

canvg(svg转canvas)
cnpm install canvg@1.5.3 --save

html2canvas(html转canvas)
cnpm install html2canvas@1.3.2 --save

swiper（轮播），注意此处不需要安装swiper
cnpm install vue-awesome-swiper@3.1.3 --save-dev

less（less-loader版本不能过高）
cnpm install less@4.1.1 --save-dev
cnpm install less-loader@6.0.0 --save-dev

```

## 4 必备代码调试插件
```
代码提示工具（eslint），在初始化项目时会自动添加此组件；

手动安装
格式工具（vetur）

格式化工具（prettier -code formatter）

```
