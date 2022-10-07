// 解决import模块quill-image-resize-module错误
const webpack = require('webpack')
module.exports = {
    chainWebpack: config => {
        config.plugin('provide').use(webpack.ProvidePlugin, [{
            'window.Quill': 'quill/dist/quill.js',
            'Quill': 'quill/dist/quill.js'
        }]);
    }
}

module.exports = {
    outputDir: 'test',
    devServer:{
        proxy:{
            '/flask':{
                target:'http://127.0.0.1:5000',
                changOrigin: true
            }
        }
    },
    publicPath: './' 
}
