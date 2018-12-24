# encoding:utf-8
# 糗事百科文章爬取
# 分析：请求https://www.qiushibaike.com/hot/page/1/  要抓取div class=‘artice’下内容  urllib或requests

import urllib.request
from fake_useragent import UserAgent
import re
# base_url='https://www.qiushibaike.com/hot/page'
# url=base_url+'1'+'/'
#
# ua=UserAgent()
#
# headers={
#     'User-Agent':ua.random
# }
# req =urllib.request.Request(url,headers=headers)
# resp = urllib.request.urlopen(req)
# html = resp.read().decode()
# print(html)

html_content=r"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta name="renderer" content="webkit"/>
<meta name="applicable-device" content="pc">
<meta name="domain_verify" content="pmrgi33nmfuw4ir2ejyws5ltnbuweyljnnss4y3pnurcyithovuwiir2ejqwmyrtguzdgobsmezdgnbyheywcmzthbrdmmtemu4tamrqg5rtmirmej2gs3lfknqxmzjchiytkmrzgq4demjugaydcnd5">


















<title>24小时爆笑笑话大全 - 糗事百科</title>






















<meta name="keywords" content="笑话,笑话大全" />
<meta name="description" content="糗事百科官网提供24小时糗搞笑笑话大全,糗百24小时内新糗事就只在糗事百科官网24小时专题,囊括恶搞、尴尬糗事精华,快乐减压！"/>
<meta http-equiv="mobile-agent" content="format=xhtml;url=//www.qiushibaike.com/hot/">
<meta http-equiv="mobile-agent" content="format=html5;url=//www.qiushibaike.com/hot/">




<meta name="robots" content="noarchive">
<link href="//static.qiushibaike.com/css/dist/web/app.min.css?v=1a44fd15c6e802cc1ab5953bd398eea8" media="screen, projection" rel="stylesheet" type="text/css"/>
<script type="text/javascript">
// Baidu Automatic push content
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
hm.src = "https://hm.baidu.com/hm.js?2670efbdd59c7e3ed3749b458cafaa37";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
// 收集运营上缓存证据
window.config = {
'user_time': '2018-12-12 11:34:02',
'version': '2017-09-04 14:36'
}
</script>
</head>
<body>



<div id="header" class="head">
<div class="content-block">
<div class="logo" id="hd_logo">
<a href="/"><h1>糗事百科</h1></a>
</div>
<div id="menu" class="menu-bar menu clearfix" style="margin:0 10px">
<a  href="/" target="_blank" rel="nofollow">热门</a>
<a  id="highlight"  href="/hot/" target="_blank">24小时</a>
<a  href="/imgrank/" target="_blank">热图</a>
<a  href="/text/" target="_blank">文字</a>
<a  href="/history/" target="_blank">穿越</a>
<a  href="/pic/" target="_blank">糗图</a>
<a  href="/textnew/" target="_blank">新鲜</a>

<!--<a href="http://www.youliaodao.cn" target="_blank" rel="nofollow">百科</a>-->
</div>
<div class="userbar clearfix hidden">
<div class="login hidden">
<a href="/my" class="username" id="uname" rel="nofollow"></a>
</div>
<div class="logout">
<a href="javascript:void(0);" class="fn-signin-required logintop" id='logintop' rel="nofollow" style="font-size:16.5px;">登录</a>
</div>
</div>
</div>
</div>



<div id="content" class="main">
<div class="content-block clearfix">
<!-- 暂停更新提示 -->
<!-- <img src="/static/images/banner.png" alt="" style="width: 100%; margin: 16px 0 0; display: block"> -->

<div id="content-left" class="col1">








<div class="article block untagged mb15 typs_long" id='qiushi_tag_121320501'>


<div class="author clearfix">
<a href="/users/14217/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1/14217/thumb/20170616202628.JPEG?imageView2/1/w/90/h/90" alt="一万万光年前">
</a>
<a href="/users/14217/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
一万万光年前
</h2>
</a>
<div class="articleGender manIcon">40</div>
</div>

<a href="/article/121320501" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


有农村的在一起聚赌，安排本庄一个老头在附近给看着点（就是布置一个暗哨），这天夜里正在楼上赌的时候，就听到那老头在外头一直嚷嚷“你们吵得让人睡不着！你们弄啥哩？赶紧回家吧”等等。弄得赌博的人直烦，几个手气差的人非要出去揍老头一顿，结果等会被派出所包了园。原来派出所接到举报过来抓赌，把车停远了步行进庄的时候碰到了暗哨老头。暗哨老头不敢明说，就在那说一些反话，结果赌博的人都没明白。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">568</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121320501" data-share="/article/121320501" id="c-121320501" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">7</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121320501" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121320501" class="up">
<a href="javascript:voting(121320501,1)" class="voting" data-article="121320501" id="up-121320501" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">571</span>
</a>
</li>
<li id="vote-dn-121320501" class="down">
<a href="javascript:voting(121320501,-1)" class="voting" data-article="121320501" id="dn-121320501" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-3</span>
</a>
</li>
<li class="comments">
<a href="/article/121320501" id="c-121320501" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335857'>


<div class="author clearfix">
<a href="/users/21610887/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2161/21610887/thumb/20181208114021.jpg?imageView2/1/w/90/h/90" alt="墨海烟云">
</a>
<a href="/users/21610887/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
墨海烟云
</h2>
</a>
<div class="articleGender manIcon">29</div>
</div>

<a href="/article/121335857" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


跟女友逛街买棉服，女友边走边说最烦过冬天，冻的脸发紫，鼻涕哗哗的，一点形象都没了……<br/>我“亲爱的，我觉得你也该喜欢冬天。。”<br/>女友不解的看着我，，<br/>我赶紧说“冬天穿的衣服厚，看不到你的五环……”<br/>“啊～”尼玛，平时瓶盖都拧不开的女友愣是一脚把我踹出五六米！！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1586</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335857" data-share="/article/121335857" id="c-121335857" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">20</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335857" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335857" class="up">
<a href="javascript:voting(121335857,1)" class="voting" data-article="121335857" id="up-121335857" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1598</span>
</a>
</li>
<li id="vote-dn-121335857" class="down">
<a href="javascript:voting(121335857,-1)" class="voting" data-article="121335857" id="dn-121335857" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/121335857" id="c-121335857" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335857" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">吃了两碗又盛：</span>
<div class="main-text">
啊啊五环，你比四环多一环
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


22

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335148'>


<div class="author clearfix">
<a href="/users/32215536/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3221/32215536/thumb/20181122212921.jpg?imageView2/1/w/90/h/90" alt="吃了两碗又盛">
</a>
<a href="/users/32215536/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
吃了两碗又盛
</h2>
</a>
<div class="articleGender manIcon">39</div>
</div>

