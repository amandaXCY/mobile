const path = require('path');
const HTMLPlugin = require('html-webpack-plugin');
const webpack = require('webpack')


console.log(path.resolve(__dirname, 'website'))
module.exports = {
    context: path.resolve(__dirname, './'),
    entry: ['./src/app.js'],
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'dist'),
    },
    devServer: {
        port: 8080,
        contentBase: path.resolve('__dirname', 'dist'),
        publicPath: '/',
    },
    module:{
      rules:[
          {
              loader: 'file-loader',
              type: 'javascript/auto',
              exclude: [/\.js$/, /\.html$/, /\.json$/]
          }
      ],
    },

    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new HTMLPlugin({
            template: path.resolve(__dirname, './index.html'),
            filename: 'index.html',
            inject: 'body',
        })
    ],
}
