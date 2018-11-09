---
title: charles授权分析与破解
date: 2018-11-09 09:55:00
categories:
- 杂七杂八
tags: 
- charles
- 激活
---

> 最近charles又更新了，对于有强迫症的人来说，无法接受这个事实，果断前往[官网](https://www.charlesproxy.com/)下载安装。

<!-- more -->
兴奋的点击了软件图标，突然间，天气骤变，窗外电闪雷鸣，罗盘不停的转动，电脑风扇也疯狂的转。老夫掐指一算，不好！今天不适宜使用charles，可是已经来不及了。此时，心跳逐渐加快，砰！砰砰！ 不知会有什么事发生，只能紧紧的凝视着电脑屏幕，视线不敢移开半点~
时间已经过去100毫秒，机子已经发烫，屏幕看起来并没有什么变化，但变得幽暗了。似乎屏幕里有双眼睛直勾勾的盯着我，眼里充满了血丝，披头散发，屋子里也没有了其他声音。啪！突然外面一声巨响，屏幕出现了一个极其恐怖的画面，我完全不敢看

![](https://i.loli.net/2018/11/08/5be3aac4e664f.png)

窗外不知啥时候也下起了雨，冷风也从吹进了屋子里。嘻嘻嘻嘻，外面突然出现一个刺耳的笑声，听得我毛骨悚然，像极了电影里鬼婴的声音，随后出现了一个声音：“这都是命”。然后笑声停止了，雨也停了，就像什么也没发生一样。我以为出现了幻觉，但是一看屏幕，那个画面还在，才知道全都是真的。看着右下角的倒计时，10……9……8…… 回想刚刚外面那句话，竟然害怕了起来。这倒计时结束会发送什么？难道是我生命的最后10秒？不！我不信！lz(楼主)要逆天改命。

好了，字数凑够了，开始正式哔哔了。charles是一个必备的网络分析工具，但是是收费的，虽然网上有破解版。但都是比较旧的版本(剧情需要)，子曰："不会破解软件的程序员不是好作家"，老子也说过：“孔子说得对”。charles授权是本地校验的，所以需要分析下校验逻辑。charles是用java写的，所以可以很方便的分析代码，推荐使用 **[jd-gui](http://jd.benow.ca/)** 和 **[Luyten](https://github.com/deathmarine/Luyten)**

#### 授权分析

打开charles，菜单栏 *Help->Register Charles* 弹出注册窗口,需要填入 *Registered Name* 和 *License Key*

![](https://i.loli.net/2018/11/08/5be3aab06473a.png)

就从这个界面开始，使用**jd-gui** 或 **Luyten** 打开安装目录里的 **java/charles.jar**文件,全局搜索  Registered Name 

![](https://i.loli.net/2018/11/08/5be3d8cd5dff7.png)

在 RegisterFrame 发现该关键字，分析代码,发现关键监听 `this.bRegister.addActionListener` 

```java
    localContainer.add(this.bCancel, "tag cancel,split 2,span,center");
    localContainer.add(this.bRegister, "tag ok");
    this.bCancel.addActionListener(new WTzz(this));
    this.bRegister.addActionListener(new HgWa(this));
```


点击进入 HgWa 的构造方法里，类里提供了一个方法,在下方通过注释说明

``` java
  public final void actionPerformed(ActionEvent paramActionEvent)
  {
    // 获取 输入框内容
    paramActionEvent = RegisterFrame.lcJx(this.lcJx).getText().trim();
    String str = RegisterFrame.KcPF(this.lcJx).getText().trim();
    if ((paramActionEvent.length() > 0) && (str.length() > 0))
    {
      Object localObject;
      //关键if
      if ((localObject = kKPk.lcJx(paramActionEvent, str)) != null)
      {
        ExtendedJOptionPane.lcJx(this.lcJx, localObject, "Charles Registration", 2);
        return;
      }
      //授权成功的提示
      ExtendedJOptionPane.lcJx(this.lcJx, "Thank you for registering. Charles will now close. Please start Charles again to continue.", "Charles Registration", 1);
    }
  }
```

最下面有个授权成功的提示，所以 `kKPk.lcJx(paramActionEvent, str)` 即为授权校验的方法。查看实现，实际上就是 实例化一个 kKPk 对象，如果实例化成功，就说明校验通过，并且将该实例 放到   kKPk.KcPF 。这里使用 Luyten  加载 kKPk ，jd看代码实在是难受，构造方法也非常简单。有两个关键的地方

```java
//line 7
private static String lcJx = "Thanks for looking at the source. Please register Charles if you use it.";

//构造方法
  if (!this.lcJx(this.KcPF(replaceAll, s, n2)) && (replaceAll.equals(ynvb) || !this.lcJx(this.KcPF(ynvb, s, n2)))) {
      throw new LicenseException(this.lcJx(2));
  }
```
在第7行有个关键字符串，不懂什么意思没关系，中文翻译就是：**牛逼啊，这个类就是做授权校验的**
kkpk要实例化成功，肯定不能进入到if里面， this.lcJx() 需要返回true, this.KcPF()只要不抛出异常即可，牛逼的人就可以根据这个算法写个注册机了。我们只要破解能用就行了，所以需要修改该类文件。

#### 开炮

修改文件有很多方式，有直接改 smail 的，具体怎么改网上一大堆教程。对于牛逼的人来说，直接写代码来改就行。这里就要用到一个工具：*javassist* ，Javassist是一个开源的分析、编辑和创建Java字节码的类库。

打开 Intellij IDEA创建一个java工程，导入charles.jar作为依赖，新建一个 Test.java ,用于测试

```
public class Test {
    public static void main(String[] args) {
        try {
            //该文件需要添加一个Artifacts，build后生成
            ClassLoader classLoader = ClassLoaderUtil.loadJarFile(new File("out/artifacts/charles_crack_jar/charles-crack.jar"));
            String name = "wrbug";
            String key = "ss";
            Class<?> kKpk = classLoader.loadClass("com.xk72.charles.kKPk");
            Constructor<?> declaredConstructor = kKpk.getDeclaredConstructor(String.class, String.class);
            declaredConstructor.setAccessible(true);
            Object obj = declaredConstructor.newInstance(name, key);
            System.out.println("破解成功");
```


然后运行，因为没有做任何处理，不出意外，会有异常抛出 

![](https://i.loli.net/2018/11/08/5be3e5e267668.png)



再新建一个 Crack.java ，用于修改class

```
public class Crack {
    public static void main(String[] args) throws Throwable {
        ClassPool classPool = ClassPool.getDefault();
        CtClass ctClass = classPool.get("com.xk72.charles.kKPk");
        //修改 lcJx 方法返回true
        CtClass[] param = new CtClass[1];
        param[0] = classPool.get("long");
        CtMethod method = ctClass.getDeclaredMethod("lcJx", param);
        method.setBody("return true;");

        //修改KcPF 返回为任意long
        param = new CtClass[3];
        param[0] = classPool.get(String.class.getName());
        param[1] = classPool.get(String.class.getName());
        param[2] = classPool.get("int");
        method = ctClass.getDeclaredMethod("KcPF", param);
        method.setBody("return 0L;");

        //静态方法 lcJx 方法返回true
        method = ctClass.getDeclaredMethod("lcJx", null);
        method.setBody("return true;");

        //  这里返回Registered Name， 可以自行修改
        method = ctClass.getDeclaredMethod("JZlU", null);
        method.setBody("return \"wrbug\";");

        // 将class文件写入到 output目录
        ctClass.writeFile("output");

    }
}
```

运行crack后，在output目录查看下修改后的kKPk.class ，可以发现，方法都已修改成功

```
    private boolean lcJx(long var1) {
        return true;
    }
    public static boolean lcJx() {
        return true;
    }
    private long KcPF(String var1, String var2, int var3) {
        return 0L;
    }
    
    public static String JZlU() {
        return "wrbug";
    }
```

再次重新build后，运行Test，见证奇迹的时候到了，提示破解成功。至此，整个charles破解完成，将生产的jar重命名为 charles.jar，替换原有的即可

### 网(tui)址(guang)

项目地址：[https://github.com/WrBug/charles-crack](https://github.com/WrBug/charles-crack)
carles授权码生成：[https://charles.wrbug.com/](https://charles.wrbug.com/)