<a href="/article/121335148" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


送儿子上学，他磨磨蹭蹭的，险些迟到，到校门口，他还不着急。<br/>当他的同学——每天最后一个到班的同学经过时，儿子赶紧撒腿就跑，，

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1353</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335148" data-share="/article/121335148" id="c-121335148" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">16</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335148" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335148" class="up">
<a href="javascript:voting(121335148,1)" class="voting" data-article="121335148" id="up-121335148" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1360</span>
</a>
</li>
<li id="vote-dn-121335148" class="down">
<a href="javascript:voting(121335148,-1)" class="voting" data-article="121335148" id="dn-121335148" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-7</span>
</a>
</li>
<li class="comments">
<a href="/article/121335148" id="c-121335148" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335148" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">我～无醉：</span>
<div class="main-text">
直到有一天  那个同学请假
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


27

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335576'>


<div class="author clearfix">
<a href="/users/26217894/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2621/26217894/thumb/20181209042528.jpg?imageView2/1/w/90/h/90" alt="聊天不撩妹子">
</a>
<a href="/users/26217894/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
聊天不撩妹子
</h2>
</a>
<div class="articleGender manIcon">53</div>
</div>

<a href="/article/121335576" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


没事跟老婆聊微信，我说：老婆你那么好看，当年那么多人追你为啥就看上我了。<br/>老婆：当年我口味重，想品尝牛粪是啥味的。我说：这么多尝出来吗？<br/>老婆：没有，关键是爸妈喜欢你。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1796</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335576" data-share="/article/121335576" id="c-121335576" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">37</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335576" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335576" class="up">
<a href="javascript:voting(121335576,1)" class="voting" data-article="121335576" id="up-121335576" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1805</span>
</a>
</li>
<li id="vote-dn-121335576" class="down">
<a href="javascript:voting(121335576,-1)" class="voting" data-article="121335576" id="dn-121335576" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-9</span>
</a>
</li>
<li class="comments">
<a href="/article/121335576" id="c-121335576" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335576" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">爱新觉罗.黄瓜：</span>
<div class="main-text">
好一坨牛粪！能赢得丈母娘和老丈人的青睐，也没谁了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


23

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_120297842'>


<div class="author clearfix">
<a href="/users/14961780/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1496/14961780/thumb/20180416070408.JPEG?imageView2/1/w/90/h/90" alt="意大利炮管委会">
</a>
<a href="/users/14961780/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
意大利炮管委会
</h2>
</a>
<div class="articleGender manIcon">33</div>
</div>

<a href="/article/120297842" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


今天倒霉，<br/>刚和女朋友分完<br/>又去医院洗胃。<br/>洗完了钱没带够<br/>就发微信给女朋友<br/>我:唉，那。。。小。。。小慧 ，借，借我点钱，急用。<br/>慧:套路太老了吧，我们分都分了，不要再套近乎了，各走各的大家都好。<br/>我:不是，慧，农药中毒在医院洗胃，钱不够，想找你借点，在这个城市，只认识你一个知根知底的。。。一个人孤苦无依真的好难。<br/>然后。。。。。沉默。。。。。<br/>继续沉默。。。<br/>过了一会儿，电话打来<br/>小慧哭着说:不就分个手么，又不是不能合，你干什么傻事啊你这个傻瓜，在哪个医院，我这就赶过来。。。<br/>我（心理活动）
…
</span>

<span class="contentForAll">查看全文</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">623</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/120297842" data-share="/article/120297842" id="c-120297842" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">10</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_120297842" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-120297842" class="up">
<a href="javascript:voting(120297842,1)" class="voting" data-article="120297842" id="up-120297842" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">636</span>
</a>
</li>
<li id="vote-dn-120297842" class="down">
<a href="javascript:voting(120297842,-1)" class="voting" data-article="120297842" id="dn-120297842" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-13</span>
</a>
</li>
<li class="comments">
<a href="/article/120297842" id="c-120297842" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/120297842" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">酱小土豆：</span>
<div class="main-text">
看看吧，谁说会舔没用的
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


32

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121336687'>


<div class="author clearfix">
<span style="height: 35px">
<img src="//static.qiushibaike.com/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87" alt="匿名用户">
</span>
<span>
<h2>匿名用户</h2>
</span>
<!-- <div class="articleGender manIcon">32</div> -->
</div>

<a href="/article/121336687" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


公司食堂是个人承包的，我们打饭都是扫微信~～我打好饭后正准备扫码，排在我身后的李丽对厨师说：我没带手机，小宋(她老公)马上就到，等会儿让他付吧<br/>我逗她：叫我老公，我帮你买单<br/>周丽马上对我说：谢谢老公，(对厨师说)<br/>他给啊，再加两个，不四个鸡腿<br/>我这一句话，四十块没了…………

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1516</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121336687" data-share="/article/121336687" id="c-121336687" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">26</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121336687" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121336687" class="up">
<a href="javascript:voting(121336687,1)" class="voting" data-article="121336687" id="up-121336687" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1526</span>
</a>
</li>
<li id="vote-dn-121336687" class="down">
<a href="javascript:voting(121336687,-1)" class="voting" data-article="121336687" id="dn-121336687" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-10</span>
</a>
</li>
<li class="comments">
<a href="/article/121336687" id="c-121336687" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121336687" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">无心弦：</span>
<div class="main-text">
你们伙食挺贵啊，一份饭加4个鸡腿就40？
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


8

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121334827'>


<div class="author clearfix">
<a href="/users/25382466/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2538/25382466/thumb/20181210232434.jpg?imageView2/1/w/90/h/90" alt="安瑾初">
</a>
<a href="/users/25382466/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
安瑾初
</h2>
</a>
<div class="articleGender manIcon">17</div>
</div>

<a href="/article/121334827" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


缘，妙不可言

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/121334827" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12133/121334827/medium/R8N0TU8CQBKNKVAD.jpg" alt="糗事#121334827" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2729</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121334827" data-share="/article/121334827" id="c-121334827" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">39</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121334827" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121334827" class="up">
<a href="javascript:voting(121334827,1)" class="voting" data-article="121334827" id="up-121334827" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2747</span>
</a>
</li>
<li id="vote-dn-121334827" class="down">
<a href="javascript:voting(121334827,-1)" class="voting" data-article="121334827" id="dn-121334827" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-18</span>
</a>
</li>
<li class="comments">
<a href="/article/121334827" id="c-121334827" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121334827" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">圖文君：</span>
<div class="main-text">
我今年也这样干，要是男的接我回来就打死楼主
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


59

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121336531'>


