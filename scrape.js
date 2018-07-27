const puppeteer = require('puppeteer');

let scrape = async () => {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();
  
  await page.goto('https://my.sa.ucsb.edu/gold/Login.aspx', {waitUntil:'networkidle2'});
  
  await page.focus('#pageContent_userNameText');
  await page.keyboard.type('priscilla_lee');
  await page.focus('#pageContent_passwordText');
  await page.keyboard.type('25754SbJ');
  await page.click('#pageContent_loginButton');
  await page.waitForNavigation();
  
  await page.click('#Li0 > a');
  await page.waitFor(1000);
  
  const result = await page.evaluate(() => {
      	let title = document.querySelector('#ctl00_pageContent_CourseList_ctl00_CourseHeadingLabel').innerText;
	let day = document.querySelector('.col-lg-days.col-lg-push-0.col-sm-2.col-sm-pull-0.col-xs-6.col-xs-pull-6').innerText;
	let time = document.querySelector('.col-lg-time.col-md-time.col-sm-4.col-xs-6').innerText;

      	return {
          title,
	  day,
	  time
      	}
  });

  browser.close();
  return result;
};

scrape().then((value) => {
    console.log(value); // Success!
});