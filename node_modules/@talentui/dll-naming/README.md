# 使用[@talentui/dll-webpack-config]()创建dll时的命名规则， 这个规则同样使用于在[@talentui/webpack-config]()引入dll时根据dllList传入dll名字，自动解析出文件路径。

## 应用

```js
    const namingConvention  = require('@talentui/dll-naming');
    const dllInfo = namingConvention('@talentui/dll-react', '1.0.3', true);
    console.log(dllInfor)
    /*
        {
            manifest: dll-react-1.0.3.manifest.json
            filename: dll-react-1.0.3.min.js
        }
    */
    const devDllInfo = namingConvention('@talentui/dl-react', '1.0.3', false)
    console.log(devDllInfo)
    /*
        {
            manifest: dll-react.dev.manifest.json
            filename: dll-react.dev.js
        }
    */
```

## 签名 namingConvention(packageName, version, isProduction = false)

## 参数
> **packageName**  包的名字，如果包含scope，但scope会被过滤掉

> **version** 包的版本号，生成用于production的dll也会使用此版本号

> isProduction 生产环境会带版本号，开发环境只会带dev