<div class="author clearfix">
<a href="/users/33887946/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3388/33887946/thumb/20181115195700.jpg?imageView2/1/w/90/h/90" alt="天涯明月刀。">
</a>
<a href="/users/33887946/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
天涯明月刀。
</h2>
</a>
<div class="articleGender manIcon">28</div>
</div>

<a href="/article/121336531" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


我二姑出嫁的时候陪嫁了一辆自行车，由于姑姑和姑父都不会骑。姑姑和姑父说留着以后给孩子骑。等表弟长大了，表弟说那个自行车太老不骑。姑妈咬着牙对表弟说：你不骑留着给你孩子骑。表弟现在都28岁了还没有女朋友，姑妈现在没事就把那辆自行车拿出来擦一擦……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1740</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121336531" data-share="/article/121336531" id="c-121336531" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">19</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121336531" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121336531" class="up">
<a href="javascript:voting(121336531,1)" class="voting" data-article="121336531" id="up-121336531" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1746</span>
</a>
</li>
<li id="vote-dn-121336531" class="down">
<a href="javascript:voting(121336531,-1)" class="voting" data-article="121336531" id="dn-121336531" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-6</span>
</a>
</li>
<li class="comments">
<a href="/article/121336531" id="c-121336531" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121336531" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">萝卜她男人：</span>
<div class="main-text">
这是一辆传世的自行车啊
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


24

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335213'>


<div class="author clearfix">
<a href="/users/19459659/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1945/19459659/thumb/20180814212146.jpg?imageView2/1/w/90/h/90" alt="南九">
</a>
<a href="/users/19459659/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
南九
</h2>
</a>
<div class="articleGender manIcon">103</div>
</div>

<a href="/article/121335213" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


我们有个边防连队特别偏僻！<br/>咯咯咯......<br/>连队汽车取给养物资，回去回去的途中，由于道路颠簸，一袋大米掉在了路上。<br/>半个月后，连队又一次去取给养物资的时候，捡到了那袋大米......

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2901</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335213" data-share="/article/121335213" id="c-121335213" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">60</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335213" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335213" class="up">
<a href="javascript:voting(121335213,1)" class="voting" data-article="121335213" id="up-121335213" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2914</span>
</a>
</li>
<li id="vote-dn-121335213" class="down">
<a href="javascript:voting(121335213,-1)" class="voting" data-article="121335213" id="dn-121335213" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-13</span>
</a>
</li>
<li class="comments">
<a href="/article/121335213" id="c-121335213" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335213" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">吃了两碗又盛：</span>
<div class="main-text">
鸟都没有
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


43

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_120296693'>


<div class="author clearfix">
<a href="/users/30797262/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3079/30797262/thumb/20180509193216.JPEG?imageView2/1/w/90/h/90" alt="不敗丶傳説">
</a>
<a href="/users/30797262/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
不敗丶傳説
</h2>
</a>
<div class="articleGender manIcon">100</div>
</div>

<a href="/article/120296693" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


女同桌问她的妹妹：“葫芦娃里面你最喜欢哪一个。”她妹说：“三娃和五娃。”“为什么？”“姐姐,你懂的…”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">208</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/120296693" data-share="/article/120296693" id="c-120296693" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">7</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_120296693" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-120296693" class="up">
<a href="javascript:voting(120296693,1)" class="voting" data-article="120296693" id="up-120296693" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">216</span>
</a>
</li>
<li id="vote-dn-120296693" class="down">
<a href="javascript:voting(120296693,-1)" class="voting" data-article="120296693" id="dn-120296693" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-8</span>
</a>
</li>
<li class="comments">
<a href="/article/120296693" id="c-120296693" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121336159'>


<div class="author clearfix">
<a href="/users/37507340/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3750/37507340/thumb/20181016231924.jpg?imageView2/1/w/90/h/90" alt="奔跑的小土狼">
</a>
<a href="/users/37507340/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
奔跑的小土狼
</h2>
</a>
<div class="articleGender manIcon">26</div>
</div>

<a href="/article/121336159" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


老爸在微信上告诉我，猪场卖猪了。问我用不用钱，不用就存整年的了<br/>我回复他：给我转1万到支付宝吧<br/>……钱到账后，我点了“给对方回个话”：收到，谢谢<br/>谁知没过一会儿，我爸电话打来了：我这是借你，可不是给你啊<br/>我：我也没说不还呀<br/>老爸：你这一句谢谢，弄的我心里没底

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">4015</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121336159" data-share="/article/121336159" id="c-121336159" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">33</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121336159" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121336159" class="up">
<a href="javascript:voting(121336159,1)" class="voting" data-article="121336159" id="up-121336159" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">4030</span>
</a>
</li>
<li id="vote-dn-121336159" class="down">
<a href="javascript:voting(121336159,-1)" class="voting" data-article="121336159" id="dn-121336159" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-15</span>
</a>
</li>
<li class="comments">
<a href="/article/121336159" id="c-121336159" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121336159" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">茂比乌斯：</span>
<div class="main-text">
我对“狼子野心”这个成语有了更清晰的了解。
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


114

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335150'>


<div class="author clearfix">
<a href="/users/17221979/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1722/17221979/thumb/20180524141023.JPEG?imageView2/1/w/90/h/90" alt="挖鼻孔的老虎">
</a>
<a href="/users/17221979/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
挖鼻孔的老虎
</h2>
</a>
<div class="articleGender manIcon">101</div>
</div>

<a href="/article/121335150" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


小姨子好像在做什么调查，问老婆：“姐夫的睡眠质量怎样？”<br/>老婆：“时好时坏。”<br/>小姨子：“什么时候最好？”<br/>老婆：“当我洗完澡穿着睡裙还喷了香水时他睡的最沉，打都不醒那种。”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2739</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335150" data-share="/article/121335150" id="c-121335150" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">40</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335150" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335150" class="up">
<a href="javascript:voting(121335150,1)" class="voting" data-article="121335150" id="up-121335150" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2748</span>
</a>
</li>
<li id="vote-dn-121335150" class="down">
<a href="javascript:voting(121335150,-1)" class="voting" data-article="121335150" id="dn-121335150" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-9</span>
</a>
</li>
<li class="comments">
<a href="/article/121335150" id="c-121335150" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335150" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">神补刀国元首：</span>
<div class="main-text">
小姨子:不对啊，每次我洗完澡穿着睡裙还喷了香水时，姐夫都跟打了鸡血一样啊。
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


86

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335845'>


<div class="author clearfix">
<a href="/users/30523551/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3052/30523551/thumb/20181208234521.jpg?imageView2/1/w/90/h/90" alt="秋心不凉">
</a>
<a href="/users/30523551/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
秋心不凉
</h2>
</a>
<div class="articleGender manIcon">32</div>
</div>

