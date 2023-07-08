# A script to show HuLuXia unauthorized access

## Background

I'm a fan of [_Roco Kingdom_](https://17roco.qq.com), and I find an offline android game which is a doujin (A Janpanese noun which means fan-made) of it. The share link is from [HuLuXia](https://tools.huluxia.com/share/page/ANDROID/4.1?app_id=61514). When I click download button, it tricked me that download its app which named HuLuXia. I'm so angry that I want to bypass its faked download page and share it.

## Step

1. If you got the link like `https://tools.huluxia.com/share/page/ANDROID/4.1?app_id=61514`, you just cut `app_id` from it.
2. Use `GET` method to request `http://tools.huluxia.com/game/detail/ANDROID/4.1.5?app_id={app_id}` to get the detail info which include real download url. Don't forget replace `{app_id}` to the id you've got from step 1.
3. Use the real download url to download and enjoy the happy time 😄

## Conclusion

A web application should check the access permission of the resource to keeping the user use the right way to use the application. But an important problem, don't trick user for business. It will make user hate your app 😣.
