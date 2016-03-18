---
title: Android 的 ORM 数据库框架 DBExecutor
tags: []
date: 2015-06-17 20:38:37
---

<div align="left">**DBExecutor****主要的功能**</div>

<div align="left">**1.使用了读写锁，支持多线程操作数据。**</div><div align="left">**2.支持事务**</div><div align="left">**3.支持ORM****4.缓存Sql，缓存表结构**</div><div align="left"><div align="left"><span style="color:rgb(51, 51, 51)">这个类库主要用于android 数据库操作。 始终围绕着一个类对应一个表的概念。 只要创建一个实体类，就不用当心它怎么存储在数据库中，不用重新写增删改查的代码。基本的功能已经帮你实现好了。 增删改查数据只要一句搞定</span></div><div align="left"><span style="color:rgb(51, 51, 51)">
</span></div><span style="color:#008000">boolean isSuccess = db.insert(person);
boolean isSuccess = db.updateById(person);
boolean isSuccess  = db.deleteById(Person.class,1);
List&lt;Person&gt; persons = db.findAll(Person.class);</span>
<!-- more -->
*   ---library_DB02 是项目的源码。

*   ---DBLibrary_TestCase 是项目的测试用例，主要介绍该类库详细的用法

*   ---doc 是网页文档

*   ---db.jar 是该类库的jar包

*   ---doc.chm 是该类库的chm文档

*   ---设计框架.docx 是该类库的uml图生成的图片