<a href="/article/121335845" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


不好意思跟哥们开口借钱，弄了个女号，被他附近人搜到了。因为比较了解他，两人越聊越嗨，这货想看照片，就网上弄组美女照片发给他，还找了几张生活照，变声器语音都是经常的。忽悠了几天，表达了一下缺钱用，这货立马给我转了1314，然后我就把号扔了。<br/>过了几天，这小子难受来找我喝酒，结果我俩都喝大了，不小心说出了真相...

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2775</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335845" data-share="/article/121335845" id="c-121335845" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">60</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335845" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335845" class="up">
<a href="javascript:voting(121335845,1)" class="voting" data-article="121335845" id="up-121335845" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2793</span>
</a>
</li>
<li id="vote-dn-121335845" class="down">
<a href="javascript:voting(121335845,-1)" class="voting" data-article="121335845" id="dn-121335845" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-18</span>
</a>
</li>
<li class="comments">
<a href="/article/121335845" id="c-121335845" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335845" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">日丽贤：</span>
<div class="main-text">
这是钱的事吗？这是一屁股帐
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


40

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335072'>


<div class="author clearfix">
<a href="/users/12218602/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1221/12218602/thumb/20181007002300.jpg?imageView2/1/w/90/h/90" alt="老柴家的郡主">
</a>
<a href="/users/12218602/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
老柴家的郡主
</h2>
</a>
<div class="articleGender womenIcon">86</div>
</div>

<a href="/article/121335072" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


检查儿子作业，作文题目我的妈妈。儿子写的:孩子是遗落人间的明珠，而妈妈则是上帝派来保护孩子的天使。而我则是上帝掉落的陀螺，我妈妈就是那个喜欢抽陀螺的魔鬼……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">9270</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335072" data-share="/article/121335072" id="c-121335072" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">92</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335072" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335072" class="up">
<a href="javascript:voting(121335072,1)" class="voting" data-article="121335072" id="up-121335072" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">9292</span>
</a>
</li>
<li id="vote-dn-121335072" class="down">
<a href="javascript:voting(121335072,-1)" class="voting" data-article="121335072" id="dn-121335072" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-22</span>
</a>
</li>
<li class="comments">
<a href="/article/121335072" id="c-121335072" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335072" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">老柴家的郡主：</span>
<div class="main-text">
我觉得这儿子平常抽少了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


114

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_120298233'>


<div class="author clearfix">
<a href="/users/33542137/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3354/33542137/thumb/20180907124011.jpg?imageView2/1/w/90/h/90" alt="王云（笨笨）">
</a>
<a href="/users/33542137/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
王云（笨笨）
</h2>
</a>
<div class="articleGender womenIcon">25</div>
</div>

<a href="/article/120298233" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


女同事刚结婚，度蜜月回来之后，经常说：我家亲爱的是万能的，这也会，那也会！<br/>我说：让你家亲爱的生个孩子，我就相信他是万能的！<br/>女同事说：除了只有女人能做到的！<br/>我说：让你家亲爱的让别的女人给他生个孩子，我就相信他是万能的！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2642</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/120298233" data-share="/article/120298233" id="c-120298233" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">61</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_120298233" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-120298233" class="up">
<a href="javascript:voting(120298233,1)" class="voting" data-article="120298233" id="up-120298233" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2688</span>
</a>
</li>
<li id="vote-dn-120298233" class="down">
<a href="javascript:voting(120298233,-1)" class="voting" data-article="120298233" id="dn-120298233" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-46</span>
</a>
</li>
<li class="comments">
<a href="/article/120298233" id="c-120298233" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/120298233" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">沐沐沐沐雨：</span>
<div class="main-text">
别的女人 : 有种叫你老公让我怀孕啊！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


25

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335204'>


<div class="author clearfix">
<a href="/users/33491754/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3349/33491754/thumb/20181204153354.jpg?imageView2/1/w/90/h/90" alt="我是煮茶">
</a>
<a href="/users/33491754/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
我是煮茶
</h2>
</a>
<div class="articleGender manIcon">33</div>
</div>

<a href="/article/121335204" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


感冒了，我躺在床上觉得一张被子太单薄，连打了几喷嚏，我老婆立马就起来，冒着冷空气去柜子取出一张被子。<br/>我当时心里满满的感动……<br/>我老婆把被子放床上：“一人一张被子，这样你打喷嚏就不会老往我被子里灌冷风...”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1903</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335204" data-share="/article/121335204" id="c-121335204" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">27</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335204" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335204" class="up">
<a href="javascript:voting(121335204,1)" class="voting" data-article="121335204" id="up-121335204" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1910</span>
</a>
</li>
<li id="vote-dn-121335204" class="down">
<a href="javascript:voting(121335204,-1)" class="voting" data-article="121335204" id="dn-121335204" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-7</span>
</a>
</li>
<li class="comments">
<a href="/article/121335204" id="c-121335204" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335204" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">道士下山会女神：</span>
<div class="main-text">
一人一被（辈）子，那叫单身
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


24

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121291022'>


<div class="author clearfix">
<a href="/users/30321363/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3032/30321363/thumb/20180916195434.jpg?imageView2/1/w/90/h/90" alt="捉鱼不抓虾">
</a>
<a href="/users/30321363/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
捉鱼不抓虾
</h2>
</a>
<div class="articleGender manIcon">21</div>
</div>

<a href="/article/121291022" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


没结婚之前，我吸烟喝酒。<br/>结婚后，媳妇以要孩子之名戒掉了我的烟酒。孩子出生，奶粉钱让我断了念想，无缘烟酒！<br/>唯一剩下一个爱好，打麻将，也是小赌怡情的那种。<br/>但老婆规定，打麻将必须得赢钱，输一次，就增加一次。<br/>现在我相信歌词里的那句话:“爱有多销魂，就有多伤人！”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2389</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121291022" data-share="/article/121291022" id="c-121291022" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">44</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121291022" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121291022" class="up">
<a href="javascript:voting(121291022,1)" class="voting" data-article="121291022" id="up-121291022" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2408</span>
</a>
</li>
<li id="vote-dn-121291022" class="down">
<a href="javascript:voting(121291022,-1)" class="voting" data-article="121291022" id="dn-121291022" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-19</span>
</a>
</li>
<li class="comments">
<a href="/article/121291022" id="c-121291022" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121291022" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">吃了两碗又盛：</span>
<div class="main-text">
增加一次什么？请大胆地说出来
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


84

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121298299'>


