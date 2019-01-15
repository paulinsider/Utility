const process = require('child_process');

const x = 720
const y = 1280
const header = 240;
const offsetTop = 337;
const goodItem = 442;


// 1. swipe top 50 缩小 header
// 2. tap 左 1
// 3. tap 右 1
// 4. swipe top 354
// 2
// 3


// 向右切换 tablayout
const swipeLeft = `adb\\adb shell input swipe ${x - 100} ${header + offsetTop + goodItem} ${x - 400} ${header + offsetTop + goodItem}`

// 收起 头
const swipeTop = `adb\\adb shell input swipe ${x/2} ${offsetTop + goodItem + header} ${x/2} ${goodItem + header}`

const tap1 = `adb\\adb shell input tap ${x / 4} ${header + goodItem/2}`
const tap2 = `adb\\adb shell input tap ${x / 4 * 3} ${header + goodItem/2}`
const tap3 = `adb\\adb shell input tap ${x / 4} ${header + goodItem/2 * 3}`
const tap4 = `adb\\adb shell input tap ${x / 4 * 3} ${header + goodItem/2 * 3}`
const taps = {tap1, tap2, tap3, tap4,}
const back = 'adb\\adb shell input keyevent 4'


const swipePage = `adb\\adb shell input swipe ${x/2} 1000 ${x/2} ${header} 500`

async function loop() {

  for (let i = 1; i <= 4; i ++) {
    await good('tap' + i)
  }
  
  process.execSync(swipePage)
  await sleep()
}

async function good(tap) {
  process.execSync(taps[tap])
  await sleep()
  // await moreBuy()
  // process.execSync(back)
  // await sleep()
  process.execSync(back)
}

async function moreBuy() {
  const top = `adb\\adb shell input swipe 360 910 360 380`
  const tap = `adb\\adb shell input tap 675 550`
  const loadMore = `adb\\adb shell input swipe 360 1070 360 220`

  process.execSync(top)
  await sleep(500)
  process.execSync(tap)
  process.execSync(loadMore)
  process.execSync(back)
  await sleep(1000)
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

  process.execSync('adb\\adb shell am start -n com.nice.main/com.nice.main.activities.MainActivity_')
  await sleep(1000)
  process.execSync(`adb\\adb shell input tap ${x / 5 * 3.5} 1240`)
  await sleep()
  process.execSync(swipeLeft)
  await sleep()
  process.execSync(swipeTop)
  await sleep()
  for(;;) {
    await loop()
  }
})()