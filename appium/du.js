
const wdio = require("webdriverio")

const opts = {
  port: 4723,
  capabilities: {
    platformName: "Android",
    platformVersion: "4.4.2",
    deviceName: "Android Emulator",
    appPackage: "com.shizhuang.duapp",
    appActivity: "com.shine.ui.home.SplashActivity",
    automationName: "UiAutomator"
  }
};

(async function() {
  const client = wdio.remote(opts);
  let moreBuyEl = await driver.element("com.shizhuang.duapp:id/tv_sold_all",);

  await moreBuyEl.click();


  //await driver.pressKeycode(4);
})()