<div class="author clearfix">
<a href="/users/39388283/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3938/39388283/thumb/20181206213844.jpg?imageView2/1/w/90/h/90" alt="我打豆豆你是豆豆">
</a>
<a href="/users/39388283/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
我打豆豆你是豆豆
</h2>
</a>
<div class="articleGender manIcon">38</div>
</div>

<a href="/article/121298299" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


媳妇儿：“老公，今天包你最爱吃的芹菜馅饺子，你快吃。”我：“媳妇儿，都一块吃呗。”媳妇儿：“不不不，我和孩儿等会再吃，你一定要好好嚼，儿子把掉帽的图钉扔馅里一个，你吃出来我们再吃。。。。。。”[楚楚可怜][楚楚可怜]

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3032</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121298299" data-share="/article/121298299" id="c-121298299" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">82</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121298299" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121298299" class="up">
<a href="javascript:voting(121298299,1)" class="voting" data-article="121298299" id="up-121298299" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3046</span>
</a>
</li>
<li id="vote-dn-121298299" class="down">
<a href="javascript:voting(121298299,-1)" class="voting" data-article="121298299" id="dn-121298299" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-14</span>
</a>
</li>
<li class="comments">
<a href="/article/121298299" id="c-121298299" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121298299" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">死去的帅哥：</span>
<div class="main-text">
懂了，楼主就是个探雷器[大笑][大笑][大笑]
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


29

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121291726'>


<div class="author clearfix">
<a href="/users/33491754/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3349/33491754/thumb/20181204153354.jpg?imageView2/1/w/90/h/90" alt="我是煮茶">
</a>
<a href="/users/33491754/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
我是煮茶
</h2>
</a>
<div class="articleGender manIcon">33</div>
</div>

<a href="/article/121291726" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


那年，我还单身，在北京出差，顺便去颐和园的昆明湖游玩。<br/>一个在健身房认识的女孩打电话给我，她还是那么干脆利落：“在哪？”<br/>我：“昆明湖！”<br/>女孩：“我飞去找你！”电话挂了。<br/>大半天后，她再次打给我：“我到昆明机场了！”   ...就这样，她在云南认识了现在的老公...

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">8669</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121291726" data-share="/article/121291726" id="c-121291726" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">93</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121291726" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121291726" class="up">
<a href="javascript:voting(121291726,1)" class="voting" data-article="121291726" id="up-121291726" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">8719</span>
</a>
</li>
<li id="vote-dn-121291726" class="down">
<a href="javascript:voting(121291726,-1)" class="voting" data-article="121291726" id="dn-121291726" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-50</span>
</a>
</li>
<li class="comments">
<a href="/article/121291726" id="c-121291726" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121291726" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">昔年°9：</span>
<div class="main-text">
你因该庆幸，这是随机抽取接盘侠的节奏阿！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


184

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_120297614'>


<div class="author clearfix">
<a href="/users/31625323/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3162/31625323/thumb/20180421211457.JPEG?imageView2/1/w/90/h/90" alt="若只如初见︶︿︶">
</a>
<a href="/users/31625323/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
若只如初见︶︿︶
</h2>
</a>
<div class="articleGender womenIcon">23</div>
</div>

<a href="/article/120297614" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


在淘宝上买了个裤子到货了，发现有一点瑕疵，以下是跟客服的聊天截图，他说好的，又撤回了，广大网友怎么办？

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/120297614" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12029/120297614/medium/app120297614.jpg" alt="糗事#120297614" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">218</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/120297614" data-share="/article/120297614" id="c-120297614" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">6</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_120297614" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-120297614" class="up">
<a href="javascript:voting(120297614,1)" class="voting" data-article="120297614" id="up-120297614" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">226</span>
</a>
</li>
<li id="vote-dn-120297614" class="down">
<a href="javascript:voting(120297614,-1)" class="voting" data-article="120297614" id="dn-120297614" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-8</span>
</a>
</li>
<li class="comments">
<a href="/article/120297614" id="c-120297614" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335592'>


<div class="author clearfix">
<a href="/users/26217894/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2621/26217894/thumb/20181209042528.jpg?imageView2/1/w/90/h/90" alt="聊天不撩妹子">
</a>
<a href="/users/26217894/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
聊天不撩妹子
</h2>
</a>
<div class="articleGender manIcon">53</div>
</div>

<a href="/article/121335592" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


星期天正准备美美的睡个回笼觉。老婆一大早就把我叫醒了。<br/>问她干啥呢？难得一天休息让我多睡一会不行吗？<br/>她说：没啥事，就是让你知道每次半夜三更把我叫醒有多讨厌。<br/>我。。。。。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1385</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335592" data-share="/article/121335592" id="c-121335592" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">26</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335592" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335592" class="up">
<a href="javascript:voting(121335592,1)" class="voting" data-article="121335592" id="up-121335592" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1392</span>
</a>
</li>
<li id="vote-dn-121335592" class="down">
<a href="javascript:voting(121335592,-1)" class="voting" data-article="121335592" id="dn-121335592" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-7</span>
</a>
</li>
<li class="comments">
<a href="/article/121335592" id="c-121335592" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335592" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
报复！真是赤果果的报复
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


16

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121308383'>


<div class="author clearfix">
<a href="/users/4370406/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/437/4370406/thumb/20150228163219.jpg?imageView2/1/w/90/h/90" alt="我爱笨女人">
</a>
<a href="/users/4370406/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
我爱笨女人
</h2>
</a>
<div class="articleGender manIcon">37</div>
</div>

<a href="/article/121308383" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


上周我大胡建地震，我一个兄弟第一时间自己跑出门，没有带上她老婆。现在已经闹了好几天了，明天周一要去办离婚。。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2125</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121308383" data-share="/article/121308383" id="c-121308383" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">74</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121308383" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121308383" class="up">
<a href="javascript:voting(121308383,1)" class="voting" data-article="121308383" id="up-121308383" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2141</span>
</a>
</li>
<li id="vote-dn-121308383" class="down">
<a href="javascript:voting(121308383,-1)" class="voting" data-article="121308383" id="dn-121308383" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-16</span>
</a>
</li>
<li class="comments">
<a href="/article/121308383" id="c-121308383" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121308383" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">罗布泊卖椰汁的喵：</span>
<div class="main-text">
要是我，我也离。这已经不是什么平常吵吵架，打打闹闹，谁先认个错的事了。已经是根本就没有把对方放在心里了。那还过什么日子？
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


32

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335472'>


<div class="author clearfix">
<a href="/users/34246786/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3424/34246786/thumb/20181208211338.jpg?imageView2/1/w/90/h/90" alt="老巫婆～～">
</a>
<a href="/users/34246786/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
老巫婆～～
</h2>
</a>
<div class="articleGender womenIcon">22</div>
</div>

<a href="/article/121335472" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


