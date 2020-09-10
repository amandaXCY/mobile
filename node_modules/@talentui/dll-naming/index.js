const afterFix = "";
module.exports = (packageName, version, isProduction = false) => {
    const outputFileName = packageName.indexOf("@") === -1
        ? packageName
        : packageName.split("/")[1];

    return {
        manifest: `${outputFileName}${isProduction
            ? `-${version}`
            : afterFix}.manifest.json`,
        filename: `${outputFileName}${isProduction
            ? `-${version}.min`
            : afterFix}.js`
    };
};
