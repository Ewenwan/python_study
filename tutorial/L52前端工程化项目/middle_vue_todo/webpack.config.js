const path = require('path')
const HTMLPlugin = require('html-webpack-plugin')
const webpack = require('webpack')
const ExtractPlugin = require('extract-text-webpack-plugin')

const isDev = process.env.NODE_ENV === 'development'

const config = {
    target: 'web',
    entry: path.join(__dirname, 'src/index.js'),
    output: {
        filename: 'bundle.[hash:8].js',
        path: path.join(__dirname, 'dist')
    },
    module: {
        rules: [
            {
                test: /.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /.jsx$/,
                loader: 'babel-loader'
            },
            {
                test: /\.(gif|jpg|jpeg|png|svg)$/,
                use: [
                    {
                        loader: 'url-loader',
                        options:{
                            limit: 1024,
                            name: '[name]-aaa.[ext]'
                        }
                    }
                ]
            },
        ]
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: isDev ? '"development"' : '"production"'
            }
        }),
        new HTMLPlugin()
    ]
}

if (isDev){
    config.module.rules.push({
        test: /.styl$/,
        use: [
        'style-loader',
        'css-loader',
        {
            loader: "postcss-loader",  // 自动为不同浏览器内核添加--webkit前缀之类的
            options: {
                sourceMap: true,
            }
        },
        'stylus-loader'
        ]
    })
    config.devtool = '#cheap-module-eval-source-map'    // 浏览器中调试为原代码
    config.devServer = {
        port: 8000,
        host: '0.0.0.0',
        overlay: {
            errors: true,
        },
        // open: false,
        // historyFallback: {
        //
        // },
        // hot: true
    }
    config.plugins.push(
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin()
    )
} else {
    config.entry = {
        app: path.join(__dirname, 'src/index.js'),
        vendor: ['vue']
    }
    config.output.filename = '[name].[chunkhash:8].js'
    config.module.rules.push(
        {
          test: /\.styl/,
          use: ExtractPlugin.extract({
              fallback: 'style-loader',
              use: [
                  'css-loader',
                  {
                      loader: 'postcss-loader',
                      options: {
                          sourceMap: true,
                      }
                  },
                  'stylus-loader'
              ]
          })
        },
    )
    config.plugins.push(
        new ExtractPlugin('styles.[contentHash: 8].css'),
        new webpack.optimize.CommonsChunkPlugin({    // 把类库跟业务代码分开打包
            name: 'vendor'
        }),
        new webpack.optimize.CommonsChunkPlugin({   // 添加模块后hash不变
            name: 'runtime'
        })
    )
}

module.exports = config