洗完澡刚踏出浴室，老公就急急忙忙地压上来，我转了一下眼睛，一只手挡着说：老公，明天双十二！老公停了一秒说：好，清空购物车！<br/>完事之后，老公坐在床头边抽烟边问我：老婆，你刚刚说什么？我不记得了呀！<br/>我………

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3217</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335472" data-share="/article/121335472" id="c-121335472" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">81</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335472" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335472" class="up">
<a href="javascript:voting(121335472,1)" class="voting" data-article="121335472" id="up-121335472" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3228</span>
</a>
</li>
<li id="vote-dn-121335472" class="down">
<a href="javascript:voting(121335472,-1)" class="voting" data-article="121335472" id="dn-121335472" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-11</span>
</a>
</li>
<li class="comments">
<a href="/article/121335472" id="c-121335472" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335472" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">恶霸张：</span>
<div class="main-text">
打他，肯定是装的，三秒前的事不可能忘这么快
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


96

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335031'>


<div class="author clearfix">
<a href="/users/29314260/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2931/29314260/thumb/20181208113550.jpg?imageView2/1/w/90/h/90" alt="贝格格*">
</a>
<a href="/users/29314260/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
贝格格*
</h2>
</a>
<div class="articleGender womenIcon">20</div>
</div>

<a href="/article/121335031" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


…买了件灰色外套，给我妈看，我妈就扣鼻子剜眼的数落我眼光差，买的衣服跟死老鼠皮一样，，<br/>老爸在旁边“噗嗤～”笑了，“我在皮革厂工作过几年，还真没见过死老鼠皮啥色，来来来，拿过来我看看，，”然后我爸拿着毛衣说“这么肥大一件衣服，这得几百条老鼠的皮吧，，”<br/>呃，你们这样，这衣服我还能穿吗。。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1565</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335031" data-share="/article/121335031" id="c-121335031" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">24</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335031" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335031" class="up">
<a href="javascript:voting(121335031,1)" class="voting" data-article="121335031" id="up-121335031" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1578</span>
</a>
</li>
<li id="vote-dn-121335031" class="down">
<a href="javascript:voting(121335031,-1)" class="voting" data-article="121335031" id="dn-121335031" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-13</span>
</a>
</li>
<li class="comments">
<a href="/article/121335031" id="c-121335031" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335031" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">死去的帅哥：</span>
<div class="main-text">
穿吧！老鼠皮也是皮[大笑][大笑][大笑]
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


20

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_120298338'>


<div class="author clearfix">
<a href="/users/12718999/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1271/12718999/thumb/20131127181058.jpg?imageView2/1/w/90/h/90" alt="撩起你的刘海">
</a>
<a href="/users/12718999/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
撩起你的刘海
</h2>
</a>
<div class="articleGender manIcon">25</div>
</div>

<a href="/article/120298338" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


一次和一损友去逛街，他走在我前头，我就低着头玩手机在后面跟着，正好遇到前面有一美女正在跨步上车，大家都知道这姿势，屁股是那样翘呀，朋友上前拍了一巴掌快步走了，美女转头回看，我刚好低头玩手机走到美女屁股后面，抬头一看，美女一脸嫌弃的脸看着我！瞬间感觉附近的空气都停止了，好委屈！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">393</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/120298338" data-share="/article/120298338" id="c-120298338" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">6</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_120298338" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-120298338" class="up">
<a href="javascript:voting(120298338,1)" class="voting" data-article="120298338" id="up-120298338" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">400</span>
</a>
</li>
<li id="vote-dn-120298338" class="down">
<a href="javascript:voting(120298338,-1)" class="voting" data-article="120298338" id="dn-120298338" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-7</span>
</a>
</li>
<li class="comments">
<a href="/article/120298338" id="c-120298338" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>





<!-- 全局翻页组件 -->

<ul class="pagination">


<li>
<span class="current" >
1
</span>
</li>




<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="page-numbers">
2
</span>
</a>
</li>



<li>
<a href="/hot/page/3/" rel="nofollow">
<!--<a href="/hot/page/3/" rel="nofollow">-->
<span class="page-numbers">
3
</span>
</a>
</li>



<li>
<a href="/hot/page/4/" rel="nofollow">
<!--<a href="/hot/page/4/" rel="nofollow">-->
<span class="page-numbers">
4
</span>
</a>
</li>



<li>
<a href="/hot/page/5/" rel="nofollow">
<!--<a href="/hot/page/5/" rel="nofollow">-->
<span class="page-numbers">
5
</span>
</a>
</li>



<li>
<span class="dots">
…
</span>
</li>


<li>
<a href="/hot/page/13/" rel="nofollow">
<!--<a href="/hot/page/13/" rel="nofollow">-->
<span class="page-numbers">
13
</span>
</a>
</li>


<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="next">
下一页
</span>
</a>
</li>

</ul>


</div>



<div class="col2">
<div id="sidebar" class="sidebar">

<div class="shopwindow">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- 新广告代码：2017-05-03 -->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29674533"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29674533";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29674533";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- <script type="text/javascript">
var cpro_id = "u693365";
</script>
<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"></script> -->
<script>
document.write('<script src="//becode.qiushibaike.com/common/e9w7.js?kfxohnx=go" type="text/javascript"><\/script>');
</script>
</div>

<div class="shopwindow" id="listAd2">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- 新广告代码：2017-05-03 -->
<!-- <script type="text/javascript">
/*右侧2*/
// var cpro_id = "u693365";
// document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
// 2017-5-23 修改
// FTAPI_slotid = 1026761;FTAPI_sync = true
// document.write('<script src="//pic.fastapi.net/sdk/js/a.js" charset="utf-8"><\/script>')
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/resource/d3nkw.js?m=hgpzzge"></script>
</div>


<div class="sidebar-other">
<img src="/static/images/productlist/ctrl_d.png">
<p>把糗事百科加入收藏夹</p>
</div>
<div class="sidebar-hot clearfix" id="sidebar-qrcode">
<div class="float-left qrcode">
<img src="/static/images/web_v3/sidebar/qiubai_qrcode.png" alt="糗事百科 APP 下载二维码">
</div>
<div class="float-left btn-box">
<a href="javascript:void(0)" class="btn-download ios" onclick="window.open('https://itunes.apple.com/cn/app/id422853458?mt=8')" target="_blank">iOS 下载</a>
<a href="javascript:void(0)" class="btn-download android" onclick="window.open('http://static.qiushibaike.com/qiushibaike.apk')" target="_blank">Android 下载</a>
<p class="tips">扫码下载糗事百科app</p>
</div>
</div>
<!-- 直播下载链接 -->
<div class="sidebar-hot clearfix" id="sidebar-remix">
<a href="https://www.app-remix.com/v1/pc/living?chn=qiubai" onclick="_hmt.push(['_trackEvent', 'web-remix', 'chick']);" target="_blank">
<img src="//static.qiushibaike.com/images/web_v3/sidebar/remix_banner.gif?v=f8bbbe7ca7cd5b9314e8235d6290fb0f" alt="">
</a>
</div>
<!-- 浪人杀下载链接 -->
<!--<div class="sidebar-hot clearfix" id="sidebar-wolf">-->
<!--<img src="//static.qiushibaike.com/images/web_v3/sidebar/wolf_banner.png?v=b18dc8556489b273af99197ebcf01a1c" alt="">-->
<!--</div>-->
<div class="sidebar-hot clearfix">
<h3>爆笑糗事精选</h3>
<ul>

