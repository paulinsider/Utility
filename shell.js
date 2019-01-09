const process = require('child_process');

const x = 720
const y = 1280
const sysBarHeight = 40;
const header = 124;
const bigHeader = 174
const goodItem = 354;

// 1. swipe top 50 缩小 header
// 2. tap 左 1
// 3. tap 右 1
// 4. swipe top 354
// 2
// 3

const swipeTop50 = `adb shell input swipe ${x/2} ${bigHeader + goodItem} ${x/2} ${header + goodItem}`

const tap1 = `adb shell input tap ${x/4} ${header + goodItem/2}`

const back = 'adb shell input keyevent 4'

const tap2 = `adb shell input tap ${x/4*3} ${header + goodItem/2}`

const swipeItem = `adb shell input swipe ${x/2} ${header + goodItem * 2} ${x/2} ${header + goodItem + 13} 500`

async function start() {
  process.execSync(swipeTop50)
  await sleep()
  process.execSync(tap1)
  await sleep()
  process.execSync(back)
  await sleep()
  process.execSync(tap2)
  await sleep()
  process.execSync(back)
  await sleep()
  process.execSync(swipeItem)

}

async function sleep(delay = 1500) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve()
    }, delay)
  })
  
}

start()
