
const wdio = require("webdriverio")

const opts = {
  port: 4723,
  capabilities: {
    platformName: "Android",
    platformVersion: "4.4.2",
    deviceName: "Android Emulator",
    appPackage: "com.shizhuang.duapp",
    appActivity: "com.shine.ui.home.SplashActivity",
    automationName: "UiAutomator",
    noReset: false,
  }
};

(async function() {
  const client = await wdio.remote(opts);
  console.log(client)
  let moreBuyEl = await client.findElementById("com.shizhuang.duapp:id/tv_sold_all",);

  await moreBuyEl.click();


  //await driver.pressKeycode(4);
})()