<li class="item">
<a href="/article/121292460" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12129/121292460/small/Y1S3NW97FZC450ZX.jpg?imageView2/1/w/146/h/146" alt="如何评价这位神级作者"/></span>
</a>
<a href="/article/121292460" title="如何评价这位神级作者" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>如何评价这位神级作者</p>
</a>
</li>

<li class="item">
<a href="/article/121223287" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12122/121223287/small/ROOP3YACYVB623UP.jpg?imageView2/1/w/146/h/146" alt="我服了俩大男人在宿舍分别给媳妇缝轮滑护具"/></span>
</a>
<a href="/article/121223287" title="我服了俩大男人在宿舍分别给媳妇缝轮滑护具" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>我服了俩大男人在宿舍分别给媳妇缝轮滑护具</p>
</a>
</li>

<li class="item">
<a href="/article/121223423" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12122/121223423/small/5F7E1808UI4YDHCK.jpg?imageView2/1/w/146/h/146" alt="呀呀呀"/></span>
</a>
<a href="/article/121223423" title="呀呀呀" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>呀呀呀</p>
</a>
</li>

<li class="item">
<a href="/article/121223512" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12122/121223512/small/AUKRPVUVEPEGZ3UY.jpg?imageView2/1/w/146/h/146" alt="买一送一还送套"/></span>
</a>
<a href="/article/121223512" title="买一送一还送套" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>买一送一还送套</p>
</a>
</li>

<li class="item">
<a href="/article/121284445" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12128/121284445/small/AUXFYOSO2VU0N4YA.jpg?imageView2/1/w/146/h/146" alt="我就想知道厕所没有手纸"/></span>
</a>
<a href="/article/121284445" title="我就想知道厕所没有手纸" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>我就想知道厕所没有手纸</p>
</a>
</li>

<li class="item">
<a href="/article/121310191" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12131/121310191/small/0U523GDI4V2SX83R.jpg?imageView2/1/w/146/h/146" alt="我分明看到小叔子眼睛里和嘴角的笑意"/></span>
</a>
<a href="/article/121310191" title="我分明看到小叔子眼睛里和嘴角的笑意" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>我分明看到小叔子眼睛里和嘴角的笑意</p>
</a>
</li>

<li class="item">
<a href="/article/121267220" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12126/121267220/small/PELUYYYW4YVD4Z82.jpg?imageView2/1/w/146/h/146" alt="糗友们试一下"/></span>
</a>
<a href="/article/121267220" title="糗友们试一下" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>糗友们试一下</p>
</a>
</li>

<li class="item">
<a href="/article/121312764" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12131/121312764/small/3ZGY0E78NZJEGDWT.jpg?imageView2/1/w/146/h/146" alt="治疗远光狗"/></span>
</a>
<a href="/article/121312764" title="治疗远光狗" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>治疗远光狗</p>
</a>
</li>

</ul>
</div>
<div class="sidebar-hot clearfix" id="sidebar-tab">
<div class="tab-head">
<h3 class="active" data-type="0">热门</h3>
<h3 data-type="1">话题</h3>
<h3 data-type="2">专区</h3>
<h3 data-type="3">推荐</h3>
</div>
<div class="sidebar-tag-block tab-content0">

</div>
<div class="sidebar-tag-block tab-content1 hide">

</div>
<div class="sidebar-tag-block tab-content2 hide">


<li><i># </i><a href="/key/6480838/">加冰的空调扇怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6481207/">吉林建筑大学建筑学怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6486625/">哮喘的人吃什么补品好</a><i> #</i></li>

<li><i># </i><a href="/key/6490996/">宝宝烫伤能吃什么水果好</a><i> #</i></li>

<li><i># </i><a href="/key/6455547/">怎么样珍珠粉京润珍珠</a><i> #</i></li>

<li><i># </i><a href="/key/6480332/">昂达h81主板怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6487189/">头晕目眩呕吐吃什么好</a><i> #</i></li>

<li><i># </i><a href="/key/6489370/">喝酒把身体</a><i> #</i></li>

<li><i># </i><a href="/key/6477979/">祛痘看中医效果怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6493683/">乌龟平常喜欢吃什么东西</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content3 hide">

</div>
</div>

<div class="shopwindow" id="listAd3">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29640993"></a >');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29640993";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29640993";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- 新广告代码：2017-05-03 -->
<!-- <script>
var cpro_id = "u1101312";
document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/klcawm.js?gb=tytyyhc"></script>
</div>

<div class="shopwindow">
<!-- 2017.10.16 注释 -->
<!-- <script type="text/javascript" src="https://s.haiyunimg.com/SSP/30169.js"></script> -->
<!-- 2017.10.16 添加 -->
<!-- <script>
var mediav_ad_pub = 'klT513_2129270';
var mediav_ad_width = '300';
var mediav_ad_height = '250';
</script>
<script type="text/javascript" language="javascript" charset="utf-8" src="//static.mediav.com/js/mvf_g2.js"></script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/common/exweb.js?h=cuzuzzie"></script>
</div>

</div>
</div>



</div>
</div>


<div class="foot">
 <div class="foot-ad" id="footAd">
<!-- 68902435：web-底部固定 类型：固定 尺寸：728x90-->
<!-- 2017/2/28 注释旧的广告代码，改为使用 https 的广告 -->
<!-- <script type="text/javascript">//<![CDATA[
ac_as_id = "mm_108378320_13540554_68902435";
ac_format = 1;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "afpeng.alimama.com/";
//]]></script>
<script type="text/javascript" src="//afpmm.alicdn.com/g/mm/afp-cdn/JS/k.js"></script> -->
<!-- <script type="text/javascript">//<!—
google_ad_client = "ca-pub-7443704194229694";
/* IDG.CN_B2C_qiushibaike.com_HY_728x90 */
google_ad_slot = "9826878184";
google_ad_width = 728;
google_ad_height = 90;
//—>
document.write('<script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js"><\/script>');
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/s401mj.js?ezovy=frbr"></script>
</div>

