---
title: android项目集成react native环境
categories:
- 杂七杂八
tags: 
- react native
date: 2015-10-22 14:30:49
---


build.gradle
``` gradle
dependencies {
    compile "com.facebook.react:react-native:+"
}
```


``` gradle
repositories {
    maven {
        url "http://xxxxxx.com/content/groups/public/"
    }
}
```

node_modules\react-native\android\com\facebook\react\react-native