*   ---设计框架.mdl 是该类库的uml图，描述整个类库的架构<div align="left"><span style="color:rgb(51, 51, 51)">最后非常感谢XUtils代码的作者wyouflf。 该代码是对开源项目XUtils的数据库模块进行重构，及性能优化。 因为他的框架设计的非常合理。很多都是在其基础上完善的。</span></div>**1.定义一个简单对应表的实体类**</div><div align="left"><span style="color:#008000">@Table(name = &quot;Person&quot;)</span>
<span style="color:#008000">public class Person {
   @Id(autoIncrement = true)
   private int id;
   private String name;
   private int age;</span></div><div align="left"><span style="color:#008000">
   public int getId() {
        return id;
   }</span>

<span style="color:#008000">   public void setId(int id) {
        this.id = id;
   }</span>

<span style="color:#008000">   public String getName() {
       return name;
   }</span>

<span style="color:#008000">   public void setName(String name) {
       this.name = name;
   }</span>

<span style="color:#008000">   public int getAge() {
      return age;
   }</span>

<span style="color:#008000">   public void setAge(int age) {
     this.age = age;
   }</span>

<span style="color:#008000"> }</span>
</div><div align="left"><div align="left"><span style="color:rgb(51, 51, 51)">必须包含@Id,@Id声明的字段对应表里的id。autoIncrement = true 自增长。 @Table 声明表的名字。@Table可以不需要。如果没有@Table以包名+类名为表的名字</span></div><div align="left"><span style="color:rgb(51, 51, 51)">支持基本类型以及基本类型的封装类，java.sql.Date 定义的字段。如果要支持其他类型的字段请查看DBLibrary_TestCase中的 TestColumnConverter.java</span></div>**2.主要类**<div align="left"><span style="color:rgb(51, 51, 51)">**1.DBExecutor主要用于执行sql语句，一个数据库对应一个DBExecutor**</span></div><div align="left"><span style="color:rgb(51, 51, 51)">   获取默认数据库的执行者 DBExecutor executor = DBExecutor.getInstance(context); </span></div><div align="left"><span style="color:rgb(51, 51, 51)">   获取指定的数据库的执行者 DBExecutor.getInstance(dbHelper)</span></div><div align="left"><span style="color:rgb(51, 51, 51)">   主要的方法用 db.execute(sqls)，db.executeQuery(sql)等 封装了简基本的增删改查操作，使用db.insert(person);可以保存一条记录。</span></div><div align="left"><span style="color:rgb(51, 51, 51)">   执行sql的时候。不用考虑表是否创建。如果表不存在，会自动创建。</span></div><div align="left"><span style="color:rgb(51, 51, 51)">**2.Sql用于DBExecutor 执行的Sql**</span></div><div align="left"><div align="left"><span style="color:#333333">  与sql文本语句是有差别的。 区别在于Sql 里包含</span></div>
<span style="color:rgb(51, 51, 51)"><div align="left"><span style="color:#333333">  sql.getTable();//操作的表</span></div>
<div align="left"><span style="color:#333333">  sql.getSqlText();//可以带有?占位符的sql语句</span></div>
<div align="left"><span style="color:#333333">  sql.getBindValues();//?占位符对应的值。</span></div>
</span></div><div align="left"><div align="left"><span style="color:rgb(51, 51, 51)">  sql.setCheckTableExit(checkTableExit);//设置执行sql时检查表是否存在，默认为true如果 检查到表不存在自动创建，设置为false 不做检查 </span></div></div><div align="left"><div align="left"><span style="color:rgb(51, 51, 51)">   不要害怕复杂，我们可以通过SqlFactory 创建它Sql</span></div></div><div align="left"><span style="color:rgb(51, 51, 51)">**3.SqlFactory主要用于创建Sql语句，可以创建复杂增删改查的sql语句。**</span></div>  <span style="color:#008000">// 查询语句  </span></div><div align="left"><span style="color:#008000">  Sql sql = SqlFactory.find(Person.class);
  sql = SqlFactory.find(Person.class).where(&quot;name&quot;, &quot;=&quot;, &quot;试着飞&quot;);
  sql = SqlFactory.find(Person.class).where(&quot;age&quot;, &quot;=&quot;, &quot;10&quot;).or(&quot;age&quot;, &quot;=&quot;, 11);
  sql = SqlFactory.find(Person.class).where(&quot;age&quot;, &quot;=&quot;, &quot;10&quot;).orderBy(&quot;name&quot;, false);
  sql = SqlFactory.find(Person.class).where(&quot;age&quot;, &quot;=&quot;, &quot;10&quot;).orderBy(&quot;name&quot;, false).limit(1);
  sql = SqlFactory.find(Person.class).where(&quot;name&quot;, &quot;like&quot;, &quot;%飞&quot;);
  sql = SqlFactory.find(Person.class).where(&quot;name&quot;, &quot;like&quot;, &quot;_着_&quot;);
  sql = SqlFactory.find(Person.class).where(&quot;age&quot;, &quot;in&quot;, new int[] { 10, 11, 12 });
  sql = SqlFactory.find(Person.class).where(&quot;name&quot;, &quot;in&quot;, new String[] { &quot;小明&quot;, &quot;小红&quot; });
  sql = SqlFactory.find(Person.class, &quot;name&quot;, &quot;age&quot;).where(&quot;name&quot;, &quot;=&quot;, &quot;试着飞&quot;);
  sql = SqlFactory.find(Person.class, &quot;count(*) as num&quot;).where(&quot;age&quot;, &quot;=&quot;, &quot;11&quot;);
  sql = SqlFactory.find(Person.class, &quot;max(age) as maxAge&quot;, &quot;min(age) as minAge&quot;).where(&quot;sex&quot;, &quot;=&quot;, &quot;男&quot;);
  sql = SqlFactory.find(Person.class, new MaxFunction(&quot;age&quot;, &quot;maxAge&quot;), 
new MinFunction(&quot;age&quot;, &quot;minAge&quot;)).where(&quot;sex&quot;, &quot;=&quot;, &quot;男&quot;);
  sql = SqlFactory.find(Person.class).where(&quot;name=? and age=?&quot;, new Object[] { &quot;小明&quot;, 11 });

  // 删除语句
  sql = SqlFactory.deleteAll(Person.class);
  sql = SqlFactory.delete(Person.class).where(&quot;age&quot;, &quot;=&quot;, 11);
  sql = SqlFactory.deleteById(Person.class, 11);
  sql = SqlFactory.deleteById(Person.class, new int[] { 11, 12 });

  // 更新语句
  sql = SqlFactory.update(Person.class, new String[] { &quot;name&quot;, &quot;age&quot; }, new Object[] { &quot;小明&quot;, &quot;11&quot; }).where(&quot;id&quot;, &quot;=&quot;, 1);
  sql = SqlFactory.updateById(new Person(1, &quot;小明&quot;, 11, &quot;男&quot;));
  sql = SqlFactory.updateById(new Person(1, &quot;小明&quot;, 11, &quot;男&quot;), &quot;name&quot;);

  // 如果存在 id为1的记录，就更新，否则 插入一条新记录
  sql = SqlFactory.updateOrInsertById(new Person(1, &quot;小明&quot;, 11, &quot;男&quot;));

  // 插入语句
  sql = SqlFactory.insert(new Person(1, &quot;小明&quot;, 11, &quot;男&quot;));

  // 自拼接sql语句
  sql = SqlFactory.makeSql(Person.class, &quot;select * from Person where age = ?&quot;, new Object[] { 11 });</span>
<div align="left"><span style="color:rgb(51, 51, 51)">更多详细信息请查看项目文档里面的内容</span></div><div align="left"><span style="color:rgb(51, 51, 51)">
</span></div><div align="left">项目地址 ：[https://github.com/LuckyJayce/DBExecutor](https://github.com/LuckyJayce/DBExecutor)</div></div>