<div class="foot-nav clearfix">
<div class="foot-nav-col">
<h3>
关于
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#team" target="_blank" rel="nofollow">
关于糗百
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#tech" target="_blank" rel="nofollow">
加入我们
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#contact" target="_blank" rel="nofollow">
联系方式
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
帮助
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/feedback.html" target="_blank" rel="nofollow">
在线反馈
</a>
</li>
<li>
<a href="//about.qiushibaike.com/agreement.html" target="_blank" rel="nofollow">
用户协议
</a>
</li>
<li>
<a href="//about.qiushibaike.com/policy.html" target="_blank" rel="nofollow">
隐私政策
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
下载
</h3>
<ul>
<li>
<a href="https://android.myapp.com/myapp/detail.htm?apkName=qsbk.app"
target="_blank" rel="external nofollow">
Android 客户端
</a>
</li>
<li>
<a href="https://itunes.apple.com/cn/app/id422853458" target="_blank" rel="external nofollow">
iPhone 客户端
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
关注
</h3>
<ul>
<li>
<a href="#" class="foot-wechat">
微信
<div class="foot-wechat-tips">
<span class="foot-wechat-icon"></span>
手机扫描二维码关注
</div>
</a>
</li>
<li>
<a href="http://weibo.com/qiushibaike" target="_blank" rel="external nofollow">
新浪微博
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058" target="_blank" rel="external nofollow">
QQ空间
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
组织
</h3>
<ul>
<li>
<a href="http://user.qzone.qq.com/1492495058/blog/1408597608" target="_blank"
rel="external nofollow">
官方粉丝群
</a>
</li>
<li>
<a href="https://www.qiushibaike.com/users/37042475" target="_blank"
rel="external nofollow">
<img style="vertical-align: middle;height: 16px;margin-top: -2px;" src="/static/images/beian.png">
首都网警
</a>
</li>
</ul>
</div>
</div>
<div class="foot-copyrights">
<!-- <p>&copy; Qiushibaike.com 糗事百科版权所有</p>
<p>
<span>京ICP备14028348号-1</span>
<span>京ICP证140448号</span>
<span>京网文[2017]2369-247号</span>
<span>
<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a>
</span>
</p>
<p style="margin-top:8px">友际无限（北京）科技有限公司</p>
<p style="margin-top:8px">
<span>互联网违法和不良信息举报电话：010-84872896</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p> -->
<p>互联网ICP备案：京ICP备14028348号-1</p>
<p>
<span>广播电视节目制作经营许可证：（京）字第08319号</span>
<span>网络文化经营许可证：
<a style='color:#333' target="_blank" href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/"
rel="nofollow">
<img src="/static/images/wenhuajingying.png?v=f5f3976cf4be787ad2be202a19d40823" style='width: 20px; height: 20px; vertical-align: top;'>京网文[2017]2369-247号</a>
</span>
</p>
<p style="margin-top: 8px">电信与信息服务业务经营许可证：京ICP证140448号</p>
<p style="margin-top: 8px"><span>营业性演出许可证：京演(机构)(2018)1940号</span></p>
<p>
<span>计算机信息网络国际联网单位备案：<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a></span>
</p>
<br>
<p style="margin-top: 8px">友际无限（北京）科技有限公司</p>
<p>
<span>违法和不良信息举报电话：0755-86967540</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p>
<br>
<p style="margin-top: 8px">&copy; Qiushibaike.com 糗事百科版权所有</p>
</div>
</div>


<div class="signin-box" id="login-form">
<div class="sigin-left">
<div class="signin-account clearfix">
<h4 class="social-signin-heading">社交帐号登录</h4>
<a rel="external nofollow" oauth_href href="https://open.weixin.qq.com/connect/qrconnect?appid=wx559af2d26b56c655&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession%3Fsrc%3Dwx&response_type=code&scope=snsapi_login#wechat_redirect" class="social-btn social-wechat">
使用 微信 账号</a>
<a rel="external nofollow" oauth_href href="https://api.weibo.com/oauth2/authorize?client_id=63372306&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession" class="social-btn social-weibo">
使用 微博 账号</a>
<a rel="external nofollow" oauth_href href="https://graph.qq.com/oauth2.0/authorize?which=Login&display=pc&client_id=100251437&response_type=code&redirect_uri=www.qiushibaike.com/new4/session?src=qq" class="social-btn social-qq">
使用 QQ 账号 </a>
</div>
<div class="signin-form clearfix">
<h4 class="social-signin-heading">糗事百科账号登录</h4>
<form method="post" action="/new4/session">
<input type="hidden" name="_xsrf" value="2|5b45a82a|58b37c13839bec89a1cb7b565b3f2b0d|1544583970"/>
<div class="signin-section clearfix">
<input type="text" class="form-input form-input-first" name="login" placeholder="昵称或邮箱">
<input type="password" class="form-input" name="password" placeholder="密码">
<input type="checkbox" id="remember_me" name="remember_me" checked="" value="checked" style="display:none">
</div>
<div class="signin-error" id="signin-error"></div>
<button type="submit" id="form-submit" class="form-submit">登录</button>
</form>
</div>
<div class="signin-foot clearfix">
<a rel="nofollow" href="/new4/fetchpass" class="fetch-password">忘记密码?</a>
</div>
</div>
</div>

<div class="float-nav">
<a class="float-nav-backtop" href="#" rel="nofollow">
<span class="float-nav-backtop-icon"></span>
</a>
</div>

<!--[if gte IE 6]>
<script type="text/javascript" src="//static.qiushibaike.com/js/src/web/json3.js?v=3a7f66a11a09842cd7555fad039657be"></script>
<![endif]-->
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/libs.min.js?v=bc8ddd36f0e7fed7c27f437c17f23ce0"></script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/app.min.js?v=5997ad16edca8ec50a1fcc40913785a6"></script>



<script type="text/javascript">
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-8780108-1', 'auto');
ga('send', 'pageview');
</script>

<script type="text/javascript" async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script type="text/javascript" src="https://cbjs.baidu.com/js/m.js"></script>
<script type="text/javascript">



window.broadJson = '[]'
</script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/v3/adsAdmin.min.js?v=9c42f35ae43e17caf141e9d6ebe32cbb"></script>
</body>
</html>
"""

pattern = re.compile(r'<div class="content">\n<span>(.*?)</span>',re.S)#re.S时候匹配包括换行的的内容
result = re.findall(pattern, html_content)
for row in result:
    pass
    print(row)
pattern2= re.compile(r'<h2>(.*?)</h2>',re.S)
result2= re.findall(pattern2,html_content)
print(result2)

