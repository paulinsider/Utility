const process = require('child_process');

const x = 720
const y = 1280
const header = 146;
const goodItem = 354;


// 1. swipe top 50 缩小 header
// 2. tap 左 1
// 3. tap 右 1
// 4. swipe top 354
// 2
// 3


// 向右切换 tablayout
const swipeLeft = `adb\\adb shell input swipe ${x - 100} ${header + goodItem} ${x - 400} ${header + goodItem}`

// 收起 头
const swipeTop = `adb\\adb shell input swipe ${x/2} ${header + goodItem} ${x/2} ${header}`

const tap1 = `adb\\adb shell input tap ${x / 4} ${header + goodItem/2}`
const tap2 = `adb\\adb shell input tap ${x / 4 * 3} ${header + goodItem/2}`
const tap3 = `adb\\adb shell input tap ${x / 4} ${header + goodItem/2 * 3}`
const tap4 = `adb\\adb shell input tap ${x / 4 * 3} ${header + goodItem/2 * 3}`
const tap5 = `adb\\adb shell input tap ${x / 4} ${header + goodItem/2 * 5}`
const tap6 = `adb\\adb shell input tap ${x / 4 * 3} ${header + goodItem/2 * 5}`

const back = 'adb\\adb shell input keyevent 4'


const swipePage = `adb\\adb shell input swipe ${x/2} 1000 ${x/2} ${header} 500`

async function loop() {
  process.execSync(tap1)
  await sleep()
  process.execSync(back)
  await sleep()
  process.execSync(tap2)
  await sleep()
  process.execSync(back)
  await sleep()
  process.execSync(tap3)
  await sleep()
  process.execSync(back)
  await sleep()
  process.execSync(tap4)
  await sleep()
  process.execSync(back)
  await sleep()
  process.execSync(tap5)
  await sleep()
  process.execSync(back)
  await sleep()
  process.execSync(tap6)
  await sleep()
  process.execSync(back)
  await sleep()
  process.execSync(swipePage)
  await sleep()
}

async function sleep(delay = 1500) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve()
    }, delay)
  })
  
}


(async function() {
  const connectResponse = process.execSync('adb\\adb connect 127.0.0.1:62001')
  console.log(connectResponse.toString())

  const devicesResponse = process.execSync('adb\\adb devices')
  console.log(devicesResponse.toString())

  process.execSync('adb\\adb shell am start -n com.shizhuang.duapp/com.shine.ui.home.SplashActivity')
  await sleep(6000)
  process.execSync(swipeTop)
  await sleep()
  process.execSync(swipeLeft)
  await sleep()
  for(;;) {
    await loop()
  }
})()